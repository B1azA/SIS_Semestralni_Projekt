"""Výukový obsah (osnova) předmětů Matematické analýzy I a II na FSI VUT.

Struktura slouží k naplnění postranního panelu aplikace:
klíč slovníku = název kapitoly (okruhu učiva),
hodnota = seznam konkrétních témat, která se v dané kapitole probírají.

Slovník je záměrně oddělen do samostatného modulu, aby šel snadno
rozšiřovat bez zásahu do logiky chatbota v ``app.py``.
"""

CURRICULUM = {
    "1. Množiny a reálná čísla": [
        "Základy výrokové logiky a teorie množin",
        "Zobrazení, prostá a inverzní funkce",
        "Reálná čísla, ohraničenost, supremum a infimum",
        "Absolutní hodnota, intervaly a okolí bodu",
    ],
    "2. Funkce jedné proměnné, limita a spojitost": [
        "Definiční obor, obor hodnot a vlastnosti funkcí",
        "Elementární a cyklometrické funkce",
        "Vlastní a nevlastní limita funkce",
        "Spojitost funkce, body nespojitosti a věty o spojitých funkcích",
    ],
    "3. Diferenciální počet funkce jedné proměnné": [
        "Derivace funkce (složená a inverzní funkce, vyšší řády)",
        "Tečna, normála a diferenciál funkce",
        "Věty o střední hodnotě a L'Hospitalovo pravidlo",
        "Monotonnost, lokální a globální extrémy",
        "Konvexnost, konkávnost, inflexní body a asymptoty",
        "Kompletní vyšetření průběhu funkce",
        "Taylorův polynom a odhad zbytku",
    ],
    "4. Integrální počet funkce jedné proměnné": [
        "Primitivní funkce, základní vzorce a úpravy integrandu",
        "Integrace metodou per partes a substituční metodou",
        "Integrace racionálních, goniometrických a iracionálních funkcí",
        "Určitý Riemannův integrál a Newtonova–Leibnizova formule",
        "Aplikace určitého integrálu (obsah, délka oblouku, objem a povrch)",
        "Nevlastní integrály 1. a 2. druhu",
    ],
    "5. Metrické prostory": [
        "Metrika, vzdálenost a koule v metrickém prostoru",
        "Vnitřek, hranice a uzávěr množiny, otevřené a uzavřené množiny",
        "Konvergence posloupností a cauchyovské posloupnosti",
        "Úplné a kompaktní metrické prostory",
        "Spojitost a stejnoměrná spojitost zobrazení, kontrakce a pevný bod",
    ],
    "6. Diferenciální počet funkce více proměnných": [
        "Definiční obor, limita a spojitost funkce více proměnných",
        "Parciální derivace, směrová derivace a gradient",
        "Totální diferenciál, tečná rovina a normála",
        "Derivace složené funkce a Taylorův polynom více proměnných",
        "Volné lokální extrémy a Hessova matice",
        "Implicitní funkce, Jacobiova matice a jakobián",
        "Vázané extrémy (Lagrangeovy multiplikátory) a globální extrémy",
    ],
    "7. Integrální počet funkce více proměnných": [
        "Dvojný integrál a Fubiniova věta na normální množině",
        "Trojný integrál v prostoru",
        "Substituce ve dvojném a trojném integrálu (polární, cylindrické, sférické souřadnice)",
        "Aplikace v mechanice (obsah, objem, hmotnost, těžiště, momenty setrvačnosti)",
    ],
    "8. Křivkové a plošné integrály": [
        "Křivky v rovině a prostoru, parametrizace a tečný vektor",
        "Křivkový integrál I. a II. druhu, Greenova věta",
        "Nezávislost křivkového integrálu na cestě a potenciálové pole",
        "Plochy v prostoru, normálový vektor a orientace plochy",
        "Plošný integrál I. a II. druhu, Gaussova–Ostrogradského a Stokesova věta",
    ],
}
