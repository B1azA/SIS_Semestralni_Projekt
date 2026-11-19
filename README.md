# AI Tutor Matematické analýzy (FSI VUT)

Specializovaný matematický chatbot pro výuku **Matematické analýzy I a II** na FSI VUT v Brně.
Umí vysvětlovat teorii (režim **Učitel**) a generovat a vyhodnocovat příklady (režim **Zkoušející**).
Matematiku **nepočítá „z hlavy“** – výsledky získává z knihovny **SymPy** a odpovědi opírá o reálné
přednášky pomocí **RAG** (vyhledávání v přednáškových textech).

> 🔗 **Živá aplikace:** https://sissemestralniprojekt-8dgvdwadhjoz59f8ewu5km.streamlit.app/
>
> 📄 **Plná dokumentace:** [DOKUMENTACE.md](DOKUMENTACE.md) · diagram architektury: [docs/architektura.svg](docs/architektura.svg)
> 💬 **Ukázky konverzací:** [docs/ukazky_konverzaci.md](docs/ukazky_konverzaci.md)

## Klíčové funkce

- **Dva režimy:** *Učitel* (trpělivý výklad krok za krokem, bez otázek) a *Zkoušející*
  (zadá jeden příklad, čeká, neprozrazuje výsledek, dává stupňované nápovědy a určí typ chyby).
- **Výběr kapitoly a obtížnosti** v postranním panelu.
- **Matematická verifikace (SymPy):** model volá nástroje
  `compute` (derivace, integrály, limity, úpravy) a `verify_equivalence` (ověření výrazů).
- **RAG** nad přednáškami (ChromaDB + OpenAI embeddingy) se zobrazením použitých zdrojů.
- **Vykreslování LaTeXu** a automatická normalizace oddělovačů.
- **Automatický reset konverzace** při změně režimu/kapitoly/obtížnosti + tlačítko „Nová konverzace“.

## Spuštění lokálně

Potřebuješ **Python** (vyvíjeno na 3.14, funguje od 3.11) a **API klíč k OpenAI**.

Nejprve vytvoř soubor `.env` v kořeni projektu s klíčem:

```bash
OPENAI_API_KEY="sk-..."
```

### Varianta A — přes `uv` (doporučeno)

```bash
uv sync
uv run streamlit run app.py
```

### Varianta B — přes `pip`

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Aplikace se otevře na <http://localhost:8501>.

> **Znalostní báze (RAG)** je součástí repa (`data/db`), takže se nic sestavovat nemusí.
> Pokud bys ji chtěl přegenerovat z přednášek (`data/*.md`), spusť:
> `uv run python -m src.build_index` (resp. `python -m src.build_index`).

## Jak aplikaci ovládat

1. V **postranním panelu** zvol *Režim asistenta*, *Kapitolu* a *Obtížnost úloh*.
2. V **chatu** napiš dotaz na teorii, požádej o příklad, nebo (ve zkoušejícím režimu) pošli své řešení.
3. Pod odpovědí rozbal **„Použité pasáže z přednášek (RAG)“** a **„Ověření výpočtu (SymPy)“**.
4. Tlačítkem **„Nová konverzace“** vyčistíš historii (čistí se i automaticky při změně nastavení).

## Struktura projektu

```
app.py                         # Streamlit UI + orchestrační vrstva (prompty, tool-loop, reset)
src/math_core.py               # matematické jádro: compute() a verify_equivalence() (SymPy)
src/rag.py                     # znalostní vrstva: RAG nad ChromaDB
src/curriculum.py              # osnova kapitol
src/build_index.py             # CLI pro sestavení vektorového indexu
src/Semestralni_projekt.ipynb  # notebook s pipeline zpracování dat (PDF -> Markdown -> index)
data/*.md                      # zpracovaná znalostní báze z přednášek
data/db/                       # vektorová databáze (ChromaDB, součást repa)
docs/architektura.svg|.mmd     # diagram architektury
docs/ukazky_konverzaci.md      # ukázky reálných konverzací
DOKUMENTACE.md                 # kompletní dokumentace projektu
requirements.txt / pyproject.toml, uv.lock  # seznam závislostí
```

## Nasazení (Streamlit Community Cloud)

Aplikace běží na [share.streamlit.io](https://share.streamlit.io) (repo `B1azA/SIS_Semestralni_Projekt`,
main file `app.py`, klíč v *Secrets* jako `OPENAI_API_KEY`). Autoři nasazení: viz [DOKUMENTACE.md](DOKUMENTACE.md).

---

Autor: **Josef Blažek** · předmět SIS, varianta 2.
