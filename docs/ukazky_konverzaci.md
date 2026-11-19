# Ukázky reálných konverzací

Přepisy níže byly vygenerovány **reálným spuštěním aplikace** (model `gpt-4o-mini`, RAG nad přednáškami FSI VUT, ověřování přes SymPy). Text matematiky je zobrazen tak, jak ho student uvidí (po normalizaci LaTeXu).

---

## 1. Režim Učitel — výklad teorie

**Nastavení:** režim *Učitel*, kapitola *3. Diferenciální počet funkce jedné proměnné*.

**🧑‍🎓 Student:** Vysvětli mi prosím, jak se derivuje složená funkce.

**🤖 Tutor:**

Derivace složené funkce je důležitý pojem v diferenciálním počtu, který nám umožňuje nalézt derivaci funkcí, které mohou být složené z více výrazu. Tento proces se nazývá pravidlo řetězce.

### Definice
Nechť $ f: \mathbb{R} \to \mathbb{R} $ a $ g: \mathbb{R} \to \mathbb{R} $ jsou dvě funkce, které mají derivace v bodě $ x_0 $. Pokud $ g(x_0) = y_0 $ a funkce $ F = f \circ g $ (tedy $ F(x) = f(g(x)) $), potom platí:

$$
F'(x_0) = f'(g(x_0)) \cdot g'(x_0)
$$

### Vysvětlení pojmu a intuice
Toto pravidlo říká, že abychom vypočítali derivaci složené funkce $ F $, musíme:
1. Zjistit, jak rychle se mění vnitřní funkce $ g $ v bodě $ x_0 $ (to je $ g'(x_0) $).
2. Potom zjistit, jak rychle se mění vnější funkce $ f $ v bodě $ g(x_0) $ (to je $ f'(g(x_0)) $).
3. Výsledek těchto dvou derivací vynásobíme dohromady, protože změna v $ F $ je ovlivněna oběma funkcemi.

### Příklad
Pojďme si ukázat konkrétní příklad:

Mějme funkci $ F(x) = \sin(3x^2) $.

1. Určíme vnitřní a vnější funkce:
   - Vnitřní funkce: $ g(x) = 3x^2 $
   - Vnější funkce: $ f(u) = \sin(u) $ (kde $ u = g(x) = 3x^2 $)

2. Nejprve spočítáme derivace:
   - Derivace vnitřní funkce $ g $:
   $$ g'(x) = \frac{d}{dx}(3x^2) = 6x $$

   - Derivace vnější funkce $ f $:
   $$ f'(u) = \frac{d}{du}(\sin(u)) = \cos(u) $$

3. Aplikujeme pravidlo řetězce:
   $$ F'(x) = f'(g(x)) \cdot g'(x) = \cos(3x^2) \cdot 6x $$

Takže bychom dostali:
$$ F'(x) = 6x \cos(3x^2) $$

### Časté chyby
1. **Zaměnění pořadí derivací** – Je důležité brat v úvahu vnitřní a vnější funkci, abychom správně použili řetězové pravidlo.
2. **Nepoužití řetězového pravidla** – U složených funkcí se často zapomíná na aplikaci pravidla řetězce, což vede k chybným výsledkům.
3. **Zapomnění na správné derivace** – Je třeba si dávat pozor na derivace funkcí sinus, exponenciálních funkcí a dalších, abychom dostali správné odpovědi.

Orientační porozumění složeným funkcím a derivacím je nezbytné pro úspěšné zvládnutí diferenciálního počtu, takže se neváhejte ptát na další detaily nebo příklady!

> 📚 *Použité pasáže z přednášek (RAG):* ### 11 Implicitní funkce, diferencovatelná zobrazení mezi prostory vyšší dimenze, ### 14 Derivace, ##### Pˇrehled vzorc˚u pro derivaci

---

## 2. Režim Zkoušející — správný i chybný postup studenta

**Nastavení:** režim *Zkoušející*, kapitola *3. Diferenciální počet funkce jedné proměnné*.

### Krok 1 — zadání příkladu

**🧑‍🎓 Student:** Zadej mi prosím jeden příklad na derivaci složené funkce ve tvaru f(x) = x^2 * sin(x) a čekej na moje řešení.

**🤖 Zkoušející:** Urči derivaci funkce $f(x) = x^2 \sin(x)$. Čekám na tvoje řešení.

Model si nejprve spočítal správný referenční výsledek nástrojem `compute`:

```json
{
  "result": "x**2*cos(x) + 2*x*sin(x)",
  "latex": "x^{2} \\cos{\\left(x \\right)} + 2 x \\sin{\\left(x \\right)}",
  "operation": "derivative"
}
```

### Krok 2 — student odpoví chybně

**🧑‍🎓 Student:** Myslím, že f'(x) = 2*x*cos(x).

**🤖 Zkoušející:** Zkontrolujme tvoje řešení. Výpočet derivace je třeba provést pomocí pravidla pro derivaci součinu. 

Očekávám, že derivace by měla mít jiný tvar. Zkus se zamyslet, co se stane, když použiješ pravidlo pro derivaci součinu. 

Zapiš prosím znovu derivaci pomocí správného postupu.

> Zkoušející **neprozradil** správný výsledek, pojmenoval oblast chyby (zde chybějící pravidlo pro derivaci součinu) a vyzval studenta k opravě.

### Krok 3 — student odpoví správně

**🧑‍🎓 Student:** Zkusím to znovu: f'(x) = x^2*cos(x) + 2*x*sin(x).

**🤖 Zkoušející:** Skvěle! Tvoje odpověď $f'(x) = x^2 \cos(x) + 2x \sin(x)$ je správná. Výborně jsi použil pravidlo pro derivaci součinu.

Teď zkusíme mírně těžší úlohu. Urči derivaci funkce $$g(x) = \frac{\sin(x)}{x^2}$$. Čekám na tvoje řešení.

Odpověď studenta byla ověřena nástrojem `verify_equivalence`:

```json
{
  "is_correct": true,
  "difference": "0"
}
```
