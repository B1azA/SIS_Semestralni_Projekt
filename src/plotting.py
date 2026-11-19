"""Vykreslování grafů funkcí jedné proměnné (Plotly + SymPy/NumPy).

Modul slouží jako nástroj pro jazykový model: umí vykreslit **jednu i více funkcí**
do jednoho grafu a u určitého integrálu vybarvit plochu pod křivkou. Je navržen
tak, aby zvládl i „bláznivé“ funkce:

- **Póly a výbuchy hodnot** (`1/x`, `tan(x)`): husté vzorkování, robustní rozsah
  osy y podle percentilů a přerušení křivky v místech skoků (asymptot).
- **Neplatný definiční obor / komplexní hodnoty** (`sqrt(x)` pro x < 0, `log(x)`):
  bere se jen reálná část a nečíselné body se vynechají.
- **Nesmyslný rozsah**: rozsah se validuje; při chybě se vrací srozumitelná
  zpráva (model může zavolat nástroj znovu s lepším rozsahem).

V grafu se vždy zvýrazní osy `x = 0` a `y = 0` (tečkovaně), pokud leží v rozsahu.
"""

from __future__ import annotations

from typing import List, Optional, Tuple, Union

import numpy as np
import plotly.graph_objects as go
import sympy as sp

N_POINTS = 2000       # počet vzorkovaných bodů
JUMP_FACTOR = 10      # jak velký skok mezi body považovat za asymptotu
MAX_WIDTH = 1e6       # maximální šířka intervalu
PALETTE = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#17becf"]


def _segment(ys: np.ndarray, y_lo: float, y_hi: float) -> np.ndarray:
    """Vloží do série ``NaN`` v místech skoků, aby se křivka přes pól nepřerušila čarou."""
    ys = ys.astype(float).copy()
    if ys.size < 2:
        return ys
    jump_cut = (y_hi - y_lo) * JUMP_FACTOR
    diffs = np.abs(np.diff(ys))
    with np.errstate(all="ignore"):
        breaks = np.where((diffs > jump_cut) | ~np.isfinite(ys[1:]) | ~np.isfinite(ys[:-1]))[0]
    for b in breaks:
        ys[b] = np.nan
    return ys


def _evaluate(e: sp.Expr, x: sp.Symbol, xs: np.ndarray) -> np.ndarray:
    """Vyjádří funkci numericky; vrátí pole (jen reálné konečné hodnoty, jinak NaN)."""
    f = sp.lambdify(x, e, modules=["numpy"])
    with np.errstate(all="ignore"):
        ys = f(xs)
    ys = np.asarray(ys, dtype=complex)
    if ys.ndim == 0:  # konstantní funkce
        ys = np.full(xs.shape, ys, dtype=complex)
    return np.where(np.isfinite(ys), ys.real, np.nan)


def _robust_range(finite: np.ndarray) -> Tuple[float, float]:
    """Robustní rozsah osy y podle percentilů (odolný vůči pólům)."""
    lo, hi = (float(v) for v in np.percentile(finite, [2, 98]))
    if not (np.isfinite(lo) and np.isfinite(hi)) or lo == hi:
        lo, hi = float(np.min(finite)), float(np.max(finite))
    fmin, fmax = float(np.min(finite)), float(np.max(finite))
    span = hi - lo
    if span <= 0:  # konstantní funkce
        return fmin - 1.0, fmax + 1.0
    pad = span * 0.1
    y_lo, y_hi = max(lo - pad, fmin), min(hi + pad, fmax)
    if y_hi - y_lo <= 0:
        return fmin - 0.5, fmax + 0.5
    return y_lo, y_hi


