"""Skript pro sestavení vektorového indexu (znalostní báze).

Spuštění z kořene projektu:

    uv run python -m src.build_index          # postaví index, pokud neexistuje
    uv run python -m src.build_index --rebuild  # přegeneruje od nuly

Před spuštěním musí být v souboru ``.env`` nastaven ``OPENAI_API_KEY``
(embeddingy se počítají přes OpenAI).
"""

from __future__ import annotations

import argparse

from dotenv import load_dotenv

from src.rag import build_index


def main() -> None:
    load_dotenv()
    parser = argparse.ArgumentParser(description="Sestaví RAG index z přednášek.")
    parser.add_argument("--rebuild", action="store_true", help="Smazat a přegenerovat index.")
    args = parser.parse_args()

    pocet = build_index(rebuild=args.rebuild)
    print(f"Hotovo. V indexu je {pocet} pasáží.")


if __name__ == "__main__":
    main()
