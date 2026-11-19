"""Vykreslování grafů funkcí jedné proměnné (Plotly + SymPy/NumPy).

Modul slouží jako nástroj pro jazykový model: umí vykreslit průběh funkce a
u určitého integrálu vybarvit plochu pod křivkou. Je navržen tak, aby zvládl
i „bláznivé“ funkce:

- **Póly a výbuchy hodnot** (`1/x`, `tan(x)`): husté vzorkování, robustní rozsah
  osy y podle percentilů a přerušení křivky v místech skoků (asymptot).
- **Neplatný definiční obor / komplexní hodnoty** (`sqrt(x)` pro x < 0, `log(x)`):
  bere se jen reálná část a nečíselné body se vynechají.
- **Nesmyslný rozsah**: rozsah se validuje; při chybě se vrací srozumitelná
  zpráva (model může zavolat nástroj znovu s lepším rozsahem).
"""

from __future__ import annotations

from typing import Optional, Tuple

import numpy as np
import plotly.graph_objects as go
import sympy as sp

N_POINTS = 2000       # počet vzorkovaných bodů
JUMP_FACTOR = 10      # jak velký skok mezi body považovat za asymptotu
MAX_WIDTH = 1e6       # maximální šířka intervalu


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


def render_plot(
    expr: str,
    variable: str = "x",
    x_min: float = -5.0,
    x_max: float = 5.0,
    area_from: Optional[float] = None,
    area_to: Optional[float] = None,
    y_min: Optional[float] = None,
    y_max: Optional[float] = None,
) -> Tuple[Optional[go.Figure], dict]:
    """Vykreslí funkci. Vrací (Plotly figure | None, souhrn pro model)."""
    # --- 1) Parsování a validace výrazu ---
    try:
        x = sp.Symbol(variable)
        e = sp.sympify(expr)
    except Exception as exc:  # noqa: BLE001
        return None, {"ok": False, "error": f"Neplatný výraz: {exc}"}

    if e.free_symbols - {x}:
        return None, {"ok": False, "error": f"Výraz smí obsahovat jen proměnnou '{variable}'."}

    # --- 2) Validace rozsahu ---
    try:
        x_min, x_max = float(x_min), float(x_max)
    except (TypeError, ValueError):
        return None, {"ok": False, "error": "x_min a x_max musí být čísla."}
    if not x_min < x_max:
        return None, {"ok": False, "error": "Musí platit x_min < x_max."}
    if (x_max - x_min) > MAX_WIDTH:
        return None, {"ok": False, "error": "Interval je příliš široký, zvol menší rozsah."}

    # --- 3) Vzorkování ---
    try:
        f = sp.lambdify(x, e, modules=["numpy"])
        xs = np.linspace(x_min, x_max, N_POINTS)
        with np.errstate(all="ignore"):
            ys = f(xs)
    except Exception as exc:  # noqa: BLE001
        return None, {"ok": False, "error": f"Funkci nelze vyčíslit: {exc}"}

    ys = np.asarray(ys, dtype=complex)
    if ys.ndim == 0:  # konstantní funkce
        ys = np.full(xs.shape, ys, dtype=complex)
    ys = np.where(np.isfinite(ys), ys.real, np.nan)  # jen reálná část a konečné hodnoty
    finite = ys[np.isfinite(ys)]
    if finite.size < 5:
        return None, {"ok": False,
                      "error": "Funkce je na tomto intervalu skoro všude nedefinovaná – zvol jiný rozsah."}

    # --- 4) Robustní rozsah osy y (percentily) ---
    if y_min is None or y_max is None:
        lo, hi = (float(v) for v in np.percentile(finite, [2, 98]))
        if not (np.isfinite(lo) and np.isfinite(hi)) or lo == hi:
            lo, hi = float(np.min(finite)), float(np.max(finite))
        fmin, fmax = float(np.min(finite)), float(np.max(finite))
        span = hi - lo
        if span <= 0:  # konstantní funkce
            y_lo, y_hi = fmin - 1.0, fmax + 1.0
        else:
            pad = span * 0.1
            # nepustit mez níž/výš, než kam funkce vůbec sahá (zbytečně to natahuje osu)
            y_lo, y_hi = max(lo - pad, fmin), min(hi + pad, fmax)
            if y_hi - y_lo <= 0:
                y_lo, y_hi = fmin - 0.5, fmax + 0.5
    else:
        y_lo, y_hi = float(y_min), float(y_max)

    ys_plot = _segment(ys, y_lo, y_hi)
    visible = np.clip(ys_plot[np.isfinite(ys_plot)], y_lo, y_hi)

    # --- 5) Sestavení grafu ---
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=ys_plot, mode="lines", name=f"f({variable}) = {sp.sstr(e)}"))

    summary = {
        "ok": True,
        "expr": str(e),
        "interval": [x_min, x_max],
        "y_rozsah": [round(y_lo, 4), round(y_hi, 4)],
        "min": round(float(np.min(visible)), 4),
        "max": round(float(np.max(visible)), 4),
    }

    # --- 6) Vybarvení plochy (určitý integrál) ---
    if area_from is not None and area_to is not None:
        try:
            a, b = float(area_from), float(area_to)
        except (TypeError, ValueError):
            return None, {"ok": False, "error": "area_from a area_to musí být čísla."}
        if a >= b:
            return None, {"ok": False, "error": "Musí platit area_from < area_to."}

        mask = (xs >= a) & (xs <= b)
        fig.add_trace(go.Scatter(
            x=xs[mask], y=np.where(np.isfinite(ys[mask]), ys[mask], 0.0),
            fill="tozeroy", mode="none",
            fillcolor="rgba(217, 130, 43, 0.35)", name=f"plocha na <{a}, {b}>",
        ))

        try:
            area_value = float(sp.integrate(e, (x, a, b)))
            if not np.isfinite(area_value):
                raise ValueError
        except Exception:  # noqa: BLE001
            xm, ym = xs[mask], ys[mask]
            good = np.isfinite(ym)
            xm, ym = xm[good], ym[good]
            area_value = float(np.sum((ym[:-1] + ym[1:]) / 2 * np.diff(xm))) if xm.size > 1 else 0.0
        summary["plocha"] = round(area_value, 6)
        summary["integral"] = f"∫ od {a} do {b}"

    fig.update_layout(
        xaxis_title=variable,
        yaxis_title=f"f({variable})",
        yaxis_range=[y_lo, y_hi],
        margin=dict(l=40, r=20, t=30, b=40),
        height=380,
        showlegend=True,
    )
    return fig, summary
