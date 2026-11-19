import os
import json
import re
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from src.math_core import verify_equivalence, compute
from src.plotting import render_plot
from src.curriculum import CURRICULUM
from src.rag import load_retriever, format_context

# Načte OPENAI_API_KEY ze souboru .env v kořenové složce (lokální spuštění)
load_dotenv()

# Pro nasazené aplikace (např. Streamlit Community Cloud) se klíč bere ze st.secrets.
try:
    if "OPENAI_API_KEY" in st.secrets:
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
except Exception:
    pass

st.set_page_config(page_title="AI Tutor Matematické analýzy – FSI VUT", page_icon="∫", layout="wide")

@st.cache_resource
def get_openai_client():
    return OpenAI()

@st.cache_resource
def get_retriever():
    """Načte RAG index z data/db (nebo None, pokud index neexistuje)."""
    return load_retriever()

client = get_openai_client()
retriever = get_retriever()


def normalize_latex(text: str) -> str:
    """Sjednotí oddělovače matematiky na ty, které Streamlit umí vykreslit.

    Streamlit (KaTeX) zobrazí matematiku jen pro ``$...$`` a ``$$...$$``.
    Model ale občas vrátí ``\\(...\\)`` nebo ``\\[...\\]``, případně matematiku
    v ``\\begin{equation}...`` nebo v ```` ```latex ```` bloku – to by se zobrazilo
    jako holý text. Tato funkce to převede na očekávané oddělovače.
    """
    if not text:
        return text
    text = re.sub(r"(?<!\\)\\\(", "$", text)
    text = re.sub(r"(?<!\\)\\\)", "$", text)
    text = re.sub(r"(?<!\\)\\\[", "$$", text)
    text = re.sub(r"(?<!\\)\\\]", "$$", text)
    text = re.sub(r"\\begin\{(equation\*?|displaymath)\}", "$$", text)
    text = re.sub(r"\\end\{(equation\*?|displaymath)\}", "$$", text)
    text = re.sub(r"```(?:latex|math)\s*(.*?)```", r"$$\1$$", text, flags=re.S)
    # odstraní prázdné/rozbité odkazy na obrázky, které model občas vloží
    text = re.sub(r"!\[[^\]]*\]\(\s*(?:attachment|image|obrázek)[^)]*\)", "", text)
    return text

# --- Inicializace stavu konverzace ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "tool_logs" not in st.session_state:
    st.session_state.tool_logs = {}
if "sources" not in st.session_state:
    st.session_state.sources = {}
if "figures" not in st.session_state:
    st.session_state.figures = {}

def reset_conversation():
    """Vymaže historii chatu, protokoly ověření, použité zdroje i grafy."""
    st.session_state.messages = []
    st.session_state.tool_logs = {}
    st.session_state.sources = {}
    st.session_state.figures = {}

# --- Postranní panel (ovládání režimů, kapitoly a obtížnosti) ---
with st.sidebar:
    st.header("Nastavení výuky")
    mode = st.radio(
        "Režim asistenta:",
        ["Učitel (výklad teorie)", "Zkoušející (procvičování)", "Spolužák (neformálně)"],
    )

    chapter = st.selectbox("Kapitola:", list(CURRICULUM.keys()))
    difficulty = st.select_slider(
        "Obtížnost úloh:",
        options=["Základní", "Střední (cvičení)", "Stačí umět všechno"],
        value="Střední (cvičení)",
    )

    st.divider()
    if st.button("🆕 Nová konverzace", width="stretch"):
        reset_conversation()

    st.divider()
    if retriever is None:
        st.warning(
            "Znalostní báze (RAG) není k dispozici. Sestav ji příkazem:\n\n"
            "`uv run python -m src.build_index`",
            icon="📚",
        )
    else:
        st.caption(f"📚 Znalostní báze: **{retriever.count}** pasáží z přednášek")

# Když student změní kapitolu / režim / obtížnost, začneme novou konverzaci.
# Jinak by model dál viděl historii o starém tématu a bavil se o něm.
selection = (mode, chapter, difficulty)
if st.session_state.get("last_selection") != selection:
    if st.session_state.get("last_selection") is not None:
        reset_conversation()
        st.toast("Nastavení se změnilo – začínáme novou konverzaci.", icon="🔄")
    st.session_state.last_selection = selection

st.title("AI Tutor Matematické analýzy (FSI VUT)")
st.caption(f"Aktivní režim: **{mode}** | Kapitola: **{chapter}** | Obtížnost: **{difficulty}**")

