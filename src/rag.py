"""RAG (Retrieval-Augmented Generation) nad přednáškovými texty.

Modul zajišťuje tzv. znalostní vrstvu aplikace:

1. Zpracuje markdown soubory vzniklé převodem přednáškových PDF
   (``data/mat-analyza-*.md``) a rozseká je na menší pasáže (chunky).
2. Pasáže oboduje pomocí OpenAI embeddings a uloží do vektorové databáze
   ChromaDB (persistentně v ``data/db``).
3. Pro dotaz studenta vrátí nejpodobnější pasáže, které se vloží do
   systémového promptu LLM. Tím se odpovědi opírají o reálné přednášky
   místo o „vymýšlení" modelu.

Veřejné rozhraní:
    build_index()      -- vytvoří / přegeneruje vektorovou DB,
    load_retriever()   -- načte hotový index (nebo vrátí None, pokud chybí),
    Retriever.retrieve -- vyhledá relevantní pasáže k dotazu,
    retrieve()         -- pohodlný obal nad load_retriever().
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Dict, List, Optional

import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# --- Konfigurace ---
COLLECTION_NAME = "mat_analyza"
EMBEDDING_MODEL = "text-embedding-3-small"
MAX_CHARS = 1500  # maximální délka jedné pasáže
OVERLAP = 250     # přesah mezi dělenými dlouhými odstavci

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "db"

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")


# ---------------------------------------------------------------------------
# Dělení textu na pasáže
# ---------------------------------------------------------------------------
def _split_sections(text: str) -> List[tuple]:
    """Rozdělí markdown na sekce podle nadpisů. Vrací seznam (nadpis, tělo)."""
    sections: List[tuple] = []
    current_heading = ""
    buf: List[str] = []
    for line in text.splitlines():
        if _HEADING_RE.match(line.strip()):
            if buf:
                sections.append((current_heading, "\n".join(buf).strip()))
                buf = []
            current_heading = line.strip()
        else:
            buf.append(line)
    if buf:
        sections.append((current_heading, "\n".join(buf).strip()))
    return sections


def chunk_markdown(text: str, source: str, max_chars: int = MAX_CHARS,
                   overlap: int = OVERLAP) -> List[Dict]:
    """Rozseká text na pasáže.

    Každá pasáž si sebou nese nadpis sekce (kvůli kontextu) a název zdrojového
    souboru. Dlouhé sekce se dělí po odstavcích, extrémně dlouhé odstavce po
    znacích s mírným přesahem.
    """
    chunks: List[Dict] = []

    def add(heading: str, body: str) -> None:
        body = body.strip()
        if not body:
            return
        content = f"{heading}\n\n{body}".strip() if heading else body
        idx = len(chunks)
        chunks.append({
            "id": f"{source}::{idx}",
            "text": content,
            "source": source,
            "heading": heading,
        })

    for heading, body in _split_sections(text):
        if not body:
            if heading:
                add("", heading)
            continue

        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        buffer = ""

        def flush() -> None:
            nonlocal buffer
            if buffer.strip():
                add(heading, buffer)
            buffer = ""

        for para in paragraphs:
            if len(para) > max_chars:
                flush()
                start = 0
                step = max(max_chars - overlap, 1)
                while start < len(para):
                    add(heading, para[start:start + max_chars])
                    start += step
            elif len(buffer) + len(para) + 2 <= max_chars:
                buffer = f"{buffer}\n\n{para}".strip()
            else:
                flush()
                buffer = para
        flush()

    return chunks


# ---------------------------------------------------------------------------
# ChromaDB
# ---------------------------------------------------------------------------
def _embedding_function() -> OpenAIEmbeddingFunction:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY není nastaven. Vytvoř soubor .env s klíčem "
            "OPENAI_API_KEY=... (viz README)."
        )
    return OpenAIEmbeddingFunction(api_key=api_key, model_name=EMBEDDING_MODEL)


def _client() -> chromadb.ClientAPI:
    DB_PATH.mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=str(DB_PATH))


def _default_md_paths() -> List[Path]:
    return sorted(DATA_DIR.glob("mat-analyza-*.md"))


def build_index(md_paths: Optional[List[Path]] = None, rebuild: bool = False) -> int:
    """Vytvoří vektorový index z markdown souborů. Vrací počet pasáží.

    Args:
        md_paths: seznam souborů; pokud None, vezme všechny ``data/mat-analyza-*.md``.
        rebuild: True = existující index smaže a postaví znovu.
    """
    paths = md_paths if md_paths is not None else _default_md_paths()
    if not paths:
        raise FileNotFoundError(f"Nenalezeny žádné markdown soubory v {DATA_DIR}")

    client = _client()

    if rebuild:
        try:
            client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=_embedding_function(),
    )

    if collection.count() > 0 and not rebuild:
        return collection.count()

    all_chunks: List[Dict] = []
    for path in paths:
        text = Path(path).read_text(encoding="utf-8")
        all_chunks.extend(chunk_markdown(text, source=Path(path).name))

    BATCH = 100
    for i in range(0, len(all_chunks), BATCH):
        batch = all_chunks[i:i + BATCH]
        collection.add(
            ids=[c["id"] for c in batch],
            documents=[c["text"] for c in batch],
            metadatas=[{"source": c["source"], "heading": c["heading"]} for c in batch],
        )
    return collection.count()


class Retriever:
    """Vyhledávač relevantních pasáží v hotovém indexu."""

    def __init__(self, collection) -> None:
        self._collection = collection

    @property
    def count(self) -> int:
        return self._collection.count()

    def retrieve(self, query: str, k: int = 4) -> List[Dict]:
        """Vrátí k nejpodobnějších pasáží k dotazu ``query``."""
        if not query or self._collection.count() == 0:
            return []
        result = self._collection.query(query_texts=[query], n_results=min(k, self._collection.count()))
        documents = result.get("documents", [[]])[0]
        metadatas = result.get("metadatas", [[]])[0]
        distances = result.get("distances", [[]])[0]
        out: List[Dict] = []
        for doc, meta, dist in zip(documents, metadatas, distances):
            out.append({
                "text": doc,
                "source": (meta or {}).get("source", ""),
                "heading": (meta or {}).get("heading", ""),
                "distance": dist,
            })
        return out


def load_retriever() -> Optional[Retriever]:
    """Načte hotový index. Pokud v DB nic není, vrátí None (aplikace funguje i bez RAG)."""
    if not DB_PATH.exists():
        return None
    try:
        client = _client()
        collection = client.get_collection(
            name=COLLECTION_NAME,
            embedding_function=_embedding_function(),
        )
    except Exception:
        return None
    if collection.count() == 0:
        return None
    return Retriever(collection)


def retrieve(query: str, k: int = 4) -> List[Dict]:
    """Zkratka: načte index a vrátí pasáže k dotazu (prázdné, když index chybí)."""
    retriever = load_retriever()
    if retriever is None:
        return []
    return retriever.retrieve(query, k=k)


def format_context(passages: List[Dict]) -> str:
    """Zformátuje pasáže do jednoho textového bloku pro systémový prompt."""
    if not passages:
        return ""
    parts = []
    for i, p in enumerate(passages, 1):
        label = p.get("heading") or p.get("source", "přednáška")
        parts.append(f"[{i}] {label}\n{p['text']}")
    return "\n\n".join(parts)