def render_plot(
    exprs: Union[str, List[str], None] = None,
    variable: str = "x",
    x_min: float = -5.0,
    x_max: float = 5.0,
    area_from: Optional[float] = None,
    area_to: Optional[float] = None,
    area_index: int = 0,
    y_min: Optional[float] = None,
    y_max: Optional[float] = None,
    expr: Optional[str] = None,
) -> Tuple[Optional[go.Figure], dict]:
    """Vykreslí jednu nebo více funkcí do jednoho grafu.

    Args:
        exprs: výraz nebo seznam výrazů v syntaxi SymPy (např. ``["x**2", "sin(x)"]``).
        expr:  varianta pro jedinou funkci (kvůli zpětné kompatibilitě).
        area_from/area_to: meze pro vybarvení plochy (určitý integrál).
        area_index: index křivky (v ``exprs``), pod kterou se plocha vybarví.

    Returns:
        (Plotly figure | None, souhrn pro model)
    """
    # --- 0) Normalizace na seznam výrazů ---
    if exprs is None:
        exprs = expr
    if exprs is None:
        return None, {"ok": False, "error": "Zadej alespoň jednu funkci (exprs)."}
    if isinstance(exprs, str):
        exprs = [exprs]
    exprs = [str(e).strip() for e in exprs if str(e).strip()]
    if not exprs:
        return None, {"ok": False, "error": "Seznam funkcí je prázdný."}

    x = sp.Symbol(variable)

    # --- 1) Parsování a validace výrazů ---
    parsed: List[sp.Expr] = []
    for raw in exprs:
        try:
            e = sp.sympify(raw)
        except Exception as exc:  # noqa: BLE001
            return None, {"ok": False, "error": f"Neplatný výraz '{raw}': {exc}"}
        if e.free_symbols - {x}:
            return None, {"ok": False, "error": f"Výraz '{raw}' smí obsahovat jen proměnnou '{variable}'."}
        parsed.append(e)

    # --- 2) Validace rozsahu ---
    try:
        x_min, x_max = float(x_min), float(x_max)
    except (TypeError, ValueError):
        return None, {"ok": False, "error": "x_min a x_max musí být čísla."}
    if not x_min < x_max:
        return None, {"ok": False, "error": "Musí platit x_min < x_max."}
    if (x_max - x_min) > MAX_WIDTH:
        return None, {"ok": False, "error": "Interval je příliš široký, zvol menší rozsah."}

    # --- 3) Vzorkování a robustní rozsah y (sjednocení přes všechny křivky) ---
    xs = np.linspace(x_min, x_max, N_POINTS)
    y_lo, y_hi = np.inf, -np.inf
    if y_min is not None and y_max is not None:
        y_lo, y_hi = float(y_min), float(y_max)
    curves = []
    for e in parsed:
        try:
            ys = _evaluate(e, x, xs)
        except Exception as exc:  # noqa: BLE001
            return None, {"ok": False, "error": f"Funkci '{sp.sstr(e)}' nelze vyčíslit: {exc}"}
        finite = ys[np.isfinite(ys)]
        if finite.size < 5:
            return None, {"ok": False,
                          "error": f"Funkce '{sp.sstr(e)}' je na tomto intervalu skoro všude "
                                   "nedefinovaná – zvol jiný rozsah."}
        curves.append((e, ys, finite))
        if y_min is None or y_max is None:
            lo_i, hi_i = _robust_range(finite)
            y_lo, y_hi = min(y_lo, lo_i), max(y_hi, hi_i)
    if not np.isfinite(y_lo) or not np.isfinite(y_hi) or y_hi <= y_lo:
        y_lo, y_hi = -5.0, 5.0

    # --- 4) Sestavení grafu (jedna křivka za výraz) ---
    fig = go.Figure()
    summaries = []
    for i, (e, ys, _finite) in enumerate(curves):
        ys_plot = _segment(ys, y_lo, y_hi)
        visible = np.clip(ys_plot[np.isfinite(ys_plot)], y_lo, y_hi)
        fig.add_trace(go.Scatter(
            x=xs, y=ys_plot, mode="lines",
            line=dict(color=PALETTE[i % len(PALETTE)]),
            name=f"f({variable}) = {sp.sstr(e)}",
        ))
        summaries.append({
            "expr": str(e),
            "min": round(float(np.min(visible)), 4),
            "max": round(float(np.max(visible)), 4),
        })

    summary = {
        "ok": True,
        "funkce": summaries,
        "pocet_funkci": len(curves),
        "interval": [x_min, x_max],
        "y_rozsah": [round(y_lo, 4), round(y_hi, 4)],
    }

    # --- 5) Vybarvení plochy (určitý integrál) pod vybranou křivkou ---
    if area_from is not None and area_to is not None:
        try:
            a, b = float(area_from), float(area_to)
            idx = int(area_index)
        except (TypeError, ValueError):
            return None, {"ok": False, "error": "area_from, area_to a area_index musí být čísla."}
        if a >= b:
            return None, {"ok": False, "error": "Musí platit area_from < area_to."}
        if idx < 0 or idx >= len(curves):
            return None, {"ok": False, "error": f"area_index musí být 0..{len(curves) - 1}."}

        e_area, ys_area, _ = curves[idx]
        mask = (xs >= a) & (xs <= b)
        fig.add_trace(go.Scatter(
            x=xs[mask], y=np.where(np.isfinite(ys_area[mask]), ys_area[mask], 0.0),
            fill="tozeroy", mode="none",
            fillcolor="rgba(217, 130, 43, 0.35)",
            name=f"plocha pod {sp.sstr(e_area)} na <{a}, {b}>",
        ))

        try:
            area_value = float(sp.integrate(e_area, (x, a, b)))
            if not np.isfinite(area_value):
                raise ValueError
        except Exception:  # noqa: BLE001
            xm, ym = xs[mask], ys_area[mask]
            good = np.isfinite(ym)
            xm, ym = xm[good], ym[good]
            area_value = float(np.sum((ym[:-1] + ym[1:]) / 2 * np.diff(xm))) if xm.size > 1 else 0.0
        summary["plocha"] = round(area_value, 6)
        summary["plocha_pod"] = sp.sstr(e_area)
        summary["integral"] = f"∫ od {a} do {b}"

    # --- 6) Zvýraznění os x = 0 a y = 0 + světlá mřížka ---
    if y_lo <= 0 <= y_hi:
        fig.add_hline(y=0, line_width=1.2, line_color="#7a7a7a", line_dash="dash")
    if x_min <= 0 <= x_max:
        fig.add_vline(x=0, line_width=1.2, line_color="#7a7a7a", line_dash="dash")

    fig.update_layout(
        xaxis_title=variable,
        yaxis_title=f"f({variable})",
        yaxis_range=[y_lo, y_hi],
        margin=dict(l=40, r=20, t=30, b=40),
        height=380,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    fig.update_xaxes(showgrid=True, gridcolor="#eef1f4", zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor="#eef1f4", zeroline=False)
    return fig, summary