# --- Definice nástrojů ze src/math_core.py pro OpenAI ---
tools = [
    {
        "type": "function",
        "function": {
            "name": "verify_equivalence",
            "description": "Ověří pomocí knihovny SymPy, zda jsou dva matematické výrazy algebraicky ekvivalentní.",
            "parameters": {
                "type": "object",
                "properties": {
                    "student_expr": {"type": "string", "description": "Výraz studenta v syntaxi SymPy (např. 'cos(2*x)')"},
                    "expected_expr": {"type": "string", "description": "Správný referenční výraz v syntaxi SymPy (např. '2*cos(2*x)')"},
                    "variable": {"type": "string", "description": "Proměnná, výchozí 'x'"}
                },
                "required": ["student_expr", "expected_expr"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "compute",
            "description": (
                "Přímo spočítá symbolický výsledek pomocí SymPy (nikdy nepočítej zpaměti). "
                "Použij pro derivaci, integrál, limitu, zjednodušení, rozvinutí, faktorizaci nebo řešení rovnice."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expr": {"type": "string", "description": "Vstupní výraz v syntaxi SymPy (např. 'sin(2*x)', 'x**2 - 1')"},
                    "operation": {
                        "type": "string",
                        "enum": ["simplify", "derivative", "derivative2", "integrate", "limit", "expand", "factor", "solve"],
                        "description": "Požadovaná operace."
                    },
                    "variable": {"type": "string", "description": "Proměnná výpočtu, výchozí 'x'"},
                    "point": {"type": "string", "description": "Bod pro limitu (např. '0', '2', 'oo', '-oo'). Povinné jen pro operation='limit'."}
                },
                "required": ["expr", "operation"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "plot_function",
            "description": (
                "Vykreslí graf funkce jedné proměnné (Plotly). Použij, když je vhodné ukázat průběh "
                "funkce – zejména u určitého integrálu vybarvi plochu pod křivkou (area_from, area_to)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expr": {"type": "string", "description": "Výraz v syntaxi SymPy (např. 'x**2', 'sin(x)', '1/x')"},
                    "variable": {"type": "string", "description": "Proměnná, výchozí 'x'"},
                    "x_min": {"type": "number", "description": "Levá mez intervalu vykreslení (výchozí -5)"},
                    "x_max": {"type": "number", "description": "Pravá mez intervalu vykreslení (výchozí 5)"},
                    "area_from": {"type": "number", "description": "Dolní mez pro vybarvení plochy (určitý integrál)"},
                    "area_to": {"type": "number", "description": "Horní mez pro vybarvení plochy (určitý integrál)"},
                    "y_min": {"type": "number", "description": "Dolní mez osy y (nepovinné)"},
                    "y_max": {"type": "number", "description": "Horní mez osy y (nepovinné)"}
                },
                "required": ["expr"]
            }
        }
    }
]

# Mapování názvů nástrojů na jejich lokální implementace (plot_function se řeší zvlášť,
# protože vrací i obrázek, který se má vykreslit v rozhraní)
AVAILABLE_FUNCTIONS = {
    "verify_equivalence": verify_equivalence,
    "compute": compute,
}

# Doplnění konkrétní úlohy ke zvolené obtížnosti
DIFFICULTY_HINTS = {
    "Základní": "Zadávej jednoduché úlohy na přímé pochopení pojmu (jeden krok).",
    "Střední (cvičení)": "Zadávej typové úlohy na úrovni cvičení (několik kroků).",
    "Stačí umět všechno": "Zadávej i netriviální a zkouškové úlohy kombinující více kroků a souvislostí.",
}

def get_system_prompt(selected_mode: str, selected_chapter: str, selected_difficulty: str) -> str:
    base = (
        "Jsi specializovaný AI tutor Matematické analýzy pro studenty FSI VUT v Brně.\n"
        f"Aktuální okruh učiva: {selected_chapter}.\n"
        f"Požadovaná obtížnost: {selected_difficulty}. "
        f"{DIFFICULTY_HINTS.get(selected_difficulty, '')}\n\n"
        "Obecná pravidla:\n"
        "- Odpovídej vždy česky, odborně, ale srozumitelně.\n"
        "- Matematiku zapisuj POUZE pomocí $...$ (řádkově) a $$...$$ (samostatné bloky). "
        "Nikdy nepoužívej \\( \\) ani \\[ \\] a nevkládej vzorce do \\begin{equation}.\n"
        "- Nikdy nepočítej zpaměti. Výsledky počítání získávej voláním nástroje `compute` "
        "(derivace, integrály, limity, úpravy) a správnost výrazů (např. odpovědi studenta) "
        "ověřuj nástrojem `verify_equivalence`.\n"
        "- Když je užitečné ukázat průběh funkce, použij nástroj `plot_function`; u určitého "
        "integrálu vykresli funkci a vybarvi plochu zadáním `area_from` a `area_to`. "
        "Graf se zobrazí automaticky – nevkládej do odpovědi žádné obrázky ani odkazy typu `![...](attachment:...)`.\n"
        "- Pokud si u definice nebo věty nejsi jistý, přiznej to a nevymýšlej si.\n"
        f"- Pokud se dotaz týká jiné kapitoly než „{selected_chapter}“, krátce odpověz a nabídni přepnutí kapitoly.\n"
    )
    if "Spolužák" in selected_mode:
        return base + (
            "\nJsi v režimu SPOLUŽÁK. Vystupuj jako kamarád ze školy, ne jako učitel.\n"
            "Pravidla:\n"
            "- Mluv neformálně, přátelsky a hlavně krátce a k věci – žádné dlouhé omáčky.\n"
            "- Vysvětluj látku jednoduše a ukazuj ji na přirovnáních z běžného života "
            "(např. derivace jako rychlost, integrál jako hromadění, limita jako „blížíme se k“).\n"
            "- Neptej se studenta na kontrolní otázky a nezadávej mu nic k počítání – "
            "odpověz rovnou a stručně.\n"
            "- Klidně použij občas hovorový obrat, ale matematiku a výsledky měj vždy správně "
            "(ověř si je nástroji `compute`/`verify_equivalence`).\n"
            "- Když je toho moc, vyber to nejdůležitější a zbytek nabídni, když se student zeptá."
        )
    if "Učitel" in selected_mode:
        return base + (
            "\nJsi v režimu UČITEL. Cílem je studentovi látku vysvětlit.\n"
            "Postupuj takto:\n"
            "1. Úvodem v 1–2 větách shrň, co daný pojem znamená a k čemu je.\n"
            "2. Uveď přesnou definici / větu (formálně, v LaTeXu), jak se probírá na přednáškách FSI.\n"
            "3. Vysvětli ji krok za krokem a přidej intuici „proč to platí“.\n"
            "4. Ukaž jeden řešený příklad a každý krok okomentuj.\n"
            "5. Upozorni na 2–3 nejčastější chyby studentů u tohoto typu úlohy.\n"
            "Vysvětluj maximálně srozumitelně a trpělivě:\n"
            "- žádný krok nevynechávej a nepředpokládej znalosti, které student mít nemusí,\n"
            "- každý netriviální pojem a krok znovu objasni, klidně i více způsoby (formálně i názorně),\n"
            "- používej jednoduchý jazyk a konkrétní příklady, ať student látku opravdu pochopí.\n"
            "Neptej se studenta na žádné kontrolní ani doplňující otázky. Nezadávej mu nic k dopočítání "
            "a nečekej na jeho odpověď – odpověz rovnou, úplně a do konce.\n"
            "Drž se jednoho pojmu a nezahlcuj – další témata můžeš nabídnout jako možný navazující krok."
        )
    return base + (
        "\nJsi v režimu ZKOUŠEJÍCÍ. Cílem je studenta procvičit.\n"
        "Pravidla:\n"
        "- Vždy zadej právě JEDEN příklad a pak čekej na studentovo řešení. Nezadávej více příkladů najednou.\n"
        "- Příklady tvoř jako obměny typových úloh z přednášek a cvičení (jiné koeficienty, jiné zadání); "
        "obtížnost odpovídá zvolené úrovni.\n"
        "- Než příklad zadáš, spočítej si správný referenční výsledek voláním `compute`.\n"
        "- Když student pošle výsledek nebo mezivýpočet, VŽDY ho ověř nástrojem `verify_equivalence` "
        "(student_expr vs. expected_expr).\n"
        "- Nikdy neprozrazuj celý výsledek dopředu; veď studenta nápovědami.\n"
        "- Při chybě urči její typ (např. chyba ve znaménku, chybná metoda integrace, chyba v algebraické úpravě, "
        "špatný definiční obor, záměna funkce a její hodnoty) a dej návodnou nápovědu.\n"
        "- Stupňuj nápovědu: 1) upozorni na oblast, 2) napověz pravidlo nebo větu, 3) ukaž jen první krok.\n"
        "- Když student vyřeší správně, krátce pochval a zadej další (klidně těžší) příklad.\n"
        "- Na konci můžeš shrnout, které typy úloh studentovi šly a které je potřeba docvičit."
    )

# Vykreslení historie zpráv
for idx, msg in enumerate(st.session_state.messages):
    with st.chat_message(msg["role"]):
        st.markdown(normalize_latex(msg["content"]))
        if idx in st.session_state.sources:
            with st.expander("Použité pasáže z přednášek (RAG)"):
                for src in st.session_state.sources[idx]:
                    st.markdown(f"**{src['heading'] or src['source']}** — `{src['source']}`")
                    st.caption(src["text"][:400] + ("…" if len(src["text"]) > 400 else ""))
        if idx in st.session_state.tool_logs:
            with st.expander("Ověření výpočtu (SymPy)"):
                for log in st.session_state.tool_logs[idx]:
                    st.json(log)
        if idx in st.session_state.figures:
            for i, fig in enumerate(st.session_state.figures[idx]):
                st.plotly_chart(fig, width="stretch", key=f"fig-hist-{idx}-{i}")

# --- Zpracování nového dotazu ---
if prompt := st.chat_input("Napiš dotaz k teorii, požádej o příklad nebo zadej své řešení..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(normalize_latex(prompt))

    # RAG: vyhledá relevantní pasáže z přednášek
    passages = retriever.retrieve(prompt, k=4) if retriever else []

    api_messages = [{"role": "system", "content": get_system_prompt(mode, chapter, difficulty)}]
    if passages:
        api_messages.append({
            "role": "system",
            "content": (
                "Níže jsou relevantní pasáže z přednášek FSI k dotazu studenta. "
                "Vycházej především z nich a drž se jejich značení a postupů. "
                "Pokud odpověď v těchto pasážích není, řekni to a odpověz obecně.\n\n"
                + format_context(passages)
            ),
        })
    api_messages += st.session_state.messages

    with st.chat_message("assistant"):
        with st.spinner("Přemýšlím a ověřuji výpočty..."):
            verification_logs = []
            figures = []
            MAX_TOOL_ROUNDS = 5  # ochrana proti zacyklení volání nástroje

            for _ in range(MAX_TOOL_ROUNDS):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=api_messages,
                    tools=tools,
                )
                msg = response.choices[0].message

                # Model nevolá nástroj -> máme finální text
                if not msg.tool_calls:
                    break

                # Model zavolal některý nástroj ze SymPy -> vykonáme jej a pošleme výsledek zpět
                api_messages.append(msg)
                for tool_call in msg.tool_calls:
                    name = tool_call.function.name
                    args = json.loads(tool_call.function.arguments)
                    if name == "plot_function":
                        fig, res_dict = render_plot(**args)
                        if fig is not None:
                            figures.append(fig)
                    else:
                        func = AVAILABLE_FUNCTIONS.get(name)
                        if func is None:
                            res_dict = {"error": f"Neznámý nástroj '{name}'."}
                        else:
                            res_dict = func(**args)
                    verification_logs.append({"nastroj": name, "vstup": args, "vysledek_sympy": res_dict})
                    api_messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(res_dict)
                    })

            reply_text = msg.content or ""
            st.markdown(normalize_latex(reply_text))
            for i, fig in enumerate(figures):
                st.plotly_chart(fig, width="stretch", key=f"fig-cur-{i}")
            if passages:
                with st.expander("Použité pasáže z přednášek (RAG)"):
                    for src in passages:
                        st.markdown(f"**{src['heading'] or src['source']}** — `{src['source']}`")
                        st.caption(src["text"][:400] + ("…" if len(src["text"]) > 400 else ""))
            for log in verification_logs:
                with st.expander("Ověření výpočtu (SymPy)"):
                    st.json(log)

    st.session_state.messages.append({"role": "assistant", "content": reply_text})
    if passages:
        st.session_state.sources[len(st.session_state.messages) - 1] = passages
    if verification_logs:
        st.session_state.tool_logs[len(st.session_state.messages) - 1] = verification_logs
    if figures:
        st.session_state.figures[len(st.session_state.messages) - 1] = figures
