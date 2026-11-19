"""Matematické jádro – deterministický výpočet a ověřování pomocí SymPy.

Modul poskytuje dva nástroje, které orchestrační vrstva (`app.py`) nabízí
jazykovému modelu jako takzvané „tools“. Díky nim model nepočítá zpaměti,
ale výsledky dostává z klasické symbolické matematiky:

- ``verify_equivalence`` – ověří, zda jsou dva výrazy algebraicky ekvivalentní,
- ``compute``             – přímo spočítá derivaci, integrál, limitu, úpravu apod.
"""

import sympy as sp
import math


def verify_equivalence(student_expr: str, expected_expr: str, variable: str = "x") -> dict:
    """Ověří, zda jsou dva výrazy algebraicky ekvivalentní (rozdíl se zjednoduší na 0).

    Args:
        student_expr: výraz studenta v syntaxi SymPy, např. ``"cos(2*x)"``.
        expected_expr: správný referenční výraz, např. ``"2*cos(2*x)"``.
        variable: proměnná, ve které se porovnává (výchozí ``"x"``).

    Returns:
        dict s ``is_correct`` a ``difference`` (nebo ``error`` při chybě zápisu).
    """
    try:
        x = sp.Symbol(variable)
        diff = sp.simplify(sp.sympify(student_expr) - sp.sympify(expected_expr))
        return {"is_correct": bool(diff == 0), "difference": str(diff)}
    except Exception as e:
        return {"is_correct": False, "error": str(e)}


# Mapování (i českých) názvů operací na interní klíč
_OPERATION_ALIASES = {
    "simplify": "simplify", "zjednodusit": "simplify", "upravit": "simplify",
    "derivative": "derivative", "derivace": "derivative", "diff": "derivative",
    "derivative2": "derivative2", "druha_derivace": "derivative2", "diff2": "derivative2",
    "integrate": "integrate", "integral": "integrate", "primitivni_funkce": "integrate",
    "limit": "limit", "limita": "limit",
    "expand": "expand", "rozvinout": "expand",
    "factor": "factor", "faktorizovat": "factor",
    "solve": "solve", "resit": "solve", "koreny": "solve",
}


def _parse_point(point) -> sp.Expr:
    """Převede bod (i nekonečno) na SymPy výraz."""
    p = str(point).strip().lower()
    if p in ("oo", "+oo", "inf", "+inf", "infinity", "nekonecno", "+nekonecno"):
        return sp.oo
    if p in ("-oo", "-inf", "-infinity", "-nekonecno"):
        return -sp.oo
    return sp.sympify(point)


def compute(expr: str, operation: str, variable: str = "x", point=None,
            lower=None, upper=None) -> dict:
    """Přímo spočítá požadovanou operaci nad výrazem pomocí SymPy.

    Args:
        expr: vstupní výraz v syntaxi SymPy, např. ``"sin(2*x)"``.
        operation: ``simplify``, ``derivative``, ``derivative2``, ``integrate``,
            ``limit``, ``expand``, ``factor`` nebo ``solve`` (lze i česky).
        variable: proměnná výpočtu (výchozí ``"x"``).
        point: bod pro ``limit`` (např. ``0``, ``"oo"``, ``"-oo"``).
        lower, upper: meze pro **určitý** integrál. Když jsou obě zadány, spočítá se
            určitý integrál ``∫_lower^upper``; jinak se (u ``integrate``) vrací
            **neurčitý** integrál (primitivní funkce).

    Returns:
        dict s ``result`` (textově), ``latex`` a ``operation``;
        při chybě ``result=None`` a ``error``.
    """
    try:
        x = sp.Symbol(variable)
        e = sp.sympify(expr)
        op = _OPERATION_ALIASES.get(str(operation).strip().lower())
        if op is None:
            return {"result": None, "error": f"Neznámá operace '{operation}'."}

        if op == "simplify":
            res = sp.simplify(e)
        elif op == "derivative":
            res = sp.diff(e, x)
        elif op == "derivative2":
            res = sp.diff(e, x, 2)
        elif op == "integrate":
            if lower is not None and upper is not None:
                res = sp.integrate(e, (x, _parse_point(lower), _parse_point(upper)))
            else:
                res = sp.integrate(e, x)  # neurčitý integrál (beze změny)
        elif op == "expand":
            res = sp.expand(e)
        elif op == "factor":
            res = sp.factor(e)
        elif op == "solve":
            res = sp.solve(e, x)
        elif op == "limit":
            if point is None:
                return {"result": None, "error": "Pro operaci 'limit' je třeba zadat 'point'."}
            res = sp.limit(e, x, _parse_point(point))
        else:  # pragma: no cover – ošetřeno výše
            return {"result": None, "error": f"Operace '{op}' není podporována."}

        try:
            latex = sp.latex(res)
        except Exception:
            latex = str(res)
        out = {"result": str(res), "latex": latex, "operation": op}
        # U číselného výsledku (určitý integrál, limita, číselné řešení…) přidáme
        # i přibližnou hodnotu, aby ji model studentovi rovnou uvedl.
        if isinstance(res, sp.Basic) and not res.free_symbols:
            try:
                numeric = float(sp.N(res))
                if math.isfinite(numeric):
                    out["numeric"] = round(numeric, 6)
            except Exception:
                pass
        return out
    except Exception as e:
        return {"result": None, "error": str(e)}
