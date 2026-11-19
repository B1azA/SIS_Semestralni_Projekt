

# Matematická analýza I 

Ludˇek Nechvátal 

Verze: 2024–09–16 

#### Pˇredmluva 

Předkládaný text je určen jako studijní opora pro předmět Matematická analýza I, který je vyučován na Fakultě strojního inženýrství VUT v Brně pro studenty prvního ročníku oborů Matematické inženýrství a Fyzikální inženýrství. Látka pokrývá zejména dvě klasické partie matematické analýzy, a to diferenciální a integrální počet funkce jedné (reálné) proměnné. Těmto dvěma kapitolám předchází jedna přípravná kapitola, ta obsahuje několik obecnějších matematických poznatků, které jsou využitelné i v jiných odvětvích matematiky a autor je považoval za vhodné zařadit. Způsob výkladu zmíněných disciplín matematické analýzy v tomto textu ctí tradici našeho regionu, která vychází z učebnic V. Jarníka – ty ovlivnily několik generací matematiků. Zároveň se však autor snažil o co nejpřístupnější formu poplatnou době. 

Na co konkrétně se tedy čtenář může těšit? Aby bylo vůbec možné se v matematice „domluvit“, obsahuje první kapitola základy výrokové logiky, toho, jak je matematika vůbec vystavěna včetně základních důkazových technik, teorie množin (zvláštní pozornost je věnována množině reálných čísel jakožto nejdůležitější množině v analýze), zobrazením, posloupnostem a funkcím. Druhá kapitola je věnována diferenciálnímu počtu, studenti se seznámí s pojmy limita, spojitost a derivace funkce, diferenciál, Taylorův polynom a zjistí, jak lze poznatky diferenciálního počtu využít v praktických úlohách. Třetí kapitola pak podá základy integrálního počtu, studenti se dozví, co je to primitivní funkce, seznámí se se základními integračními technikami, s konstrukcí Riemannova určitého integrálu a tím, jak spočítat jeho hodnotu. Na závěr bude pojem Riemannova integrálu rozšířen na tzv. nevlastní integrál a uvedeme si několik praktických aplikací, ve kterých lze integrální počet využít. 

Většina uváděných tvrzení je v textu dokázána, autor se také snažil o komentáře formou četných poznámek, jejichž smyslem je, aby student získal větší vhled do problematiky, či motivovat, proč se například daný pojem vůbec zavádí, na co si dát při aplikaci teorie pozor, atp. Při přípravě textu autor čerpal poznatky, včetně ilustrujících příkladů, ze zdrojů uvedených na konci v seznamu literatury a také ze svých poznámek nashromážděných během studia a pedagogické praxe. 

Přeji čtenářům, aby je látka předmětu zaujala, a aby získali pocit, že matematika není jenom krásná věda, která tříbí logické myšlení, ale že je také velmi užitečným pomocníkem při řešení úloh technické praxe. Za korekci textu a cenné připomínky děkuji doc. Ing. Jiřímu Šremrovi, Ph.D. 

Brno, srpen 2022 

Autor 

# Obsah 

|**1**<br>**Vyb**|**rané statě z matematiky**|**7**|
|---|---|---|
|1|Úvod do matematické logiky . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>7|
|2|Stavební prvky matematiky . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>11|
|3|Množiny . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>18|
|4|Relace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>21|
|5|Zobrazení . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>25|
|6|Reálná čísla . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>27|
|7|Posloupnosti . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>31|
|8|Funkce reálné proměnné<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>39|
|9|Rozdělení funkcí<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>42|
|10|Základní elementární funkce . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>42|
|11|Racionální funkce . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>47|
|**2**<br>**Dife**|**renciální počet**|**55**|
|12|Limita funkce . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>55|
|13|Spojitost funkce . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>58|
|14|Derivace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>62|
|15|Derivace vyšších řádů, diferenciál<br>. . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>66|
|16|Obecné věty o derivaci . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>68|
|17|Taylorův polynom . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>71|
|18|Průběh funkce . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>74|
|**3**<br>**Inte**|**grální počet**|**81**|
|19|Primitivní funkce . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>81|
|20|Speciální substituce (integrační metody) . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>85|
|21|Určitý (Riemannův) integrál<br>. . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>89|
|22|Výpočet a vlastnosti Riemannova integrálu . . . . . . . . . . . . .|. . . . . . . . . . . .<br>95|
|23|<br>Integrál jako funkce horní meze<br>. . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . 102|
|24|Nevlastní integrály<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . 104|
|25|Aplikace určitého integrálu . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . 106|



## Kapitola 1 

# Vybrané statˇe z matematiky 

### 1 Úvod do matematické logiky 

Logikou v běžném slova smyslu rozumíme myšlenkovou cestu, která vede k určitým závěrům. Logika je také formální věda, která zkoumá způsob vyvozování závěrů. Za zakladatele logiky (tzv. sylogistické logiky) je považován Aristotelés<sup>1</sup> . Princip sylogismu lze ukázat na známém příkladu: „Předpoklad 1: Každý člověk je smrtelný. Předpoklad 2: Sokrates je člověk. Závěr: Sokrates je smrtelný.“ 

Matematická logika je vědní disciplína nacházející se na rozhraní mezi logikou a matematikou (zabývá se zejména těmi oblastmi logiky, na jejichž základech je postavena matematika). K rozvoji a modernímu pojetí matematické logiky velkou měrou přispěl anglický matematik a filozof Boole<sup>2</sup> , který si všiml analogie logických operací s klasickými algebraickými operacemi na číslech. Jádrem matematické logiky je tzv. výroková logika (jejím rozšířením je predikátová logika), kde základním pojmem je _výrok_ . Výrokem budeme rozumět jakékoliv tvrzení, o kterém má smysl uvažovat, zda je pravdivé či nikoliv. 

Pˇríklad 1.1. a) „Brno je město“ je výrok (pravdivý). 

- b) „Ve vesmíru existuje mimozemská civilizace“ je výrok – výroky jsou i tvrzení, u kterých k danému okamžiku nelze rozhodnout, zda jsou pravdivé (takovým výrokům říkáme hypotézy). 

- c) „Jihomoravský kraj je v rámci ČR čtvrtým nejlidnatějším krajem a má největší rozlohu“ je výrok (nepravdivý, nemá největší rozlohu). 

- d) „Bude-li zítra pršet, vezme si Karel deštník“ je výrok – opět nejsme v okamžiku vyřčení schopni rozhodnout, zda je pravdivý. 

- e) „Každé přirozené číslo je dělitelné dvěma“ je výrok (nepravdivý). 

- f) „Co děláš?“ není výrok – výroky nejsou otázky, rozkazy, jazykově nesmyslné věty. 

- g) „Číslo x je dělitelné dvěma“ není výrok (nevíme, jakou hodnotu má x). 

Poznámka 1.2. Výroky a), b), e) jsou tzv. _elementární (atomární)_ výroky (nelze je totiž dále dělit), výrok c) je _složený_ – skládá se z elementárních výroků „JM kraj je čtvrtým nejlidnatějším“ a „JM kraj má největší rozlohu“. Stejně tak je složený výrok d), obsahuje elementární výroky „bude zítra pršet“ a „Karel si vezme deštník“. 

Složené výroky tvoříme pomocí logických spojek (funktorů), přičemž pravdivostní hodnoty vzniklých výroků se řídí danými pravidly, viz tabulky 1.1 a 1.2 níže. 

Tabulka 1.1: Logické spojky 

||konjunkce|disjunkce|implikace|ekvivalence|
|---|---|---|---|---|
|zápis|^|_|)|,|
|význam|a (zároveň)|nebo|jestliže, pak|právě tehdy, když|



> 1Aristotelés ze Stageiry 384–322 př. n. l., Starořek 

> 2George Boole 1815–1864, Angličan 

Kapitola 1. Vybrané statˇe z matematiky 

8 

Tabulka 1.2: Pravdivostní tabulka 

|A|B|A^|B<br>A_|B<br>A)B|A,B|
|---|---|---|---|---|---|
|1|1|1|1|1|1|
|1|0|0|1|0|0|
|0|1|0|1|1|0|
|0|0|0|0|1|1|



Poznámka 1.3. a) V běžné mluvě se „nebo“ používá ve dvou významech, vylučovacím a slučovacím. Např. „musím to nyní dodělat, nebo nebudou prémie“ (buď..., nebo...) představuje vylučovací význam (v psaném textu se v tomto případě píše před „nebo“ čárka). Příkladem slučovacího významu je věta „k určování stáří fosilií se používá metoda radioaktivního thoria nebo uhlíku“ (píšeme bez čárky před „nebo“). Ve slučovacím významu tedy platí alespoň jedna možnost (ale mohou platit obě). Z pravdivostní tabulky je zřejmé, že v případě disjunkce se jedná o slučovací význam. 

b) V běžné řeči se implikace „jestliže A, pak B “ používá v případech, kdy jednotlivé výroky A, B spolu obsahově nějak souvisí, např. „dojíš-li oběd, dostaneš čokoládu“. Toto ve výrokové logice není nutné, např. výrok „jestliže 2 je záporné, potom 3 je dělitelé dvěma“ je pravdivý výrok (vyjdeme-li z nepravdy, potom již můžeme říkat cokoliv a výsledný výrok bude pravdivý). 

c) Implikace navíc často bývá v běžné mluvě špatně chápána jako ekvivalence. Např. věta „bude-li zítra pršet, vezme si Karel deštník“ by mohla svádět k závěru, že pokud pršet nebude, tak si Karel deštník určitě nevezme. On si jej ale může vzít (třeba proto, aby jej použil jako slunečník). Jiný příklad: výrok „končí-li přirozené číslo nulou, potom je dělitelné pěti“ je pravdivý, ale číslo může být dělitelné pěti, i když nekončí nulou (končí pěti). 

_Negace_ pravdivého výroku je výrok nepravdivý a naopak. Značíme :A (a čteme non A), také A<sup>0</sup> nebo A, viz tabulka 1.3. 

Tabulka 1.3: Pravdivostní hodnoty negace 

|A<br>:A<br>1<br>0<br>0<br>1|
|---|



Zřejmě platí, že pravdivost :.:A/ je stejná jako pravdivost A. Jak tvořit negaci? Vždy můžeme použít obratu „Není pravda, že...“. 

Pˇríklad 1.4. Znegujte výroky z příkladu 1.1a,b). 

_Řešení._ „Není pravda, že Brno je město“, stručně „Brno není město“. „Ve vesmíru neexistují mimozemské civilizace“. 

V pravdivostní tabulce jsme namísto konkrétních elementárních výroků psali zastupující symbol A, resp. B. Tyto symboly nazýváme _výrokové proměnné_ . 

_Výroková formule_ je složený výrok, který vznikne z konečného počtu výrokových proměnných, logických spojek, negací a závorek, např. ..A ) B/ _ C/ , .A ^ C/. 

Výrokové formule, které jsou vždy pravdivé bez ohledu na pravdivost výrokových proměnných, se nazývají _tautologie_ . Ty, které jsou naopak vždy nepravdivé, se nazývají _kontradikce (spory)_ . 

Řekneme, že dvě výrokové formule ' a jsou _logicky ekvivalentní_ , jestliže formule ' , je tautologie. 

Pˇríklad 1.5. Ukažte, že následující výrokové formule jsou tautologie: 

a) .A ) B/ , :B ) :A transpozice (obměna) implikace; b) ..A ) B/ ^ .B ) C// ) .A ) C/ tranzitivita implikace; c) :.A ) B/ , .A ^ :B/; 

1 Úvod do matematické logiky 

9 

d) .A , B/ , ..A ) B/ ^ .B ) A//; 

e) A _ .:A/ zákon vyloučení třetího (tertium non datur); 

f) A ) .B ) A/ zákon simplifikace; 

g) :.A ^ B/ , ..:A/ _ .:B//, :.A _ B/ , ..:A/ ^ .:B// De Morganovy<sup>3</sup> zákony; h) ..A ^ B/ ^ C/ , .A ^ .B ^ C//, ..A _ B/ _ C/ , .A _ .B _ C// asociativní zákony; i) .A ^ B/ , .B ^ A/, .A _ B/ , .B _ A/ komutativní zákony; 

- j) .A ^ .B _ C// , ..A ^ B/ _ .A ^ C//, .A _ .B ^ C// , ..A _ B/ ^ .A _ C// distributivní zákony. 

_Řešení._ Pomocí pravdivostní tabulky ověřme např. tautologie e), f) a h) (tautologie z ostatních bodů by se ověřily analogicky). 

||A|d e)||||Ad f)||
|---|---|---|---|---|---|---|---|
|A|:A|A_.:A/|A|B|B )|A<br>A)|.B )A/|
|1|0|1|1|1|1||1|
|0|1|1|1|0|1||1|
||||0|1|0||1|
||||0|0|1||1|



||||||Ad h)|||
|---|---|---|---|---|---|---|---|
|A|B|C|A^B|B ^C|A^.B ^C/|.A^B/^C|,|
|1|1|1|1|1|1|1|1|
|1|1|0|1|0|0|0|1|
|1|0|0|0|0|0|0|1|
|1|0|1|0|0|0|0|1|
|0|1|1|0|1|0|0|1|
|0|1|0|0|0|0|0|1|
|0|0|1|0|0|0|0|1|
|0|0|0|0|0|0|0|1|



Všimněme si, že počet řádků v tabulkách je 2<sup>n</sup> , kde n je počet výrokových proměnných (z kombinatorického hlediska se jedná o variace s opakováním). 

Poznámka 1.6. Tautologie a)–d) z předchozího příkladu tvoří základ matematických důkazů (viz následující kapitola). Díky vlastnosti b) lze stručně psát A ) B ) C . Vlastnost b) lze navíc pomocí principu matematické indukce (viz následující kapitola) rozšířit na libovolný konečný počet výrokových proměnných A1; : : : ; An, tj. platí ..A1 ) A2/ ^ .A2 ) A3/ ^ ���^ .An�1 ) An// ) .A1 ) An/, stručně zapsáno A1 ) A2 ) A3 ) ���) An. Negace tautologie je kontradikce, negace kontradikce je tautologie. 

Pˇríklad 1.7. Znegujte výroky c), d) z příkladu 1.1. „JM kraj není v rámci ČR čtvrtým nejlidnatějším krajem nebo nemá největší rozlohu“, viz první de Morganův zákon, příklad 1.5g). „Zítra bude pršet a zároveň si Karel nevezme deštník“, viz příklad 1.5c). 

Pˇríklad 1.8. Ukažte, že formule .A ^ B/ ^ .:A/ je kontradikce. 

_Řešení._ Podobně jako v případě ověření tautologií využijeme pravdivostní tabulku: 

3Augustus De Morgan 1806–1871, Angličan 

Kapitola 1. Vybrané statˇe z matematiky 

10 

|A|B|A^B|:A|.A^B/^.:A/|
|---|---|---|---|---|
|1|1|1|0|0|
|1|0|0|0|0|
|0|1|0|1|0|
|0|0|0|1|0|



V příkladu 1.1g) jsme uvedli, že věta „číslo x je dělitelné dvěma“ není výrok. Dosadíme-li však za proměnnou x konkrétní hodnotu, pak už dostaneme výrok. Obecně, pokud se nějaké tvrzení (obsahující jednu proměnnou) po dosazení libovolného prvku z předem dané množiny za proměnou stane výrokem, nazýváme takové tvrzení _výrokovou formou_ , značíme V.x/. Pokud má výroková forma více proměnných x1; x2; : : : ; xn, píšeme V.x1; x2; : : : ; xn/. 

Dosazení prvků do výrokové formy není jediným způsobem, jak z ní vytvořit výroky. Lze to též pomocí slovních vazeb, které nazýváme kvantifikátory. Stěžejní jsou následující dva kvantifikátory: 

- a) _obecný kvantifikátor_ – „pro všechna“ („pro každé“), značíme 8 (z anglického „all“); 

b) _existenční kvantifikátor_ – „existuje“ (alespoň jeden), značíme 9 (z anglického „exists“). 

Je-li V.x/ výroková forma proměnné x, pak pomocí uvedených kvantifikátorů dostáváme kvantifikované výroky: 

8x 2 M W V.x/ – čteme „pro každé x z množiny M (viz kap. 3) platí V.x/“; 

- 9x 2 M W V.x/ – čteme „existuje x z množiny M takové, že platí V.x/“. 

Poznámka 1.9. Jednoznačnou existenci značíme 9Š, kvantifikovaný výrok 9Šx 2 M W V.x/ potom čteme „existuje právě jedno x z množiny M takové, že platí V.x/“. 

De Morganovy zákony pro kvantifikované výroky: 

- :.8x 2 M W V.x// , 9x 2 M W :V.x/; 

- :.9x 2 M W V.x// , 8x 2 M W :V.x/. 

Podobně, pro výroky se dvěma kvantifikátory platí: 

- :.8x 2 M; 9y 2 N W V.x; y// , 9x 2 M; 8y 2 N W :V.x; y/; 

- :.9x 2 M; 8y 2 N W V.x; y// , 8x 2 M; 9y 2 N W :V.x; y/. 

Pˇríklad 1.10. Negujte výrok z příkladu 1.1e). 

_Řešení._ „Existuje alespoň jedno přirozené číslo, které není dělitelné dvěma.“ 

Poznámka 1.11. Existují i další kvantifikátory, viz tabulka 1.4. 

Tabulka 1.4: Vybrané kvantifikátory a jejich negace 

|V.n/|:V.n/|
|---|---|
|Alespoňn... je...|Nejvýšen�1... je...|
|Nejvýšen... je...|AlespoňnC1... je...|
|Právěn... je...|Nejvýšen�1... je... nebo alespoňnC1... je...|



#### Pˇríklady k procviˇcení 

- 1.1. Vyslovte negace následujících výroků (a určete jejich pravdivost): 

   - a) „každé číslo tvaru n<sup>2</sup> , n 2 N, je sudé“; 

   - b) „alespoň dvě čísla jsou kladná“; 

   - c) „právě dvě čísla jsou kladná“; 

   - d) „číslo 12 je dělitelné 3 a zároveň není dělitelné 5“; 

   - e) „9Šx 2 R W sin x > 1“; 

   - f) „jestliže pro strany trojúhelníka platí vzorec c<sup>2</sup> D a<sup>2</sup> C b<sup>2</sup> , trojúhelník je pravoúhlý“; 

   - g) „přirozené číslo je dělitelné pěti, právě když končí nulou nebo pěti“. 

2 Stavební prvky matematiky 

11 

- 1.2. Rozhodněte, zda dané výrokové formule jsou tautologie. 

   - a) ..A ) B/ _ .B ) A// , ..:A ) :B/ ^ A/; 

   - b) ..B ) A/ ^ .C ) A// ) ..B _ C/ ) A/. 

1.3. Utvořte výroky A ) B, B ) A, A , B a určete, které z nich jsou pravdivé. V případě pravdivé implikace vytvořte pomocí zákona transpozice obrácenou implikaci. 

- a) A W „Pro daná čísla x; y platí x<sup>2</sup> D y<sup>2</sup> “, B W „Pro daná čísla platí x D y.“, 

- b) A W „sin x > 0.“, B W „x 2 .0; �/:“. 

1.4. Definujme vztahem A ˚ B , :.A , B/ logickou spojku „vylučovací nebo“. Ukažte, že formule A ˚ .B ˚ C/ a .A ˚ B/ ˚ C jsou logicky ekvivalentní. 

_Výsledky._ 1.2. a) Ne, b) ano. 

### 2 Stavební prvky matematiky 

- (i) _Primitivní pojmy_ (nedefinované), např. v eukleidovské geometrii bod, přímka, rovina; v teorii množin např. množina, pojem „patřit do (náležet)“; v Peanově aritmetice číslo nula a funkce následovníka; 

- (ii) _Axiomy_ jsou tvrzení, která se nedokazují (považují se za platná), např. „existuje prázdná množina“, „každými dvěma body lze vést (právě jednu) přímku“. Důležité je, aby systém axiomů byl bezesporný a zároveň se snažíme, aby byl nezávislý, tj. aby některý z axiomů nešel odvodit z axiomů ostatních; 

- (iii) _Definice_ jsou zavedení nového pojmu pomocí již známých pojmů, např. „sudým číslem nazveme každé celé číslo, které je dělitelné dvěma“, „kružnice je množina všech bodů v rovině, které leží ve stejné vzdálenosti od pevně daného bodu“; 

- (iv) _Věty (teorémy)_ jsou tvrzení, která se vyvozují z axiomů a již známých (tj. dokázaných) vět prostřednictvím logiky. Nedílnou součástí věty je tedy důkaz. Věty mají obvykle tvar elementárního (nekvantifikovaného nebo kvantifikovaného) výroku, implikace nebo ekvivalence. 

Poznámka 2.1. Nové pojmy (definice) často zavádíme pomocí spojky „jestliže“, resp. „právě když“. Např. definici sudého čísla bychom mohli formulovat také takto: „Nechť z je celé číslo. Řekneme, že z je sudé, jestliže je dělitelné dvěma“. Použili jsme tedy implikaci „je-li z dělitelné dvěma, pak je sudé“ (předpokladem „nechť z je celé číslo“ jsme vymezili obor čísel, kterých se sudost týká). Neříkáme tedy nic o číslech, která dělitelná dvěma nejsou, nicméně tím, že výrok uvozujeme jako definici, říkáme, že čísla, která nejsou dělitelná dvěma za sudá nepovažujeme. Z tohoto pohledu je korektnější uvést definici jako ekvivalenci, tj. „Nechť z je celé číslo. Řekneme, že z je sudé, právě když je dělitelné dvěma“. Na druhou stranu, argumentem proti je, že až do chvíle, kdy definujeme nový pojem (v našem příkladu sudé číslo), nemá smyl implikace „je-li z sudé číslo, pak je dělitelné dvěma“ (protože sudost teprve definujeme pomocí opačné implikace). V dalším tedy budeme (pokud to bude definice vyžadovat) zpravidla používat „jestliže“. 

##### Vˇety ve tvaru elementárního výroku 

V – výrok, který se má dokázat. 

###### Pˇrímý d˚ukaz 

Vyjdeme z pravdivého výroku A (nalezeného mezi axiomy nebo již dokázanými výroky) a pomocí pravdivé implikace (konečného počtu pravdivých implikací) přejdeme k výroku V . Využíváme zde tzv. _pravidlo odvozování (modus ponens)_ : jestliže platí A a zároveň A ) V , pak musí platit V , viz tabulka. 

|A|V<br>A|)V|
|---|---|---|
|**1**|**1**|**1**|
|1|0|0|
|0|1|1|
|0|0|1|



Kapitola 1. Vybrané statˇe z matematiky 

12 

###### D˚ukaz sporem 

Předpokládáme, že V neplatí, tj. platí :V a pomocí pravdivé implikace (konečného počtu pravdivých implikací) dojdeme k výroku A, který je ve sporu se známou skutečností (tj. platilo by A i :A). Toto nám zaručí, že platí V , viz tabulka. 

|:V|A|:V )A|V|
|---|---|---|---|
|1|1|1|0|
|1|0|0|0|
|0|1|1|1|
|**0**|**0**|**1**|**1**|



Pˇríklad 2.2. Dokažte, že pro 8a; b 2 R (reálná čísla, viz kapitola 6) platí a<sup>2</sup> C b<sup>2</sup> � 2ab. 

##### _Řešení._ 

- Přímo: Nechť a; b 2 R jsou libovolná. Protože po každé x 2 R platí x<sup>2</sup> � 0, dostaneme (položením x D a � b) .a � b/<sup>2</sup> � 0 ) a<sup>2</sup> � 2ab C b<sup>2</sup> � 0 ) a<sup>2</sup> C b<sup>2</sup> � 2ab. 

- Sporem: předpokládejme, že existují a; b 2 R taková, že a<sup>2</sup> C b<sup>2</sup> < 2ab ) a<sup>2</sup> C b<sup>2</sup> � 2ab < 0 ) 0 � .a � b/<sup>2</sup> < 0, což je spor. Musí tedy platit původní tvrzení. 

##### Vˇety ve tvaru implikace 

Jedná se tedy o výrok typu A ) B (A – předpoklady věty, B – tvrzení věty, říkáme také, že A je postačující podmínka pro B nebo B je nutná podmínka pro A) 

###### Pˇrímý d˚ukaz 

Předpokládáme, že výrok A je pravdivý a pomocí konečného počtu pravdivých implikací dokážeme B (tj. A ) A1 ) A2 ) ���) Ak ) B). 

###### Nepˇrímý d˚ukaz (kontrapozice) 

Využívá tautologie .A ) B/ , .:B ) :A/ (viz příklad 1.5a)), které se říká _transpozice (obměna) implikace_ . Dále stejně jako u přímého důkazu, tj. :B ) B1 ) B2 ) ���) Bk ) :A. 

###### D˚ukaz implikace sporem 

Využívá tautologie :.A ) B/ , .A ^ :B/ (viz příklad 1.5c)). Předpokládáme platnost negace :.A ) B/, tedy platnost výroku A ^ :B a následně ukážeme jeho nepravdivost tím, že pravdivou implikací (konečným počtem pravdivých implikací) dojdeme k tomu, že pravdivé je nějaké tvrzení C i :C (tj. máme spor). Předpoklad pravdivosti A ^ :B je tedy chybný, a proto musí platit původní tvrzení. 

Pˇríklad 2.3. Dokažte větu „je-li přirozené číslo dělitelné 4, potom je dělitelné 2“. 

_Řešení._ Máme tedy dokázat: 8n 2 N W 4jn ) 2jn. 

   - 2N 

- ‚…„ƒ 

- � Přímo: 4jn ) 9k 2 N W n D 4k ) n D 2 .2k/ ) 2jn. 

- Nepřímo: 2 ∤ n ) 9k 2 N W n D 2k � 1. Pokud k je sudé, pak existuje ` 2 N takové, že k D 2`, a tedy n D 4` � 1 ) 4 ∤ n. Pokud je k liché, pak existuje m 2 N takové, že k D 2m � 1, a tedy n D 2.2m � 1/ � 1 D 4m � 3 ) 4 ∤ n. 

- Sporem: předpokládejme, že platí 4jn ^ 2 ∤ n. Protože 4jn, existuje k 2 N takové, že n D 4k D 2.2k/ ) 2jn. Zároveň má ale platit 2 ∤ n, což je spor. Byla tedy chyba v předpokladu 2 ∤ n a platí původní tvrzení. 

Pˇríklad 2.4. Nechť a; c jsou přirozená čísla a nechť k je nejmenší přirozené číslo takové, že cjak (takové číslo existuje, neboť ak patří do množiny společných násobků čísel a; c, která je neprázdná, obsahuje totiž alespoň číslo ac, a každá neprázdná podmnožina množiny přirozených čísel má nejmenší prvek, to bude ukázáno později v příkladu 2.11). Nechť dále b je přirozené číslo takové, že cjab. Dokažte, že potom kjb a kjc. 

2 Stavební prvky matematiky 

13 

_Řešení._ Sporem: předpokládejme, že k ∤ b. Nechť q; r, 1 � r < k, jsou taková čísla, že b D kq C r. Potom ab D akq C ar. Protože c podle předpokladu dělí levou stranu a první člen na pravé straně, musí dělit i druhý člen na pravé straně, tj. cjar. To je ale ve sporu s tím, že k je nejmenší přirozené číslo takové, že cjak. Musí tedy platit kjb. Položíme-li b D c, pak předpoklad cjab je splněn (protože cjac), a tedy kjc. 

Poznámka 2.5. Důsledkem vlastnosti z předchozího příkladu je _Eukleidovo_<sup>_4_</sup> _lemma_ , což je známé tvrzení z teorie čísel. To říká, že pokud nějaké prvočíslo dělí součin dvou přirozených čísel, pak dělí také první nebo druhé z nich. Skutečně, označíme-li p zmíněné prvočíslo, a; b dvě přirozená čísla taková, že pjab, a vezmeme nejmenší k 2 N takové, že pjak, pak podle předchozího příkladu platí kjb a kjp. Druhá dělitelnost dává buď k D 1, nebo k D p. V prvním případě to znamená, že pja, ve druhém případě pjb. 

##### Vˇety ve tvaru ekvivalence 

Díky tautologii .A , B/ , ..A ) B/ ^ .B ) A// (viz příklad 1.5d)) dokazujeme dvojici implikací. 

Pˇríklad 2.6. Dokažte větu „Je-li n přirozené, pak 3jn, právě když 3jn<sup>2</sup> “. 

_Řešení._ „)“ Přímý důkaz: 3jn ) 9k 2 N W n D 3k ) n<sup>2</sup> D 9k<sup>2</sup> D 3.3k<sup>2</sup> / ) 3jn<sup>2</sup> . „(“ Nepřímý důkaz: 3 ∤ n ) 9k 2 N W .n D 3k�1_n D 3k�2/ ) Œn<sup>2</sup> D .3k�1/<sup>2</sup> D 9k<sup>2</sup> �6kC1 D 

3.3k<sup>2</sup> � 2k/ C 1 _ n<sup>2</sup> D .3k � 2/<sup>2</sup> D 9k<sup>2</sup> � 12k C 4 D 3.3k<sup>2</sup> � 4k/ C 4� ) 3 ∤ n<sup>2</sup> . 

##### D˚ukaz matematickou indukcí 

Touto technikou dokazujeme věty typu „Pro všechna n přirozená (případně pro všechna n přirozená, taková, že n � n0) platí V.n/“ (V.n/ je výroková forma reprezentující nějakou vlastnost přirozeného čísla n), tj. chceme ukázat platnost V.n/ pro n D 1; 2; : : : (resp. pro n D n0; n0 C 1; : : : ). Princip matematické indukce říká (coby axiom), že k důkazu stačí, když provedeme následující dva kroky: 

1. krok ( _báze indukce_ ): Ukážeme, že V.n/ platí pro n D 1 (resp. n D n0); 

2. krok ( _indukční krok_ ): Předpokládáme, že V.n/ platí pro jakékoliv (pevně zvolené) přirozené číslo n D k � 1 (resp. n D k � n0) – hovoříme o _indukčním předpokladu_ – a ukážeme, že V.n/ pak platí i pro následující číslo n D k C 1 (je tedy potřeba ověřit pravdivost implikace V.k/ ) V.k C 1/). 

Poznámka 2.7. Princip matematické indukce je podobný domino efektu (první kostka domina vyvolá pád druhé, druhá pád třetí atd.). Když v prvním kroku ukážeme, že platí V.1/ (resp. V.n0/), tak podle druhého kroku platí V.2/ (resp. V.n0 C 1/). Když ale platí V.2/ (resp. V.n0 C 1/), tak (opět podle druhého kroku) platí V.3/ (resp. V.n0 C 2/) atd. Jak již bylo řečeno, princip matematické indukce není věta, kterou můžeme dokázat, ale je to axiom. Je to vlastně trochu jinak formulovaný 5-tý Peanův<sup>5</sup> axiom, pět Peanových axiomů umožňuje korektně definovat množinu všech přirozených čísel, není to ale jediná možná konstrukce této množiny. 

Pˇríklad 2.8. Dokažte, že pro každé přirozené číslo n � 5 platí 2<sup>n</sup> > n<sup>2</sup> . 

_Řešení._ Pro n D 5 tvrzení platí, protože 2<sup>5</sup> D 32 > 25 D 5<sup>2</sup> . Potřebujeme ukázat, že pokud platí 2<sup>k</sup> > k<sup>2</sup> , tak platí také 2<sup>kC1</sup> > .k C 1/<sup>2</sup> . Pomůžeme si následující nerovností. Pro k � 5 jistě platí .k � 1/<sup>2</sup> � 4<sup>2</sup> > 2. Odtud, k<sup>2</sup> � 2k C 1 > 2 = C k<sup>2</sup> ) 2k<sup>2</sup> � 2k � 1 > k<sup>2</sup> ) 2k<sup>2</sup> > .k C 1/<sup>2</sup> . Tato nerovnost a indukční předpoklad 2<sup>k</sup> > k<sup>2</sup> dávají 2<sup>kC1</sup> D 2 � 2<sup>k</sup> > 2k<sup>2</sup> > .k C 1/<sup>2</sup> , tedy 2<sup>kC1</sup> > .k C 1/<sup>2</sup> . 

Pˇríklad 2.9. Nechť n 2 N a a1; a2; : : : ; an jsou kladná reálná čísla, jejichž součin je roven jedné. Dokažte, že platí 



<!-- Start of picture text -->
a1 C a2 C ���C an � n; (N)<br><!-- End of picture text -->

přičemž rovnost nastane pouze v případě a1 D a2 D ���D an D 1. 

_Řešení._ Pro n D 1 nerovnost (N) platí, protože a1 D 1 � 1. Jako indukční předpoklad uvažujme platnost nerovnosti (N) pro n D k (kde k � 1 je libovolné přirozené číslo) a dokažme, že potom tato nerovnost platí 

> 4Eukleidés z Megary asi 450–368 př. n. l., Starořek 

> 5Giuseppe Peano 1858–1932, Ital 

Kapitola 1. Vybrané statˇe z matematiky 

14 

i pro n D k C 1 kladných čísel a1; a2; : : : ; akC1 splňujících a1a2 ��� akC1 D 1. Bez újmy na obecnosti můžeme předpokládat, že a1 � 1 je největší z čísel a1; a2; : : : ; akC1 a a2 � 1 naopak nejmenší (pokud by tomu tak nebylo, tak můžeme čísla přeznačit). Tato dvě čísla pak splňují nerovnost 



<!-- Start of picture text -->
a1 C a2 � a1a2 � 1 (N1)<br><!-- End of picture text -->

(z toho důvodu, že a1Ca2�a1a2�1 D .a1�1/.1�a2/ � 0). Protože k kladných čísel a1a2; a3; : : : ; akC1 má součin 1, podle indukčního předpokladu platí 



<!-- Start of picture text -->
a1a2 C a3 C ���C akC1 � k: (N2)<br><!-- End of picture text -->

Sečteme-li nyní nerovnosti (N1) a (N2), dostaneme 

a1 C a2 � a1a2 C a1a2 C a3 C ���C akC1 � 1 C k; tj. a1 C a2 C ���C akC1 � k C 1; tedy nerovnost (N) platí také pro n D k C 1. Princip matematické indukce potom říká, že (N) platí pro každé n 2 N. 

Pokud má v indukčním kroku nastat rovnost, tak nutně musí být rovnost i v nerovnosti (N1), a to nastane pouze tehdy, když a1 D 1 nebo a2 D 1. Je-li a1 D 1, pak podmínka a1a2 ��� akC1 D 1 implikuje, že také a2 D 1 (a1 D 1 je totiž podle předpokladu největší číslo z uvažované množiny k C 1 čísel, tj. ai � 1 pro každé i D 1; 2; : : : ; k C 1, a kdyby a2 < 1, pak bychom měli a1a2 ��� akC1 � a2 < 1, což by byl spor). Analogicky, je-li a2 D 1, pak musí být také a1 D 1 (kdyby a1 > 1, tak by muselo platit a1a2 ��� akC1 � a1 > 1, což by byl spor s a1a2 ��� akC1 D 1). Celkově tedy, rovnost v nerovnosti (N2) nastane právě tehdy, když 1 D a1 � ai � a2 D 1 (i D 1; 2; : : : ; k C 1), neboli a1 D a2 D ���D akC1 D 1. Tím je důkaz kompletní. 

Pˇríklad 2.10. Nechť x1; x2; : : : ; xn jsou kladná reálná čísla. Dokažte, že platí 



<!-- Start of picture text -->
x1 C x2 C ���C xn<br>� p n x1xx ��� xn;<br>n<br><!-- End of picture text -->

přičemž rovnost nastane pouze tehdy, když x1 D x2 D ���D xn (jedná se o známou _AG-nerovnost_ , kde levá strana představuje aritmetický průměr čísel x1; : : : ; xn, zatímco pravá strana představuje geometrický průměr). 

_Řešení._ Důkaz je velmi snadný, pokud využijeme výsledku z předchozího příkladu. Položíme-li totiž 



<!-- Start of picture text -->
xi<br>ai D ; i D 1; 2; : : : ; n;<br>p n x1x2 ��� xn<br><!-- End of picture text -->

pak a1a2 ��� an D 1 a nerovnost (N) z příkladu 2.9 ihned dává 



<!-- Start of picture text -->
x1 C x2 C ���C xn D x1 C x2 C ���C xn � n;<br>p n x1x2 ��� xn p n x1x2 ��� xn p n x1x2 ��� xn p n x1x2 ��� xn<br><!-- End of picture text -->

tj. 



<!-- Start of picture text -->
x1 C x2 C ���C xn<br>� p n x1xx ��� xn;<br>n<br><!-- End of picture text -->

což jsme chtěli dokázat. Rovnost nastává pro a1 D a2 D ���D an D 1, tedy pro x1 D x2 D ���D xn. Pˇríklad 2.11. Dokažte, že každá neprázdná podmnožina množiny přirozených čísel má nejmenší prvek (tato vlastnost úzce souvisí s pojmem dobře uspořádané množiny). 

_Řešení._ Nechť M je nějaká neprázdná podmnožina N a nechť vlastnost V.n/ přirozeného čísla n 2 N znamená, že f1; 2; : : : ; ng \ M D ; (jinými slovy, množiny f1; 2; : : : ; ng a M nemají společný žádný prvek). Kdyby vlastnost V.n/ byla pravdivá pro každé n 2 N, tak by to znamenalo, že n … M pro každé n 2 N, a tedy M by byla prázdná množina, což je ve sporu s předpokladem, že M je neprázdná. Vlastnost V.n/ tedy pro nějaké n 2 N neplatí. Uvažujme dále následující dvě tvrzení: 

(i) V.1/ platí; 

2 Stavební prvky matematiky 

15 

(ii) Pro jakékoliv n 2 N, jestliže platí V.n/, pak platí i V.n C 1/. Kdyby byla pravdivá obě tvrzení (i) a (ii), tak by podle principu matematické indukce byla vlastnost V.n/ pravdivá pro každé n 2 N, což již víme, že není. Alespoň jedno z těchto dvou tvrzení tedy není pravdivé. 

Jestliže není pravda (i), tj. není pravda V.1/, tj. není pravda f1g \ M D ;, tak 1 2 M . Jelikož M � N, tak 1 � k pro každé k 2 M , tedy číslo 1 je nejmenším prvkem množiny M . 

Jestliže není pravda (ii), což znamená, že existuje n 2 N takové, že neplatí implikace V.n/ ) V.n C 1/, tak pro toto n platí, že V.n/ je pravda a zároveň V.n C 1/ je nepravda (viz pravdivostní tabulka 1.2). Máme tedy f1; 2; : : : ; ng \ M D ;, ale f1; 2; : : : ; n C 1g \ M ¤ ;. To znamená, že n C 1 2 M , přičemž čísla 1; 2; : : : ; n nepatří do M . Platí tedy n C 1 � k pro každé k 2 M , tj. M má opět nejmenší prvek. 

Rozborem obou případů jsem ukázali, že M má vždy nejmenší prvek. 

Poznámka 2.12. V některých případech je snadnější aplikovat variantu matematické indukce, která se nazývá _silná indukce_ (někdy také _úplná indukce_ ). Zatímco báze indukce je stejná jako doposud, tj. ověřujeme platnost V.1/ (resp. V.n0/), indukční krok spočívá v důkazu implikace „jestliže platí V.i/ pro i D 1; 2; : : : ; k (resp. pro i D n0; n0 C 1; : : : ; k), kde k � 1 (resp. k � n0) je libovolné přirozené číslo, pak platí V.k C 1/“. Princip silné indukce říká, že V.n/ platí pro každé n 2 N (resp. každé n 2 N, n � n0). Pozor, slovo „silná“ se nevztahuje k tomu, že by bylo možné touto variantou indukce dokázat více tvrzení než matematickou indukcí, ale k faktu, že v indukčním kroku je silnější indukční předpoklad (platnost V.k C 1/ nedokazujeme pouze za předpokladu platnosti V.k/, ale za předpokladu platnosti celé sekvence V.1/; V.1/; : : : ; V.k/). Ve skutečnosti jsou matematická a silná indukce ekvivalentní v tom smyslu, že pokud lze nějaké tvrzení dokázat matematickou indukcí, pak je možné jej dokázat i silnou indukcí a naopak, viz příklad 2.14. 

Pˇríklad 2.13. Dokažte _základní větu aritmetiky_ , která říká, že každé přirozené číslo větší jak jedna lze jednoznačně rozložit na součin prvočísel. Přesněji, je-li n 2 N, n > 1, pak existuje právě jedna skupina prvočísel p1 < p2 < ��� < p` a existuje právě jedna skupina přirozených čísel n1; n2; : : : ; n`, přičemž platí 



<!-- Start of picture text -->
n D p1 n1 p 2 n2 ��� p ` n` :<br><!-- End of picture text -->

_Řešení._ Nejprve dokažme existenci takového rozkladu pomocí principu silné indukce. Potřebujeme ukázat, že každé přirozené číslo n > 1 je buď prvočíslo, nebo je součinem prvočísel. Pro číslo n D 2 to platí, protože 2 je prvočíslem (báze indukce je tedy ověřena). Jako indukční předpoklad uvažujme pravdivost uvedené vlastnosti pro každé i D 1; 2; : : : ; k (kde k � 1 je libovolně zvolené přirozené číslo). Číslo k C 1 buď je, nebo není prvočíslo. Pokud je (označme jej p1), tak příslušný rozklad je 



<!-- Start of picture text -->
k C 1 D p1 1:<br><!-- End of picture text -->

Pokud k C 1 není prvočíslo, tak musí existovat dvě přirozená čísla a; b menší jak k C 1 taková, že k C 1 D a � b. Podle indukčního předpokladu platí, že existují dvě skupiny prvočísel a příslušných mocnin takové, že 



<!-- Start of picture text -->
a D p1 n1 p 2 n2 ��� p ` n` ; b D q1 m1 q2 m2 ��� qr mr :<br><!-- End of picture text -->

Po vynásobení rozkladů na pravé straně a případném přeskládání jednotlivých faktorů dostáváme požadovaný rozklad pro k C 1. 

Zbývá dokázat jednoznačnost uvedeného rozkladu, což provedeme sporem. Předpokládejme, že existuje přirozené číslo, které má (alespoň) dva prvočíselné rozklady a vezměme nejmenší možné n 2 N s touto vlastností (toto číslo existuje, protože už víme, že každá neprázdná podmnožina N má nejmenší prvek, viz příklad 2.11). Máme tedy 



<!-- Start of picture text -->
n D p1 n1 p 2 n2 ��� p ` n` D q1 m1 q2 m2 ��� qr mr : (R)<br><!-- End of picture text -->

Vidíme, že p1 dělí q1<sup>m1</sup> q2<sup>m2</sup> ��� qr<sup>mr</sup> . Musí dělit také nějaké qi , to je zaručeno Eukleidovým lemmatem (viz poznámka 2.5). Protože ale p1 a qi jsou prvočísla, musí být p1 D qi . Vzhledem k tomu, že prvočísla pi (resp. qi ) jsou uspořádána vzestupně, máme p1 D qi D q1. Pokud oba rozklady v rovnostech (R) vydělíme číslem p1 dostaneme dva nové různé rozklady nějakého přirozeného čísla n<sup>�</sup> D n=p1 < n, což je však spor s tím, že n bylo minimální číslo, pro které existují dva různé prvočíselné rozklady. 

Kapitola 1. Vybrané statˇe z matematiky 

16 

Pˇríklad 2.14. Dokažte, že principy matematické a silné indukce jsou ekvivalentní. 

_Řešení._ Předpokládejme, že vlastnost V.n/ přirozeného čísla n � n0 2 N lze dokázat principem matematické indukce, tj. tato vlastnost vyhovuje tvrzením: (m1) V.n0/ platí; 

(m2) Pro n D k, kde k � n0 je libovolně zvolené přirozené číslo, je pravdivá implikace V.k/ ) V.k C 1/ 

za předpokladu pravdivosti V.k/. 

Potřebujeme ukázat, že pak lze vlastnost dokázat také principem silné indukce, tj. že platí výroky: (s1) V.n0/ platí; 

(s2) Pro n D k, kde k � n0 je libovolně zvolené přirozené číslo, platí implikace 



<!-- Start of picture text -->
.V.n0/ ^ V.n0 C 1/ ^ ���^ V.k// ) V.k C 1/<br><!-- End of picture text -->

za předpokladu pravdivosti V.n0/; V.n0 C 1/; : : : ; V.k/. Zřejmě (s1) je splněno, protože je to totéž co (m1). Jestliže pro nějaké n D k � n0 budou pravdivé V.n0/; V.n0 C 1/; : : : ; V.k/, tedy samotné V.k/ platí, pak podle (m2) platí V.k C 1/, čímž je dokázáno (s2). 

Nyní naopak předpokládejme, že vlastnost V.n/ je možné dokázat principem silné indukce, tj. že vyhovuje tvrzením (s1) a (s2). Tvrzení (m1) jistě platí, neboť je stejné jako (s1). Definujme novou vlastnost W.n/ přirozeného čísla n � n0 takto: W.n/ platí, jestliže platí V.i/ pro i D n0; n0 C 1; : : : ; n. Nechť n D n0. Protože podle (s1) platí V.n0/, W.n0/ také platí. Nechť nyní n D k, kde k � n0 je libovolně zvolené přirozené číslo, a předpokládejme, že platí W.k/, což znamená, že platí V.n0/; V.n0 C1/; : : : ; V.k/. Podle (s2) pak platí V.k C 1/, neboli platí W.k C 1/. Dokázali jsem tedy platnost implikace W.k/ ) W.k C 1/, tj. (m2) platí pro W.n/. Princip matematické indukce potom říká, že W.n/ platí pro každé n 2 N, n � n0, to ale znamená (vzhledem k definici W.n/), že platí V.n/ pro každé n � n0. Vidíme tedy, že V.n/ lze prostřednictvím W.n/ dokázat i principem matematické indukce. 

Poznámka 2.15. Pro zajímavost zmíníme ještě jednu variantu matematické indukce, nazývanou obvykle _zpětná indukce_ . Ta říká, že vlastnost V.n/ platí pro každé přirozené číslo n � n0 2 N, je-li splněno: (z1) V.n/ platí pro nekonečně mnoho hodnot n D n1; n2; : : : (n0 � n1 < n2 < : : : ); 

(z2) Pro n D k, kde k � n0 je libovolně zvolené přirozené číslo, je-li pravdivé V.k C 1/, pak V.k/ je pravdivé. 

Intuitivně, (z1) říká, že V.n/ platí sice pro nekonečně mnoho přirozených čísel větších jak n0, ale neříká, že pro všechna. Indukční krok (z2) pak „mezery platnosti“ doplní. Skutečně, kdyby existovalo nějaké přirozené číslo n D k � n0 takové, že V.k/ neplatí, tj. platí :V.k/, pak by podle (z2) platilo i :V.k C 1/ (využíváme tautologii z příkladu 1.5a)). Princip matematické indukce by zajistil platnost :V.n/ pro každé n � k, což by bylo ve sporu se (z1). První použití zpětné indukce je přisuzováno Cauchymu<sup>6</sup> , který ji použil při důkazu již zmíněné _AG_ -nerovnosti, viz následující příklad (původní Cauchyho důkaz je pouze nepatrně odlišný). 

Pˇríklad 2.16. Pomocí zpětné indukce dokažte _AG_ -nerovnost, tj. 



<!-- Start of picture text -->
x1 C x2 C ���C xn<br>� p n x1x2 ��� xn; xi > 0; i D 1; 2; : : : ; n;<br>n<br><!-- End of picture text -->

(viz také příklad 2.10). Případ n D 1 je triviální, nechť tedy n � 2 a dokažme nejprve, že tvrzení platí pro nekonečně mnoho hodnot n � 2. To provedeme principem matematické indukce. Báze indukce (případ n D 2) platí, protože když v nerovnosti z příkladu 2.2 položíme a D<sup>~~p~~</sup> <u>x1</u> a b D<sup>~~p~~</sup> <u>x2, tak tato nerovnost</u> ihned dává 



<!-- Start of picture text -->
x1 C x2<br>� p x1x2:<br>2<br><!-- End of picture text -->

Jako indukční předpoklad uvažujme platnost _AG_ -nerovnosti pro n D m, kde m � 2 je libovolně zvolené přirozené číslo, a ukažme, že pak tato nerovnost platí také pro n D 2m. Vyjdeme-li z aritmetického průměru pro n D 2m, pak 



<!-- Start of picture text -->
x1 C x2 C ���C x2m D 1 C xmC1 C xmC2 C ���C x2m<br>2m 2 � x1 C x2 C ���Cm  xm m �<br><!-- End of picture text -->

6Augustin Loius Cauchy 1789–1857, Francouz 

2 Stavební prvky matematiky 

17 



<!-- Start of picture text -->
m p x1x2 ��� xm C m p xmC1xmC2 ��� x2m<br>�<br>2<br>� q m p x1x2 ��� xm m p xmC1xmC2 ��� x2m D 2m p x1x2 ��� x2m;<br><!-- End of picture text -->

kde nerovnost na druhém řádku plyne z indukčního předpokladu a nerovnost na třetím řádku z báze indukce. Báze indukce říká, že nerovnost platí pro n D 2. Indukční krok potom dává platnost pro n D 2; 4; 8; : : : , tj. ověřili jsme, že _AG_ -nerovnost platí pro n D 2<sup>k</sup> , k 2 N, tedy pro nekonečně mnoho hodnot n, což je požadováno v (z1). 

Nyní můžeme přistoupit ke zpětné indukci. Jako indukční předpoklad vezměme platnost _AG_ -nerovnosti pro n D k C 1, kde k � 2 je libovolně zvolené přirozené číslo, a dokažme její platnost pro n D k. Protože nerovnost má platit pro libovolné hodnoty xi > 0, i D 1; 2; : : : ; k C 1, tak speciálně bude platit také, pokud položíme 



<!-- Start of picture text -->
xkC1 D x1 C x2 C ���C xk :<br>k<br><!-- End of picture text -->

Máme tedy 



<!-- Start of picture text -->
x1 C x2 C ���C xk C xkC1 D x1 C x2 C ���C xk C x1Cx2 k C���Cxk<br>k C 1 k C 1<br>D .k C 1/.x1 C x2 C ���C xk/ D x1 C x2 C ���C xk<br>k.k C 1/ k<br>kC1 x1 C x2 C ���C xk<br>� kC p 1 x1x2 : : : xkxkC1 D x1x2 : : : xk :<br>r k<br><!-- End of picture text -->

Vzniklou nerovnost (kterou jsme obdrželi z indukčního předpokladu) lze ekvivalentně psát jako 



<!-- Start of picture text -->
x1 C x2 C ���C xk<br>� x1x2 : : : xk ;<br>� x1 C x2 C ���Ck  xk �kC1 k<br><!-- End of picture text -->

což, po pokrácení faktorem<sup>x1Cx2</sup> k<sup><u>C���Cxk</u></sup> a odmocnění k-tou odmocninou, dává 



<!-- Start of picture text -->
x1 C x2 C ���C xk<br>� p k x1x2 : : : xk:<br>k<br><!-- End of picture text -->

Platnost _AG_ -nerovnosti pro každé n � 2 pak plyne z principu zpětné indukce (připomeňme, že pro n D 1 platí také, tento případ je triviální). 

Poznámka 2.17. a) Existuje ještě několik dalších variací na téma matematická indukce. 

b) Z uvedených příkladů je zřejmé, že existují tvrzení, která je možné dokázat vícero způsoby, to jsme ilustrovali např. na _AG_ -nerovnosti (existuje dokonce několik dalších způsobů, jak tuto nerovnost dokázat). 

c) Ne každé tvrzení lze dokázat výše uvedenými metodami, např. některé věty typu „9x 2 M W V.x/“. Zde je potřeba (nějak) nalézt takové x (konstruktivní důkaz) nebo, když to nelze, tak prokázat, že x musí existovat (existenční důkaz). Naopak, pokud potřebujeme prokázat neplatnost tvrzení 8x 2 M W V.x/, stačí nalézt x, při kterém neplatí V.x/. Tomu se potom říká, že jsme ukázali (nalezli) _protipříklad_ . 

V této sekci se již ve větší míře vyskytovaly pojmy, jako jsou podmnožina, prázdná množina, nejmenší prvek apod. Spolu s tím jsme použili symbol pro průnik, pro ostrou a neostrou nerovnost, množiny přirozených a reálných čísel byly značeny N a R atd. Tyto pojmy a symboly budou přesněji zavedeny v následujících sekcích. 

#### Pˇríklady k procviˇcení 

2.1. Dokažte nepřímo 8n 2 N W 7jn<sup>2</sup> ) 7jn. _Nápověda._ V argumentaci využijte základní větu aritmetiky (viz příklad 2.13). 

2.2. Dokažte sporem, že číslo ~~p~~ 7 je iracionální. _Nápověda._ Využijte tvrzení z předchozího příkladu. 

Kapitola 1. Vybrané statˇe z matematiky 

18 

2.3. Dokažte přímo i matematickou indukcí: 8n 2 N: 2j.n<sup>2</sup> � n/. 

2.4. Dokažte přímo, že pro každé n 2 N platí 



<!-- Start of picture text -->
n 1 n 1 1<br>X Nápověda.  Využijte rovnosti<br>j.j C 1/ D n C 1 : j.j C 1/ D j 1 � j C 1 :<br>j D1<br><!-- End of picture text -->

- 2.5. Dokažte rovnost z předchozího příkladu také matematickou indukcí. 

2.6. Matematickou indukcí dokažte, že pro n 2 N, n � 2, platí nerovnost 



<!-- Start of picture text -->
1 1 1<br>1 C p 2 C p 3 C ���C p n > p n:<br><!-- End of picture text -->

### 3 Množiny 

_Množina_ je primitivní pojem, lze ji popsat jako soubor objektů, které nazýváme prvky množiny (prvky se v množině neopakují a nezáleží na pořadí, v jakém je zapíšeme). Množiny značíme obvykle velkými písmeny a její prvky malými. Zápis a 2 A značí, že prvek a patří (náleží) do množiny A. Podobně, b 62 A znamená, že prvek b nepatří do A. Množina je obvykle určena výčtem jejích prvků nebo řečením charakteristické vlastnosti prvků množiny, např. A D fa; b; cg, B D fx W x je sudég. U zadání množiny charakteristickou vlastností je třeba dbát jisté obezřetnosti, může totiž dojít k _paradoxu_ . Asi nejznámější příklad byl objeven roku 1901 a je znám jako _Rusellův_<sup>_7_</sup> _paradox_ . Uvažujme množinu (označme ji např. M ), která obsahuje právě ty množiny, které neobsahují samy sebe (jako svůj prvek). Tj. M D fA W A … Ag. Jak je to se samotnou množinou M ? Pokud neobsahuje samu sebe, pak M 2 M . Na druhou stranu, když M 2 M (tj. M je prvkem M ), pak M obsahuje samu sebe. Podle definice M 62 M . Nelze tedy rozhodnout, zda M je nebo není prvkem M . Právě takové důvody vedly na začátku 20. století ke vzniku axiomatické teorie množin, ve které jsou dána přesná pravidla o tom, co množina je a co není. V současnosti je nejpoužívanější _Zermelova_<sup>_8_</sup> _–Fraenkelova_<sup>_9_</sup> _teorie množin_ . 

- Definice 3.1 — množinových operací a souvisejících pojm˚u. a) _Prázdná množina_ : je to množina, která neobsahuje žádné prvky, značíme ji ; nebo fg; 

- b) _Podmnožina_ : Řekneme, že množina A je podmnožinou množiny B (píšeme A � B, znaku � se říká _inkluze_ ), jestliže platí, že každý prvek a 2 A je zároveň prvkem množiny B, formálně zapsáno: A � B, jestliže 8a W a 2 A ) a 2 B; 

- c) _Rovnost množin:_ A D B, jestliže .A � B/ ^ .B � A/; 

- d) _Vlastní podmnožina:_ A � B, jestliže .A � B/ ^ .A ¤ B/; 

- e) _Sjednocení množin:_ A [ B WD fa W a 2 A _ a 2 Bg (čteme A sjednoceno s B); 

- f) _Průnik množin:_ A \ B WD fa W a 2 A ^ a 2 Bg (čteme A průnik B), množiny A; B nazveme _disjunktní_ , jestliže A \ B D ;; 

- g) _Doplněk množiny:_ je-li A � U (universum), pak doplněk množiny A v množině U definujeme jako A<sup>0</sup> WD fu 2 U W u 62 Ag; 

- h) _Rozdíl množin:_ A n B WD fa 2 A W a 62 Bg (značí se také A � B); 

- i) _Symetrický rozdíl množin:_ A4B WD .A n B/ [ .B n A/ (značí se také A � B nebo A � B). 

- Poznámka 3.2. 1. Pozor na zápis f;g! To není prázdná množina, ale jednoprvková množina, jejímž prvkem je prázdná množina. 

2. Pro libovolnou množinu A vždy platí ; � A a A � A. 

Pˇríklad 3.3. Mějme množiny A D fa; b; c; e; j g, B D fa; c; e; gg. Určete: a) Je B podmnožina A?, b) A \ B, c) A [ B, d) A n B, e) A4B. 

> 7Bertrand Russell 1872–1970, Velšan 

> 8Ernst Zermelo 1971–1953, Němec 

> 9Adolf Fraenkel 1891–1965, Izraelec narozený v Německu 

3 Množiny 

19 

_Řešení._ ad a) Není, protože g 62 A. ad b) A \ B D fa; c; eg. ad c) A [ B D fa; b; c; e; g; j g. ad d) A n B D fb; j g. ad e) B n A D fgg ) A4B D fb; g; j g. 

Na obrázku 3.1 jsou znázorněny některé z výše uvedených množinových operací pomocí Vennových<sup>10</sup> diagramů. 



<!-- Start of picture text -->
A B A B A B A B U<br>A<br>A \ B A [ B A n B A4B A 0<br><!-- End of picture text -->

Obrázek 3.1: Vennovy diagramy znázorňující průnik, sjednocení, rozdíl a symetrický rozdíl dvou množin A a B. Poslední diagram pak představuje doplněk množiny A v universu U 

Vedle Vennových diagramů se používají také Eulerovy<sup>11</sup> diagramy, rozdíl mezi oběma uvedenými bude patrný z následujícího příkladu. 

Pˇríklad 3.4. Mějme balíček karet a uvažujme množinu A všech červených karet, množinu B všech černých karet a množinu C všech srdcových karet. Načrtněte pro tyto množiny Eulerův a Vennův diagram. 



<!-- Start of picture text -->
B A B<br>␆<br>␆<br>␄<br>A ␅<br>␅<br>␄ C ␃<br>␃<br>C<br><!-- End of picture text -->

Obrázek 3.2: Eulerův (vlevo) a Vennův (vpravo) diagram k příkladu 3.4. Platí C � A, A \ B D ;, C \ B D ; 

Z obrázku 3.2 je zřejmé, že zatímco Eulerův diagram uvažuje pouze (v dané situaci) relevantní vztahy mezi množinami, Vennův diagram musí obsahovat všechny možné vztahy (průnik, sjednocení atd.) mezi množinami. Na stejném diagramu lze tedy modelovat různé situace. V případě Vennova diagramu je tedy potřeba kruhy (nebo jiné tvary) reprezentující jednotlivé množiny kreslit tak, aby se objevila pole představující všechny možné průniky daných množin. Uvažujeme-li n množin, pak je těchto polí 2<sup>n</sup> � 1 (pokud jsou uvažované množiny podmnožinami nějakého universa U , pak 2<sup>n</sup> -té pole znázorňuje doplněk sjednocení těchto množin). V případě čtyř množin již nemusí být úplně zřejmé, jak množiny zakreslit, abychom dostali všech 2<sup>4</sup> � 1 D 15 průniků. Dvě možnosti, jak to provést, jsou znázorněny na obrázku 3.3. 



<!-- Start of picture text -->
A B B C<br>C A D<br>D<br><!-- End of picture text -->

Obrázek 3.3: Dvě možnosti Vennova diagramu pro čtyři množiny 

Definice 3.5 — potenˇcní množiny. Nechť A je libovolná množina. Potom množinu všech podmnožin množiny A nazveme _potenční množinou množiny_ A, značíme 2<sup>A</sup> . 

> 10John Venn 1834–1923, Angličan 

> 11Leonhard Paul Euler 1707–1783, Švýcar 

Kapitola 1. Vybrané statˇe z matematiky 

20 

Pˇríklad 3.6. Mějme množinu A D f□; 4; ıg. Určete 2<sup>A</sup> . 

_Řešení._ 2<sup>A</sup> D f;; f□g; f4g; fıg; f□; 4g; f□; ıg; f4; ıg; f□; 4; ıgg – 2<sup>3</sup> prvků. 

■ Vˇeta 3.7. _Nechť_ A; B; C; U _jsou množiny. Pak platí:_ 

- a) A [ B D B [ A _a_ A \ B D B \ A _(komutativita);_ 

- b) A [ .B [ C/ D .A [ B/ [ C _a_ A \ .B \ C/ D .A \ B/ \ C _(asociativita);_ 

- c) A [ .B \ C/ D .A [ B/ \ .A [ C/ _a_ A \ .B [ C/ D .A \ B/ [ .A \ C/ _(distributivita);_ 

- d) _Je-li_ A; B � U _, pak_ .A [ B/<sup>0</sup> D .A<sup>0</sup> \ B<sup>0</sup> / _a_ .A \ B/<sup>0</sup> D .A<sup>0</sup> [ B<sup>0</sup> / _(de Morganovy zákony);_ 

- e) _Je-li_ A � B _a_ B � C _, pak_ A � C _(tranzitivita inkluze)._ 

_Důkaz._ ad a) Podle definice je A [ B je množina všech prvků, které leží v A nebo B. B [ A je ale definováno stejně. 

ad b) „�“: Nechť a 2 A[.B [C/. To znamená, že a 2 A_a 2 .B [C/ a tedy a 2 A_.a 2 B _a 2 C/. Protože ale platí asociativita pro logické „nebo“, viz příklad 1.5h), máme .a 2 A _ a 2 B/ _ a 2 C , tj. a 2 .A [ B/ [ C . Dokázali jsme tedy inkluzi A [ .B [ C/ � .A [ B/ [ C . Obrácená inkluze se ukáže analogicky, stejně tak asociativita průniku. 

ad c) „�“: Nechť a 2 A [ .B \ C/. Podle definice sjednocení a 2 A _ a 2 .B \ C/. Pokud a 2 A, tak je určitě také v .A [ B/ a zároveň v .A [ C/, tj. a 2 .A [ B/ \ .A [ C/. Pokud a 2 .B \ C/, tak a 2 B ^a 2 C . Potom ale musí platit a 2 .A[B/^a 2 .A[C/, což znamená, že a 2 .A[B/\.A[C/. Celkově tedy platí inkluze A [ .B \ C/ � .A [ B/ \ .A [ C/. Obrácená inkluze a druhý distributivní zákon se dokáží analogicky. 

ad d) „�“: Nechť a 2 .A [ B/<sup>0</sup> , tedy a 2 U , a 62 .A [ B/. To znamená :.a 2 A _ a 2 B/. To ale podle De Morganova zákona pro logické nebo je :.a 2 A/ ^ :.a 2 B/, tedy a 62 A ^ a 62 B ) a 2 A<sup>0</sup> ^ a 2 B<sup>0</sup> ) a 2 .A<sup>0</sup> \ B<sup>0</sup> /. Obrácená inkluze a druhý De Morganův zákon se ukáží obdobně. 

ad e) Nechť a 2 A je libovolné. Protože A � B znamená, že a 2 A ) a 2 B, máme a 2 B. Protože ale také B � C , máme a 2 B ) a 2 C , tedy a 2 C . Díky tranzitivitě implikace (viz příklad 1.7b) tedy platí a 2 A ) a 2 C , což znamená, že A � C . 

Poznámka 3.8. Vlastnosti uvedené ve větě 3.7 je možné graficky znázornit opět pomocí Vennových diagramů. 

#### Pˇríklady k procviˇcení 

3.1. Během jednoho roku vystoupila dvakrát v jednom městě známá rocková skupina. Koncertu této skupiny se aspoň jednou zúčastnilo 290 rockerů, právě jednou 200 rockerů. Počet rockerů, kteří byli pouze na prvním koncertu, je třikrát větší než počet rockerů, kteří byli pouze na druhém koncertu. Kolik rockerů bylo na prvním a kolik na druhém koncertu? 

3.2. Ve městě jsou linky autobusů A, B a C . Na lince A je 18 zastávek, na lince B je 20 zastávek a na lince C 25 zastávek. Počet společných stanic na linkách A; B je stejný jako na A; C , a to o 2 méně než na linkách B a C . Samostatných zastávek na lince A je 10, stejně tak na lince B. Zastávek na A nebo B, kde nestaví C , je 22. Kolik je zastávek, kde staví všechny 3 autobusy a kolik je všech zastávek ve městě? 

3.3. Uvažujte množiny A D fn 2 N W n < 7g a B D fx 2 R W x � 5g. Napište množiny A [ B, A \ B, A n B a B n A. 

3.4. Pomocí Vennových diagramů znázorněte množiny: 

   - a) A [ .B [ C/; 

   - b) A \ .B [ C/; 

   - c) .A [ B/ n C ; 

   - d) .A \ B/ n C . 

- 3.5. Rozhodněte, zda platí .A n B/ n C D A n .B n C/. 

21 

4 Relace 

3.6. Dokažte, že pro libovolné dvě množiny A; B platí: 

a) A � B , A [ B D BI b) A � B , A \ B D A: 

_Výsledky._ 3.1. Na prvním 240, na druhém 140. 3.2. Společné zastávky jsou 4, celkem je 47 zastávek. 3.5. Neplatí. 

### 4 Relace 

Relace představuje matematický ekvivalent pojmu vztah. 

Definice 4.1 — kartézského souˇcinu. _Kartézský součin_ množin A; B (v tomto pořadí) je množina A � B WD fŒa; b� W a 2 A ^ b 2 Bg (Œa; b� je zde uspořádaná dvojice). 

Pˇríklad 4.2. Napište kartézské součiny A � B a B � A množin A D fa; bg, B D f□; 4; ıg. 

_Řešení._ A � B D fŒa; □�; Œa; 4�; Œa; ı�; Œb; □�; Œb; 4�; Œb; ı�g; B � A D fŒ□; a�; Œ□; b�; Œ4; a�; Œ4; b�; Œı; a�; Œı; b�g. 

Zřejmě tedy A � B ¤ B � A, rovnost platí pouze v případě, kdy A D B nebo alespoň jedna z A; B je prázdná množina. 

Definice 4.3 — binární relace. _Binární relací_ R mezi množinami A; B nazýváme libovolnou podmnožinu kartézského součinu A � B, tj. R � A � B. Zápis aRb (nebo Œa; b� 2 R) čteme jako „a je v relaci s b “. Naopak :.aRb/ bude znamenat, že a není v relaci s b (budeme psát stručně aRb). Je-li A D B, hovoříme o relaci na množině A, tj. R � A<sup>2</sup> (A<sup>2</sup> WD A � A). 

Pˇríklad 4.4. Mějme množiny s relací R: a) A D fa; b; cg, B D f1; 2; 3g, R představuje vztah „písmeno – pořadí písmene v abecedě“; b) A D N, B D N, R je definována tak, že a je v relaci s b, jestliže a < b; c) A je potenční množina množiny f1; 2g a R na A představuje vztah „být vlastní podmnožinou“. Vypište ve všech případech R. 

_Řešení._ Ad a) R D fŒa; 1�; Œb; 2�; Œc; 3�g. Ad b) R D fŒ1; 2�; Œ1; 3�; : : : ; Œ2; 3�; Œ2; 4�; : : : g. Ad c) R D fŒ;; f1g�; Œ;; f2g�; Œ;; f1; 2g�; Œf1g; f1; 2g�; Œf2g; f1; 2g�g. 

Definice 4.5 — významných relací na množinˇe. Nechť R je relace na neprázdné množině A. Řekneme, že R je: 

a) _reflexivní_ , jestliže 8a 2 A W aRa; b) _ireflexivní_ , jestliže 8a 2 A W aRa; 

c) _symetrická_ , jestliže 8a; b 2 A W aRb ) bRa; 

d) _antisymetrická_ , jestliže 8a; b 2 A W aRb ^ bRa ) a D b; 

e) _asymetrická (silně antisymetrická)_ , jestliže 8a; b 2 A W aRb ) bRa; 

f) _tranzitivní_ , jestliže 8a; b; c 2 A W aRb ^ bRc ) aRc. 

Příkladem reflexivity (každý prvek musí být v relaci sám se sebou) je rovnost na N nebo dělitelnost na N (aRb , ajb). Naopak relace „menší než“ na N není reflexivní (a < a neplatí), je ireflexivní. Příkladem symetrie je např. relace „být sourozencem“. Již zmíněná relace „menší než“ symetrická není (nemůže být zároveň a < b a b < a) je to antisymetrická relace. Pozor, antisymetrie není opakem symetrie, relace může být symetrická i antisymetrická zároveň, např. zmíněná rovnost na N. Relace je asymetrická , je ireflexivní a antisymetrická. Příkladem asymetrie je opět relace „menší než“, ale např. relace „menší nebo rovno“ asymetrická není (není totiž ireflexivní). Relace „být sourozencem“ je také příkladem tranzitivní relace. Relace, která není tranzitivní je např. „být matkou své dcery“ (pokud Alena je matkou Jany a Jana matkou Heleny, tak Alena není matkou Heleny, je babičkou). 

Kapitola 1. Vybrané statˇe z matematiky 

22 

Pˇríklad 4.6. Je dána množina A D fa; b; c; d g a relace R D fŒa; b�; Œb; a�; Œb; b�; Œb; c�g. Zjistěte, zda R je reflexivní, symetrická, tranzitivní. 

_Řešení._ Relace je znázorněna v následující tabulce. 

||a|b|c|d||
|---|---|---|---|---|---|
|a||~~p~~|||Relace není reflexivní (na diagonále by musely být samé „<sup>p</sup>“). Není|
|b|~~p~~|~~p~~|~~p~~||symetrická, tabulka by musela být symetrická podle diagonály. Není|
|c<br>d|||||ani tranzitivní (aRb,bRc, alea<br>Rc).|



Definice 4.7 — relace ekvivalence. Relace, která je reflexivní, symetrická a tranzitivní se nazývá _ekvivalencí_ . 

Příkladem relace ekvivalence je „obce ČR náležející stejnému kraji“ (obec a je v relaci s obcí b, jestliže a i b leží ve stejném kraji), rozmyslete si proč. 

Definice 4.8 — rozkladu množiny. Nechť A ¤ ;. _Rozkladem množiny_ A se nazývá množina _A_ � 2<sup>A</sup> (jedná se tedy o podmnožinu potenční množiny), která splňuje: a) ; … _A_ ; 

b) Pokud M1; M2 2 _A_ , pak buď M1 D M2, nebo M1 \ M2 D ; (tj. M1 a M2 jsou _disjunktní_ ); c)<sup>S</sup> M 2 _A_<sup>MD A.</sup> 

Prvkům množiny _A_ se říká _třídy rozkladu_ . 

- Vˇeta 4.9. 1. _Nechť_ R _je relace ekvivalence na množině_ A _. Pro každé_ a 2 A _definujme množinu_ Œa� WD fb 2 A W aRbg _(tzv. třídu ekvivalence) a označme A_ R WD fŒa� W a 2 Ag _. Pak A_ R _je rozklad množiny_ A _._ 

2. _Nechť A je rozklad množiny_ A _. Definujme relaci_ R _A tak, že_ aR _A_ b _, jestliže_ 9M 2 _A taková, že_ a; b 2 M _. Potom_ R _A je relace ekvivalence._ 

_Důkaz._ Ad 1. Nechť R je relace ekvivalence na A. Ukažme, že množina _A_ R je rozklad A (tj. ověřme body a)–c) z definice 4.8). 

a) Pro každé Œa� 2 _A_ R je Œa� ¤ ;, protože a 2 Œa�. 

b) Nechť Œa�; Œb� 2 _A_ R a ukažme, že když Œa� \ Œb� ¤ ;, pak Œa� D Œb�. Jestliže Œa� \ Œb� ¤ ;, pak existuje c 2 A takové, že c 2 Œa� a zároveň c 2 Œb�. Podle definice Œa�, Œb� to znamená, že aRc ^ bRc, a tedy také cRb z důvodu symetrie R. Protože R je tranzitivní, platí aRb a také bRa opět z důvodu symetrie. „Œa� � Œb�:“ Nechť p 2 Œa�. Pak aRp a dále bRa (viz výše). Protože R je tranzitivní, máme bRp, což znamená, že p 2 Œb�. „�:“ Nechť p 2 Œb�. Pak bRp a také aRb (viz výše). Tranzitivita dává aRp, tedy p 2 Œa�. Celkově tedy Œa� D Œb�. 

c) Platí<sup>S</sup> Œa�2 _A_ R<sup>Œa�D A, protože a 2 Œa�pro všechna a 2 A.</sup> 

Ad 2. Nechť _A_ je rozklad množiny A. Ukažme, že R _A_ je relace ekvivalence na A. 

Reflexivita: Buď a 2 A libovolné. Protože _A_ je rozklad na A, musí existovat M 2 _A_ taková, že a 2 M (jinak spor s podmínku c) z definice 4.8). Proto aR _A_ a, tj. R _A_ je reflexivní. 

Symetrie: Nechť aR _A_ b. Podle definice R _A_ pak existuje M 2 _A_ taková, že a; b 2 M . To ale znamená, že také bR _A_ a, tedy R _A_ je symetrická. 

Tranzitivita: Nechť aR _A_ b a bR _A_ c. Podle definice R _A_ existují množiny M1, M2 2 _A_ takové, že a; b 2 M1 a b; c 2 M2. Protože M1 \ M2 ¤ ;, musí být M1 D M2, viz podmínka b) z definice 4.8. Tedy a; c 2 M1 D M2 a podle definice R _A_ je aR _A_ c. 

Poznámka 4.10. Uvedené přiřazení rozkladu _A_ R relaci R (resp. přiřazení relace R _A_ rozkladu _A_ ) je jednoznačné v tom smyslu, že máme R _A_ R D R (resp. _A_ R _A_ D _A_ ). 

23 

4 Relace 

Pˇríklad 4.11. Uvažujte relaci R na N, ve které aRb, jestliže a C b je sudé. Je R ekvivalencí? Pokud ano, napište příslušný rozklad. 

_Řešení._ Relace R je reflexivní, protože 8a 2 N je a C a D 2a je sudé. R je i symetrická, protože když a C b je sudé, tak b C a je také sudé (komutativita sčítání). Ukažme, že R je i tranzitivní, tj. je-li a C b sudé a zároveň b C c sudé, tak nutně a C c bude sudé. Platí vlastnost, že a C b sudé, právě když a i b jsou obě sudá nebo obě lichá (ověřte!!). Případ 1: a i b je sudé. Potom, je-li b C c sudé, tak c je také sudé, protože b je sudé. Protože nyní a i c jsou sudé, tak a C c je také sudé. Případ 2: a i b je liché. Je-li b C c sudé, tak c musí být liché, protože b je liché. Nyní jsou a i c lichá a tedy a C c je sudé. Celkově, R je tranzitivní. Rozklad se potom skládá ze dvou tříd f1; 3; 5; : : : g a f2; 4; 6; : : : g. 

Definice 4.12 — uspoˇrádání. Relace na množině A, která je reflexivní, antisymetrická a tranzitivní se nazývá _uspořádání_ (přesněji _neostré částečné uspořádání_ ). Značíme �. 

Tuto relaci chápeme stejně jako v běžném slova smyslu, např. uspořádaní potravin podle ceny – je-li rohlík levnější než chleba, stěží chtít, aby byl chleba levnější než rohlík (antisymetrie). Je-li dále chleba levnější než kilo párků, tak zjevně rohlík je také levnější než kilo párků (tranzitivita). Konečně reflexivita říká, že rohlík stojí méně nebo stejně jako rohlík. Proč hovoříme o částečném uspořádání? V částečném uspořádání nemusí být každé dva prvky porovnatelné! Vezměme například relaci uspořádaní, kde A � B, jestliže A � B (množiny A; B jsou prvky nějaké množiny). Je-li A D fa; bg, B D fa; b; cg, pak jistě A � B, protože A � B. Je-li ale např. A D fa; bg, B D fa; cg, pak A 6� B a B 6� A, tj. neplatí A � B ani B � A, takové dva prvky tedy nejdou porovnat. 

Definice 4.13 — ostrého uspoˇrádání. Relace na A, která je ireflexivní a tranzitivní se nazývá _ostré uspořádání_ . Značíme �. 

Příkladem ostrého uspořádání je relace „menší než“ na N, tj. a � b, jestliže a < b. V ostrém uspořádání opět nemusí být každé dva prvky porovnatelné. Poznamenejme ještě, že ireflexivita a tranzitivita implikují antisymetrii. Skutečně, předpokládejme, že v relaci jsou „symetrické dvojice“, tj. máme aRb ^ bRa. Pak tranzitivita dává aRb ^ bRa ) aRa, což je ale spor s ireflexivitou. Případ aRb ^ bRa tedy nastat nemůže, a proto je podmínka v definici antisymetrické relace splněna triviálně (předpoklad aRb ^ bRa v implikaci je nepravdivý, a tedy implikace aRb ^ bRa ) a D b je pravdivá, viz pravdivostní tabulka v kapitole 1). Ostré uspořádání je tedy dokonce asymetrická relace (protože je ireflexivní a antisymetrická). 

Definice 4.14 — dalších významných relací. Relace R na množině A, která je a) definována R WD fŒa; a� W a 2 Ag, se nazývá _identická relace_ (značí se obvykle idA); b) definována R WD A � A, se nazývá _univerzální relace_ ; 

c) definována vlastností 8a; b 2 A W aRb _ bRa, se nazývá _úplná relace_ ; 

d) definována vlastností 8a; b 2 A W aRb _ bRa _ a D b, se nazývá _trichotomická relace_ ; e) částečným neostrým uspořádáním a úplná, se nazývá _lineární (úplné) uspořádání_ . f) ostrým uspořádáním a navíc trichotomická, se nazývá _ostré lineární (úplné) uspořádání_ . 

Relace identity je nejmenší (ve smyslu množinových inkluzí) relací ekvivalence. Naopak největší relací ekvivalence je univerzální relace. Vezměme např. A D f□; 4g. Potom příkladem trichotomické relace na A je R D fŒ□; □�; Œ□; 4�g. Tato relace ale není úplná, aby byla úplná, musela by obsahovat ještě dvojici Œ4; 4�. Příkladem lineárního uspořádání je relace „�“ na N a příkladem ostrého lineárního uspořádání je relace „<“ na N. V lineárním uspořádání jsou každé dva prvky porovnatelné. 

Poznámka 4.15. Je-li � relace uspořádání na množině A, pak relace � definovaná a � b, jestliže a � b ^ a ¤ b (množinově �WD �n idA), se nazývá _ostré uspořádání odvozené z uspořádání_ �. Zřejmě platí 8a; b 2 A: a � b ) a � b (tato implikace plyne ihned z právě uvedené definice, ta říká, že má-li být uspořádaná dvojice prvků v relaci �, tak musí být také v relaci �; je to vidět ihned i z množinového vyjádření, protože ���). Není až tak těžké ověřit, že takto definovaná relace je skutečně ostrým 

Kapitola 1. Vybrané statˇe z matematiky 

24 

uspořádáním (ve smyslu definice 4.13), viz následující příklad. Podobně, vyjdeme-li z relace ostrého uspořádaní � na množině A a definujeme relaci � jako a � b, jestliže a � b _ a D b (množinově �WD �[ idA), pak se � nazývá _(částečné) uspořádání odvozené z ostrého uspořádání_ �. Fakt, že se jedná skutečně o relaci uspořádání (ve smyslu definice 4.12), by se ukázal podobně jako v příkladu 4.16. 

Pˇríklad 4.16. Ukažte, že relace � ostrého uspořádání odvozeného z uspořádání � je skutečně ostrým uspořádáním, tj. tranzitivní a ireflexivní relace. 

_Řešení._ Dokažme nejprve vlastnost 



<!-- Start of picture text -->
8a; b; c 2 A W . .a � b ^ b � c/ _ .a � b ^ b � c/ / ) a � c: (V)<br><!-- End of picture text -->

Již víme, že platí implikace a � b ) a � b a díky tautologii .P ) Q/ ) ..P ^ R/ ) .Q ^ R// (ověřte!) platí také implikace .a � b ^ b � c/ ) .a � b ^ b � c/. Protože relace � je tranzitivní, platí dále .a � b ^ b � c/ ) .a � c/. Celkově tedy .a � b ^ b � c/ ) .a � c/ (využili jsme zde tranzitivitu implikace). Zároveň ale nemůže být a D c, protože pak bychom měli 

.a � b ^ b � a/ ) .a � b ^ b � a/ ) a D b 

z důvodu, že � je antisymetrická relace. To je ale spor s a � b (v relaci � musí být a ¤ b). Celkově tedy platí implikace .a � b ^ b � c/ ) a � c: Analogicky bychom ukázali, že platí .a � b ^ b � c/ ) a � c: Dohromady dávají tyto dvě implikace vlastnost (V). 

Nyní již snadno ukážeme tranzitivitu relace �. Skutečně, s využitím výše uvedené tautologie máme 

.a � b ^ b � c/ ) .a � b ^ b � c/ ) a � c: 

Relace je zřejmě také ireflexivní, protože kdyby a � a, pak by podle definice a ¤ a, což je spor. 

Definice 4.17 — složení relací. Nechť R � A � B, S � B � C . _Složením relací_ R _a_ S (v tomto pořadí) se nazývá relace S ı R � A � C definovaná S ı R WD fŒa; c� 2 A � C W 9b 2 B takové, že aRb ^ bScg (čteme „R složeno s S “ nebo „S po R“). 

Pˇríklad 4.18. Uvažujme relace 

R D fŒJan; Petr�; ŒPavel; Roman�g – relace otec–syn, 

S D fŒPetr; Jana�; ŒPetr; Hana�; ŒRoman; Lucie�g – relace bratr–sestra. 

Napište S ı R a interpretujte tuto relaci. 

_Řešení._ S ı R D fŒJan; Jana�; ŒJan; Hana�; ŒPavel; Lucie�g – relace otec–dcera. 

Definice 4.19 — inverzní relace. Nechť R je relace mezi množinami A a B. _Inverzní relací_ k R nazveme relaci R<sup>�1</sup> mezi B a A, pro kterou platí: 8a 2 A; 8b 2 B W bR<sup>�1</sup> a , aRb. 

Pˇríklad 4.20. A D fMarek; Norbert; Otag, B D f25; 50; 38g, R D fŒMarek; 50�; ŒOta; 25�g. Napište R<sup>�1</sup> . 

_Řešení._ R<sup>�1</sup> D fŒ50; Marek�; Œ25; Ota�g. 

Poznámka 4.21. Pro inverzi složené relace platí .S ı R/<sup>�1</sup> D R<sup>�1</sup> ı S<sup>�1</sup> . Skutečně, je-li c.S ı R/<sup>�1</sup> a, pak aS ı Rc, tj. podle definice složené relace existuje b 2 B takové, že aRb ^ bSc. To ale znamená, že cS<sup>�1</sup> b ^ bR<sup>�1</sup> a, neboli cR<sup>�1</sup> ı S<sup>�1</sup> a. 

Poznámka 4.22. Vedle binární relace je možné uvažovat obecněji n-nární relaci (n D 1; 2; 3; : : : ) jakožto libovolnou podmnožinu kartézského součinu A1 � A2 ����� An. 

5 Zobrazení 

25 

#### Pˇríklady k procviˇcení 

4.1. Jsou dány množiny A D f2; 3; 10g a B D f2; 7; 8g. Rozhodněte, zda množina C D fŒ2; 2�; Œ2; 7�; Œ7; 3�g je relací mezi množinami A a B. 

4.2. Uvažujte relaci R D fŒx; y� 2 R � R W y<sup>2</sup> � 4x D 0g. Rozhodněte, zda uspořádané dvojice Œ�1; 3� a Œ9; 6� jsou prvky relace R. 

4.3. Na množině A D f□; 4; ?; ıg je dána relace 

R D fŒ□; □�; Œ□; ı�; Œ□; ?�; Œ4; 4�; Œı; □�; Œı; ı�; Œı; ?�; Œ?; □�; Œ?; ı�; Œ?; ?�g: 

Rozhodněte, zda R je relací ekvivalence, pokud ano, tak napište příslušný rozklad množiny A. 

4.4. Nechť A je množina všech slov a R je relace „stejně dlouhé slovo“, tj. slovo a je v relaci se slovem b, jestliže a i b mají stejnou délku. Rozhodněte, zda R je relací ekvivalence a pokud zjistíte, že ano, tak napište, jak vypadají příslušné třídy ekvivalence. 

4.5. Nechť A je množina všech přímek v rovině. Rozhodněte, zda jsou ekvivalencemi relace a) rovnoběžnost přímek, b) kolmost přímek. 

4.6. a) Kolik existuje symetrických relací na dvouprvkové množině? b) A kolik tranzitivních? 

4.7. Dokažte, že je-li relace ireflexivní a tranzitivní, pak je asymetrická. 

_Výsledky._ 4.1. Není. 4.2. Ne, ano. 4.3. Je, _A_ R D ff□; ı; ?g; f4gg. 4.4. Je, v jedné třídě jsou všechna slova o stejné délce. 4.5. a) Ano, b) ne. 4.6. a) 8, b) 13. 

### 5 Zobrazení 

- Definice 5.1 — zobrazení a souvisejících pojm˚u. a) _Zobrazení z množiny_ A _do množiny_ B se nazývá binární relace R, která 8a 2 A, 8b; c 2 B, splňuje .aRb ^ aRc/ ) .b D c/ (tato podmínka říká, že k jednomu prvku z A nemůžeme mít dva různé prvky z B, prvkům z A říkáme vzory a prvkům z B obrazy). Značíme obvykle f , přičemž namísto f � A � B píšeme f W A ! B a namísto af b píšeme b D f .a/. 

- b) _Definiční obor_ : D.f / WD fa 2 A W 9b 2 B takové, že f .a/ D bg. 

- c) _Obor hodnot_ : H.f / WD fb 2 B W 9a 2 A takové, že f .a/ D bg. 

- d) Je-li D.f / D A, hovoříme o _zobrazení množiny_ A _do množiny_ B. 

- e) Je-li H.f / D B, hovoříme o _zobrazení na množinu_ B _(surjekce, pokrytí)_ . 

- f) Platí-li 8a; b 2 D.f / W a ¤ b ) f .a/ ¤ f .b/ (tj. každé dva různé vzory mají dva různé obrazy), hovoříme o _prostém (injektivním) zobrazení_ . 

- g) Je-li D.f / D A a f je zároveň surjektivní i injektivní, hovoříme o _bijektivním (vzájemně jednoznačném) zobrazení_ . 

Poznámka 5.2. a) Chceme-li zdůraznit, že se jedná o zobrazení množiny a ne z množiny, používá se obratu „Nechť f W A ! B je zobrazení na A“. Podobně, „f W A ! B je surjekce na A“ znamená, že hovoříme o zobrazení množiny na množinu. 

b) Množinová rovnost D.f / D A v definici bijektivního zobrazení se v literatuře často požaduje již v definici prostého zobrazení, je tedy potřeba dávat pozor na užitou terminologii. 

Pˇríklad 5.3. Je dána množina A D f2; 3; 4; 6; 11g a relace R na A, přičemž aRb, jestliže b dělí a. Je R zobrazení? 

_Řešení._ Relace obsahuje např. dvojice Œ4; 2� a Œ4; 4�, a tedy nemůže být zobrazením. 

Kapitola 1. Vybrané statˇe z matematiky 

26 

Definice 5.4 — inverzního zobrazení. Nechť f W A ! B je zobrazení. Je-li inverzní relace k f také zobrazením, hovoříme o _inverzním zobrazení_ a píšeme f<sup>�1</sup> W B ! A. 

Následující věta říká, za jakých podmínek f<sup>�1</sup> existuje. 

■ Vˇeta 5.5. _Inverzní zobrazení_ f<sup>�1</sup> _k zobrazení_ f _existuje, právě když_ f _je prosté._ 

_Důkaz._ „)“ (sporem): Nechť f<sup>�1</sup> W B ! A je zobrazení a předpokládejme, že f není prosté. Potom existují a1; a2 2 A, a1 ¤ a2, a b 2 B takové, že Œa1; b� 2 f ^ Œa2; b� 2 f , a tedy také Œb; a1� 2 f<sup>�1</sup> ^ Œb; a2� 2 f<sup>�1</sup> . To je ovšem spor s předpokladem, že f<sup>�1</sup> je zobrazení. 

„(“ (sporem): Nechť f W A ! B je prosté zobrazení. Předpokládejme, že relace f<sup>�1</sup> není zobrazení, tj. existují prvky b 2 B a a1; a2 2 R, a1 ¤ a2, takové, že Œb; a1� 2 f<sup>�1</sup> ^ Œb; a2� 2 f<sup>�1</sup> . Tedy Œa1; b� 2 f ^ Œa2; b� 2 f . To je ale spor s předpokladem, že f je prosté. 

Pˇríklad 5.6. Vyjádřete se k typu zobrazení f W A ! B, kde A D fa; b; c; d; eg, B D fu; v; wg, u D f .a/, u D f .c/, w D f .d/, w D f .e/. 

_Řešení._ Nezobrazuje celou množinu A, protože D.f / ¤ A, není surjekce, protože H.f / ¤ B, není injekce, protože např. a; c se oba zobrazují na u. 

Poznámka 5.7. Zřejmě, každá bijekce má inverzi. Tato inverze je bijekcí, přičemž platí 



<!-- Start of picture text -->
f �1 .f .a// D a 8a 2 A a f .f �1 .b// D b 8b 2 B:<br><!-- End of picture text -->

Pomocí bijektivního (resp. injektivního) zobrazení lze porovnávat množiny z hlediska „počtu prvků“, a to i v případě, kdy množiny jsou nekonečné. 

- Definice 5.8 — porovnání množin z hlediska mohutnosti. a) Řekneme, že _množiny_ A _a_ B _jsou stejně mohutné (mají stejnou kardinalitu)_ , jestliže existuje bijektivní zobrazení f W A ! B. Značíme A � B. 

- b) Řekneme, že _množina_ A _má stejnou nebo menší mohutnost než množina_ B _(má menší nebo stejnou kardinalitu)_ , jestliže existuje injektivní zobrazení f W A ! B, přičemž D.f / D A. Píšeme A � B. 

- c) Řekneme, že _množina_ A _má menší mohutnost než množina_ B _(má menší kardianlitu)_ , jestliže A � B, ale přitom neplatí A � B. Píšeme A � B. 

Poznámka 5.9. Uvedená definice má komparativní charakter (potřebujeme dvě množiny), nedefinuje mohutnost množiny přímo. Pro kvantitativní popis mohutnosti se užívá pojem _kardinálního čísla_ . V případě konečných množin je mohutnost rovna počtu jejích prvků (mohutnost množiny A značíme jAj nebo card.A/). Poznamenejme ještě, že Cantorova<sup>12</sup> věta říká, že pro jakoukoliv množinu A platí, že A � 2<sup>A</sup> . 

#### Pˇríklady k procviˇcení 

5.1. Jsou dány množiny A D f2; �2; 5g a B D fa; b; cg. Rozhodněte, zda relace R D fŒ2; b�; Œ�2; b�; Œ5; a�g je zobrazení z množiny A do množiny B. Pokud zjistíte, že ano, je injektivní? A je surjektivní? 

5.2. Nechť A D fa; b; c; d g, B D fp; q; r; s; tg, C D fx; y; zg jsou množiny. Napište složené zobrazení F D g ı f W A ! C , jsou-li zobrazení f W A ! B, g W B ! C definované předpisy 



<!-- Start of picture text -->
f D ˚Œa; p�; Œb; p�; Œc; r�; Œd; t�� a g D ˚Œp; x�; Œq; z�; Œr; y�; Œs; y�; Œt; y��:<br><!-- End of picture text -->

(Ověřte nejprve, že relace f; g jsou skutečně zobrazeními). 

5.3. Načrtněte v rovině relaci R D fŒx; y� 2 R � R W x<sup>2</sup> � 4y<sup>2</sup> D 0g a rozhodněte, zda je tato relace zobrazením. 

12Georg Cantor 1845–1918, Němec 

6 Reálná ˇcísla 

27 

5.4. Jsou množiny N a Z (množina všech celých čísel) stejně mohutné? Pokud se domníváte, že ano, pokuste se napsat příslušnou bijekci. 

5.5. Jsou stejně mohutné množiny .��=2; �=2/ a R D .�1; 1/? Pokud se domníváte, že ano, tak se pokuste napsat příslušnou bijekci. 

_Výsledky._ 5.1. Je; není; není. 5.2. F D ˚Œb; x�; Œc; y�; Œd; y�� 5.3. Není. 

### 6 Reálná ˇcísla 

Pro matematickou analýzu je to nejdůležitější číselná množina. Na střední škole se vychází z geometrické interpretace reálného čísla, kde reálná čísla ztotožňujme s body na přímce (číselné reálné ose). Ke korektnímu zavedení některých pojmů však toto pojetí nestačí. Existují dvě možnosti, jak reálná čísla zavést. První možnost je založena na postupném budování, nejprve přirozených čísel, pak celých čísel, dále racionálních a z nich pak čísel reálných (motivací k zavedení N je počet prvků nějaké množiny, na této množině umíme sčítat a násobit, umíme ji uspořádat, ale nelze zde bez omezení odečítat nebo dělit, Z lze chápat jako doplnění N tak, aby operace odečítání měla vždy výsledek, Q je zase doplnění Z tak, aby operace dělení měla vždy výsledek, motivací k I je potřeba pracovat s čísly, která nelze vyjádřit ve tvaru p=q, např. ~~p~~ 2, ln 3; : : : ). Tato cesta je relativně zdlouhavá a technicky náročná. Druhá možnost je zavést množinu reálných čísel axiomaticky (a výše zmíněné číselné množiny chápat jako určité podmnožiny). 

Definice 6.1 — pojmy týkající se uspoˇrádaných množin. Nechť M je množina s relací uspořádání � a A � M . Řekneme, že: 

- a) prvek m 2 M je _horní_ (resp. _dolní_ ) _závora_ množiny A, jestliže 8a 2 A platí a � m, resp. m � a; 

- b) množina A je _ohraničená shora_ (resp. _zdola_ ), jestliže existuje horní (resp. dolní) závora; 

- c) b 2 A je _maximum_ (resp. _minimum_ ) a píšeme b D max A (resp. b D min A), jestliže 8a 2 A platí a � b (resp. b � a); 

- d) s 2 M je _supremum_ (resp. _infimum_ ) množiny A, a píšeme s D sup A (resp. s D inf A), jestliže je nejmenší horní závorou množiny A (resp. největší dolní závorou), tj. jestliže platí 

.s1/ 8a 2 A W a � s; .i1/ 8a 2 A W s � a; resp. .s2/ .8a 2 A W a � b/ ) s � b; .i2/ .8a 2 A W b � a/ ) b � s: 

■ Vˇeta 6.2. _Libovolná_ A � M _má nejvýše jedno supremum (resp. infimum)._ 

_Důkaz._ Tvrzení dokážeme sporem. Předpokládejme, že suprema existují alespoň dvě, označme je m D sup A a m<sup>�</sup> D sup A. Potom m<sup>�</sup> je horní závora A, tj. m � m<sup>�</sup> . Analogicky m je horní závora a tedy m<sup>�</sup> � m. Protože ale � je antisymetrická relace, platí m D m<sup>�</sup> , což je spor. Pro infimum se ukáže analogicky. 

Definice 6.3 — množiny reálných ˇcísel. _Množina reálných čísel_ (budeme ji značit R) je množina, na které jsou definovány dvě binární operace (binární operace na množině M je zobrazení M � M ! M ) C (plus), � (krát) a jedna binární relace <, které splňují podmínky: (A1) 8a; b 2 R W a C b D b C a (komutativita sčítání); (A2) 8a; b; c 2 R W .a C b/ C c D a C .b C c/ (asociativita sčítání); 

- (A3) 90 2 R tak, že 8a 2 R je a C 0 D a (existence neutrálního prvku vzhledem ke sčítání); 

- (A4) ke každému a 2 R existuje prvek �a 2 R tak, že a C .�a/ D 0 (existence opačného prvku); (A5) 8a; b 2 R W a � b D b � a (komutativita násobení); 

- (A6) 8a; b; c 2 R W .a � b/ � c D a � .b � c/ (asociativita násobení); 

- (A7) existuje prvek 1 2 R (1 ¤ 0) takový, že 8a 2 R platí a � 1 D a (existence neutrálního prvku vzhledem k násobení); 

- (A8) ke každému a 2 R n f0g existuje prvek a<sup>�1</sup> 2 R takový, že a � a<sup>�1</sup> D 1 (existence inverzního prvku); 

Kapitola 1. Vybrané statˇe z matematiky 

28 

(A9) 8a; b; c 2 R platí a � .b C c/ D .a � b/ C .a � c/ (distributivní zákon); 

- (A10) každá dvojice prvků a; b 2 R splňuje právě jeden ze vztahů a < b, a D b, b < a, tj. každé dva prvky jsou porovnatelné (zákon trichotomie); 

- (A11) jestliže pro a; b; c 2 R platí a < b a b < c, pak také a < c (tranzitivita relace <); 

- (A12) jestliže pro a; b 2 R platí a < b, pak pro každé c 2 R je a C c < b C c (monotonie vzhledem ke sčítání); 

- (A13) jestliže pro a; b; c 2 R platí a < b a 0 < c, pak a � c < b � c (monotonie vzhledem k násobení); 

- (A14) je-li M neprázdná shora ohraničená podmnožina množiny R, pak existuje sup M 2 R (supremum je zde chápáno vzhledem k relaci � odvozené z relace <; připomeňme, že ta je definována: a � b, jestliže a < b _ a D b). Této vlastnosti říkáme _axiom spojitosti_ . 

Poznámka 6.4. a) Odečítání dvou prvků je definováno jako a � b WD a C .�b/ pro libovolná a; b 2 R a operace dělení jako a=b WD a � b<sup>�1</sup> pro libovolné a 2 R a libovolné b 2 R n f0g (pro a 2 R není tedy definováno a=0). 

b) Axiomy (A1)–(A4) a (A5)–(A8) jsou axiomy komutativní grupy, (A1)–(A9) jsou axiomy pole, axiomy (A10)–(A11) říkají, že relace < je ostré lineární uspořádání (ireflexivita je zde schována v trochu jiné formulaci trichotomie). Vedle relace � pak definujeme další odvozené relace > a � jako: a > b, jestliže b < a a a � b, jestliže b � a. Axiomy (A1)–(A13) jsou axiomy uspořádaného pole, axiomy (A1)–(A14) jsou axiomy spojitě uspořádaného pole (axiom (A14) odlišuje reálná čísla od racionálních). Až na izomorfismus (zhruba řečeno jiné pojmenování prvků) existuje jediné spojitě uspořádané pole (jeho modelem je právě množina R). 

c) Pomocí výše uvedených axiomů lze ukázat, že každá neprázdná zdola ohraničená podmnožina R má infimum, viz následující příklad. 

Pˇríklad 6.5. Ukažte, že každá neprázdná zdola ohraničená množina v R má infimum. 

_Řešení._ Ukažme nejprve, že pro každé a 2 R platí �.�a/ D a. Skutečně, 



<!-- Start of picture text -->
.A3/ .A4/ .A2/<br>a D a C 0 D a C .�a C .�.�a/// D .a C .�a// C .�.�a//<br>.A3/ .A1/ .A3/<br>D 0 C .�.�a// D �.�a/ C 0 D �.�a/:<br><!-- End of picture text -->

Dále ukážeme platnost implikace a < b ) �b < �a. 

(A12) (A4) (A12) a < b H) a C .�a/ < b C .�a/ H) 0 < b C .�a/ H) 0 C .�b/ < .b C .�a// C .�b/ (A1) (A3) (A2) H) �b C 0 < .�b/ C .b C .�a// H) �b < .�b/ C .b C .�a// H) �b < .�b C b/ C .�a/ (A1) (A4) (A1) (A3) H) �b < .b C .�b// C .�a/ H) �b < 0 C .�a/ H) �b < �a C 0 H) �b < �a: 

Platí také implikace a � b ) �b ��a, kde � je relace uspořádání odvozená z relace <. Relace � je totiž definována jako a � b, jestliže a < b _ a D b. Je-li a < b, pak podle předchozího kroku je �b < �a a je-li a D b, pak zřejmě �b D �a (�a je opačný prvek k a, �b je opačný prvek k b, a protože a D b a opačný prvek je jediný, musí být �b D �a). 

Nyní již můžeme přistoupit k důkazu existence infima. Nechť tedy A � R je neprázdná, zdola ohraničená množina a b 2 R je její dolní závora. Položme A<sup>?</sup> D f�x W x 2 Ag. Protože b je dolní závorou množiny A, platí b � x pro každé x 2 A, a tedy podle třetího kroku �x � b pro každé �x 2 A<sup>?</sup> . To znamená, že množina A<sup>?</sup> je shora ohraničená a tedy existuje supremum sup A<sup>?</sup> D s 2 R. Podle axiomu (A4) je �s 2 R. Ukažme, že inf A<sup>?</sup> D �s. Nechť x 2 A je libovolné. Pak podle (s1) definice 6.1 je �x � s a podle třetího bodu je �s � x. Protože x 2 A bylo libovolné, platí podmínka (i1) definice 6.1. Nechť dále c 2 R je takové, že c � x pro každé x 2 A (takové c jistě existuje, protože množina A je zdola ohraničená). Pak, opět podle třetího kroku, je �x ��c pro každé �x 2 A<sup>?</sup> a podle vlastnosti (s2) definice 6.1 platí s ��c. To znamená, že �.�c/ ��s. Podle prvního kroku tedy máme c ��s, tj. podmínka (i2) definice 6.1 je také splněna, a tedy �s je infimem. 

6 Reálná ˇcísla 

29 

Pˇríklad 6.6. Pro množinu A D ˚ 1n<sup>Wn2N</sup> � platí sup A D max A D 1, min A neexistuje, inf A D 0. Skutečně, platí n<sup><u>1</u>�1 8n 2 N, tj. 1 je horní závora. Zároveň neexistuje menší horní závora, protože 1 2 A.</sup> Odtud sup A D max A D 1. Dále, číslo 0 je dolní závorou, neboť 0 � n<sup><u>1</u>8n 2 N. Zvolme ı> 0 libovolně</sup> a předpokládejme, že ı je také dolní závora. Položíme-li ale n0 D b1=ıc (bxc je dolní celá část x), potom pro všechny prvky n<sup><u>1</u>takové, že n>n0, platí</sup> n<sup><u>1</u><ı, což je spor s předpokladem, že ıje dolní závora.</sup> Máme tedy inf A D 0 (toto číslo ale není minimem, protože 0 … A). 

Pˇríklad 6.7. Ukažte, že a) neutrální prvek množiny R vzhledem ke sčítání je jediný, b) platí vlastnost 0 � a D 0 pro každé a 2 R. 

_Řešení._ ad a) Sporem. Předpokládejme, že v R existují alespoň dva různé neutrální prvky 0 a 0<sup>�</sup> . To znamená, že každý prvek x 2 R splňuje x C 0 D x a také x C 0<sup>�</sup> D x. Dosadíme-li do prvního vyjádření x D 0<sup>�</sup> a do druhého x D 0, dostaneme 0<sup>�</sup> C 0 D 0<sup>�</sup> a 0 C 0<sup>�</sup> D 0. Protože je ale sčítání komutativní, viz axiom (A1), poslední rovnost můžeme psát jako 0<sup>�</sup> C 0 D 0. Obě rovnosti tedy dávají 0<sup>�</sup> D 0<sup>�</sup> C 0 D 0, tj. 0<sup>�</sup> D 0 (přičemž jsme využili symetrii a tranzitivitu relace D). To je spor s předpokladem různosti prvků 0 a 0<sup>�</sup> . 

ad b) Nechť a 2 R. Pak 0 � a 2 R a podle axiomu (A4) existuje opačný prvek �0 � a takový, že platí 0 � a C .�0 � a/ D 0. Dále, 



<!-- Start of picture text -->
(A3) (A5), (A9)<br>D<br>0 D 0 � a C .�0 � a/ D .0 C 0/ � a C .�0 � a/ .0 � a C 0 � a/ C .�0 � a/<br>(A2) (A4) (A3)<br>D 0 � a C .0 � a C .�0 � a// D 0 � a C 0 D 0 � a:<br><!-- End of picture text -->

Platí tedy číslo 0 � a D 0 (a protože podle (A1) máme 0 � a D a � 0, tak také a � 0 D 0). 

Definice 6.8 — rozšíˇrené množiny reálných ˇcísel. Množinu R<sup>�</sup> D R [ f�1; 1g nazýváme _rozšířená množina reálných čísel_ , symboly �1; 1 (minus a plus nekonečno) nazýváme nevlastní reálná čísla (nevlastní body číselné osy). Klademe �1 < a < 1 8a 2 R. Pozor, symboly �1; 1 nejsou čísla, nejsou pro ně definovány veškeré početní operace. Přesněji, definovány jsou následující operace: Pro libovolné c 2 R, c > 0, je 

1 C 1 D 1; 1 ˙ c D ˙c C 1 D 1; 1 � .˙1/ D ˙1; �1 �1 D �1; �1 ˙ c D ˙c �1 D �1; .�1/ � .�1/ D 1; ˙c 1 ˙c �1 D 1 � .˙c/ D ˙1; 1<sup>D</sup> �1<sup>˙cD 0;</sup> ˙c<sup>D ˙1;</sup> 0 �1 ˙c � .�1/ D �1 � .˙c/ D �1; ˙1<sup>D 0;</sup> ˙c<sup>D �1;</sup> kde C1 D 1. 

Poznámka 6.9. a) Následující výrazy obvykle necháváme nedefinovány: 1 �1, 0 �1,<sup><u>1</u></sup> 1<sup>(stejně tak</sup> 0 � .�1/,<sup>�</sup> 1<sup><u>1</u>,</sup> �11<sup>a�</sup> �1<sup><u>1</u>).Tytořadímemezitzv.</sup><sup>_neurčitévýrazy_.Existujíještědalšíčtyřineurčité</sup> výrazy, vrátíme se k nim při diskuzi l’Hospitalova pravidla v poznámce 16.8. Pozor, výraz<sup><u>1</u></sup> 0<sup>(resp.�</sup> 0<sup><u>1</u>)</sup> je vždy nedefinován (neřadíme jej mezi neurčité výrazy)! 

b) V případě A � R neohraničené shora (resp. zdola) pak klademe sup A D 1 (resp. inf A D �1). 

Definice 6.10 — interval˚u. Buďte a; b 2 R, a < b. Potom 

- a) _uzavřeným intervalem_ o krajních (koncových, hraničních) bodech a; b rozumíme množinu ha; bi WD fx 2 R W a � x � bg, 

- b) _otevřeným intervalem_ množinu .a; b/ WD fx 2 R W a < x < bg, 

- c) _polouzavřenými intervaly_ zprava (resp. zleva) množiny .a; bi WD fx 2 R W a < x � bg, ha; b/ WD fx 2 R W a � x < bg. 

d) Intervaly nekonečné délky definujeme jako množiny ha; 1/ WD fx 2 R W x � ag, .a; 1/ WD fx 2 R W x > ag, 

Kapitola 1. Vybrané statˇe z matematiky 

30 

.�1; bi WD fx 2 R W x � bg, .�1; b/ WD fx 2 R W x < bg, .�1; 1/ WD R. Je-li J interval jakéhokoliv typu a x0 2 J , přičemž bod x0 není krajní, řekneme, že x0 _je vnitřním bodem intervalu_ J . 

Poznámka 6.11. V dalším budeme užívat také značení R<sup>C</sup> WD .0; 1/ a R<sup>C</sup> 0<sup>WDh0; 1/, resp. R�WD</sup> .�1; 0/ a R<sup>�</sup> 0<sup>WD .�1; 0i.</sup> 

Definice 6.12 — okolí a ryzího okolí. a) _Okolím_ (podrobněji _(symetrickým)_ ı _-okolím,_ ı > 0) _bodu_ x0 2 R rozumíme interval .x0 � ı; x0 C ı/. Značíme Oı .x0/, stručně O.x0/. 

b) _Okolím bodu_ 1 (resp. �1) rozumíme interval .a; 1/ (resp. .�1; a/), kde a 2 R. 

c) _Ryzím (prstencovým) okolím bodu_ x0 2 R rozumíme množinu O.x0/ n fx0g. Okolí nevlastního bodu je vždy ryzí. Budeme značit O<sup>�</sup> .x0/. 

Definice 6.13 — jednostranných okolí. Nechť x0 2 R, ı > 0. _Pravým_ (resp. _levým_ ) ı _-okolím bodu_ x0 rozumíme interval hx0; x0 C ı/ (resp. .x0 � ı; x0i). Budeme označovat Oı<sup>C.x0/, stručně OC.x0/ (resp.</sup> Oı<sup>�.x0/, stručně O�.x0/).</sup><sup>_Ryzím pravým_(resp.</sup><sup>_levým_) ı</sup><sup>_-okolím bodu_x0rozumíme otevřený interval</sup> .x0; x0 C ı/ (resp. .x0 � ı; x0/). Budeme označovat Oı<sup>�C</sup> .x0/, stručně O<sup>�C</sup> .x0/ (resp. Oı<sup>��</sup> .x0/, stručně O<sup>��</sup> .x0/). 

Poznámka 6.14. Někdy se okolí bodu x0 uvažuje jako libovolný otevřený interval takový, že x0 je vnitřním bodem tohoto intervalu. V takovém případě hovoříme o _okolí v širším smyslu_ . 

- Vˇeta 6.15. (i) _Mezi dvěma libovolnými reálnými čísly_ x1 _,_ x2 _(_ x1 < x2 _) leží racionální i iracionální číslo._ 

(ii) _V libovolném okolí libovolného čísla_ x0 2 R _leží racionální i iracionální číslo._ 

_Důkaz._ ad (i) Položme 



<!-- Start of picture text -->
1<br>n D C 1; m D bnx1c C 1<br>� x2 � x1 �<br><!-- End of picture text -->



<!-- Start of picture text -->
(připomeňme, že b�c značí dolní celou část reálného čísla). Pak m 2 Z, n 2 N, a tedy q WD m n 2 Q.<br>Z definic čísel m a n plyne, že m > nx1 (tj. x1 < m n ), m � nx1 C 1, n > x2�1 x1 (tj. nx2 � nx1 > 1, tj.<br>nx2 > nx1 C 1). Odtud<br>x1 < m n � nx1 n  C 1 < nx n 2 :<br>To znamená, že q je racionální číslo mezi x1 a x2.<br>Položme dále<br>p 2<br>s D C 1; r D x1 C 1:<br>$ x2 � x1 % � p s2 �<br>Pak r 2 Z, s 2 N a t D p 2 r s 2 I (kdyby nebylo, pak by i p 2 muselo být racionální, což víme, že není).<br>Z definic čísel r a s plyne, že<br>s s p 2 s s<br>r > p 2 x1; tj. x1 < p 2 r s I r � p 2 x1 C 1I s > x2 � x1 ; tj. p 2 x2 > p 2 x1 C 1/:<br>Odtud<br>p 2� p s2 x1 C 1 � p 2 p s 2 x2<br>x1 < p 2 r s � s < s D x2:<br><!-- End of picture text -->

To znamená, že t je iracionální číslo mezi x1 a x2. 

ad (ii) Tvrzení je důsledkem (i), protože mezi čísly x0 � ı a x0 C ı leží racionální i iracionální číslo. 

31 

7 Posloupnosti 

Poznámka 6.16. Množina, která má stejnou mohutnost jako nějaká podmnožina množiny přirozených čísel se nazývá _spočetná_<sup>_13_</sup> (její prvky můžeme očíslovat), přičemž mohutnost množiny přirozených čísel značíme @0 („alef“ – první písmeno v hebrejské abecedě), tj. jNj D @0. V opačném případě hovoříme o _nespočetné_ množině. Intuice by mohla svádět k tomu, že např. množina Z všech celých bude mít „dvakrát více“ prvků něž N a množina S<sup>C</sup> všech přirozených sudých čísel naopak „dvakrát méně“ prvků než N. Na intuici však v případě nekonečných množin nelze příliš spoléhat. Platí totiž jZj D jS<sup>C</sup> j D jNj D @0 (příslušná bijektivní zobrazení mezi množinami není těžké zkonstruovat, viz též cvičení 5.4 a 5.5). Stejně tak jQj D @0. Existence nespočetných množin plyne přímo z Cantorovy věty, podle které je N � 2<sup>N</sup> . Mohutnost množiny 2<sup>N</sup> nazýváme _mohutnost kontinua_ . Důvodem názvu je fakt, že množina všech reálných čísel má stejnou mohutnost jako množina 2<sup>N</sup> ; reálná čísla na sebe „kontinuálně (spojitě) navazují“ (nejsou mezi nimi „díry“). Nespočetnost množiny R lze ukázat např. pomocí Cantorovy diagonální metody. Mohutnost kontinua se označuje c nebo 2<sup>@0</sup> . Georg Cantor v roce 1878 publikoval tzv. _hypotézu kontinua_ , která říká, že neexistuje podmnožina S reálných čísel, pro kterou by platilo @0 < jSj < 2<sup>@0</sup> . Tj. první ostře větší mohutnost (kardinální číslo) než @0 by byla @1 D 2<sup>@0</sup> . Až v roce 1963 matematik Cohen<sup>14</sup> dokázal, že o pravdivosti hypotézy nelze v rámci Zermelovy–Fraenkelovy teorie množin rozhodnout. 

#### Pˇríklady k procviˇcení 

6.1. Uvažujte množinu A D f0;5I 0;55I 0;555I : : : g jakožto podmnožinu R. Dokažte, že sup A D<sup>5</sup> =9. 

6.2. V množině R uvažujte množinu A D ˚ 2C.n�1/n W n 2 N�. Určete sup A a inf A. 

6.3. Nechť A; B jsou neprázdné shora ohraničené podmnožiny R takové, že A � B. Ukažte, že pak sup A � sup B. 

6.4. Nechť a; b jsou reálná čísla. Pomocí axiomů reálných čísel ukažte, že platí implikace a � b D 0 ) .a D 0 _ b D 0/. _Nápověda._ Dokazujte sporem, rozepište si výraz a<sup>�1</sup> � .a � b/. 

6.5. Pomocí axiomů reálných čísel ukažte, že pro každá a; b; c 2 R platí implikace aCb D aCc ) b D c. 

6.6. Ukažte, že pro libovolné a 2 R platí �a D .�1/a. _Nápověda._ Aplikujte vhodné axiomy reálných čísel na výraz a C .�1/a a využijte vlastnost z předchozího cvičení 6.5. 

_Výsledky._ 6.2. sup A D<sup>3</sup> =2, inf A D 0. 

### 7 Posloupnosti 

Definice 7.1 — posloupnosti. _Posloupností_ rozumíme zobrazení f W N ! R, přičemž D.f / D N. Namísto fn WD f .n/ píšeme obvykle an (nazýváme _členem posloupnosti_ , posloupnost se pak značí fang<sup>1</sup> nD1<sup>, stručně fang).</sup> 

Definice 7.2 — ohraniˇcenosti a monotonie posloupnosti. Řekneme, že posloupnost fang je: 

a) _shora_ (resp. _zdola_ ) _ohraničená (omezená)_ , jestliže 9c 2 R tak, že an � c (resp. an � c) 8n 2 N; 

b) _ohraničená_ , jestliže je shora i zdola ohraničená; 

c) _neklesající_ (resp. _nerostoucí_ ), jestliže an � anC1 (resp. an � anC1) 8n 2 N; 

d) _rostoucí_ (resp. _klesající_ ), jestliže an < anC1 (resp. an > anC1) 8n 2 N; 

e) _monotónní_ (resp. _ostře monotónní_ ), jestliže je neklesající nebo nerostoucí (resp. rostoucí nebo klesající). 

> 13V tomto pojetí tedy spočetnou množinou rozumíme buď konečnou množinu, nebo množinu, která má stejnou mohutnost jako množina N. V literatuře v tomto směru nepanuje jednotnost, často se spočetnou množinou rozumí množina, která má mohutnost právě jako množina N a množina, která má stejnou mohutnost jako nějaká podmnožina množiny N, se nazývá nejvýše spočetná 14Paul Cohen 1934–2007, Američan 

Kapitola 1. Vybrané statˇe z matematiky 

32 

Definice 7.3 — limity posloupnosti. Řekneme, že posloupnost fang má _limitu_ a 2 R (píšeme 

nlim!1<sup>anD a</sup> nebo stručněji lim an D a; resp. an ! a/; 

jestliže ke každému " > 0 existuje n0 2 N takové, že pro každé n � n0 platí jan � aj < ". Posloupnost, která má limitu, se nazývá _konvergentní_ . 

■ Vˇeta 7.4 — o jednoznaˇcnosti limity. _Jakákoliv posloupnost má nejvýše jednu limitu._ 

_Důkaz._ Předpokládejme, že lim an D a a lim an D b, a ¤ b. Bez újmy na obecnosti můžeme předpokládat a < b. Zvolme " D<sup><u>1</u></sup> 4<sup>.b �a/> 0. Protože a i bjsou limity, od určitého n0platí jan �aj <</sup><sup><u>1</u></sup> 4<sup>.b �a/,</sup> jan � bj <<sup><u>1</u></sup> 4<sup>.b �a/. Odtud máme b �aDjb �ajDjb �a C an �anjDj.an �a/ �.an �b/j�</sup> jan � aj C jan � bj <<sup><u>2</u></sup> 4<sup>.b �a/ ) b �a <</sup><sup><u>1</u></sup> 2<sup>.b �a/ ) 2b �2a < b �a ) b< a ) spor.</sup> 

Pˇríklad 7.5. Dokažte, že lim n<sup><u>1</u>D 0.</sup> 

_Řešení._ Zvolme " > 0 libovolně a položme n0 D ˙ 1" � C 1 (horní celá část, např. d2;8e D 3). Potom 8n � n0 platí ˇˇ 1n<sup>�0</sup> ˇˇ D n1<sup>< ".</sup> 

■ Vˇeta 7.6. _Každá konvergentní posloupnost je ohraničená._ 

_Důkaz._ Nechť lim an D a a " > 0 libovolné. Potom 9n0 2 N tak, že 8n � n0 platí a � " < an < a C ". Označme h D maxfa1; a2; : : : ; an0�1; aC"g, d D minfa1; a2; : : : ; an0�1; a�"g. Potom zřejmě 8n 2 N platí d � an � h, tj. fang je shora i zdola ohraničená. 

Poznámka 7.7. a) Jsou-li fang, fbng konvergentní posloupnosti takové, že an < bn (nebo an � bn) pro každé n � n0 2 N, pak lim an � lim bn. 

b) Je-li pro fang lim an D 0 a fbng je ohraničená, pak lim anbn D 0. 

c) Posloupnost fang, kde an D c pro 8n 2 N se nazývá _stacionární posloupnost_ a platí pro ni lim an D c. 

d) Je-li fang je monotónní a neohraničená, pak lim a<sup><u>1</u></sup> n<sup>D 0.</sup> 

_Důkaz._ ad a) Označme a D lim an a b D lim bn. Připusťme opak, tj. a > b a položme " D 2<sup><u>1</u>.a �b/.</sup> Pak " > 0 a existuje n1 2 N takové, že pro 8n � n1 je a � " < an < a C ", a existuje n2 2 N takové, že pro 8n � n2 je b � " < bn < b C ". Pro n � maxfn0; n1; n2g tedy platí a � " D<sup><u>1</u></sup> 2<sup>.a C b/ < an�</sup> bn < b C " D<sup><u>1</u></sup> 2<sup>.a C b/, což je spor.</sup> 

ad b) Protože fbng je ohraničená, existuje h 2 R takové, že jbnj < h pro každé n 2 N. Nechť " > 0 je libovolné. K h<sup><u>"</u>> 0 existuje n02 N takové, že pro každé n �n0je janj D jan �0j <</sup> h<sup><u>"</u>. Pro tato n tedy</sup> pak platí janbnj D janjjbnj < h<sup><u>"</u>h D ", a proto lim anbnD 0.</sup> 

ad c) Zřejmě pro libovolné " > 0 a každé n 2 N platí jan �aj D jc �cj D 0 < ", tj. lim an D lim c D c. 

ad d) Nechť fang je neklesající a " > 0 libovolné. Protože je fang neohraničená, existuje n0 2 N takové, že an0 ><sup><u>1</u></sup> "<sup>. Dále platí také an�an0></sup><sup><u>1</u></sup> "<sup>> 0 pro 8n �n0, protože fang je neklesající. Odtud</sup> plyne, že pro 8n � n0 platí j a<sup><u>1</u></sup> n<sup>�0j D j</sup> a<sup><u>1</u></sup> n<sup>j D</sup> a1n<sup>< ", a proto lim</sup> a<sup><u>1</u></sup> n<sup>D 0. Pro nerostoucí posloupnost</sup> by se důkaz provedl analogicky. 

Pˇríklad 7.8. Určete limity 



<!-- Start of picture text -->
a) lim sin n2 ; b) lim 1<br>n n 2 :<br><!-- End of picture text -->

_Řešení._ ad a) Položme bn D sin n<sup>2</sup> a an D n<sup><u>1</u>. Platí j sin n2j �1 8n 2 N, a tedy bn je ohraničená. Protože</sup> lim an D lim n<sup><u>1</u>D 0, je podle předchozí poznámky b) lim</sup><sup><u>sin</u></sup> n<sup><u>n2</u></sup> D 0. 

33 

7 Posloupnosti 

ad b) Posloupnost fang D fn<sup>2</sup> g<sup>1</sup> nD1<sup>je(ostře)monotónní,neboťprokaždén2NplatíanC1D</sup> .n C 1/<sup>2</sup> D .n C 1/.n C 1/ > .n C 1/n > nn. Využíváme přitom axiomů (A11)–(A13) množiny R. (Monotonii je možné ověřit také matematickou indukcí.) Dále, posloupnost fang není shora ohraničená. Skutečně, předpokládejme opak, tj., že je shora ohraničená. Musí tedy existovat h > 0 takové, že n<sup>2</sup> � h pro 8n 2 N. Vezměme libovolné n0 2 N, které splňuje n0 > ~~p~~ h (takové n0 určitě existuje, protože množina N je neohraničená). Potom ale každé přirozené n � n0 splňuje n<sup>2</sup> � n<sup>2</sup> 0<sup>> .</sup> ~~p~~ h/<sup>2</sup> D h, což je spor s předpokladem. Podle předchozí poznámky d) je tedy lim n<sup><u>12</u>D 0. Jiný způsob: a) přímo z definice,</sup> b) využitím předchozí poznámky b) a příkladu 7.5. 

- Vˇeta 7.9. _Nechť_ fang _,_ fbng _jsou konvergentní posloupnosti takové, že_ lim an D a _,_ lim bn D b _. Pak_ 

- (i) _existuje_ lim janj _a platí_ lim janj D jaj _,_ 

- (ii) _existuje_ lim.an ˙ bn/ _a platí_ lim.an ˙ bn/ D a ˙ b _,_ 

- (iii) _existuje_ lim anbn _a platí_ lim anbn D ab _,_ 

- (iv) _pokud_ bn ¤ 0 _,_ b ¤ 0 _, pak existuje_ lim<sup><u>a</u></sup> bn<sup><u>n</u></sup><sup>_a platí_lim</sup><sup><u>a</u></sup> bn<sup><u>n</u>D</sup><sup><u>a</u></sup> b<sup>_._</sup> 

_Důkaz._ ad (i) Zvolme " > 0 libovolně. Pak existuje n0 2 N tak, že pro n � n0 je jan � aj < ". Pro n � n0 tedy platí jjanj �jajj �jan � aj < ", což znamená lim janj D a. 

ad (ii) Buď " > 0 libovolné. K 2<sup><u>"</u>existuje n12 N takové, že pro n �n1je jan �aj <</sup> 2<sup><u>"</u>, a existuje</sup> n2 2 N takové, že pro n � n2 je jbn � bj < 2<sup><u>"</u>. Pro n �n0D maxfn1; n2g platí j.an C bn/ �.a C b/j D</sup> j.an � a/ C .bn � b/j �jan � aj C jbn � bj < 2<sup><u>"</u>C</sup> 2<sup><u>"</u>D " a tedy lim.an C bn/ D a C b. Pro rozdíl se</sup> ukáže podobně (využijme jx � yj �jxj C jyj). 

ad (iii) Je-li a D 0, plyne tvrzení z věty z předchozí poznámky b) a věty 7.6. Nechť a ¤ 0 a zvolme " > 0 libovolně. Podle věty 7.6 existuje h > 0 takové, že jbnj < h pro 8n 2 N. K 2h"<sup>existuje n12N</sup> takové, že pro n � n1 je jan � aj < 2h"<sup>. K</sup> 2j"aj<sup>existuje n22 N takové, že pro n �n2je jbn �bj <</sup> 2j"aj<sup>.</sup> Pro n � n0 D maxfn1; n2g platí obě nerovnosti současně, tedy janbn �abj D janbn �abn Cabn �abj � janbn � abnj C jabn � abj D jan � ajjbnj C jajjbn � bj < 2h"<sup>h C jaj</sup> 2j"aj<sup>D</sup> 2<sup><u>"</u>C</sup> 2<sup><u>"</u>D ".</sup> 

ad (iv) Podle (i) je lim jbnj D jbj a podle předpokladu jbj > 0. Tedy k<sup><u>jb</u></sup> 2<sup><u>j</u>existuje n12N takové,</sup> <u>jbj</u> D <u>jbj</u> že pro n � n1 je jjbnj �jbjj < 2<sup>,tj.jbnj>jbj�</sup><sup><u>jb</u></sup> 2<sup><u>j</u></sup> 2<sup>.Odtudplyne,žepron�n1je</sup> jb1nj<sup><</sup> jb2j<sup>. Buď ">0 libovolné. K</sup><sup><u>b</u></sup> 2<sup>2"</sup> existuje n2 2 N takové, že pro n � n2 je jbn � bj <<sup><u>b</u></sup> 2<sup>2". Pro</sup> n � n0 D maxfn1; n2g je j b<sup><u>1</u></sup> n<sup>�</sup> b<sup><u>1</u>jDj</sup> j<sup><u>b</u></sup> b<sup>�</sup> jjb<sup><u>b</u></sup> n<sup><u>n</u></sup> j<sup>j<</sup><sup><u>b</u></sup> 2<sup>2"</sup> jb1j jb2j<sup>D"atedylim</sup> b<sup><u>1</u></sup> n<sup>D</sup> b<sup><u>1</u>.Podle(iii)je</sup> lim<sup><u>a</u></sup> bn<sup><u>n</u>D lim an �lim</sup> b<sup><u>1</u></sup> n<sup>D a</sup> b<sup><u>1</u>D</sup><sup><u>a</u></sup> b<sup>.</sup> 

Poznámka 7.10. Z věty 7.9(iii) a předchozí poznámky c) plyne, že je-li fang konvergentní posloupnost a c 2 R, pak lim.can/ D c lim an. 



<!-- Start of picture text -->
3n 2 �4n<br>Pˇríklad 7.11. Určete lim<br>n 2 C4n�3 .<br><!-- End of picture text -->

_Řešení._ 



<!-- Start of picture text -->
3n 2 � 4n 3n 2 � 4n 3 � 4=n<br>lim n 2 C 4n � 3 D lim n 2 C 4n � 3 � 1 1=n =n22 ! D lim 1 C 1=n � 3=n 2 D 3;<br><!-- End of picture text -->

kde v posledním kroku jsme využili vlastností z věty 7.9 a faktu, že lim n<sup><u>1</u>D lim</sup> n<sup><u>12</u>D 0 (viz příklady 7.5</sup> a 7.8). 

Poznámka 7.12. Je-li ak ¤ 0, b` ¤ 0 (k; ` 2 N), pak platí 



<!-- Start of picture text -->
akn k C ak�1n k�1 C ���C a1k C a0<br>lim<br>n!1 b`n ` C b`�1n `�1 C ���C b1n C b0<br>80 je-li k < `;<br>D ak=b` je-li k D `;<br>ˆ<<br>ˆ:˙1 je-li k > ` .nevlastní limita, viz definice 7.19/:<br><!-- End of picture text -->

Kapitola 1. Vybrané statˇe z matematiky 

34 

V posledním případě je znaménko plus, jsou-li obě ak, bk kladná nebo záporná, a znaménko minus v opačném případě. 

■ Vˇeta 7.13 — o tˇrech posloupnostech. _Nechť_ fang _,_ fbng _,_ fcng _jsou posloupnosti takové, že existuje_ n1 2 N _, že pro_ n � n1 _je_ an � bn � cn _. Jestliže_ lim an D lim cn D a _, pak také_ lim bn D a _._ 

_Důkaz._ Buď " > 0 libovolné. K němu existuje n2 2 N takové, že pro n � n2 je jan � aj < " a tedy an > a � ". Dále existuje n3 2 N takové, že pro n � n3 je jcn � aj < " a tedy cn < a C ". Pro n � n0 D maxfn1; n2; n3g platí a � " < an � bn � cn < a C ", tj. a � " < bn < a C ", což znamená lim bn D a. 

Pˇríklad 7.14. Určete lim<sup><u>ln n</u></sup> n<sup>2.</sup> 

_Řešení._ Protože n � ln n � 0 pro každé n 2 N, platí 



<!-- Start of picture text -->
0 � ln n<br>n 2 � n n2 D n 1 ! 0<br><!-- End of picture text -->

a podle předchozí věty tedy musí k nule konvergovat i posloupnost fln n=n<sup>2</sup> g, tj. máme 



<!-- Start of picture text -->
lim ln n<br>n 2 D 0:<br><!-- End of picture text -->

■ Vˇeta 7.15 — o monotónních posloupnostech. (m1) _Je-li posloupnost_ fang _neklesající a shora ohraničená (resp. nerostoucí a zdola ohraničená), pak je konvergentní a platí_ lim an D supfan W n 2 Ng _(resp._ lim an D inffan W n 2 Ng _)._ 

(m2) _Je-li monotónní posloupnost_ fang _ohraničená, pak je konvergentní._ 

_Důkaz._ ad (m1) Nechť fang je neklesající a shora ohraničená posloupnost. Potom podle axiomu (A14) z definice R existuje a D supfan W n 2 Ng 2 R. Dále, nechť " > 0 je libovolné. Protože a je horní závora, existuje an0 2 fang takové, že a � " < an0 (kdyby takový prvek neexistoval, byla by a � " horní závora menší než a, což je spor s a D supfang). Protože fang je neklesající, je také a � " < an pro každé n � n0. Tedy pro n � n0 je a � " < an � a < a C ", a proto lim an D a. Pro nerostoucí a zdola ohraničenou posloupnost se tvrzení ukáže analogicky. 

Tvrzení (m2) je přímým důsledkem (m1). 



<!-- Start of picture text -->
Pˇríklad 7.16. Dokažte, že posloupnost ˚.1 C n 1 /n�1 nD1 má limitu.<br><!-- End of picture text -->

_Řešení._ Nejprve ukažme, že posloupnost je rostoucí. K tomu využijeme Bernoulliovu<sup>15</sup> nerovnost .1 C x/<sup>n</sup> > 1 C nx pro 8n 2 N, n � 2 a 8x 2 R, x > �1, x ¤ 0, kterou lze dokázat matematickou indukcí. Položíme-li x D � n<sup><u>12</u>, dává tato nerovnost</sup> 



<!-- Start of picture text -->
�1 � n 12 �n > 1 � n 1 ) �1 � n 1 �n�1 C n 1 �n > 1 � n 1 ) �1 C n 1 �n > �1 � n 1 �1�n<br>1<br>D 1 C ; tedy an > an�1 pro každé n � 2; což znamená, že fang je rostoucí:<br>� n � 1 �n�1<br><!-- End of picture text -->

Dále ukažme, že posloupnost je ohraničená. Podle binomické věty platí 



<!-- Start of picture text -->
1 C 1 D 1 C n 1 n 1 n 1 n 1<br>� n �n 1 n C 2 n 2 C 3 n 3 C ���C n n n<br>! ! ! !<br>D1 C 1Šn n C n. 2Šn n �21/ C n.n � 3Šn 1/.3n � 2/ C ���C n.n � nŠn 1/ : : : 2n  � 1<br>D1 C 1Š 1 C 2Š 1 �1 � n 1 � C 3Š 1 �1 � n 1 ��1 � n 2 � C ���C nŠ 1 �1 � n 1 ��1 � n 2 � : : : �1 � n � n 1 �<br><!-- End of picture text -->

15Jacob Bernoulli 1654–1705, Švýcar 

35 

7 Posloupnosti 



<!-- Start of picture text -->
<1 C 1 1 C 1 1 D 1 C 1 � . 2 1 /n<br>1Š C 2Š 1 C 3Š 1 C ���C nŠ 1 < 1 C � 2 C 2 12 C 2 13 C ���C 2 n�1 � 1 � 1<br>2<br>D 1 C 2 1 � 1 < 1 C 2 D 3;<br>� 2 n �<br><!-- End of picture text -->

kde v předposledním řádku jsme využili nerovnost nŠ > 2<sup>n�1</sup> 8n 2 N, n � 3 (ověřte matematickou indukcí!), a vzorce pro součet prvních n členů geometrické posloupnosti. Dále an > a1 D 2 8n 2 N. Ukázali jsme tedy, že 2 < an < 3 pro 8n 2 N, tj. posloupnost je ohraničená. Celkově, podle věty 7.15(m2) má posloupnost limitu. 

Definice 7.17 — Eulerova ˇcísla. Limitu z předchozího příkladu nazýváme _Eulerovým číslem_ a značíme e (e 2 I, e � 2; 71828182846). 

Poznámka 7.18. Eulerovo číslo lze (ekvivalentně) definovat vícero způsoby, jeho objev (právě skrz limitu z příkladu 7.16) je přisuzován již zmíněnému Jacobu Bernoullimu. 

Definice 7.19 — nevlastní limity posloupnosti. Řekneme, že posloupnost fang má _nevlastní limitu_ 1 (resp. �1), jestliže ke každému h 2 R existuje n0 2 N takové, že pro každé n � n0 platí an > h (resp. an < h). Má-li posloupnost fang buď nevlastní limitu, nebo žádnou limitu nemá, řekneme, že _diverguje_ (někdy dále rozlišujeme, má-li nevlastní limitu, říkáme, že _určitě diverguje_ a nemá-li žádnou limitu, říkáme, že _osciluje_ ). 

Poznámka 7.20. a) Nahradíme-li ve větách 7.4 a 7.13 slovo „limita“ slovem „nevlastní limita“, zůstanou obě tvrzení v platnosti. 

b) Nechť fang je posloupnost taková, že lim an D 0. Jestliže existuje n1 2 N takové, že pro každé n � n1 je an > 0 (resp. an < 0, resp. an ¤ 0), pak lim a<sup><u>1</u></sup> n<sup>D1(resp.lim</sup> a<sup><u>1</u></sup> n<sup>D�1,resp.</sup> lim ja1nj<sup>D 1).</sup> 

c) Nechť lim an D 1 (resp. lim an D �1) a nechť posloupnost fbng je zdola (resp. shora) ohraničená. Pak lim.an C bn/ D 1 (resp. lim.an C bn/ D �1). 

d) Nechť lim an D 1 a nechť fbng je posloupnost taková, že existují n1 2 N, ı > 0 taková, že pro n � n1 je bn > ı (resp. bn < �ı). Pak lim anbn D 1 (resp. lim anbn D �1). Nechť lim an D �1 a nechť fbng je posloupnost taková, že existují n1 2 N, ı > 0 taková, že pro n � n1 je bn > ı (resp. bn < �ı). Pak lim anbn D �1 (resp. lim anbn D 1). 

e) Nechť lim janj D 1 a fbng je ohraničená posloupnost. Pak lim a<sup><u>1</u></sup> n<sup>D 0 a lim</sup> a<sup><u>bn</u></sup> n<sup>D 0.</sup> 

f) Je-li posloupnost fang neklesající (resp. nerostoucí) a není ohraničená shora (resp. zdola), pak je určitě divergentní a lim an D 1 (resp. lim an D �1). 

Definice 7.21 — vybrané posloupnosti. Nechť fang<sup>1</sup> nD1<sup>je posloupnost a fnkg1</sup> kD1<sup>je rostoucí posloupnost</sup> přirozených čísel. Posloupnost fank g<sup>1</sup> kD1<sup>se nazývá</sup><sup>_vybraná posloupnost z posloupnosti_fang.</sup> 

Například fa2ng D fa2; a4; a6; : : : g, fan2 g D fa1; a4; a9; : : : g, fangn<sup>1</sup> Dm<sup>Dfam; amC1; amC2; : : : g</sup> pro m 2 N jsou posloupnosti vybrané z fang. 

■ Vˇeta 7.22. _Nechť_ fang _je posloupnost. Pak_ limn!1 an D a 2 R<sup>�</sup> , _pro každou posloupnost_ fank g _vybranou z_ fang _platí_ limk!1 ank D a _._ 

_Důkaz._ „)“ Nechť a 2 R a buď " > 0 libovolné. K tomuto " existuje n0 2 N takové, že jan � aj < " pro každé n � n0. Poněvadž fnkg je rostoucí posloupnost přirozených čísel, existuje k0 2 N takové, že nk0 � n0 a nk � nk0 pro každé k � k0. Tedy pro každé k � k0 je jank � aj < ", což znamená lim ank D a. Pro a D ˙1 dokážeme tvrzení analogicky. 

„(“ Je triviální. Je-li klim!1<sup>ankD a pro každou rostoucí fnkg, platí to zejména pro nkD k.</sup> 

Kapitola 1. Vybrané statˇe z matematiky 

36 

Definice 7.23 — hromadného bodu. Číslo a 2 R nazveme _hromadným bodem_ posloupnosti fang, jestliže pro každé " > 0 existuje nekonečně mnoho indexů m 2 N tak, že platí jam � aj < ". 

Pˇríklad 7.24. Nalezněte hromadné body posloupnosti fang D f2.�1/<sup>n</sup> g. 

_Řešení._ Platí an D 2 pro n D 2k a an D �2 pro n D 2k � 1, k 2 N. Posloupnost má tedy dva hromadné body 2 a �2 (žádný další bod hromadným bodem být nemůže, protože vždy by bylo možné najít jeho okolí, ve kterém se nenachází žádný bod posloupnosti). 

■ Vˇeta 7.25. _Číslo_ a 2 R _je hromadným bodem posloupnosti_ fang , _existuje posloupnost_ fank g _vybraná z_ fang _, která konverguje k číslu_ a _._ 

_Důkaz._ „)“ Nechť a je hromadným bodem posloupnosti fang. K "1 D 1 existuje n1 2 N takové, že jan1 � aj < 1. K "2 D<sup><u>1</u></sup> 2<sup>existuje n22 N, n2> n1, takové, že jan2�aj <</sup><sup><u>1</u></sup> 2<sup>. K "3D</sup><sup><u>1</u></sup> 3<sup>existuje n32 N,</sup> n3 > n2, takové, že jan3 � aj <<sup><u>1</u></sup> 3<sup>. Touto konstrukcí dostaneme rostoucí posloupnost přirozených čísel</sup> fnkg takových, že jank � aj < k<sup><u>1</u>pro každé k2 N. Protože lim</sup> k<sup><u>1</u>D 0, ke každému " > 0 existuje k02 N</sup> takové, že j k<sup><u>1</u>�0jD</sup> k<sup><u>1</u><" pro každé k�k0. Tedy pro k�k0platí jank�aj<", což znamená, že</sup> lim ank D a. 

„(“ Jestliže existuje fank g taková, že lim ank D a, pak ke každému " > 0 existuje k0 2 N takové, že pro 8k � k0 (tedy pro nekonečně mnoho indexů k) platí jank � aj < ", což znamená, že a je hromadným bodem posloupnosti fang. 

■ Vˇeta 7.26 — Bolzanova<sup>16</sup> –Weierstrassova<sup>17</sup> . _Každá ohraničená posloupnost má alespoň jeden hromadný bod._ 

_Důkaz._ Ohraničenost posloupnosti fang znamená, že existují h; H 2 R taková, že h � an � H pro každé n 2 N. Položme Mk D fan W n � kg, k 2 N. Z konstrukce plyne, že Mk ¤ ; a Mk je shora ohraničená (H je její horní závora). Existuje tedy bk D sup Mk. Zřejmě bk � h pro každé k 2 N a poněvadž Mk � MkC1, platí bk � bkC1. Tedy posloupnost fbkg je nerostoucí a zdola ohraničená. Podle věty 7.15 je fbkg konvergentní, tj. existuje b 2 R tak, že lim bk D b. 

Ukažme, že b je hromadný bod posloupnosti fang. Pro spor připusťme, že není. Pak existuje " > 0 takové, že v intervalu .b � "; b C "/ leží pouze konečně mnoho členů posloupnosti fang nebo v něm neleží žádný člen posloupnosti. Jinak vyjádřeno, existuje n0 2 N takové, že pro každé k � n0 je buď ak � b � ", nebo ak � b C ". Protože číslo bk je definováno bk D supfan W n � kg, máme ak � bk 8k 2 N (viz vlastnost (s1) suprema v definici 6.1). Navíc, z lim bk D b plyne, že existuje k0 2 N takové, že pro každé k � k0 je bk < b C ". Poslední dvě nerovnosti dávají, že pro každé k � k0 je ak � bk < b C ". Pro k � n0 tedy nerovnost ak � b C " nemůže nastat a musí platit ak � bk � b � " (druhá nerovnost plyne z vlastnosti (s2) suprema v definici 6.1). Protože dále pro dvě konvergentní posloupnosti fcng, fdng, cn � dn platí lim cn � lim dn (viz poznámka a) za větou 7.6), je b D lim bk � b � ", což je spor. 

Přímým důsledkem vět 7.25 a 7.26 je následující tvrzení. 

■ Vˇeta 7.27. _Z každé ohraničené posloupnosti lze vybrat konvergentní podposloupnost. Je-li množina hromadných bodů posloupnosti prázdná, je posloupnost neohraničená._ 

Definice 7.28 — ˇcísel lim sup a lim inf. Buď fang posloupnost a M množina jejích hromadných bodů. a) Nechť M ¤ ;. Je-li fang ohraničená shora, klademe lim supn!1 an WD max M (stručně lim sup an), je-li fang ohraničená zdola, klademe lim infn!1 an WD min M . Není-li fang ohraničená shora (resp. zdola), klademe lim sup an D 1 (resp. lim inf an D �1). 

b) Nechť M D ;. Je-li posloupnost fang ohraničená shora (resp. zdola), klademe lim sup an D lim inf an D 

> 16Bernard Bolzano 1781–1848, Čech 

> 17Karl Weierstrass 1815–1897, Němec 

37 

7 Posloupnosti 

�1 (resp. lim sup an D lim inf an D 1). Není-li fang ohraničená shora ani zdola, klademe lim sup an D 1, lim inf an D �1. 

Číslo lim sup an (resp. lim inf an) se nazývá _limes superior_ (resp. _limes inferior_ ) posloupnosti fang. 

Poznámka 7.29. Stručně: lim sup an (resp. lim inf an) je největší (resp. nejmenší) hromadný bod posloupnosti fang, pokud je tato posloupnost ohraničená shora (resp. zdola), lim sup (resp. lim inf) tedy představuje nejmenší (resp. největší) omezení posloupnosti shora (zdola) „v nekonečnu“. Definice je korektní, lze totiž ukázat, že je-li množina hromadných bodů M shora (resp. zdola) ohraničená, pak existuje max M (resp. min M ). Dále lze ukázat, že v případě shora (resp. zdola) ohraničené posloupnosti 



<!-- Start of picture text -->
lim sup an D nlim!1 .supfak W k � ng/ .resp. lim inf an D nlim!1 .inffak W k � ng/ /:<br><!-- End of picture text -->

Tyto vztahy se někdy berou za definiční. Dále zřejmě platí lim inf an � lim sup an, lim inf an D lim sup an , existuje vlastní nebo nevlastní limita lim an. Zdůrazněme, že na rozdíl od limity, lim sup a lim inf existují vždy! 

Z početního hlediska je užitečné následující tvrzení: 

■ Vˇeta 7.30. _Nechť posloupnost_ fang _je ohraničená a_ fank.1/ g; fank.2/ g; : : : ; fank.`/ g _jsou vybrané podposloupnosti z_ fang _takové, že_ 



<!-- Start of picture text -->
lim ank.j / D a .j/ 2 R; j D 1; 2; : : : ; `<br><!-- End of picture text -->



<!-- Start of picture text -->
a platí  fnk .1/ g [ fnk .2/ g [ ���[ fnk .`/ g D N . Potom<br>lim sup an D maxfa .1/ ; : : : ; a .`/ g a lim inf an D minfa .1/ ; : : : ; a .`/ g:<br><!-- End of picture text -->

_Důkaz._ Nechť fanr g je vybraná podposloupnost z fang taková, že lim sup an D lim anr 2 R (taková posloupnost určitě existuje, neboť lim sup an je podle definice největším hromadným bodem a každý hromadný bod je podle věty 7.25 limitou nějaké vybrané podposloupnosti z fang). Protože sjednocení posloupností výběrů fn<sup>.j/</sup> k<sup>g je celá množina N, musí platit, že průnik fnrg \ fn.j /</sup> k<sup>g obsahuje nekonečně</sup> mnoho prvků (indexů) pro nějaké j 2 f1; 2; : : : ; `g. Pokud prvky tohoto průniku uspořádáme do rostoucí posloupnosti fnsg, pak fans g je vybraná podposloupnost zároveň z fanr g i z fank.j / g. Podle věty 7.22 je tedy 



<!-- Start of picture text -->
lim ans D lim anr D lim an .j / k D a.j / D lim sup a n :<br><!-- End of picture text -->

Protože číslo a<sup>.j /</sup> je limes superior posloupnosti, musí podle definice být největší ze všech čísel a<sup>.1/</sup> ; a<sup>.2/</sup> ; : : : ; a<sup>.`/</sup> . Pro lim inf bychom ukázali analogicky. 

Poznámka 7.31. Tvrzení zůstane v platnosti, i když vynecháme předpoklad ohraničenosti fang. Potom, pokud je některá z limit a<sup>.1/</sup> ; : : : ; a<sup>.`/</sup> plus (resp. minus) nekonečno, tak namísto maxima (resp. minima) klademe plus (resp. minus) nekonečno. 

Pˇríklad 7.32. Určete lim inf a lim sup posloupnosti fang D f2<sup>n sin �n=2</sup> g 

_Řešení._ Platí lim a2n D 2<sup>0</sup> D 1, lim a4n�3 D lim 2<sup>4n�3</sup> D 1, lim a4n�1 D lim 2<sup>�.4n�1/</sup> D 0, přičemž f2ng<sup>1</sup> nD1<sup>[ f4n �3g1</sup> nD1<sup>[ f4n �1g1</sup> nD1<sup>D N, a tedy podle věty 7.30 (a poznámky 7.31) platí</sup> lim inf an D 0 a lim sup an D 1. 

Definice 7.33 — cauchyovské poslouposti. Posloupnost fang se nazývá _cauchyovská (fundamentální)_ , jestliže ke každému " > 0 existuje n0 2 N takové, že pro každé n � n0 a každé m � n0 platí jam �anj < ". 

■ Vˇeta 7.34 — Cauchyovo–Bolzanovo kriterium konvergence. _Posloupnost_ fang _je konvergentní_ , _je cauchyovská._ 

Kapitola 1. Vybrané statˇe z matematiky 

38 

_Důkaz._ „)“ Nechť fang je konvergentní a lim an D a. Buď " > 0 libovolné. K 2<sup><u>"</u>existujen02N</sup> takové, že pro n � n0 je jan � aj < 2<sup><u>"</u>a pro m �n0je jam �aj <</sup> 2<sup><u>"</u>. Tedy pro n �n0a m �n0platí</sup> jam � anj D jam � a C a � anj �jam � aj C jan � aj < 2<sup><u>"</u>C</sup> 2<sup><u>"</u>D ".</sup> 

„(“ Nechť fang je cauchyovská. K číslu 1 existuje N 2 N takové, že pro 8n � N platí jan � aN j < 1, tedy aN � 1 < an < aN C 1. Položme h D minfa1; a2; : : : ; aN �1; aN � 1g, H D maxfa1; a2; : : : ; aN �1; aN C 1g. Pak pro každé n 2 N je h � an � H , tedy fang je ohraničená a podle věty existuje vybraná posloupnost fank g taková, že lim ank D a 2 R. Nechť " > 0 je libovolné. K 2<sup><u>"</u></sup> existuje k0 2 N takové, že pro každé k � k0 je jank � aj < 2<sup><u>"</u>. Současně existuje n02 N takové, že pro</sup> 8m; n � n0 je jam � anj < 2<sup><u>"</u>. Nechť n�n0je libovolné. Zvolme k1�k0takové, že nk</sup> 1<sup>�n0. Pak</sup> jan � aj D jan � ank1 C ank1 � aj �jan � ank1 j C jank1 � aj < 2<sup><u>"</u>C</sup> 2<sup><u>"</u>D ", a proto lim anD a.</sup> 

#### Pˇríklady k procviˇcení 

7.1. Ukažte, že lim<sup>~~p~~n</sup> a D 1 pro libovolné a 2 R<sup>C</sup> . _Nápověda._ Důkaz rozdělte na větve a > 1, a D 1 a 0 < a < 1. První případ potom řešte pomocí definice nebo pomocí Bernoulliovy nerovnosti, druhý případ je triviální a ve třetím případě využijte lim.an=bn/ D lim an= lim bn. 

7.2. Určete limitu 

7.3. Určete limitu 

7.4. Určete limitu 



<!-- Start of picture text -->
lim� p 9n 2 � 4 � 2n�:<br>lim 2n 3n  C  �  sin 1  n :<br>lim p n 2 n C 3 n :<br><!-- End of picture text -->

_Nápověda._ Využijte větu o třech posloupnostech. 

7.5. Určete limitu 



<!-- Start of picture text -->
1 n 3 � 2<br>lim :<br>n cos n 2 C 2n C 1<br>!<br><!-- End of picture text -->

_Nápověda._ Využijte větu o třech posloupnostech. 

7.6. Vypočítejte limitu 



<!-- Start of picture text -->
1 1<br>nlim!1 � 1 �13 C 3 � 5 C ���C .2n � 1/ � .2n C 1/ � :<br>1 1 1<br>Nápověda.  Platí .2n�1/�.2nC1/ D 2 1 � 2n�1 � 2nC1 �.<br>7.7. Určete limitu<br>nlim!1 �1 � n 1 �n :<br><!-- End of picture text -->

7.8. Ukažte, že posloupnost f<sup>~~p~~</sup> n 2 C 1=ng<sup>1</sup> nD1<sup>je monotónní a ohraničená.</sup> 

7.9. Určete lim sup a lim inf posloupnosti 



<!-- Start of picture text -->
n<br>� n C 1 sin2 n� 4 �1nD1 :<br><!-- End of picture text -->

_Nápověda._ Využijte větu 7.30. 

7.10. Určete limitu 



<!-- Start of picture text -->
lim 2n C 2 � . 4 �n2/n :<br><!-- End of picture text -->

_Výsledky._ 7.2. 1. 7.3.<sup>2</sup> =3. 7.4. 3. 7.5. 0. 7.6.<sup>1</sup> =2. 7.7.<sup>1</sup> =e. 7.9. lim sup an D 1, lim inf an D 0. 7.10. 0. 

8 Funkce reálné promˇenné 

39 

### 8 Funkce reálné promˇenné 

Definice 8.1 — funkce reálné promˇenné. _Funkcí reálné proměnné_ rozumíme zobrazení f W R ! R. Množina D.f / D fx 2 R W 9y 2 R takové, že y D f .x/g se nazývá _definiční obor funkce_ f . Množina H.f / D fy 2 R W 9x 2 R takové, že f .x/ D yg se nazývá _obor hodnot funkce_ f . 

Poznámka 8.2. Namísto y D f .x/ někdy píšeme x 7! y nebo x 7!f y. Prvky z D.f / se nazývají _hodnoty nezávislé proměnné_ ( _argumentu_ ). Prvky z H.f / se nazývají _hodnoty závislé proměnné_ ( _funkční hodnoty_ ). Pokud není explicitně uvedeno jinak, definičním oborem rozumíme největší (vzhledem k množinové inkluzi) množinu, pro jejíž prvky lze funkční hodnotu určit. 

Definice 8.3 — grafu funkce. _Grafem funkce_ f rozumíme množinu G D fŒx; f .x/� W x 2 D.f /g, kde Œx; y� značí kartézské souřadnice bodu v rovině. 

Pˇríklad 8.4. Určete D.f / a H.f / pro funkce 

x 1 je-li x 2 Q a) f .x/ D b) �.x/ D (Dirichletova<sup>18</sup> funkce): ~~p~~ 1 � x<sup>2;</sup> (0 je-li x 2 I _Řešení._ ad a) D.f / D .�1; 1/, neboť musí platit 1 � x<sup>2</sup> > 0 ) 1 > x<sup>2</sup> ) 1 > jxj. H.f / D R, neboť pro libovolné r 2 R je x ˙jrj r D ) .1 � x<sup>2</sup> /r<sup>2</sup> D x<sup>2</sup> ) r<sup>2</sup> D .1 C r<sup>2</sup> /x<sup>2</sup> ) x1;2 D ~~p~~ 1 � x<sup>2</sup> 1 C r<sup>2:</sup> Znaménko u x musí být stejné jako znaménko u r, tedy x D ~~p~~ 1rCr<sup>22 .�1; 1/.</sup> ad b) D.f / D R, H.f / D f0; 1g. Definice 8.5 — zúžení funkce. a) Funkce g se nazývá g se nazývá se nazývá _zúžením (restrikcí)_ funkce f , jestliže D.g/ � f , jestliže D.g/ � , jestliže D.g/ � D.g/ � � D.f / a pro 8x 8xx 2 D.g/ platí g.x/ D f .x/. D.g/ platí g.x/ D f .x/. platí g.x/ D f .x/. g.x/ D f .x/. D f .x/. f .x/.. b) Řekneme, že f f D g, jestliže D.f / D D.g/ a pro 8x g, jestliže D.f / D D.g/ a pro 8x, jestliže D.f / D D.g/ a pro 8x D.f / D D.g/ a pro 8x D D.g/ a pro 8x D.g/ a pro 8x a pro 8x 8xx 2 D.f / je f .x/ D g.x/. D.f / je f .x/ D g.x/. je f .x/ D g.x/. f .x/ D g.x/. D g.x/. g.x/.. Definice 8.6 — poˇcetních operací s funkcemi. Buďte f; g funkce, D.f / \ D.g/ ¤ ;. Pak definujeme _součet a rozdíl funkcí_ f; g: .f ˙ g/.x/ WD f .x/ ˙ g.x/ pro x 2 D.f / \ D.g/, _součin funkcí_ f; g: .fg/.x/ WD f .x/g.x/ pro x 2 D.f / \ D.g/, _podíl funkcí_ f; g: � <u>fg</u> �.x/ WD<sup><u>f</u></sup> g.x/<sup><u>.x/</u>pro x2 D.f / \ .D.g/ n fx2 D.g/ W g.x/ D 0g/,</sup> _absolutní hodnotu_ funkce f : jf j.x/ D jf .x/j D maxff .x/; �f .x/g pro x 2 D.f /. 

Definice 8.5 — zúžení funkce. a) Funkce g se nazývá g se nazývá se nazývá _zúžením (restrikcí)_ funkce f , jestliže D.g/ � f , jestliže D.g/ � , jestliže D.g/ � D.g/ � � D.f / a pro 8x 8xx 2 D.g/ platí g.x/ D f .x/. D.g/ platí g.x/ D f .x/. platí g.x/ D f .x/. g.x/ D f .x/. D f .x/. f .x/.. b) Řekneme, že f f D g, jestliže D.f / D D.g/ a pro 8x g, jestliže D.f / D D.g/ a pro 8x, jestliže D.f / D D.g/ a pro 8x D.f / D D.g/ a pro 8x D D.g/ a pro 8x D.g/ a pro 8x a pro 8x 8xx 2 D.f / je f .x/ D g.x/. D.f / je f .x/ D g.x/. je f .x/ D g.x/. f .x/ D g.x/. D g.x/. g.x/.. 

Definice 8.7 — ohraniˇcenosti funkce. Funkce f se nazývá _ohraničená_ ( _shora ohraničená, zdola ohraničená_ ), je-li množina H.f / ohraničená (shora ohraničená, zdola ohraničená) podmnožina množiny R. 

Poznámka 8.8. Funkce f je ohraničená právě tehdy, když existují a; b 2 R taková, že a � f .x/ � b pro každé x 2 D.f /, což nastane právě tehdy, když existuje h 2 R takové, že jf .x/j � h pro každé x 2 D.f /. Analogická tvrzení platí pro funkci ohraničenou shora nebo zdola. 

Kapitola 1. Vybrané statˇe z matematiky 

40 

Definice 8.9 — sudosti a lichosti funkce. Funkce f se nazývá _sudá_ , jestliže x 2 D.f / ) �x 2 D.f / a f .�x/ D f .x/. Funkce f se nazývá _lichá_ , jestliže x 2 D.f / ) �x 2 D.f / a f .�x/ D �f .x/. 

Pˇríklad 8.10. Příklady sudé funkce: x<sup>2</sup> , cos x, jxj. Příklady liché funkce: x<sup>3</sup> , sin x, tg x. 

Poznámka 8.11. Graf sudé funkce je symetrický pode osy y, graf liché funkce je symetrický podle počátku souřadné soustavy. 

■ Vˇeta 8.12. _Má-li funkce_ f _vlastnost_ x 2 D.f / ) �x 2 D.f / _, pak ji lze vyjádřit jako součet funkce sudé a liché._ 

_Důkaz._ Pro každé x 2 D.f / platí f .x/ D <u>12</u><sup>.f .x/Cf .�x//C</sup><sup><u>1</u></sup> 2<sup>.f .x/�f .�x//.Označíme-li</sup> g.x/ D <u>12</u><sup>.f .x/Cf .�x//,pakg.�x/D</sup> <u>12</u><sup>.f .�x/Cf .x//Dg.x/,tj.gjesudá.Označíme-li</sup> h.x/ D<sup><u>1</u></sup> 2<sup>.f .x/ �f .�x//, pak h.�x/ D</sup> 2<sup><u>1</u>.f .�x/ �f .x// D �f .x/, tj. h je lichá.</sup> 

Definice 8.13 — periodiˇcnosti funkce. Buď p 2 R, p > 0. Řekneme, že funkce f je _periodická s periodou_ p, jestliže x 2 D.f / ) x C p 2 D.f / a f .x C p/ D f .x/. 

Pˇríklad 8.14. Funkce sin a cos jsou periodické s periodou 2�, funkce tg a cotg s periodou �, konstantní funkce f .x/ D c 2 R má periodu jakékoliv p > 0. 

Poznámka 8.15. a) Je-li f periodická s periodou p > 0, pak je periodická i s periodou np, n 2 N. 

b) Množina period periodické funkce je nekonečná, tedy neprázdná a zdola ohraničená nulou. Musí tedy existovat p0 D inffp W p je perioda funkce f g. Pokud p0 je periodou f , nazýváme ji _nejmenší_ nebo _základní periodou_ funkce f . Periodická funkce nemusí mít nejmenší periodu. Např. periodou Dirichletovy funkce je každé kladné racionální číslo. 

Definice 8.16 — monotonie funkce. Řekneme, že funkce f je (i) _rostoucí_ (resp. _klesající_ ) _na intervalu_ I , jestliže I � D.f / a pro libovolná x1; x2 2 I platí x1 < x2 ) f .x1/ < f .x2/ (resp. x1 < x2 ) f .x1/ > f .x2/); 

(ii) _neklesající_ (resp. _nerostoucí_ ) _na intervalu_ I , jestliže I � D.f / a pro libovolná x1; x2 2 I platí x1 < x2 ) f .x1/ � f .x2/ (resp. x1 < x2 ) f .x1/ � f .x2/). Funkce buď rostoucí, nebo klesající na intervalu se nazývá _ryze monotónní na intervalu_ , funkce buď nerostoucí, nebo neklesající na intervalu se nazývá _monotónní na intervalu_ . 

Poznámka 8.17. Slovo „interval I “ v předchozí definici lze nahradit slovem „množina M � D.f /“. Uvedené pojmy v definici lze namísto v intervalu (globální vlastnost) zavést také v bodě (lokální vlastnost). 

Pˇríklad 8.18. Ukažte, že funkce f .x/ D x<sup>2</sup> není monotónní na R, ale je monotónní na h0; 1/. 

_Řešení:_ Např. pro x1 D �2, x2 D 3 je x1 < x2 a f .x1/ D 4 < 9 D f .x2/, a pro x1 D �3, x2 D �2 je x1 < x2, ale f .x1/ D 9 > 4 D f .x2/, f tedy nemůže být na R monotónní. Omezíme-li se ale na interval h0; 1/, pak x1 < x2 ) x1x1 < x1x2 < x2x2 ) x1<sup>2<x</sup> 2<sup>2(využili jsme axiomu (A13) množiny R).</sup> Tedy, f .x1/ < f .x2/, což znamená, že f je rostoucí, tedy je (ostře) monotónní. 

Definice 8.19 — konvexnosti a konkávnosti funkce. Řekneme, že funkce f je (i) _konvexní_ (resp. _konkávní_ ) na intervalu I , jestliže 8� 2 h0; 1i a 8x1; x2 2 I platí f .�x1 C.1��/x2/ � �f .x1/ C .1 � �/f .x2/ (resp. f .�x1 C .1 � �/x2/ � �f .x1/ C .1 � �/f .x2/); 

(ii) _ryze konvexní_ (resp. _ryze konkávní_ ) na intervalu I , jestliže pro každé � 2 .0; 1/ a každá dvě x1; x2 2 I , x1 ¤ x2, platí f .�x1 C .1 � �/x2/ < �f .x1/ C .1 � �/f .x2/ (resp. f .�x1 C .1 � �/x2/ > �f .x1/ C .1 � �/f .x2/). 

8 Funkce reálné promˇenné 

41 

Poznámka 8.20. Konvexnost znamená, že vedeme-li přímku body Œx1; f .x1/� a Œx2; f .x2/�, pak pro libovolné x3 2 hx1; x2i leží bod Œx3; f .x3/� pod nebo na této přímce. 

Definice 8.21 — složené funkce. Nechť f; ' jsou funkce přičemž platí H.'/ � D.f /. Pak funkce F D f ı ' W D.'/ ! R daná předpisem 

F.x/ D f .'.x// 

se nazývá _složená funkce_ . Funkce ' se nazývá _vnitřní složka funkce_ F , funkce f se nazývá _vnější složka funkce_ F . 

Pˇríklad 8.22. Vyšetřete složené funkce f ı ', kde a) '.x/ D x<sup>2</sup> , f .u/ D sin u; b) '.x/ D �x<sup>2</sup> , f .u/ D ln u. 

_Řešení._ ad a) Máme H.'/ D h0; 1/, D.f / D .�1; 1/, a tedy H.'/ � D.f /, F.x/ D f .'.x// D sin x<sup>2</sup> . 

ad b) Protože H.'/ D .�1; 0i a D.f / D .0; 1/, neplatí H.'/ � D.f / a složená funkce tedy neexistuje. 

Poznámka 8.23. Podmínka H.'/ � D.f / je nutná a postačující pro existenci složené funkce. Není-li tato podmínka splněna, lze jí někdy dosáhnout vhodným zúžením D.'/. Proces skládání lze opakovat, např. y D ln<sup>3</sup> .<sup>~~p~~</sup> x/ je složení y D u<sup>3</sup> , u D ln v, v D<sup>~~p~~</sup> x. 

Definice 8.24 — inverzní funkce. _Inverzní funkcí_ k prosté funkci f nazveme funkci f<sup>�1</sup> , pro kterou platí: D.f<sup>�1</sup> / D H.f / a zároveň každému y 2 D.f<sup>�1</sup> / je přiřazeno právě to x 2 D.f /, pro které je f .x/ D y. 

Poznámka 8.25. a) Protože f je prostá a zároveň surjekce D.f / na H.f /, je tedy bijekcí mezi D.f / a H.f / a musí platit také H.f<sup>�1</sup> / D D.f /. 

b) Graf inverzní funkce f<sup>�1</sup> je symetrický s grafem funkce f podle osy prvního a třetího kvadrantu. 

■ Vˇeta 8.26. _Je-li funkce_ f _ryze monotónní, pak je prostá._ 

_Důkaz._ Nechť pro určitost je f rostoucí a buďte x1; x2 2 D.f /, x1 ¤ x2. Pokud x1 < x2, pak f .x1/ < f .x2/; pokud x1 > x2, pak f .x1/ > f .x2/, a tedy f .x1/ ¤ f .x2/. 

Poznámka 8.27. Naopak tvrzení věty 8.26 neplatí, např. funkce 



<!-- Start of picture text -->
x C 1 na .0; 1i<br>f .x/ D<br>(2 � x na .1; 2/<br><!-- End of picture text -->

je na intervalu .0; 2/ prostá, ale není ryze monotónní (není ani monotónní). 

■ Vˇeta 8.28. _Nechť_ f _je rostoucí (resp. klesající) na množině_ D.f / _. Pak_ f<sup>�1</sup> _je rostoucí (resp. klesající) na množině_ H.f / _._ 

_Důkaz._ Nechť f je rostoucí na D.f / a nechť y1; y2 2 H.f /, y1 < y2. Označme x1 D f<sup>�1</sup> .y1/, x2 D f<sup>�1</sup> .y2/, tj. y1 D f .x1/, y2 D f .x2/. Kdyby x1 � x2, pak by y1 D f .x1/ � f .x2/ D y2 (protože f je rostoucí), což by byl spor s předpokladem y1 < y2. Platí tedy x1 D f<sup>�1</sup> .y1/ < f<sup>�1</sup> .y2/ D x2. 

#### Pˇríklady k procviˇcení 

- 8.1. Rozhodněte, zda dané relace jsou funkcemi: 

   - a) f D fŒx; y� 2 R<sup>2</sup> W x<sup>2</sup> C y<sup>2</sup> � 2x D �1g; 

Kapitola 1. Vybrané statˇe z matematiky 

42 

b) g D fŒx; y� 2 R<sup>2</sup> W y<sup>2</sup> C 2y C 1 D 0g. 

- 8.2. Napište definiční obor funkcí 



<!-- Start of picture text -->
3<br>a) f .x/ D p x 3 � 4x 2 C b) g.x/ D ln.ln.ln x//:<br>x � 6 ;<br><!-- End of picture text -->

8.3. Načrtněte graf funkcí f .x/ D x<sup>2</sup> C sin x, g.x/ D jx C jxj C 1j. 

8.4. Dokažte, že platí<sup>~~p~~</sup> n a<sup><u>m</u></sup> D .<sup>~~p~~n</sup> a/<sup>m</sup> pro každé m; n 2 N a a > 0. 

8.5. Rozložte funkci f .x/ D xC1 1<sup>, x¤ ˙1, na součet sudé a liché funkce.</sup> 

8.6. Je funkce f .x/ D cos x � 3 sin 4x periodická? Pokud ano, určete základní periodu. 



<!-- Start of picture text -->
Výsledky. 8.1. a) Ano, b) ano. 8.2. a) f0g [ h4; 6/ [ .6; 1/, b) .e; 1/. 8.5. 1�1x 2 � 1�xx 2 . 8.6. Ano, 2�.<br><!-- End of picture text -->

### 9 Rozdˇelení funkcí 

_Základní elementární funkce_ : konstantní, mocninná, exponenciální a logaritmická, goniometrická a cyklometrická, hyperbolická a hyperbolometrická funkce. 

_Elementární funkce_ : jsou to funkce, které lze vytvořit ze základních elementárních funkcí pouze pomocí konečného počtu operací sčítání, odčítání, násobení, dělení a mocnění racionálním číslem, přičemž můžeme použít i skládání. Ne každá funkce je elementární, např. �.x/ nebo sgn.x/. 

_Algebraické funkce_ : jsou to ty elementární funkce, které lze vytvořit pomocí operací sčítání, odčítání, násobení, dělení a mocnění s racionálním exponentem pouze z konstantní funkce a mocninné funkce x<sup>˛</sup> , ˛ 2 Q n f0g, přičemž opět připouštíme skládaní. Např. x<sup>3</sup> � 2x C 1,<sup>~~p~~</sup> 3 x<sup>2</sup> C 1. 

_Transcendentní funkce_ : jsou to elementární funkce, které nejsou algebraické, např. sin.x<sup>2</sup> � 1/, ln xe<sup>�x</sup> . _Vyšší transcendentní funkce:_ jsou funkce, které nelze vyjádřit v konečném tvaru pomocí elementárních funkcí, např. Si.x/ D R x0 <u>sint t</u> dt . 

_Racionální funkce_ : jsou to algebraické funkce, které jsou vytvořené pouze pomocí operací sčítání, odčítání, násobení a dělení z konstantní funkce a funkce x, např. x<sup>2</sup> C 4x � 5, x<sup><u>x32</u></sup> C<sup>�2</sup> 1<sup>. Racionální funkce</sup> lze dále rozdělit na _polynomy_ a _racionální lomené funkce (ryze a neryze)_ . 

~~<u>p</u>~~ xC3 _Iracionální funkce_ : jsou to algebraické funkce, které nejsou racionální, např.<sup>~~p~~</sup> 3 x�1<sup>.</sup> 

#### Pˇríklady k procviˇcení 

9.1. Napište, do jaké skupiny, patří následující funkce: 



<!-- Start of picture text -->
1 x � 1<br>a) b) tg 2 x C 1; c) d) p x x<br>p 1 � x 2 ; x 2 C x C 1 ;<br><!-- End of picture text -->

_Výsledky._ 9.1. a) Iracionální, b) transcendentní, c) racionální lomená, d) transcendentní. 

### 10 Základní elementární funkce 

##### Funkce exponenciální a logaritmická 

U exponenciální funkce jde o zavedení obecné mocniny a<sup>x</sup> , kde a > 0, x 2 R. Vyjdeme z 



<!-- Start of picture text -->
x D n 2 N W a n WD a„ � ƒ‚a ���…a; a 0 WD 1; x D �n; n 2 N W a �n WD a 1n ;<br>n�<br>x D n 1 ; n 2 N W a1=n WD p n a je číslo, pro které � p n x � n D a;<br>x D m n ; m 2 Z; n 2 N W am=n WD p n a m D � p n a � m:<br><!-- End of picture text -->

10 Základní elementární funkce 

43 

■ Lemma 10.1. a) _Ke každému_ x 2 R _existuje posloupnost racionálních čísel_ fxng _s_ lim xn D x _(existuje dokonce monotónní posloupnost s limitou_ x _)._ 

b) _Nechť_ a > 0 _,_ x 2 R _. Je-li_ fxng _libovolná posloupnost racionálních čísel taková, že_ lim xn D x _, pak existuje_ lim a<sup>xn</sup> D ˛ 2 R _. Platí_ ˛ > 0 _a tato hodnota nezávisí na volbě posloupnosti_ fxng _._ 

_Důkaz._ ad a) Tvrzení je důsledkem věty 6.15. Hledanou posloupnost je možné sestrojit takto. Pro každé n 2 N vybereme z intervalu .x � n<sup><u>1</u>; x C</sup> n<sup><u>1</u>/ libovolně xn2 Q (takové racionální číslo jistě existuje podle</sup> věty 6.15(ii)). Dostáváme tak posloupnost fxng � Q tak, že x � n<sup><u>1</u>< xn< x C</sup> n<sup><u>1</u>pro 8n 2 N. Protože</sup> lim�x � n<sup><u>1</u></sup> � D lim�x C n<sup><u>1</u></sup> � D x, podle věty o třech posloupnostech (viz věta 7.13) je lim xn D x. Pokud bychom racionální xn vybírali např. z intervalu �x � n<sup><u>1</u>; x �</sup> nC1 1 � (resp. �x C nC1 1<sup>; x C</sup> n<sup><u>1</u></sup> �), tak výsledná posloupnost bude rostoucí (resp. klesající). 

ad b) Nechť a > 1 a fxng neklesající posloupnost racionálních čísel s limitou x. Neklesající posloupnost znamená, že x1 � x2 � x3 ���� , což dává a<sup>x1</sup> � a<sup>x2</sup> � a<sup>x3</sup> ���� , tj. fa<sup>xn</sup> g je neklesající. Zvolíme-li h 2 Q tak, že h � x, pak také h � xn pro 8n 2 N, a tudíž a<sup>h</sup> � a<sup>xn</sup> pro každé n 2 N. To ale znamená, že fa<sup>xn</sup> g je shora ohraničená. Podle věty 7.15 (o monotónních posloupnostech) existuje lim a<sup>xn</sup> D ˛ 2 R, přičemž ˛ � a<sup>xn</sup> > 0. Dále, nechť nyní fyng � Q je libovolná posloupnost, která má limitu x a ukažme, že také lim a<sup>yn</sup> D ˛. Položme zn D yn � xn (zn je tedy racionální číslo). Pak podle věty 7.9 platí lim zn D lim yn � lim xn D x � x D 0. Ukažme, že lim a<sup>zn</sup> D 1. Platí lim<sup>~~p~~n</sup> a D 1 D lim a<sup>1=n</sup> (tuto limitu lze ověřit buď přímo z definice, nebo pomocí Bernoulliovy nerovnosti, viz cvičení 7.1) a tedy také (podle věty 7.9(iv)) lim a<sup>1=n</sup> <u>1</u><sup>D 1. Buď " > 0 libovolné. Pak existuje n12 N takové, že pro každé n �n1</sup> je 1�" < a<sup>1=n</sup> < 1C", a existuje n2 2 N takové, že pro každé n � n2 je 1�" < a<sup>�1=n</sup> < 1C". Tedy pro m D maxfn1; n2g platí 1 � " < a<sup>�1=m</sup> < 1 < a<sup>1=m</sup> < 1 C ". Protože lim zn D 0, existuje n0 2 N takové, že pro každé n � n0 je � m<sup><u>1</u>< zn<</sup> m<sup><u>1</u>, a tedy 1 �" < a�1=m< azn< a1=m< 1 C ", což znamená, že</sup> lim a<sup>zn</sup> D 1. Celkově tedy, lim a<sup>yn</sup> D lim a<sup>znCxn</sup> D lim.a<sup>zn</sup> � a<sup>xn</sup> / D lim a<sup>zn</sup> � lim a<sup>xn</sup> D 1 � ˛ D ˛. 

Nechť a D 1. Tento případ je triviální, neboť 1<sup>xn</sup> D 1 pro každé xn 2 Q a tedy lim 1<sup>xn</sup> D 1. 

Nechť 0 < a < 1. Pak b D a<sup><u>1</u>> 0. Je-li fxng libovolná posloupnost racionálních čísel s limitou x, pak</sup> podle první části důkazu existuje limita ˇ D lim b<sup>xn</sup> . Podle věty 7.9(iv) existuje lim a<sup>xn</sup> D lim b<sup><u>x</u></sup> <u>1</u><sup>nD</sup> 1=ˇ. 

Definice 10.2 — exponenciální funkce. Buď a > 0. _Exponenciální funkcí_ nazveme funkci f .x/ D a<sup>x</sup> definovanou pro každé x 2 R předpisem a<sup>x</sup> D lim a<sup>xn</sup> , kde fxng je libovolná posloupnost racionálních čísel s limitou x. 

Vlastnosti: 

- a) D.f / D R, H.f / D R<sup>C</sup> ; 

- b) Pro každá dvě x; y 2 R platí a<sup>xCy</sup> D a<sup>x</sup> � a<sup>y</sup> , a<sup><u>ayx</u>D ax�y, .ax/yD axy;</sup> 

c) Pro a > 1 je funkce rostoucí, pro 0 < a < 1 je klesající, pro a D 1 je 1<sup>x</sup> D 1, x 2 R. 

Poznámka 10.3. a) Je-li x > 0, pak lze definici rozšířit i na případ a D 0, kdy klademe 0<sup>x</sup> D 0. 

b) Z exponenciálních funkcí má největší význam funkce f .x/ D e<sup>x</sup> , kde e D lim.1 C n<sup><u>1</u>/n(označuje</sup> se také exp x). Tuto funkci nazýváme _přirozená exponenciální funkce_ . 

Definice 10.4 — logaritmické funkce. Buď a > 0, a ¤ 1. Inverzní funkce k funkci f .x/ D a<sup>x</sup> se nazývá _logaritmická funkce_ . Značíme ji loga x. 

Vlastnosti: 

- (i) D.f / D R<sup>C</sup> , H.f / D R; 

- (ii) loga.xy/ D loga x C loga y, loga yx<sup>Dlogax �logay, pro x2RCa y2R platí: logaxyD</sup> y loga x; 

- (iii) Pro a > 0 je rostoucí, pro 0 < a < 1 je klesající. 

Kapitola 1. Vybrané statˇe z matematiky 

44 

Poznámka 10.5. Buďte a > 0, b > 0, a ¤ 1 ¤ b. Pro každé x 2 R<sup>C</sup> platí logb x D<sup>logax</sup> loga b<sup>. Podobně jako</sup> u exponenciální funkce má největší význam logaritmická funkce loge x. Značí se ln x a nazývá _přirozená_ nebo _přirozený logaritmus_ . Libovolný logaritmus lze převést na přirozený: loga x D<sup><u>ln</u></sup> ln<sup><u>x</u></sup> a<sup>. Také obecnou</sup> exponenciální funkci lze převést na přirozenou, neboť pro a > 0, x 2 R platí e<sup>x ln a</sup> D .e<sup>ln a</sup> /<sup>x</sup> D a<sup>x</sup> . 

##### Mocninná funkce 

Definice 10.6 — mocninné funkce. Nechť a 2 R. Funkce f .x/ D x<sup>a</sup> definovaná vztahem x<sup>a</sup> WD e<sup>a ln x</sup> se nazývá _obecná mocninná funkce_ . 

Vlastnosti: 

   - a) D.f / D R<sup>C</sup> , H.f / D .0; 1/; 

   - b) Pro každá dvě x; y 2 R<sup>C</sup> platí: .xy/<sup>a</sup> D x<sup>a</sup> y<sup>a</sup> , � yx �a D yxa<sup><u>a</u>.</sup> 

   - c) Je rostoucí pro a > 0 a klesající pro a < 0. 

- Poznámka 10.7. V některých speciálních případech lze definiční obor rozšířit i mimo interval .0; 1/: 

   - Je-li a 2 N0, pak D.f / D R. 

   - Je-li a 2 Z, a < 0, pak D.f / D R n f0g. 

   - Je-li a D<sup><u>m</u></sup> n<sup>2Q, m2Z, n2N, m; n nesoudělná a n liché, pak pro a�0 je D.f /DR a pro</sup> a < 0 je D.f / D R n f0g. 

##### Funkce goniometrické a cyklometrické 

Na jednotkovou kružnici se středem v počátku souřadné soustavy naneseme od bodu A D Œ1; 0� oblouk délky jxj v kladném smyslu (tj. proti směru pohybu hodinových ručiček) pro x > 0 a v záporném smyslu pro x < 0. Obdržíme bod B, jehož první souřadnici označíme cos x a druhou sin x. Dále klademe tg x WD cos<sup><u>sin x</u></sup> x<sup>, cotg xWD</sup><sup><u>cos</u></sup> sin x<sup><u>x</u>. Tento popis není definicí, protože se používá vágní pojem„délka oblouku“,</sup> který nebyl přesně zaveden. _Goniometrické funkce_ sin, cos, tg, cotg jsou tedy prozatím dány intuitivně. 

Vlastnosti: 

- a) D.sin/ D D.cos/ D R, H.sin/ D H.cos/ D h�1; 1i, D.tg/ D R n ˚ �2<sup>C k�Wk2Z</sup> �, D.cotg/ D R n fk� W k 2 Zg, H.tg/ D H.cotg/ D R; 

- b) sin, cos jsou periodické se základní periodou 2�, tg, cotg jsou periodické se základní periodou �. c) sin je rostoucí na ˝�<sup><u>�</u></sup> 2<sup>C 2k�;</sup><sup><u>�</u></sup> 2<sup>C 2k�</sup> ˛ a je klesající na ˝ �2<sup>C 2k�;</sup><sup><u>3�</u></sup> 2<sup>C 2k�</sup> ˛, k 2 Z, cos je rostoucí �<sup><u>�</u></sup> 

- na h.2k � 1/�; 2k�i a je klesající na h2k�; .2k C 1/�i, k 2 Z, tg je rostoucí na � 2<sup>C k�;</sup><sup><u>�</u></sup> 2<sup>C k�</sup> �, k 2 Z, cotg je klesající na .k�; .k C 1/�/, k 2 Z; 

- d) sin, tg, cotg jsou liché, cos je sudá funkce; 

- e) sin<sup>2</sup> x C cos<sup>2</sup> x D 1, tg x � cotg x D 1, sin x D cos�x �<sup><u>�</u></sup> 2 � D cos� <u>�2</u><sup>�x</sup> �, cos x D sin�x C<sup><u>�</u></sup> 2 � D sin� <u>�2</u><sup>�x</sup> � pro všechna přípustná x; 

- f) Vzorce (vybrané): 



<!-- Start of picture text -->
sin.x ˙ y/ D sin x cos y ˙ sin y cos x; cos.x ˙ y/ D cos x cos y � sin x sin y;<br>tg.x C y/ D tg x C tg y sin 2x D 2 sin x cos x; cos 2x D cos 2 x � sin 2 x;<br>1 � tg x tg y ;<br>1 � cos x 1 C cos x<br>; ;<br>ˇˇˇsin x2 ˇˇˇ D r 2 ˇˇˇcos x2 ˇˇˇ D r 2<br>sin x ˙ sin y D 2 sin x ˙ y cos x � y ; cos x C cos y D 2 cos x C y cos x � y ;<br>2 2 2 2<br>cos x � cos y D �2 sin x C y sin x � y ; sin x cos y D 1<br>2 2 2 .sin.x C y/ C sin.x � y//;<br>cos x cos y D 1 sin x sin y D 1<br>2 .cos.x C y/ C cos.x � y//; 2 .cos.x � y/ � cos.x C y//:<br>Pˇríklad 10.8. Dokažte, že funkce f .x/ D cos x C cos p 2x není periodická.<br><!-- End of picture text -->

10 Základní elementární funkce 

45 

_Řešení._ Pro spor předpokládejme, že f je periodická, tj. existuje p > 0 takové, že f .x C p/ D f .x/ pro každé x 2 R. Položíme-li x D 0, pak tato rovnost dává cos p C cos ~~p~~ 2p D cos 0 C cos 0 D 2. Protože funkce cos nabývá nejvýše hodnoty 1, musí být současně cos p D 1 a cos ~~p~~ 2p D 1. Odtud plyne, že p D 2�k pro nějaké k 2 Z a zároveň ~~p~~ 2p D 2�j pro nějaké j 2 Z. To znamená, že je buď p D 0, nebo, dosadíme-li z prvního vyjádření do druhého, ~~p~~ 2.2�k/ D 2�j , tj. ~~p~~ 2 D k=j je racionální číslo. V obou případech tedy máme spor. 

_Funkce cyklometrické_ jsou funkce inverzní k funkcím goniometrickým. Ve všech případech je nutno zúžit definiční obor příslušné goniometrické funkce tak, aby funkce byla ryze monotónní (tedy prostá). Je přirozené tento interval vzít „co nejblíže počátku“. Pro sin bereme interval ˝�<sup><u>�</u></sup> 2<sup>;</sup><sup><u>�</u></sup> 2 ˛, pro cos interval h0; �i, pro tg interval ��<sup><u>�</u></sup> 2<sup>;</sup><sup><u>�</u></sup> 2 � a pro cotg interval .0; �/. Funkce cyklometrické se nazývají _arcus_ a značí se arcsin, arccos, arctg, arccotg. 

Vlastnosti: 

- (i) D.arcsin/ D D.arccos/ D h�1; 1i, H.arcsin/ D ˝�<sup><u>�</u></sup> 2<sup>;</sup><sup><u>�</u></sup> 2 ˛, H.arccos/ D h0; �i, D.arctg/ D D.arccotg/ D R, H.arctg/ D .�<sup><u>�</u></sup> 2<sup>;</sup><sup><u>�</u></sup> 2<sup>/, H.arccotg/ D .0; �/;</sup> 

- (ii) Pro každé x 2 h�1; 1i platí arcsin x C arccos x D<sup><u>�</u></sup> 2<sup>.</sup> 

- (iii) Pro každé x 2 R platí arctg x C arccotg x D<sup><u>�</u></sup> 2<sup>.</sup> (iv) Vztahy mezi cyklometrickými funkcemi: 



<!-- Start of picture text -->
arcsin x D � x x<br>2 � arccos x D arctg p 1 � x 2 D � 2 � arccotg p 1 � x 2 ;<br>arccos x D � 2 � arcsin x D � 2 � arctg p 1 �x x 2 D arccotg p 1 �x x 2 ;<br>x x<br>arctg x D arcsin p 1 C x 2 D � 2 � arccos p 1 C x 2 D � 2 � arccotg x;<br>arccotg x D � x x<br>2 � arcsin p 1 C x 2 D arccos p 1 C x 2 D � 2 � arctg x:<br><!-- End of picture text -->

Lze odvodit celou řadu dalších identit podobně jako u goniometrických funkcí, např. platí arctg xCarctg y D arctg 1<sup>x</sup> �<sup><u>C</u></sup> xy<sup><u>y</u>pro jxyj < 1.</sup> 

Poznámka 10.9. Namísto kartézských souřadnic Œx; y� bodu v rovině lze tento bod popsat pomocí polárních souřadnic Œ'; ��, ' 2 h0; 2�/. Transformace polárních souřadnic na kartézské je dána vztahy x D � cos ', y D � sin ' a transformace kartézských na polární je dána vztahy 



<!-- Start of picture text -->
� D q x 2 C y 2 ; ' D arctg 2.x; y/;<br><!-- End of picture text -->

kde zobrazení arctg 2 W R � R ! h0; 2�/ je definováno: 



<!-- Start of picture text -->
8arctg y x pro x > 0; y � 0;<br>arctg y x C � pro x < 0; y 2 R;<br>arctg y x C 2� pro x > 0; y < 0;<br>arctg 2.x; y/ D ˆˆˆˆˆˆˆˆ< �2 pro x D 0; y > 0;<br>3�2 pro x D 0; y < 0;<br>ˆˆˆˆˆˆˆˆ:nedefinováno pro x D 0; y D 0:<br><!-- End of picture text -->

Pro počátek Œ0; 0� je � D 0 a ' není zobrazením arctg 2 definováno, pro tento bod pak obvykle klademe ' D 0. 

##### Funkce hyperbolické a hyperbolometrické 

_Hyperbolické funkce_ jsou sinh, cosh, tgh, cotgh. Mají podobné vlastnosti jako goniometrické funkce. Definujeme 



<!-- Start of picture text -->
sinh x WD ex � e�x ; cosh x WD ex C e�x (graf funkce se nazývá řetězovka);<br>2 2<br><!-- End of picture text -->

Kapitola 1. Vybrané statˇe z matematiky 

46 



<!-- Start of picture text -->
tgh x WD sinh x cotgh x WD cosh x<br>cosh x ; sinh x :<br>y y<br>3<br>3<br>2<br>1<br>2<br>x<br>�2 �1 1 2<br>�1<br>1<br>�2<br>�3 x<br>�2 �1 0 1 2<br><!-- End of picture text -->

Obrázek 10.1: Grafy funkcí sinh (vlevo) a cosh (vpravo) 



<!-- Start of picture text -->
y<br>4<br>y<br>1<br>2<br>0; 5<br>x x<br>�2 �1 1 2 �3 �2 �1 1 2 3<br>�0; 5<br>�2<br>�1<br>�4<br><!-- End of picture text -->

Obrázek 10.2: Grafy funkcí tgh (vlevo) a cotgh (vpravo) 

Vlastnosti: 

a) D.sinh/ D D.cosh/ D D.tgh/ D R, D.cotgh/ D R n f0g, H.sinh/ D R, H.cosh/ D h1; 1/, H.tgh/ D .�1; 1/, H.cotgh/ D .�1; �1/ [ .1; 1/; b) sinh, tgh a cotgh jsou liché funkce, cosh je sudá. c) Vzorce: 

cosh<sup>2</sup> x � sinh<sup>2</sup> x D 1; sinh 2x D 2 sinh x cosh x; cosh 2x D sinh<sup>2</sup> x C cosh<sup>2</sup> x; sinh<sup>2</sup> x D<sup>1</sup> 2<sup>.cosh 2x �1/;</sup> cosh<sup>2</sup> x D<sup>1</sup> 2<sup>.cosh 2x C 1/;</sup> tgh 2x D 1 C2 t tghgh x<sup>2</sup> x ; sinh.x ˙ y/ D sinh x cosh y ˙ cosh x sinh y; cosh.x ˙ y/ D cosh x cosh y ˙ sinh x sinh y; tgh.x ˙ y/ D<sup>tgh x ˙ tgh</sup><sup><u>y</u></sup> 1 ˙ tgh x tgh y<sup>:</sup> 

_Hyperbolometrické funkce_ argsinh, argcosh, argtgh, argcotgh (arg je zkratka z „argument“) jsou funkce inverzní k hyperbolickým (hyperbolický kosinus není na svém D.f / prostá, bereme tedy interval h0; 1/). 

11 Racionální funkce 

47 



<!-- Start of picture text -->
2 y y<br>2<br>1 1; 5<br>x<br>1<br>�4 �2 2 4<br>�1 0; 5<br>x<br>�2<br>0 1 2 3 4<br>Obrázek 10.3: Grafy funkcí argsinh (vlevo) a argcosh (vpravo)<br>y<br>2<br>y<br>1; 5<br>1<br>1<br>0; 5<br>x x<br>�1 �0; 5 0; 5 1 �3 �2 �1 0 1 2 3<br>�0; 5<br>�1<br>�1<br>�1; 5<br>�2<br><!-- End of picture text -->

Obrázek 10.4: Grafy funkcí argtgh (vlevo) a argcotgh (vpravo) 

Vlastnosti: 

- (i) D.argsinh/ D R, D.argcosh/ D h1; 1/, D.argtgh/ D .�1; 1/, D.argcotgh/ D .�1; �1/ [ .1; 1/, H.argsinh/ D R, H.argcosh/ D h0; 1/, H.argtgh/ D R, H.argcotgh/ D R n f0g; 

- (ii) argsinh, argtgh a argcotgh jsou liché funkce; 

(iii) Na svých definičních oborech platí: 



<!-- Start of picture text -->
argsinh x D ln.x C p x 2 C 1/; argcosh x D ln.x C p x 2 � 1/;<br>argtgh x D 1 2 ln 1 1  C  �  x x ; argcotgh x D 1 2 ln x x  C  �  1 1 :<br><!-- End of picture text -->

#### Pˇríklady k procviˇcení 

10.1. Dokažte, že pro každá dvě x; y 2 R<sup>C</sup> platí loga.xy/ D loga x C loga y. 



<!-- Start of picture text -->
10.2. Dokažte, že pro libovolné x 2 R platí arctg x D arcsin x<br>p 1Cx 2 .<br><!-- End of picture text -->

### 11 Racionální funkce 

##### Polynomy 

Definice 11.1 — polynomu. Nechť n 2 N0 a a0; a1; : : : ; an 2 R, an ¤ 0. _Polynom (celistvá racionální funkce)_ je funkce daná předpisem 



<!-- Start of picture text -->
P.x/ D anx n C an�1x n�1 C ���C a1x C a0:<br><!-- End of picture text -->

Číslo n nazýváme _stupeň polynomu_ a čísla a0; a1; : : : ; an nazýváme _koeficienty polynomu_ . Pokud 

Kapitola 1. Vybrané statˇe z matematiky 

48 

připustíme, že všechny koeficienty jsou nulové, pak dostaneme funkci P.x/ D 0, x 2 R, kterou nazveme _nulovým polynomem_ . 

Pro každý polynom P platí D.P / D R a 



<!-- Start of picture text -->
8R je-li n liché;<br>H.P / D hb; 1/ je-li n sudé a an > 0;<br>ˆ<<br>ˆ:.�1; bi je-li n sudé a an < 0;<br><!-- End of picture text -->

kde číslo b 2 R závisí na konkretním polynomu. 

Budeme potřebovat širší číselný obor než je R, tím budou komplexní čísla. _Množina komplexních čísel_ je množina 

C WD fa C b i W a; b 2 Rg; kde i<sup>2</sup> D �1 .i se nazývá _imaginární jednotka_ / 

s operacemi C W .a1 C b1 i/ C .a2 C b2 i/ D .a1 C a2/ C .b1 C b2/ i a �W .a1 C b1 i/ � .a2 C b2 i/ D .a1a2 � b1b2/ C .a1b2 C a2b1/ i. Reálná čísla lze chápat jako podmnožinu komplexních čísel, kdy reálné číslo a ztotožníme s komplexním číslem a C 0 i. Komplexní číslo z D a C b i, pro které je b ¤ 0 se nazývá _imaginární_ , a je-li navíc a D 0, tak se nazývá _ryze imaginární_ . Je-li z D a C b i, pak <u>z</u> D a � b i se nazývá _číslo komplexně sdružené_ , jzj D ~~<u>p</u>~~ z � <u>z</u> D ~~p~~ a<sup>2</sup> C b<sup>2</sup> se nazývá _absolutní hodnota (modul)_ čísla z. Platí <u>z1 C z2</u> D <u>z1</u> C <u>z2, z1 � z2</u> D <u>z1</u> � <u>z2</u> a z<sup><u>n</u></sup> D <u>z</u><sup>~~n~~</sup> pro n 2 N. Dále platí z 2 R , b D 0 , z D <u>z.</u> Množina C s operacemi C; � splňuje axiomy (A1)–(A9) z definice reálných čísel, tvoří tedy pole. Toto pole však nelze uspořádat. Přesněji, relaci (ostrého) uspořádaní na C zavést lze, ale nikdy ne tak, aby platily axiomy (A10), (A12) a (A13) z definice množiny R. 

Definice 11.2 — koˇrene polynomu. Číslo ˛ 2 C se nazývá _kořen (nulový bod)_ polynomu P , jestliže platí P.˛/ D 0. Je-li ˛ kořenem P , pak lineární polynom x � ˛ se nazývá _kořenovým činitelem (faktorem)_ polynomu P . 

■ Vˇeta 11.3 — základní vˇeta algebry. _Každý polynom stupně_ n � 1 _s komplexními koeficienty má alespoň jeden komplexní kořen._ 

Tato věta je známa od 17. století. První (chybný) pokus o důkaz publikoval d’Alembert<sup>19</sup> roku 1746, větu dokázal Gauss<sup>20</sup> roku 1799. Dodneška je známo mnoho důkazů, zajímavé je, že ač se jedná o algebraický problém, žádný z důkazů nevyužívá čistě algebraické postupy. Obsáhle je o důkazech pojednáno např. v diplomové práci `http://is.muni.cz/th/326140/prif_m/DP_Cechova_Petra.pdf` . 

■ Vˇeta 11.4 — Bézoutova<sup>21</sup> vˇeta. _Buď_ P _polynom stupně_ n � 1 _. Číslo_ ˛ 2 C _je kořenem_ P _, právě když existuje polynom_ Q _stupně_ n � 1 _takový, že_ P.x/ D .x � ˛/Q.x/ _._ 

_Důkaz._ „)“ Nechť P je polynom stupně n a ˛ 2 C jeho kořen. Pak 

P.x/ D P.x/ � 0 D P.x/ � P.˛/ 

D anx<sup>n</sup> C an�1x<sup>n�1</sup> C ���C a1x C a0 � .an˛<sup>n</sup> C an�1˛<sup>n�1</sup> C ���C a1˛ C a0/ D an.x<sup>n</sup> � ˛<sup>n</sup> / C an�1.x<sup>n�1</sup> � ˛<sup>n�1</sup> / C ���C a1.x � ˛/ C a0.1 � 1/: 

Pro každé k 2 N platí .x<sup>k</sup> � ˛<sup>k</sup> / D .x � ˛/.x<sup>k�1</sup> C x<sup>k�2</sup> ˛ C x<sup>k�3</sup> ˛<sup>2</sup> C ���C x˛<sup>k�2</sup> C ˛<sup>k�1</sup> /. Tedy 

P.x/ D an.x � ˛/.x<sup>n�1</sup> C x<sup>n�2</sup> ˛ C x<sup>n�3</sup> ˛<sup>2</sup> C ���C ˛<sup>n�1</sup> / 

C an�1.x � ˛/.x<sup>n�2</sup> C x<sup>n�3</sup> ˛ C ���C ˛<sup>n�2</sup> / C ���C a1.x � ˛/: 

> 19Jean Baptiste Le Rond d’Alembert, 1717–1783, Francouz 

> 20Carl Friedrich Gauss 1777–1855, Němec 

> 21Étienne Bézout 1730–1783, Francouz 

11 Racionální funkce 

49 

Označíme-li Q.x/ D an.x<sup>n�1</sup> C x<sup>n�2</sup> ˛ C x<sup>n�3</sup> ˛<sup>2</sup> C ���C ˛<sup>n�1</sup> / C an�1.x<sup>n�2</sup> C x<sup>n�3</sup> ˛ C ���C ˛<sup>n�2</sup> / C ���C a1, dostaneme požadované tvrzení. 

„(“ Zřejmé. 

Je-li n � 1 stupeň polynomu P , pak podle předchozí věty existuje kořen ˛1 a polynom Q1 stupně n � 1 takový, že P.x/ D .x � ˛1/Q1.x/. Je-li n � 1 � 1, pak Q1.x/ D .x � ˛2/Q2.x/ a tedy P.x/ D .x � ˛1/.x � ˛2/Q2.x/. Pokud budeme takto analogicky pokračovat, dostaneme po n krocích 



<!-- Start of picture text -->
P.x/ D an.x � ˛1/.x � ˛2/ : : : .x � ˛n/:<br><!-- End of picture text -->

Může se stát, že ˛1 D ˛2 D ���D ˛k, k � n. Pak P.x/ D an.x � ˛1/<sup>k1</sup> .x � ˛2/<sup>k2</sup> : : : .x � ˛m/<sup>km</sup> , přičemž k1; k2; : : : ; km 2 N, k1 C k2 C ���C km D n. 

Definice 11.5 — násobného koˇrene polynomu. Číslo ˛ 2 C se nazývá _k-násobný kořen_ polynomu P , jestliže P.x/ D .x � ˛/<sup>k</sup> Q.x/ pro každé x 2 R, kde Q je polynom nemající kořen ˛ (1-násobný kořen se nazývá _jednoduchý_ ). 

Důsledkem věty 11.4 a úvahy pod touto větou je tvrzení: 

■ Vˇeta 11.6 — o rozkladu polynomu na koˇrenové faktory. _Nechť_ P _je polynom stupně_ n � 1 _a nechť_ ˛1; ˛2; : : : ; ˛m _jsou všechny jeho navzájem různé kořeny, přičemž_ ˛1 _je_ k1 _-násobný,_ ˛2 _je_ k2 _-násobný,_ : : : _,_ ˛m _je_ km _-násobný. Pak platí_ 

P.x/ D an.x � ˛1/<sup>k1</sup> .x � ˛2/<sup>k2</sup> : : : .x � ˛m/<sup>km</sup> ; k1; k2; : : : ; km 2 N; k1 C k2 C ���C km D n: 

■ D˚usledek 11.7. _Každý polynom stupně_ n � 1 _má právě_ n _kořenů, pokud_ k _-násobný kořen počítáme_ k _-krát._ 

Poznámka 11.8. Předchozí tvrzení mají existenční charakter, nedávají návod, jak kořeny určit. Pro polynomy stupně 1,2,3 a 4 existují obecné vzorce pro výpočet kořenů, pro polynom stupně 5 a výše už žádný takový vzorec neexistuje (přesněji, lze dokázat, že takový vzorec nelze napsat). V praxi je při hledání kořenů možno použít Hornerovo<sup>22</sup> (Ruffinovo<sup>23</sup> ) schéma. Je to „tipovací“ metoda pro získání reálného kořene, jejíž předností je, že při jeho nalezení zároveň obdržíme koeficienty polynomu Q z věty 11.4). 

Pˇríklad 11.9. Rozložte polynomy a) P.x/ D x<sup>5</sup> Cx<sup>4</sup> Cx<sup>3</sup> �x<sup>2</sup> �x �1, b) P.x/ D x<sup>5</sup> �3x<sup>4</sup> Cx<sup>3</sup> Cx<sup>2</sup> C4. 

_Řešení._ ad a) P.x/ D x<sup>5</sup> Cx<sup>4</sup> Cx<sup>3</sup> �x<sup>2</sup> �x�1 D x<sup>3</sup> .x<sup>2</sup> CxC1/�.x<sup>2</sup> CxC1/ D .x<sup>3</sup> �1/.x<sup>2</sup> CxC1/ D .x � 1/.x<sup>2</sup> C x C 1/.x<sup>2</sup> C x C 1/ D .x � 1/�x � �� 2<sup><u>1</u>C i</sup> ~~<u>p</u>~~ 23 ��2�x � ��<sup><u>1</u></sup> 2<sup>�i</sup> ~~<u>p</u>~~ 23 ��2. 

ad b) P.x/ D .x C 1/.x � 2/<sup>2</sup> .x<sup>2</sup> C 1/ D .x C 1/.x � 2/<sup>2</sup> .x C i/.x � i/. 

■ Vˇeta 11.10. _Nechť polynom_ P _má reálné koeficienty a komplexní kořen_ ˛ _. Pak má také komplexně sdružený kořen_ <u>˛</u> _a násobnosti kořenů_ ˛ _a_ <u>˛</u> _jsou stejné._ 

_Důkaz._ Pro x 2 R je <u>x</u> D x a tedy P.x/ D aNn Nx<sup>n</sup> C <u>an�1 Nx</u><sup>n�1</sup> C ���C <u>a0</u> D anx<sup>n</sup> C an�1x<sup>n�1</sup> C ���C a0 D P.x/. Podle věty 11.6 je P.x/ D an.x � ˛1/<sup>k1</sup> .x � ˛2/<sup>k2</sup> : : : .x � ˛m/<sup>km</sup> , a tedy P.x/ D an.x � <u>˛1/</u><sup>k1</sup> .x � <u>˛2/</u><sup>k2</sup> : : : .x � <u>˛m/</u><sup>km</sup> (využíváme vlastností <u>z1 � z2</u> D <u>z1</u> � <u>z2, z1 � z2</u> D <u>z1</u> � <u>z2</u> a <u>z</u><sup>~~n~~</sup> D z<sup><u>n</u></sup> ). Z rovnosti P.x/ D P.x/, x 2 R, plyne tvrzení. 

Poznámka 11.11. Polynom s reálnými koeficienty se nazývá _reálný polynom_ , s komplexními koeficienty _komplexní polynom_ . 

> 22William Gorge Horner 1786–1837, Angličan 

> 23Paolo Ruffini 1765–1822, Ital 

Kapitola 1. Vybrané statˇe z matematiky 

50 

■ Vˇeta 11.12 — o rozkladu reálného polynomu v reálném oboru na ireducibilní polynomy. _Buď_ P _reálný polynom stupně_ n � 1 _. Nechť_ ˛1; ˛2; : : : ; ˛m _jsou všechny jeho reálné kořeny, přičemž_ ˛1 _je_ k1 _-násobný,_ ˛2 _je_ k2 _-násobný, . . . ,_ ˛m _je_ km _-násobný. Nechť_ a1 ˙ i b1; a2 ˙ i b2; : : : ; ar ˙ i br _jsou všechny jeho imaginární kořeny, přičemž_ a1 ˙ i b1 _je_ `1 _-násobný,_ a2 ˙ i b2 _je_ `2 _-násobný, . . . ,_ ar ˙ i br _je_ `r _-násobný. Pak pro každé_ x 2 R _platí_ 



<!-- Start of picture text -->
P.x/ D an.x � ˛1/ k1 .x � ˛2/ k2 ��� .x � ˛m/ km<br>� ..x � a1/ 2 C b1 2/`1 ..x � a2/2 C b 2 2/`2 ��� ..x � ar /2 C b r 2/`r ;<br><!-- End of picture text -->

_kde_ k1 C k2 C ���C km C 2`1 C 2`2 C ���C 2`r D n _._ 

_Důkaz._ Podle vět 11.6 a 11.10 v rozkladu P vystupuje pro každou dvojici komplexně sdružených kořenů součin faktorů 

.x � .aj C i bj //<sup>`j</sup> .x � .aj � i bj //<sup>`j</sup> D .x<sup>2</sup> �.aj Ci bj /x�.aj �i bj /xC.aj Ci bj /.aj �i bj //<sup>`j</sup> D .x<sup>2</sup> �2aj xCaj<sup>2Cb</sup> j<sup>2Ci.aj bj �aj bj //`j</sup> D .x<sup>2</sup> � 2aj x C aj<sup>2C b</sup> j<sup>2/`jD ..x �aj /2 C b</sup> j<sup>2/`j :</sup> 

Poznámka 11.13. Faktory .x � aj /<sup>2</sup> C bj<sup>2se někdy nahrazují kvadratickým polynomem x2 C pj x C qj</sup> se záporným diskriminantem pj<sup>2�4qj .</sup> 

Pˇríklad 11.14. Rozložte v reálném oboru polynom P.x/ D x<sup>5</sup> C x<sup>4</sup> C x<sup>3</sup> � x<sup>2</sup> � x � 1. 

_Řešení._ Podle předchozího příkladu 



<!-- Start of picture text -->
P.x/ D .x � 1/.x 2 C x C 1/.x 2 C x C 1/ D .x � 1/�x � �� 2 1 C i p 23 ��2�x � �� 1 2 � i p 23 ��2<br>D .x � 1/ x C 1 C 3 nebo P.x/ D .x � 1/.x 2 C x C 1/ 2 :<br> � 2 �2 4 !2<br><!-- End of picture text -->

Racionální lomené funkce 

Definice 11.15 — racionální lomené funkce. Budťe P; Q nenulové polynomy. Funkce R daná předpisem R.x/ D<sup>P</sup><sup><u>.x/</u></sup> Q.x/<sup>senazývá</sup><sup>_racionálnílomenáfunkce_.Je-listupeňPmenšínežstupeňQ,funkceRse</sup> nazývá _ryze lomená_ , je-li stupeň P větší nebo roven než stupeň Q, funkce R se nazývá _neryze lomená_ . 

D.R/ D R n f˛1; ˛2; : : : ; ˛kg, kde ˛1; ˛2; : : : ; ˛k jsou všechny reálné kořeny polynomu Q. Je-li R neryze lomená funkce, lze provést dělení. Výsledkem je polynom S a zbytek, tj. polynom T , který je buď nulový, nebo stupeň T je menší než stupeň Q. Tedy R.x/ D S.x/, nebo R.x/ D S.x/ C<sup>T .x/</sup> Q.x/<sup>. Odtud</sup> plyne, že neryze lomená funkce je buď polynomem nebo ji lze vyjádřit jako součet polynomu a ryze lomené racionální funkce. 

■ Lemma 11.16. _Buď_ R D Q<sup><u>P</u></sup><sup>_ryzelomenáracionálnífunkceanechť_˛</sup><sup>_jereálný_k</sup><sup>_-násobnýkořen_</sup> _polynomu_ Q _, tj._ Q.x/ D .x � ˛/<sup>k</sup> Q1.x/ _,_ Q1.˛/ ¤ 0 _. Pak existují reálná čísla_ a1; a2; : : : ; ak _taková, že pro všechna_ x 2 D.R/ _platí_ 



<!-- Start of picture text -->
P .x/ ak ak�1 a2 a1<br>R.x/ D<br>.x � ˛/ k Q1.x/ D .x � ˛/ k C .x � ˛/ k�1 C ���C .x � ˛/ 2 C x � ˛ C Q P1 1 . .x/ x/ ;<br><!-- End of picture text -->

_kde_ P1 _je buď nulový polynom, nebo stupeň_ P1 _je menší než stupeň_ Q1 _._ 

11 Racionální funkce 

51 

P <u>.x/ a</u> P <u>.˛/</u> _Důkaz._ Pro každé a 2 R platí .x�˛/<sup>k</sup> Q1.x/<sup>D</sup> .x�˛/<sup>kCP</sup> .x<sup><u>.</u></sup> �<sup>x</sup> ˛/<sup><u>/�ka</u></sup> Q<sup><u>Q</u></sup> 1<sup><u>1</u></sup> .x/<sup><u>.x/</u>.PoložmeakWD</sup> Q1.˛/<sup>.</sup> Pak P.˛/ � akQ1.˛/ D 0. Je-li P.x/ � akQ1.x/ nulový polynom, tak tvrzení lemmatu platí platí s ak�1 D ���D a1 D 0. Nechť P.x/ � akQ1.x/ není nulový. Pak ˛ je jeho kořen a podle věty 11.4 je P.x/ � akQ1.x/ D .x � ˛/Pk.x/ a tedy 



<!-- Start of picture text -->
P .x/ ak Pk.x/<br>8x 2 D.R/:<br>.x � ˛/ k Q1.x/ D .x � ˛/ k C .x � ˛/ k�1 Q1.x/<br>Pk .x/<br>aplikujeme na racionální lomenou funkci .x�˛/ k�1 Q1.x/ a po k krocích dostaneme<br><!-- End of picture text -->

Stejný postup aplikujeme na racionální lomenou funkci požadované tvrzení. 

■ Lemma 11.17. _Buď_ R D Q<sup><u>P</u></sup><sup>_ryze lomená racionální funkce a nechť_˛D aCi b</sup><sup>_je imaginární_r</sup><sup>_-násobný_</sup> _kořen polynomu_ Q _, tj._ Q.x/ D ..x � a/<sup>2</sup> C b<sup>2</sup> /<sup>r</sup> Q1.x/ _,_ Q1.a C i b/ ¤ 0 _. Pak existují reálná čísla_ c1; d1; c2; d2; : : : ; cr ; dr _, taková, že pro všechna_ x 2 D.R/ _platí_ 



<!-- Start of picture text -->
P .x/ cr x C dr cr�1x C dr�1<br>R.x/ D<br>..x � a/ 2 C b 2 / r Q1.x/ D ..x � a/ 2 C b 2 / r C ..x � a/ 2 C b 2 / r�1<br>c2x C d2 c1x C d1<br>C ���C<br>..x � a/ 2 C b 2 / 2 C .x � a/ 2 C b 2 C Q P1 1 . .x/ x/ ;<br><!-- End of picture text -->

_kde_ P1 _je buď nulový polynom, nebo stupeň_ P1 _je menší než stupeň_ Q1 _._ 

_Důkaz._ Pro každá dvě c; d 2 R je 



<!-- Start of picture text -->
P .x/ cx C d<br>..x � a/ 2 C b 2 / r Q1.x/ D ..x � a/ 2 C b 2 / r C ..x P .x  � / � a/ .2cx C  C  b 2 d / r/Q Q 1 1 . .x/ x/ :<br><!-- End of picture text -->

Nechť QP1..˛/˛/<sup>D</sup> QP1..aaCCi bi b//<sup>D p C i q. Položme crWD</sup><sup><u>q</u></sup> b<sup>, drWD</sup><sup><u>pb�</u></sup> b<sup><u>qa</u></sup> . Pak je 



<!-- Start of picture text -->
P.˛/ � .cr ˛ C dr /Q1.˛/ D P.˛/ � Q1.˛/<br>� qb a C i q b b C p � q b a �<br>D P.˛/ � .p C i q/Q1.˛/ D P.˛/ � P .˛/<br>Q1.˛/ Q1.˛/ D 0:<br><!-- End of picture text -->

Je-li P.x/ � .cr x C dr /Q1.x/ nulový polynom, tvrzení lemmatu platí s cr�1 D dr�1 D ���D c1 D d1 D 0. Nechť P.x/ � .cr x C dr /Q1.x/ není nulový. Pak je číslo ˛ jeho kořenem. Podle věty 11.10 je také ˛N jeho kořenem a P.x/ � .cr x C dr /Q1.x/ D .x � ˛/.x � <u>˛/Pr</u> .x/ D ..x � a/<sup>2</sup> C b<sup>2</sup> /Pr .x/, 



<!-- Start of picture text -->
P .x/ cr x C dr Pr .x/<br>..x � a/ 2 C b 2 / r Q1.x/ D ..x � a/ 2 C b 2 / r C ..x � a/ 2 C b 2 / r�1 Q1.x/ :<br><!-- End of picture text -->

Stejný postup aplikujeme na racionální lomenou funkci 



<!-- Start of picture text -->
Pr .x/<br>..x � a/ 2 C b 2 / r�1 Q1.x/<br><!-- End of picture text -->

a po r krocích obdržíme požadavek tvrzení. 

Zlomky tvaru 



<!-- Start of picture text -->
aj cj x C dj<br>.j D 1; 2; : : : ; k/ a .j D 1; 2; : : : ; r/<br>.x � ˛/ j ..x � a/ 2 C b 2 / j<br><!-- End of picture text -->

nazýváme _parciální zlomky_ . Důsledkem předchozích dvou tvrzení je 

Kapitola 1. Vybrané statˇe z matematiky 

52 

■ Vˇeta 11.18 — o rozkladu ryze lomené racionální funkce na parciální zlomky. _Každou ryze lomenou racionální funkci lze rozložit na součet parciálních zlomků. Každému reálnému_ k _-násobnému kořenu_ ˛ _jmenovatele odpovídá skupina právě_ k _zlomků_ 



<!-- Start of picture text -->
ak ak�1 a2 a1<br>: : : ;<br>.x � ˛/ k ; .x � ˛/ k�1 ; .x � ˛/ 2 ; x � ˛<br><!-- End of picture text -->

_a každému imaginárnímu_ r _-násobnému kořenu_ a C i b _jmenovatele odpovídá skupina právě_ r _zlomků_ 



<!-- Start of picture text -->
cr x C dr cr�1x C dr�1 c2x C d2 c1x C d1<br>..x � a/ 2 C b 2 / r ; ..x � a/ 2 C b 2 / r�1 ; : : : ; ..x � a/ 2 C b 2 / 2 ; .x � a/ 2 C b 2 :<br><!-- End of picture text -->

Poznámka 11.19. Koeficienty v rozkladu racionální lomené funkce lze vypočítat postupem naznačeným v důkazech lemmatů 11.16 a 11.17, v praxi se však používá _metoda neurčitých koeficientů_ , viz následující příklad. 

Pˇríklad 11.20. Rozložte na parciální zlomky funkci 



<!-- Start of picture text -->
3x 2 � 5x C 8<br>R.x/ D<br>x 3 � 2x 2 C x � 2 :<br><!-- End of picture text -->

_Řešení._ Rozklad jmenovatele v reálném oboru (na ireducibilní polynomy) je x<sup>3</sup> � 2x<sup>2</sup> C x � 2 D x<sup>2</sup> .x � 2/ C x � 2 D .x<sup>2</sup> C 1/.x � 2/ a tedy 



<!-- Start of picture text -->
3x 2 � 5x C 8 A<br>x 3 � 2x 2 C x � 2 D x � 2 C Bx x 2 C C  C  1 . � .x 2 C 1/.x � 2/<br>3x 2 � 5x C 8 D A.x 2 C 1/ C .Bx C C/.x � 2/ D Ax 2 C A C Bx 2 � 2Bx C Cx � 2C<br>D .A C B/x 2 C .�2B C C/x C A � 2C:<br><!-- End of picture text -->

Protože dva polynomy se sobě rovnají pouze v případě, kdy se rovnají koeficienty u odpovídajících si mocnin, máme 



<!-- Start of picture text -->
x 2 W 3 D A C B;<br>x 1 W �5 D �2B C C;<br>x 0 W 8 D A � 2C;<br><!-- End of picture text -->

což je soustava lineárních rovnic. Vyřešením máme A D 1, B D 1, C D �3, a tedy 



<!-- Start of picture text -->
x 3 3x� 2 2x� 2 5xC C x � 8 2 D x �1 2 C x x2 � C 3  1 :<br><!-- End of picture text -->

#### Pˇríklady k procviˇcení 

11.1. Rozložte polynom P.x/ D x<sup>6</sup> C x<sup>5</sup> C x<sup>2</sup> � x<sup>4</sup> � x � 1 na a) kořenové činitele, b) ireducibilní polynomy. 

11.2. Určete všechny kořeny polynomu P.x/ D x<sup>5</sup> C 2x<sup>3</sup> C x � 2x<sup>4</sup> � 4x<sup>2</sup> � 2. 

11.3. Rozložte polynom P.x/ D x<sup>5</sup> � x<sup>4</sup> � 4 C 4x na a) ireducibilní polynomy, b) kořenové činitele. 

11.4. Rozložte na součet polynomu a parciálních zlomků neryze lomenou racionální funkci 



<!-- Start of picture text -->
R.x/ D 2x5 C 5x4 C x2 C 4 :<br>x 4 C 2x 3<br><!-- End of picture text -->

11 Racionální funkce 

53 

11.5. Rozložte racionální lomenou funkci 



<!-- Start of picture text -->
R.x/ D x5 C 3x4 C 4x3 C 7x2 C 2x C 1<br>x 6 � 2x 3 C 1<br><!-- End of picture text -->

na parciální zlomky. 

_Výsledky._ 11.1. a) .x � 1/.x C 1/<sup>3</sup> .x �<sup>1</sup> =2 � i ~~p~~ 3=2/.x � 1=2 C i ~~p~~ 3=2/, b) .x � 1/.x C 1/<sup>3</sup> .x<sup>2</sup> � x C 1/. 11.2. x1 D 2, x2;3 D i, x4;5 D �i. 11.3. a) .x � 1/.x<sup>2</sup> � 2x C 2/.x<sup>2</sup> C 2x C 2/ D .x � 1/..x � 1/<sup>2</sup> C 1/ ..x C1/<sup>2</sup> C1/, b) .x �1/.x �1�i/.x �1Ci/.x C1�i/.x C1Ci/. 11.4. 2x C1C<sup>1</sup> =x �<sup>1</sup> =x<sup>2</sup> C<sup>2</sup> =x<sup>3</sup> �<sup>3</sup> =xC2. 11.5.<sup>1</sup> =x�1 C<sup>2</sup> =.x�1/<sup>2</sup> �<sup>x</sup> =.x<sup>2</sup> CxC1/<sup>2</sup> . 

## Kapitola 2 

# Diferenciální poˇcet 

### 12 Limita funkce 

Definice 12.1 — limity funkce. Řekneme, že funkce f má v bodě x0 2 R<sup>�</sup> _limitu_ a 2 R<sup>�</sup> a píšeme limx!x0 f .x/ D a, jestliže ke každému okolí O.a/ existuje ryzí okolí O<sup>�</sup> .x0/ takové, že pro každé x 2 O<sup>�</sup> .x0/ je f .x/ 2 O.a/. 

Poznámka 12.2. a) Definice zahrnuje 4 případy: je-li x0; a 2 R, hovoříme o _vlastní limitě ve vlastním bodě_ , je-li x0 D ˙1, a 2 R, hovoříme o _vlastní limitě v nevlastním bodě_ , je-li x 2 R, a D ˙1, hovoříme o _nevlastní limitě ve vlastním bodě_ a je-li x0 D ˙1 a a D ˙1, hovoříme o _nevlastní limitě v nevlastním bodě_ . 

b) V definici se hovoří o ryzím okolí bodu x0, nevyskytuje se tedy žádný požadavek na f .x0/. Existence a hodnota limx!x0 f .x/ nezávisí na tom, zda x0 2 D.f /, a pokud ano, tak nezávisí na hodnotě f .x0/. Existuje-li však limx!x0 f .x/, musí být funkce f definována v nějakém ryzím okolí bodu x0. 



<!-- Start of picture text -->
x 2 pro x ¤ 0;<br>Pˇríklad 12.3. Ukažte, že limx!0 f .x/ D 0, kde f .x/ D<br>(1 pro x D 0:<br><!-- End of picture text -->

_Řešení._ Nechť " > 0 je libovolné. Potom 8x 2 Oı<sup>�.0/, kde ıD</sup><sup>~~p~~</sup> ", platí jx<sup>2</sup> � 0j D x<sup>2</sup> < ı<sup>2</sup> D ". 

> ■ Vˇeta 12.4 — Heineho<sup>1</sup> podmínka. _Funkce_ f _má v bodě_ x0 2 R<sup>�</sup> _limitu_ a 2 R<sup>�</sup> , _pro každou posloupnost_ fxng<sup>1</sup> nD1<sup>�D.f /</sup><sup>_takovou,že_limn!1 xnDx0</sup><sup>_,přičemž_xn¤x08n2N</sup><sup>_,platí_</sup> limn!1 f .xn/ D a _._ 

_Důkaz._ „)“ Nechť limx!x0 f .x/ D a 2 R<sup>�</sup> a fxng je posloupnost splňující předpoklady. Buď O.a/ libovolné. Pak existuje ryzí okolí O<sup>�</sup> .x0/ takové, že pro x 2 O<sup>�</sup> .x0/ je f .x/ 2 O.a/. Poněvadž xn ! x0, xn ¤ x0, existuje n0 2 N takové, že pro n � n0 platí xn 2 O<sup>�</sup> .x0/ a tedy f .xn/ 2 O.a/, což znamená, že limn!1 f .xn/ D a. 

„(“ Předpokládejme, že pro každou fxng, takovou, že xn ! x0, xn ¤ x0, platí limn!1 f .xn/ D a 2 R<sup>�</sup> . Ukážeme, že limx!x0 f .x/ D a. Připusťme, že existuje O.a/ takové, že v každém ryzím okolí O<sup>�</sup> .x0/ existuje x takové, že f .x/ … O.a/. Je-li x0 2 R (resp. x0 D 1, resp. x0 D �1), položíme Un.x0/ D .x0 � n<sup><u>1</u>; x0 C</sup> n<sup><u>1</u>/ n fx0g (resp. Un.x0/ D .n; 1/, resp. Un.x0/ D .�1; �n/). Pro libovolné</sup> n 2 N existuje yn 2 Un.x0/ takové, že f .yn/ … O.a/. Z konstrukce Un.x0/ plyne, že yn ! x0, yn ¤ x0 a tedy limn!1 f .yn/ D a. To ale není možné, protože f .yn/ … O.a/. 

Poznámka 12.5. a) Heineho podmínka umožňuje převést vyšetřování vlastností limity funkce na vlastnosti limity posloupnosti. 

1Heinrich Eduard Heine 1821–1881, Němec 

Kapitola 2. Diferenciální poˇcet 

56 

b) Zejména pak platí analogie vlastností z vět 7.4 (jednoznačnost limity), 7.6 (funkce mající limitu je ohraničená na ryzím okolí bodu x0), 7.9 (limita součtu, součinu atd.), 7.13 (pro funkce se nazývá věta o třech limitách). 

- c) Dále platí: 

- Nechť x0 2 R<sup>�</sup> , limx!x0 f .x/ D 0 a nechť existuje ryzí okolí bodu x0, v němž je f .x/ ¤ 0 (resp. f .x/ > 0, resp. f .x/ < 0). Pak limx!x0 jf .x/1 j<sup>D1(resp.limx!x0</sup> f .x/1<sup>D1,resp.</sup> 

- limx!x0 f .x/1<sup>D �1).</sup> 

- Nechť x0 2 R<sup>�</sup> a limx!x0 jf .x/j D 1. Pak limx!x0 f .x/1<sup>D 0.</sup> 

- Je-li x0 2 R<sup>�</sup> , limx!x0 f .x/ D 1 a g.x/ je zdola ohraničená na nějakém O<sup>�</sup> .x0/, pak limx!x0 Œf .x/ C g.x/� D 1. Podobně pro limitu �1 a shora ohraničenou funkci. 

- Je-li x0 2 R<sup>�</sup> , limx!x0 f .x/ D 1 a g.x/ � d > 0 (resp. g.x/ � h < 0) na nějakém O<sup>�</sup> .x0/, pak limx!x0 f .x/ � g.x/ D 1 (resp. limx!x0 f .x/ � g.x/ D �1). 

##### Základní limity 

1. Nechť f .x/ D c 2 R pro každé x 2 R. Pak pro každé x0 2 R<sup>�</sup> je limx!x0 f .x/ D c. 

2. Buď P polynom. Pak pro libovolné x0 2 R je limx!x0 P.x/ D P.x0/. 

3. Buď R racionální lomená funkce a x0 2 D.R/. Pak limx!x0 R.x/ D R.x0/. 

4. Buď a > 0, f .x/ D a<sup>x</sup> . Pak pro libovolné x0 2 R je limx!x0 a<sup>x</sup> D a<sup>x0</sup> . 

5. Buď a 2 R, f .x/ D x<sup>a</sup> . Pak pro libovolné x0 > 0 je limx!x0 x<sup>a</sup> D x0<sup>a.</sup> 

6. Pro libovolné x0 2 R je limx!x0 sin x D sin x0, limx!x0 cos x D cos x0. 

7. limx!0<sup><u>sin</u></sup> x<sup><u>x</u></sup> D 1, limx!1�1 C x<sup><u>1</u></sup> �x D e, limx!0 <u>1�xcos</u><sup>2</sup> <u>x</u> D<sup><u>1</u></sup> 2<sup>,</sup> 

■ Vˇeta 12.6 — o limitˇe složené funkce. _Nechť_ x0 2 R<sup>�</sup> _,_ limx!x0 '.x/ D ˛ 2 R<sup>�</sup> _,_ limt!˛ f .t/ D a 2 R<sup>�</sup> _a nechť je splněna alespoň jedna z následujících podmínek:_ 

- (i) _existuje ryzí okolí_ O<sup>�</sup> .x0/ _, v němž platí_ '.x/ ¤ ˛ _,_ 

- (ii) f .˛/ D a _(podmínka spojitosti funkce_ f _v bodě_ ˛ _, viz následující kapitola)._ 

_Pak_ limx!x0 f .'.x// D a _(tj._ limx!x0 f .'.x// D limt!limx!x0 '.x/ f .t/ D a _)._ 

_Důkaz._ Nechť okolí O.a/ je libovolné. K němu existuje ryzí okolí O<sup>�</sup> .˛/ takové, že pro t 2 O<sup>�</sup> .˛/ je f .t/ 2 O.a/. K O.˛/ existuje ryzí okolí O<sup>e�</sup> .x0/ takové, že pro 8x 2 O<sup>e�</sup> .x0/ je '.x/ 2 O.˛/. 

Nechť je splněn předpoklad (i). Položme O<sup>b�</sup> .x0/ D O<sup>�</sup> .x0/ \ O<sup>e�</sup> .x0/. Pak pro 8x 2 O<sup>b�</sup> .x0/ je '.x/ 2 O.˛/ a '.x/ ¤ ˛, tj. '.x/ 2 O<sup>b�</sup> .˛/. Tedy f .'.x// 2 O.a/, což dává limx!x0 f .'.x// D a. 

Nechť je splněn předpoklad (ii). Limita limt !˛ f .t/ D a znamená, že ke každému O.a/ existuje O<sup>�</sup> .˛/ takové, že 8t 2 O<sup>�</sup> .˛/ platí f .t/ 2 O.a/, a protože f .˛/ D a, máme navíc, že 8t 2 O.˛/ je f .t/ 2 O.a/. Protože dále limx!x0 '.x/ D ˛, tak k našemu O.˛/ existuje O<sup>�</sup> .x0/ takové, že 8x 2 O<sup>�</sup> .x0/ je '.x/ 2 O.˛/. Celkově tedy pro každé x 2 O<sup>�</sup> .x0/ máme f .'.x// 2 O.a/, což znamená, že xlim!x0<sup>f .'.x// D a.</sup> 

Poznámka 12.7. a) Pokud není splněn ani jeden z předpokladů (i) nebo (ii), tak tvrzení obecně neplatí. Např. pro 



<!-- Start of picture text -->
0 pro t ¤ 0;<br>'.x/ D 0; f .t/ D<br>(1 pro t D 0<br><!-- End of picture text -->

platí f .'.x// D 1 pro každé x 2 R, a tedy pro libovolné x0 2 R<sup>�</sup> je limx!x0 f .'.x// D 1, avšak limx!x0 '.x/ D 0, limt!0 f .t/ D 0. 

b) Je-li splněn předpoklad (ii), pak lze psát limx!x0 f .'.x// D f .limx!x0 '.x//. c) Je-li ˛ D ˙1, pak je předpoklad (i) splněn automaticky. 

Pˇríklad 12.8. Určete limitu limx!0<sup>~~<u>p</u>~~</sup> 3 1Cxx�1 . 

_Řešení._ Provedeme-li substituci y D<sup>~~p~~</sup> 3 1 C x, pak úlohu převedeme na výpočet limity složené funkce 

12 Limita funkce 

57 



<!-- Start of picture text -->
f .'.x//, kde '.x/ D p 3 1 C x a f .y/ D yy 3 ��11 (protože ze substituce je x D y3 � 1). Platí<br><!-- End of picture text -->



<!-- Start of picture text -->
xlim!0 '.x/ D p 3 1 C 0 D 1;<br><!-- End of picture text -->

přičemž na každém ryzím okolí bodu x D 0 máme<sup>~~p~~</sup> 3 1 C x ¤ 1, je tedy splněna podmínka (i) věty 12.6. Dále 



<!-- Start of picture text -->
y � 1 1 p 3 1 C x � 1<br>lim a tedy lim D 1<br>y!1 f .y/ D y lim !1 .y � 1/.y 2 C y C 1/ D y lim !1 y 2 C y C 1 D 3 1 x!0 x 3 :<br><!-- End of picture text -->

Poznamenejme, že limitu lze vyřešit také bez použití substituce, a to rozšířením faktorem 



<!-- Start of picture text -->
p 3 .1 C x/ 2 C p 3 1 C x C 1<br>p 3 .1 C x/ 2 C p 3 1 C x C 1 :<br><!-- End of picture text -->

Definice 12.9 — jednostranných limit. Je-li x0 2 R a nahradíme-li v definici limity ryzí okolí O<sup>�</sup> .x0/ levým ryzím okolím O<sup>��</sup> .x0/ (resp. pravým ryzím okolím O<sup>�C</sup> .x0/), dostaneme definici _limity zleva_ (resp. _limity zprava_ ). Souhrnně se tyto limity nazývají _jednostranné_ limity. Značíme limx!x0� f .x/ a limx!x0C f .x/. 

■ Vˇeta 12.10. _Funkce_ f _má v bodě_ x0 2 R _limitu_ a 2 R<sup>�</sup> , _má v tomto bodě limitu zprava i zleva a platí_ limx!x0� f .x/ D limx!x0C f .x/ D a _._ 

_Důkaz._ Plyne přímo z definic limity a jednostranných limit a z faktu O<sup>�</sup> .x0/ D .x0 � ı; x0/ [ .x0; x0 C ı/. 

Poznámka 12.11. a) Pro jednostranné limity platí analogie Heineho podmínky (posloupnost akorát bereme zleva, resp. zprava od bodu x0). V důsledku toho platí základní vlastnosti limity i pro jednostranné limity. 

b) Pomocí jednostranných limit lze dokázat další „základní“ limitu limx!0<sup><u>ex</u></sup> x<sup>�1</sup> D 1. 

Poznámka 12.12. Analogií hromadného bodu posloupnosti je pojem _limitního bodu (částečné limity)_ funkce. Pomocí množiny limitních bodů lze potom také zavést lim sup a lim inf funkce v bodě x0 (např. limx!x0 �.x/ neexistuje v žádném x0, ale lim supx!x0 �.x/ D 1, lim infx!x0 �.x/ D 0 v libovolném x0 2 R<sup>�</sup> ). 

#### Pˇríklady k procviˇcení 



<!-- Start of picture text -->
12.1. Určete limitu<br>xlim!1 23x=.xC2/:<br><!-- End of picture text -->

12.2. Určete limitu 

12.3. Určete limitu 



<!-- Start of picture text -->
xlim!0 � sinx 2x �1Cx :<br>e x � e �x<br>xlim!0 sin 2x :<br><!-- End of picture text -->

12.4. Vyšetřete limitu 

12.5. Určete limitu 



<!-- Start of picture text -->
lim :<br>x!5 arctg � 5x � � x3 �<br>x C 20<br>lim<br>x!1 e x�5 �1 :<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet 

58 

12.6. Určete limitu 



<!-- Start of picture text -->
xlim!1�ln x � x 2� :<br><!-- End of picture text -->

_Výsledky._ 12.1. 8. 12.2. 2. 12.3. 1. 12.4. neexistuje. 12.5. 0. 12.6. �1. 

### 13 Spojitost funkce 

Definice 13.1 — spojitosti funkce v bodˇe. Řekneme, že funkce f je _spojitá v bodě_ x0 2 R, jestliže limx!x0 f .x/ D f .x0/. Řekneme, že funkce f je _spojitá v bodě_ x0 2 R _zprava_ (resp. _zleva_ ), jestliže limx!x0C f .x/ D f .x0/ (resp. limx!x0� f .x/ D f .x0/). 

Poznámka 13.2. a) Z definice ihned plyne: f je spojitá v x0 , 8" > 0 9ı > 0 takové, že 8x 2 .x0 � ı; x0 C ı/ platí jf .x/ � f .x0/j < ". 

- b) Je-li f spojitá v bodě, pak je na nějakém okolí tohoto bodu ohraničená. 

- c) Spojitost je definována pouze v bodech z R. Nelze definovat spojitost v nevlastním bodě. 

- d) Spojitost funkce v bodě je lokální vlastností této funkce. 

Není-li f spojitá v bodě x0 2 R a je přitom definována na nějakém okolí (případně ryzím okolí) bodu 

x0, mohou nastat tyto možnosti: 

1. xlim!x0<sup>f .x/ neexistuje a</sup> 1a. x!limx0C<sup>f .x/,</sup> x!limx0�<sup>f .x/ existují a jsou reálné různé –</sup><sup>_bod nespojitosti 1. druhu_(např. f .x/ D</sup> bxc, x0 D 1); 

- 1b. Alespoň jedna z jednostranných limit neexistuje – _bod nespojitosti 2. druhu_ (např. f .x/ D sin x<sup><u>1</u>,</sup> x0 D 0, nebo Dirichletova funkce �, kde x0 je libovolné); 

- 1c. x!limx0C<sup>f .x/,</sup> x!limx0�<sup>f .x/ existují, jsou různé a alespoň jedna z nich je nevlastní (např. f .x/ D</sup> tg x, x0 D<sup><u>�</u></sup> 2<sup>);</sup> 

- 2. xlim!x0<sup>f .x/ D a 2 R�, a ¤ f .x0/ a</sup> 



<!-- Start of picture text -->
2a. xlim!x0 f .x/ je nevlastní (např. f .x/ D x1 2 , x0 D 0);<br>2b. xlim!x0 f .x/ D a 2 R a f .x0/ ¤ a nebo x0 … D.f / –  bod odstranitelné nespojitosti . Nespojitost<br>f .x/; x 2 D.f / n fx0g;<br>lze odstranit změnou f .x0/ nebo dodefinováním f .x0/: f .x/ Q  D<br>(limx!x0 f .x/; x D x0;<br>x 2 ; x ¤ 0 x � 1<br>(např. f .x/ D (1; x D 0 , x0 D 0, g.x/ D x 2 � 1 , x0 D 1. Nespojitost odstraníme<br>definováním f .0/ Q  D 0, g.1/Q  D 2 1 ).<br><!-- End of picture text -->

■ Vˇeta 13.3. _Funkce_ f _je spojitá v bodě_ x0 2 R _právě tehdy, když je v tomto bodě spojitá zprava i zleva._ 

_Důkaz._ Plyne ihned z věty 12.10. 

■ Vˇeta 13.4. _Funkce_ f _je spojitá v bodě_ x0 2 R , _pro každou posloupnost_ fxng _takovou, že_ limn!1 xn D x0 _, platí_ limn!1 f .xn/ D f .x0/ _. Funkce_ f _je spojitá v bodě_ x 2 R _zprava (resp. zleva)_ , _pro každou posloupnost_ fxng _takovou, že_ xn � x0 _(resp._ xn � x0 _)_ 8n 2 N _a_ limn!1 xn D x0 _, platí_ limn!1 f .xn/ D f .x0/ _._ 

_Důkaz._ Plyne ihned z Heineho podmínky (věta 12.4) a poznámky 12.11a). 

■ Vˇeta 13.5. _Jsou-li_ f _a_ g _spojité v bodě_ x0 2 R _, pak jsou v bodě_ x0 _spojité také_ jf j _,_ f C g _,_ f � g _,_ fg _. Je-li navíc_ g.x0/ ¤ 0 _, je i_<sup><u>f</u></sup> g<sup>_spojitá v bodě_x0</sup><sup>_._</sup> 

_Důkaz._ Plyne z vlastností limity (limita součtu je součet limit atd.). 

13 Spojitost funkce 

59 

■ Vˇeta 13.6. _Nechť_ ' _je spojitá v bodě_ x0 _a_ f _je spojitá v bodě_ '.x0/ _. Pak je také_ f .'.x// _spojitá v bodě_ x0 _._ 

_Důkaz._ Buď " > 0 libovolné. K němu existuje ı1 > 0 takové, že pro y 2 .'.x0/ � ı1; '.x0/ C ı1/ platí jf .y/ � f .'.x0//j < ". K ı1 > 0 existuje ı > 0 takové, že pro x 2 .x0 � ı; x0 C ı/ platí j'.x/ � '.x0/j < ı1. Tedy pro x 2 .x0 � ı; x0 C ı/ je jf .'.x// � f .'.x0//j < ", což znamená limx!x0 f .'.x// D f .'.x0//. 

Definice 13.7 — spojitosti funkce na intervalu. Řekneme, že funkce f je spojitá na intervalu I � D.f /, jestliže platí: 

(i) f je spojitá v každém vnitřním bodě intervalu I . 

(ii) Patří-li levý (resp. pravý) krajní bod intervalu I do tohoto intervalu, pak je v něm funkce f spojitá zprava (resp. zleva). 

Poznámka 13.8. a) Tedy f je spojitá na otevřeném intervalu .a; b/ , je spojitá v každém bodě tohoto intervalu a f je spojitá na uzavřeném intervalu ha; bi právě tehdy, když je spojitá v každém bodě .a; b/, v bodě a je spojitá zprava a v bodě b je spojitá zleva. Spojitost na intervalu je globální vlastnost. 

b) Funkci, která je definovaná na ha; bi, nazveme _po částech spojitou_ , jestliže je spojitá v každém bodě tohoto intervalu s výjimkou konečného počtu bodů, v nichž má nespojitost prvního druhu. 

■ Vˇeta 13.9. _Nechť_ f _je spojitá a ryze monotónní na intervalu_ I _a zobrazuje tento interval na interval_ J _. Pak_ f<sup>�1</sup> _je spojitá na intervalu_ J _._ 

_Důkaz._ Nechť f je rostoucí na I , y0 2 J a y0 není levý koncový bod J . Ukažme, že f<sup>�1</sup> je spojitá zleva v bodě y0 D f .x0/ (zřejmě je x0 prvkem intervalu I a není levý koncový bod tohoto intervalu). Buď " > 0 libovolné takové, že x0 � " 2 I . Pak f .x0 � "/ < f .x0/. Označme ı D f .x0/ � f .x0 � "/ > 0. Pak y0 � ı D f .x0 � "/ a odtud plyne, že y0 � ı 2 J . Nechť dále y 2 .y0 � ı; y0i je libovolný. Protože podle věty 8.28 je f<sup>�1</sup> rostoucí, platí f<sup>�1</sup> .y0 � ı/ < f<sup>�1</sup> .y/, a tedy f<sup>�1</sup> .y0 � ı/ D f<sup>�1</sup> .f .x0/ � f .x0/ C f .x0 � "// D x0 � ". To znamená, že x0 � " D f<sup>�1</sup> .y0/ � " < f<sup>�1</sup> .y/, neboli f<sup>�1</sup> .y0/ � f<sup>�1</sup> .y/ < ". Ukázali jsme tedy, že pro každé y 2 .y0 � ı; y0i D Oı<sup>�.y0/platí</sup> f<sup>�1</sup> .y/ 2 �f<sup>�1</sup> .y0/ � "; f<sup>�1</sup> .y0/˛ D O"<sup>�.f�1.y0//,tj.f�1jespojitázlevavboděy0.Ostatní</sup> možnosti (spojitost zprava v bodě y0 a jednostrannou spojitost v krajních bodech, pokud patří do intervalu) bychom provedli analogicky. 

Poznámka 13.10. Základní elementární funkce, polynomy a racionální lomené funkce jsou spojité na svých definičních oborech. 

■ Vˇeta 13.11 — 1. Weierstrassova. _Funkce spojitá na uzavřeném intervalu je na tomto intervalu ohraničená._ 

_Důkaz._ Sporem. Připusťme, že funkce f spojitá na ha; bi není ohraničená shora. Pak ke každému n 2 N existuje xn 2 ha; bi takové, že f .xn/ > n. Takto definovaná posloupnost fxng je ohraničená .a � xn � b/ a tedy podle věty 7.27 existuje vybraná posloupnost fxnk g<sup>1</sup> kD1<sup>taková, že limk!1 xnkD x0. Protože</sup> a � xnk � b, tak také a � x0 � b, tj. x0 2 ha; bi (vlastnost an � bn ) lim an � lim bn byla uvedena v poznámce a) pod větou 7.6). Poněvadž f je spojitá (případně jednostranně spojitá), podle věty 13.4 je limk!1 f .xnk / D f .x0/ 2 R. Současně ale f .xnk / > nk, limk!1 nk D 1 což implikuje limk!1 f .xnk / D 1. To je spor. Analogicky by se vyloučila možnost, že by funkce f spojitá na uzavřeném intervalu nebyla ohraničená zdola. 

■ Vˇeta 13.12 — 2. Weierstrassova. _Funkce spojitá na uzavřeném intervalu zde nabývá minima a maxima._ 

_Důkaz._ Nechť funkce f je spojitá na ha; bi. Podle 1. Weierstrassovy věty je na tomto intervalu ohraničená a tedy existuje m D supff .x/ W x 2 ha; big. Ukažme, že existuje x1 2 ha; bi takové, že f .x1/ D m. Připusťme, že f .x/ < m pro každé x 2 ha; bi. Pak m � f .x/ > 0 pro každé x 2 ha; bi a podle věty 13.5 

Kapitola 2. Diferenciální poˇcet 

60 

je funkce m�f .x/1<sup>spojitá na ha; bi. Podle 1. Weierstrassovy věty existuje c2R, že</sup> m�f .x/1<sup><cpro</sup> každé x 2 ha; bi. Zřejmě je c > 0. Tedy f .x/ < m �<sup><u>1</u></sup> c<sup>pro každé 2ha; bi. Protože m je supremum,</sup> existuje x0 2 ha; bi tak, že f .x0/ � m �<sup><u>1</u></sup> c<sup>, tj. c�</sup> m�f .x1 0/<sup>, což je spor. Analogicky by se ukázalo, že</sup> existuje x2 2 ha; bi takové, že x2 D infff .x/ W x 2 ha; big. 

■ Vˇeta 13.13 — 1. Bolzanova. _Nechť funkce_ f _je spojitá na_ ha; bi _a nechť platí_ f .a/f .b/ < 0 _. Pak existuje_ c 2 .a; b/ _takové, že_ f .c/ D 0 _._ 

_Důkaz._ Položme d D<sup><u>b�</u></sup> 2<sup><u>a</u>.Pakd2.a; b/.Pokudf .d/D0,jecDd.Nechťf .d/¤0.Jestliže</sup> f .a/f .d/ < 0, položme a1 D a, b1 D d ; jestliže f .a/f .d/ > 0, položme a1 D d , b1 D b. Nyní platí b1 � a1 D<sup><u>b�</u></sup> 2<sup><u>a</u>, f .a/f .b1/ < 0, f .a1/f .b/ < 0, a1�a, b1�b.</sup> 

Dále položme d1 D<sup>b1�</sup> 2<sup>a1</sup> . Pak d1 2 .a1; b1/ � .a; b/. Pokud f .d1/ D 0, je c D d1. Nechť f .d1/ ¤ 0. Jestliže f .a1/f .d1/ < 0, položme a2 D a1, b2 D d1; jestliže f .a1/f .d1/ > 0, položme a2 D d1, b2 D b1. Nyní platí b2 � a2 D<sup><u>b</u></sup> 2<sup>�2a, f .a/f .b2/ < 0, f .a2/f .b/ < 0, a2�a1, b2�b1.</sup> 

Analogicky postupujeme dále. Buď po konečném počtu kroků nalezneme dk takové, že f .dk/ D 0, nebo dostaneme dvě posloupnosti fang, fbng takové, že bn � an D<sup><u>b</u></sup> 2<sup>�na, f .a/f .bn/ < 0, f .an/f .b/ < 0.</sup> V prvním případě je c D dk. Nechť nastane druhý případ. Posloupnost fang je neklesající, ohraničená shora číslem b a tedy podle věty o monotónních posloupnostech (viz věta 7.15) existuje c1 D lim an � b. Podobně, posloupnost fbng je nerostoucí, zdola hraničená číslem a a tedy existuje číslo c2 D lim bn � a. Platí c1 � c2 D lim an � lim bn D lim.an � bn/ D lim<sup><u>a</u></sup> 2<sup>�nb</sup> D 0, tedy c1 D c2 D c 2 ha; bi. Kdyby f .a/f .c/ < 0 a f .c/f .b/ < 0, pak by f .a/f .c/f .c/f .b/ > 0, tj. f .a/f .b/ > 0, což by byl spor. Pokud f .a/f .c/ � 0, pak 0 � f .a/ lim f .bn/ D lim f .a/f .bn/ � 0, tedy f .a/f .c/ D 0, což je možné, pouze když f .c/ D 0. Pokud f .c/f .b/ � 0, pak 0 � .lim f .an//f .b/ D lim f .an/f .b/ � 0, tedy f .c/f .b/ D 0, což je možné, pouze když f .c/ D 0. Poznámka 13.14. Princip důkazu spočívá v metodě, která se v numerické matematice nazývá _metoda půlení intervalu (bisekce)_ . 

■ Vˇeta 13.15 — 2. Bolzanova. _Nechť funkce_ f _je spojitá na_ ha; bi _. Pak zde nabývá všech hodnot mezi svou největší a nejmenší hodnotou._ 

_Důkaz._ Položme M D maxff .x/ W x 2 ha; big, m D minff .x/ W x 2 ha; big, a nechť p 2 R je takové, že m < p < M . Podle 2. Weierstrassovy věty existují x1 2 ha; bi, x2 2 ha; bi takové, že f .x1/ D M , f .x2/ D m. Potom f .x1/�p > 0, f .x2/�p < 0, tedy .f .x1/�p/.f .x2/�p/ < 0. Podle 1. Bolzanovy věty existuje v uzavřeném intervalu s krajními body x1 a x2 číslo c takové, že 0 D .f � p/.c/ D f .c/ � p, tedy f .c/ D p. 

■ D˚usledek 13.16. _Spojitým obrazem uzavřeného intervalu je buď jednoprvková množina nebo uzavřený interval._ 

Definice 13.17 — stejnomˇerné spojitosti funkce. Řekneme, že funkce f je stejnoměrně spojitá na intervalu I � D.f /, jestliže ke každému " > 0 existuje ı > 0 takové, že pro každá dvě x1; x2 2 I splňující jx1 � x2j < ı platí jf .x1/ � f .x2/j < ". 

Poznámka 13.18. a) Stejnoměrně spojitá funkce na I je spojitá na I . Naopak tvrzení neplatí, např. funkce f .x/ D x<sup><u>1</u>je na .0; 1/ spojitá, ale není zde stejnoměrně spojitá. Skutečně, negací podmínky v definici</sup> dostaneme, že funkce nebude stejnoměrně spojitá, pokud existuje " > 0 tak, že pro každé ı > 0 existují x1; x1 splňující jx1 � x2j < ı a přitom jf .x1/ � f .x2/j � ". Nechť ı > 0 je libovolné a vezměme m takové přirozené číslo, že 1=m < ı. Položme 



<!-- Start of picture text -->
1<br>x1 D a x2 D 1<br>2m m :<br><!-- End of picture text -->

13 Spojitost funkce 

61 

Potom 



<!-- Start of picture text -->
1 � 1<br>ˇˇˇˇ x1 x2 ˇˇˇˇ D 2m � m D m � 1:<br><!-- End of picture text -->

Pro " D 1 tedy neexistuje žádné ı > 0, které by vždy splňovalo pro jx1 � x2j < ı vztah ˇˇ x11<sup>�</sup> x<sup><u>1</u></sup> 2 ˇˇ < ", a tedy funkce f není na .0; 1/ stejnoměrně spojitá. 

b) Funkci stejnoměrně spojitou na .a; b/ lze spojitě prodloužit na ha; bi (pomocí jednostranných limit v krajních bodech), viz následující příklad. 

c) Stejnoměrně spojitá funkce na libovolném intervalu konečné délky je na tomto intervalu ohraničená. 

Pˇríklad 13.19. Dokažte vlastnost z poznámky 13.18b), tj. že funkci stejnoměrně spojitou na .a; b/ lze spojitě prodloužit na ha; bi pomocí jednostranných limit v krajních bodech. Je tedy potřeba ukázat, že tyto jednostranné limity existují a jsou konečné. 

_Řešení._ Předně si uvědomme, že když v intervalu .a; b/ vezmeme cauchyovskou posloupnost fxng, pak posloupnost ff .xn/g funkčních hodnot je také cauychovská. Skutečně, stejnoměrná spojitost funkce f znamená, že ke každému " > 0 existuje ı > 0 takové, že jf .x/ � f .�/j < ", kdykoliv jx � �j < ı. Protože fxng je cauchyovská, existuje n0 2 N takové, že 8m; n 2 N, m; n � n0, je jxm � xnj < ı, což implikuje jf .xm/ � f .xn/j < ", a tedy ff .xn/g je cauchyovská. 

Nechť dále fxng � .a; b/ je nějaká posloupnost konvergující zprava k bodu a (taková posloupnost určitě existuje, viz Lemma 10.1a)). Podle Cauchyova–Bolzanova kritéria je tato posloupnost cauchyovská. Podle předchozího kroku je cauchyovská také posloupnost ff .xn/g, a tedy (opět podle podle Cauchyova– Bolzanova kritéria) je tato posloupnost konvergentní (tj. existuje konečná limita lim f .xn/ D `1). Vezmeme-li v intervalu .a; b/ jinou posloupnost, označme ji např. f�ng, konvergující zprava k bodu a, pak posloupnost ff .�n/g bude opět cauchyovská, a tedy existuje konečná limita lim f .�n/ D `2. 

Nyní je potřeba ukázat, že `1 D `2, jinými slovy, že limita cauchyovských posloupností ff .xn/g nezávisí na volbě posloupnosti fxng. To lze udělat vícero způsoby, např. následujícím obratem. Sestrojme posloupnost fung tak, že u2n�1 D xn, u2n D �n (tj. fung D fx1; �1; x2; �2; : : : g). Zřejmě, fung konverguje zprava k bodu a (zkuste si přeci jen rozmyslet, proč tomu tak je). Podle prvního kroku je ff .un/g opět cauchyovská, a tedy má vlastní limitu `. Protože však ff .xn/g a ff .�n/g jsou posloupnosti vybrané z ff .un/g, musí být ` D `1 D `2. Odtud plyne, že ať vezmeme jakoukoliv posloupnost fxng konvergující k bodu a zprava, tak posloupnost funkčních hodnot ff .xn/g má vždy stejnou vlastní limitu, která je, podle Heineho podmínky, pravostrannou limitou funkce f v bodě a. Analogicky by se ukázalo, že f má levostrannou vlastní limitu v bodě b. 

Definujeme-li nyní funkci 



<!-- Start of picture text -->
8limx!aC f .x/; pro x D a;<br>f � .x/ D f .x/ pro x 2 .a; b/;<br>ˆ<<br>ˆ:limx!b� f .x/; pro x D b;<br><!-- End of picture text -->

pak f<sup>�</sup> je zřejmě spojitá zprava v bodě a (protože f<sup>�</sup> .a/ D limx!aC f .x/) a spojitá zleva v bodě b (protože f<sup>�</sup> .b/ D limx!b� f .x/). Tím je tvrzení dokázáno. 

■ Vˇeta 13.20 — Heineho–Cantorova. _Je-li funkce_ f _spojitá na_ ha; bi _, pak je na tomto intervalu spojitá stejnoměrně._ 

_Důkaz._ Sporem: Připusťme, že f je spojitá na ha; bi, ale ne stejnoměrně. Existuje tedy " > 0 takové, že ke každému ı > 0 existuje dvojice bodů x; y 2 ha; bi taková, že jx � yj < ı a zároveň jf .x/ � f .y/j � ". Zejména tedy pro ı D n1<sup>existujíxn; yn2ha; bi,takžejxn�ynj<</sup> n1<sup>ajf .xn/�f .yn/j�</sup> ". Posloupnost fxng je ohraničená a tedy podle věty 7.27 existuje podposloupnost fxnk g vybraná z fxng taková, že limk!1 xnk D x0 2 ha; bi. Dále platí limk!1 jxnk � ynk j � limk!1 n1k<sup>D0,</sup> tedy limk!1 jxnk � ynk j D 0, což znamená limk!1 ynk D x0. Poněvadž f je spojitá v x0, je limk!1 f .xnk / D f .x0/ D limk!1 f .ynk /, což implikuje limk!1 jf .xnk / � f .ynk /j D 0. To je ale spor s tím, že jf .xnk / � f .ynk /j � ". 

Kapitola 2. Diferenciální poˇcet 

62 

#### Pˇríklady k procviˇcení 

13.1. U následujících funkcí vyšetřete intervaly spojitosti a typ bodů nespojitosti: 



<!-- Start of picture text -->
1<br>f .x/ D x sin 1 g.x/ D 1 h.x/ D u.x/ D x2 � 9 w.x/ D 1 � cos x :<br>x 2 ; x ; ln x ; jx 2 � 9j ; sin x<br>Rozhodněte, zda funkce<br>3 C x 2 pro x � 0;<br>f .x/ D ( sinx 3x pro x > 0<br><!-- End of picture text -->

13.2. Rozhodněte, zda funkce 

je spojitá na R. 

13.3. Prokažte, že rovnice x<sup>3</sup> C 4x � 3 D 0 má v intervalu h0; 1i kořen. _Nápověda._ Aplikujte 1. Bolzanovu větu. 

_Výsledky._ 13.1. Funkce f je spojitá na R n f0g, počátek je bodem odstranitelné nespojitosti; funkce g je spojitá na R n f0g, nespojitost v počátku je typu 1c; funkce h je spojitá na R<sup>C</sup> n f1g, v bodě 1 je nespojitost typu 1c; funkce u je spojitá na R n f�3; 3g, body nespojitosti ˙3 jsou typu „skok“ (nespojitost 1. druhu); funkce w je spojitá na R n fk� W k 2 Zg, body nespojitosti 2k�, k 2 Z, představují odstranitelnou nespojitost, zatímco body .2k C 1/�, k 2 Z jsou typu 1c. 13.2. Ano. 

### 14 Derivace 

Definice 14.1 — derivace funkce v bodˇe. Nechť f je funkce a x0 2 R. Existuje-li vlastní limita 



<!-- Start of picture text -->
f .x/ � f .x0/<br>xlim!x0 x � x0 ;<br><!-- End of picture text -->

nazýváme ji _derivace funkce_ f _v bodě_ x0 a označujeme ji f<sup>0</sup> .x0/. Je-li tato limita nevlastní, řekneme, že f má v bodě x0 _nevlastní derivaci_ . Neexistuje-li tato limita, řekneme, že funkce f nemá derivaci v bodě x0. 

Poznámka 14.2. 1. Má-li f derivaci v bodě x0, pak je v tomto bodě a nějakém jeho okolí definována. 2. Funkce f má v libovolném bodě x0 2 D.f / nejvýše jednu derivaci (plyne z jednoznačnosti limity). 

3. Derivace je definována pouze v x0 2 R. Nelze definovat derivaci v ˙1. 

4. Existence a hodnota derivace f<sup>0</sup> .x0/ je lokální vlastností f . 



<!-- Start of picture text -->
5. Označíme-li x D x0 C h, lze v definici psát limh!0 f .x0Chh/�f .x0/ .<br><!-- End of picture text -->

6. Lze definovat i jednostranné derivace f v bodě x0: 



<!-- Start of picture text -->
f .x/ � f .x0/ f .x0/ � f .x0 � h/<br>derivace zleva f� 0 .x0/ D lim D lim ;<br>x!x0� x � x0 h!0� h<br>f .x/ � f .x0/ f .x0 C h/ � f .x0/<br>derivace zprava fC 0 .x0/ D lim D lim :<br>x!x0C x � x0 h!0C h<br><!-- End of picture text -->

   - Funkce f má v bodě x0 derivaci právě tehdy, když v něm má derivaci zprava a derivaci zleva a platí f�<sup>0.x0/ D f</sup> C<sup>0.x0/.</sup> 

7. Tečnu ke grafu funkce f v bodě Œx0; f .x0/� lze definovat jako přímku, která je limitou sečen procházejících body Œx0; f .x0/� a [x0 C h; f .x0 C h/� při h ! 0 (načrtněte si obrázek). Směrnice sečny procházející těmito body je dána jako tangens úhlu ˛h, který sečna svírá s kladným směrem osy x, tedy (uvědomíme-li si, že tangens úhlu je v pravoúhlém trojúhelníku dán poměrem protilehlé a přilehlé strany) 



<!-- Start of picture text -->
tg ˛h D f .x0 C h/ � f .x0/ :<br>h<br><!-- End of picture text -->

Směrnice tečny tg ˛0 je potom dána limitou 



<!-- Start of picture text -->
f .x0 C h/ � f .x0/<br>tg ˛0 D lim ;<br>h!0 h<br><!-- End of picture text -->

63 

14 Derivace 

což ale není nic jiného než derivace funkce f v bodě x0. Shrnutí: derivaci v bodě lze geometricky interpretovat jako směrnici tečny ke grafu funkce f v bodě x0. Tato tečna má rovnici 



<!-- Start of picture text -->
y � y0 D f 0 .x0/.x � x0/; kde Œx0; y0� D Œx0; f .x0/� je tečný bod;<br><!-- End of picture text -->

a, je-li f<sup>0</sup> .x0/ ¤ 0, rovnice normály (přímka kolmá na tečnu a procházející tečným bodem) má tvar 



<!-- Start of picture text -->
1<br>y � y0 D � f 0 .x0/ .x � x0/:<br><!-- End of picture text -->

8. Derivaci v bodě lze také interpretovat fyzikálně. Má-li proměnná x význam času, tak derivace v bodě pak představuje (okamžitou) rychlost změny veličiny f .x/. 

■ Vˇeta 14.3. _Má-li funkce_ f _v bodě_ x0 2 D.f / _derivaci, pak je v tomto bodě spojitá._ 

_Důkaz._ Nechť f<sup>0</sup> .x0/ existuje. Pak 



<!-- Start of picture text -->
xlim!x0 f .x/ D x lim !x0�f .x/ � f .x0/ C f .x0/� D xlim!x0 � f .xx/ � � fx0.x0/ .x � x0/ C f .x0/�<br>Df 0 .x0/ xlim!x0 .x � x0/ C f .x0/ D f 0.x0/ � 0 C f .x0/ D f .x0/;<br><!-- End of picture text -->

což je požadavek definice spojitosti v bodě (viz definice 13.1). 

Poznámka 14.4. Obrácené tvrzení neplatí, např. f .x/ D jxj je spojitá v bodě 0, ale nemá v tomto bodě derivaci (jednostranné derivace se nerovnají). 

- Vˇeta 14.5. _Nechť_ f; g _mají derivaci v bodě_ x0 2 D.f / \ D.g/ _. Pak platí:_ 

   1. _Pro každé_ c 2 R _je_ .cf /<sup>0</sup> .x0/ D cf<sup>0</sup> .x0/ _._ 

   2. .f ˙ g/<sup>0</sup> .x0/ D f<sup>0</sup> .x0/ ˙ g<sup>0</sup> .x0/ _._ 



<!-- Start of picture text -->
3. .fg/ 0 .x0/ D f 0 .x0/g.x0/ C f .x0/g 0 .x0/ .<br>4. Je-li  g.x0/ ¤ 0 , pak � fg �0 .x0/ D f 0.x0/g.x g 02/ .x �f 0 . / x0/g 0.x0/ .<br><!-- End of picture text -->

_Důkaz._ Je snadný, čtenář si může rozepsat sám. 

■ Vˇeta 14.6 — o derivaci složené funkce. _Nechť_ f _má derivaci v bodě_ �0 2 R _a nechť_ ' _má derivaci v bodě_ x0 2 R _takovém, že_ '.x0/ D �0 _. Pak složená funkce_ F D f ı ' _má derivaci v bodě_ x0 _a platí_ F<sup>0</sup> .x0/ D f<sup>0</sup> .�0/'<sup>0</sup> .x0/ D f<sup>0</sup> .'.x0//'<sup>0</sup> .x0/ _._ 

_Důkaz._ Máme dokázat, že 



<!-- Start of picture text -->
F .x/ � F .x0/ f .'.x// � f .'.x0//<br>F 0 .x0/ D lim D lim D f 0 .�0/' 0 .x0/:<br>x!x0 x � x0 x!x0 x � x0<br><!-- End of picture text -->

Definujme pomocnou funkci g předpisem 



<!-- Start of picture text -->
g.�/ D f .�/ � f .�0/ � f 0 .�0/ pro � ¤ �0; g.�/ D 0 pro � D 0:<br>� � �0<br><!-- End of picture text -->

Protože lim�!�0 g.�/ D f<sup>0</sup> .�0/ � f<sup>0</sup> .�0/ D 0 D g.�0/, je funkce g spojitá v bodě �0. Funkce ' je spojitá v bodě x0, protože má v tomto bodě derivaci (viz věta 14.3). Podle věty 13.6 je pak spojitá v bodě x0 i složená funkce g ı ', tj. platí 



<!-- Start of picture text -->
xlim!x0 g.'.x// D g.'.x0// D g.�0/ D 0:<br><!-- End of picture text -->

Dále platí 



<!-- Start of picture text -->
g.'.x// D f .'.x// � f .'.x0// � f 0 .�0/ pro '.x/ ¤ �0:<br>'.x/ � '.x0/<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet 

64 

Z této rovnosti jednoduchou úpravou dostaneme, že pro každé x 2 O<sup>�</sup> .x0/ takové, že '.x/ ¤ �0, platí rovnost 



<!-- Start of picture text -->
�g.'.x// C f 0 .�0/� '.x/ � '.x0/ D f .'.x// � f .'.x0// :<br>x � x0 x � x0<br><!-- End of picture text -->

Tato rovnost je ale splněna i pro ty x z O<sup>�</sup> .x0/, pro které je '.x/ D �0 (protože pak také '.x/ � '.x0/ D 0 D f .'.x// � f .'.x0//). Máme tedy 



<!-- Start of picture text -->
F .x/ � F .x0/ f .'.x// � f .'.x0//<br>lim D lim<br>x!x0 x � x0 x!x0 x � x0<br>'.x/ � '.x0/<br>D lim g.'.x// C f 0 .�0/� '.x/ � '.x0/ D lim<br>x!x0 �� x � x0 � x!x0 .g.'.x// C f 0.�0// � x lim !x0 x � x0<br>D �xlim!x0 g.'.x// C x lim !x0 f 0.�0/ �' 0 .x0/ D �0 C f 0 .�0/�' 0 .x0/ D f 0 .�0/' 0 .x0/;<br><!-- End of picture text -->

a proto má funkce F derivaci v bodě x0 a platí F<sup>0</sup> .x0/ D f<sup>0</sup> .'.x0//'<sup>0</sup> .x0/. 

■ Vˇeta 14.7 — o derivaci inverzní funkce. _Nechť_ f _je ryze monotónní a spojitá na intervalu_ I _. Nechť_ y0 _je vnitřní bod_ I _a nechť_ f _má v tomto bodě derivaci_ f<sup>0</sup> .y0/ ¤ 0 _. Pak inverzní funkce_ f<sup>�1</sup> _má derivaci v bodě_ x0 D f .y0/ _a platí_ 



<!-- Start of picture text -->
1 1<br>.f �1 / 0 .x0/ D<br>f 0 .y0/ D f 0 .f �1 .x0// :<br><!-- End of picture text -->

_Důkaz._ Protože f je ryze monotónní na I , tak je zde prostá, a tedy inverze existuje. Pro x ¤ x0 platí y D f<sup>�1</sup> .x/ ¤ f<sup>�1</sup> .x0/ D y0 a podle věty o limitě složené funkce (viz věta 12.6) platí 



<!-- Start of picture text -->
f �1 .x/ � f �1 .x0/ 1<br>lim D lim<br>x!x0 x � x0 x!x0 f �1 .x/x��xf0 �1 .x0/<br>1 1 1<br>D lim D lim D<br>x!x0 f .f �1 .x//�f .f �1 .x0// y!y0 f .y/�f .y0/ f 0 .y0/ ;<br>f �1 .x/�f �1 .x0/ y�y0<br><!-- End of picture text -->

kde předposlední rovnost plyne ze spojitosti f (x ! x0 ) y D f .x/ ! f .x0/ D y0). 

Definice 14.8 — derivace funkce. Buď .a; b/ � D.f / otevřený interval, na němž má f derivaci. Pak zobrazení x 7! f<sup>0</sup> .x/ je funkcí s definičním oborem .a; b/. Tato funkce se nazývá _derivace funkce_ f _na intervalu_ .a; b/ a označuje se f<sup>0</sup> . Analogicky zavedeme derivaci na uzavřeném intervalu ha; bi s tím rozdílem, že budeme vyžadovat, aby funkce měla v krajních bodech příslušné jednostranné derivace. 

##### Pˇrehled vzorc˚u pro derivaci 



<!-- Start of picture text -->
.1/ c 0 D 0 8c 2 R; .2/ .x a / 0 D ax a�1 ;<br>.3/ .e x / 0 D e x ; .4/ .a x / 0 D a x ln a;<br>1<br>.5/ .ln x/ 0 D 1 .6/ .loga x/ 0 D<br>x; x ln a ;<br>.7/ .sin x/ 0 D cos x; .8/ .cos x/ 0 D � sin x;<br>1 �1<br>.9/ .tg x/ 0 D .10/ .cotg x/ 0 D ;<br>cos 2 x ; sin 2 x<br>1 �1<br>.12/ .arcsin x/ 0 D .13/ .arccos x/ 0 D<br>p 1 � x 2 ; p 1 � x 2 ;<br>1 �1<br>.13/ .arctg x/ 0 D .14/ .arccotg x/ 0 D<br>1 C x 2 ; 1 C x 2 ;<br><!-- End of picture text -->

14 Derivace 

65 



<!-- Start of picture text -->
.15/ .sinh x/ 0 D cosh x; .16/ .cosh x/ 0 D sinh x;<br>1 �1<br>.17/ .tgh x/ 0 D ; .18/ .cotgh x/ 0 D<br>cosh 2 x sinh 2 x<br>1 1<br>.19/ .argsinh x/ 0 D ; .20/ .argcosh x/ 0 D ;<br>p x 2 C 1 p x 2 � 1<br>1 �1<br>.21/ .argtgh x/ 0 D .22/ .argcotgh x/ 0 D<br>1 � x 2 ; 1 � x 2 :<br><!-- End of picture text -->

Pˇríklad 14.9. Zderivujte a) f .x/ D<sup>~~p~~</sup> x x, b) f .x/ D<sup>~~p~~</sup> 3 x<sup>2</sup> , c) f .x/ D x<sup>2</sup> sin x<sup><u>1</u></sup> pro x ¤ 0; (0 pro x D 0: 

_Řešení._ ad a) D.f / D R<sup>C</sup> . Pro každé x > 0 máme 



<!-- Start of picture text -->
1 1 p x x<br>f 0 .x/ D . p x x/ 0 D �e x ln x�0 D e x ln x� � x 21 ln x C x 1 � x 1 � D x 2 .1 � ln x/:<br><!-- End of picture text -->

ad b) D.f / D R. V každém bodě x ¤ 0 je 



<!-- Start of picture text -->
1<br>f 0 .x/ D � p 3 x 2�0 D .x 2=3 / 0 D 2 3 x�1=3 D 2 3 p 3 x :<br><!-- End of picture text -->

V bodě x D 0 pak platí 



<!-- Start of picture text -->
p 3 x 2 � 0 1 p 3 x 2 � 0 1<br>fC 0 .0/ D lim D lim f� 0 .0/ D lim D lim<br>x!0C x � 0 x!0C p 3 x D 1; x!0� x � 0 x!0� p 3 x D �1;<br><!-- End of picture text -->

a tedy derivace v bodě 0 neexistuje. 

ad c) D.f / D R. Pro x ¤ 0 máme 



<!-- Start of picture text -->
f 0 .x/ D 2x sin x 1 C x2 cos x 1 �� x 12 � D 2x sin x 1 � cos x 1<br><!-- End of picture text -->

a pro x D 0 máme 



<!-- Start of picture text -->
f 0 .0/ D lim f .x/ � f .0/ D lim x 2 sin x 1 D lim x sin 1 D 0:<br>x!0 x � 0 x!0 x x!0 � x �<br><!-- End of picture text -->

Naproti tomu limx!0 f<sup>0</sup> .x/ neexistuje. Obecně tedy nelze zaměňovat f<sup>0</sup> .x0/ (resp. f˙<sup>0.x0/) s limx!x0f0.x/</sup> (resp. limx!x0˙ f<sup>0</sup> .x/). Následující věta říká, za jakých okolností to lze. 

■ Vˇeta 14.10. _Nechť funkce_ f _je spojitá na nějakém_ Oı<sup>C.x0/Dhx0; x0 C ı/</sup><sup>_(resp._O</sup> ı<sup>�.x0/D</sup> .x0 � ı; x0i _) a má derivaci_ f<sup>0</sup> _na_ Oı<sup>�C</sup> .x0/ D .x0; x0 C ı/ _(resp._ Oı<sup>��</sup> .x0/ D .x0 � ı; x0/ _). Existuje-li vlastní nebo nevlastní limita_ limx!x0C f<sup>0</sup> .x/ _(resp._ limx!x0� f<sup>0</sup> .x/ _), pak existuje také_ fC<sup>0.x0/</sup><sup>_(resp._</sup> f�<sup>0.x0/</sup><sup>_) a platí_</sup> 



<!-- Start of picture text -->
fC 0 .x0/ D x!limx0C f 0.x/ (resp. f� 0 .x0/ D x!limx0� f 0.x/ ) :<br><!-- End of picture text -->

Důkaz tvrzení využívá větu 16.3, dokážeme jej tedy později. 

Poznámka 14.11. Věta bezprostředně implikuje, že když f je spojitá funkce na Oı .x0/ D .x0 �ı; x0 Cı/, která má derivaci na O<sup>�</sup> .x0/ D .x0 � ı; x0 C ı/ n fx0g, přičemž jednostranné limity limx!x0˙ f<sup>0</sup> .x/ (vlastní nebo nevlastní) existují a rovnají se, pak existuje i f<sup>0</sup> .x0/ a platí f<sup>0</sup> .x0/ D limx!x0˙ f<sup>0</sup> .x/. 

Kapitola 2. Diferenciální poˇcet 

66 

#### Pˇríklady k procviˇcení 

14.1. Pomocí definice určete derivaci funkce f v bodě x0: 

- a) f .x/ D x<sup>2</sup> C 3, x0 D 0; 

- b) f .x/ D 1=.x � 1/, x0 D 2; 

- c) f .x/ D sin 2x, x0 D �=4. 

14.2. Uvažujte funkci f .x/ D 2x<sup>2</sup> C 1. Najděte všechny body x, ve kterých platí f .x/ D f<sup>0</sup> .x/. 

14.3. Určete derivaci f<sup>0</sup> funkce f , kde: 

- a) f .x/ D sin.1=x<sup>2</sup> /; 

- b) f .x/ D 1= ~~p~~ 1 C 2x; 

- c) f .x/ D 2x sin x=.x<sup>2</sup> � 1/; 

- d) f .x/ D ~~q~~ x ~~<u>p</u>~~ x<sup>~~p~~</sup> x; 

- e) f .x/ D .cosh x/<sup>ln x</sup> . 

14.4. Pomocí vzorce pro derivaci inverzní funkce určete derivaci funkce f : 

- a) f .x/ D<sup>~~p~~</sup> 5 x C 1; 

- b) f .x/ D log2 x � 2. 

14.5. Dokažte, že když f je lichá funkce na intervalu .�a; a/ (a > 0), pak derivace f<sup>0</sup> je sudá funkce na tomto intervalu. 

14.6. V kterých bodech grafu funkce f .x/ D 2 C x � x<sup>2</sup> je tečna rovnoběžná s osou x? 

_Výsledky._ 14.1. a) 0; b) �1; c) 0. 14.2. 1˙<sup>1</sup> = ~~p~~ 2. 14.3. a) �2x<sup>�3</sup> cos x<sup>�2</sup> ; b) �.1C2x/<sup>�3=2</sup> ; c) 2.�x cos xC x<sup>3</sup> cos x �sin x �x<sup>2</sup> sin x/=.x<sup>2</sup> �1/<sup>2</sup> ; d) 7x<sup>�1=8</sup> =8; e) .cosh x/<sup>1Cln x</sup> .cosh x ln cosh x Cx ln x sinh x/=x. 14.4. a) x<sup>�4=5</sup> =5; b) 1=.x ln 2/. 14.6. V bodě Œ<sup>1</sup> =2;<sup>9</sup> =4�. 

### 15 Derivace vyšších ˇrád˚u, diferenciál 

Definice 15.1 — derivace funkce ˇrádu **n** v bodˇe. Buď f funkce, která má derivaci na množině M1 � D.f / a buď x0 2 M1. Má-li funkce f<sup>0</sup> derivaci v bodě x0, nazýváme tuto derivaci _druhou derivací funkce_ f _v bodě_ x0 a značíme ji f<sup>00</sup> .x0/. Obecně: Buď f funkce, která má na množině Mn�1 � D.f / .n � 1/-ní derivaci f<sup>.n�1/</sup> a buď x0 2 Mn�1. Má-li funkce f<sup>.n�1/</sup> derivaci v bodě x0, nazýváme tuto derivaci n _-tou derivací funkce_ f _v bodě_ x0 a značíme ji f<sup>.n/</sup> .x0/. 

##### Užiteˇcné vzorce 

.1/ .x<sup>a</sup> /<sup>.n/</sup> D a.a � 1/.a � 2/ : : : .a � n C 1/x<sup>a�n</sup> .a > n/ .2/ .e<sup>x</sup> /<sup>.n/</sup> D e<sup>x</sup> ; 

.3/ .a<sup>x</sup> /<sup>.n/</sup> D a<sup>x</sup> ln<sup>n</sup> a; .4/ .ln x/<sup>.n/</sup> D .�1/<sup>n�1 .n �1/Š</sup> ; x<sup>n</sup> .5/ .sin x/<sup>.n/</sup> D sin�x C n<sup>�</sup> 2 � .6/ .cos x/<sup>.n/</sup> D cos�x C n<sup>�</sup> 2 �; n n .7/ .fg/<sup>.n/</sup> .x/ D X i f<sup>.n�i/</sup> .x/g<sup>.i/</sup> .x/ (Leibnizova formule). iD0 ! 

Důkaz lze ve všech případech provést matematickou indukcí. 

Definice 15.2 — diferencovatelnosti a diferenciálu funkce v bodˇe. Buď f funkce definovaná na nějakém Oı .x0/ bodu x0 2 R. Řekneme, že f je _diferencovatelná v bodě_ x0, jestliže existují a 2 R 

15 Derivace vyšších ˇrád˚u, diferenciál 

67 

a funkce � W .�ı; ı/ ! R splňující limh!0 �.h/ D 0 takové, že pro každé h 2 .�ı; ı/ platí 

f .x0 C h/ � f .x0/ D ah C h�.h/: 

V tomto případě se lineární funkce h 7! ah nazývá _diferenciál funkce_ f _v bodě_ x0 a značí se df .x0/.h/, stručně df .x0/. 

Poznámka 15.3. Rozdíl f .x0Ch/�f .x0/ se nazývá přírůstek funkce f v bodě x0 při přírůstku h nezávisle proměnné a značí se �f .x0/.h/, stručně �f .x0/. Pro diferencovatelnou funkci platí �f .x0/.h/ D df .x0/.h/ C h�.h/. 

■ Vˇeta 15.4. _Funkce_ f _je diferencovatelná v bodě_ x0 2 R _právě tehdy, když má v tomto bodě derivaci. V tomto případě je_ a D f<sup>0</sup> .x0/ _._ 

_Důkaz._ „)“ Nechť f je diferencovatelná v x0, tj. platí f .x0 C h/ � f .x0/ D ha C h�.h/. Vydělením h ¤ 0 máme 



<!-- Start of picture text -->
f .x0 C h/ � f .x0/ f .x0 C h/ � f .x0/<br>D a C �.h/ a tedy f 0 .x0/ D lim D lim<br>h h!0 h h!0 .a C �.h//<br>D a C hlim!0 �.h/ D a:<br>„ ƒ‚ …<br>D0<br><!-- End of picture text -->

„(“ Nechť f má v bodě x0 derivaci. Položme a D f<sup>0</sup> .x0/ a 



<!-- Start of picture text -->
�.h/ D f .x0 C h/ � f .x0/ � hf 0.x0/ :<br>h<br><!-- End of picture text -->

Pak f .x0 C h/ � f .x0/ D ah C h�.h/ a 



<!-- Start of picture text -->
f .x0 C h/ � f .x0/ � hf 0 .x0/<br>lim D f 0 .x0/ � f 0 .x0/ D 0:<br>h!0 �.h/ D h lim !0 h<br><!-- End of picture text -->

Pro diferenciál tedy platí df .x0/.h/ D f<sup>0</sup> .x0/h. Z tohoto vyjádření plyne geometrická interpretace diferenciálu. Diferenciál je přírůstek naměřený na tečně, tj. �f .x0/.h/ � f<sup>0</sup> .x0/h. Toho lze využít k přibližnému výpočtu funkční hodnoty, viz následující příklad. 

Pˇríklad 15.5. Vypočtěte přibližně hodnotu<sup>~~p~~</sup> 4;02. 

_Řešení._ Položme f .x/ D<sup>~~p~~</sup> x. Potom<sup>~~p~~</sup> 4;02 � ~~p~~ 4 D f .4;02/ � f .4/ � df .4/.0;02/. Protože f<sup>0</sup> .x/ D 21<sup>x�1=2, máme df .4/.0;02/ D</sup> 4<sup><u>1</u>�0;02 D 0;005 a tedy</sup><sup>~~p~~</sup> 4;02 � 2 C 0;005 D 2;005 (přesnější hodnota je 2; 00499). 

Poznámka 15.6. Položíme-li f .x/ D x, pak f<sup>0</sup> .x0/ D 1 pro každé x0 2 R, a tedy df .x0/.h/ D h, stručně dx D h. Lze tedy psát df .x0/ D f<sup>0</sup> .x0/ dx a naopak f<sup>0</sup> .x0/ D<sup>df</sup> d<sup><u>.</u></sup> x<sup>x0/</sup> , stručně f<sup>0</sup> D<sup>d</sup> d<sup><u>f</u></sup> x (Leibnizův zápis derivace). Za použití této symboliky pak dostane názorný tvar např. vzorec pro derivaci složené funkce 



<!-- Start of picture text -->
ddfx D d d f ' � d d ' x :<br><!-- End of picture text -->

Definice 15.7 — **n** -tého diferenciálu funkce v bodˇe. Nechť f má v bodě x0 n-tou derivaci f<sup>.n/</sup> .x0/, n � 1. Pak n _-tý diferenciál v bodě_ x0, který budeme značit d<sup>n</sup> f .x0/, je definován jako zobrazení h 7! f<sup>.n/</sup> .x0/h<sup>n</sup> . Symbolicky lze psát d<sup>n</sup> f .x0/ D f<sup>.n/</sup> .x0/ dx<sup>n</sup> . 

Kapitola 2. Diferenciální poˇcet 

68 

Poznámka 15.8. Díky poslednímu vztahu je tedy možno psát f<sup>.n/</sup> D<sup>d</sup> d<sup>n</sup> x<sup><u>fn</u>(Leibnizůvzápisn-té</sup> derivace). 

#### Pˇríklady k procviˇcení 

15.1. Doba kmitu kyvadla je dána vzorcem 



<!-- Start of picture text -->
l<br>T D 2�<br>s g ;<br><!-- End of picture text -->

kde l je délka kyvadla a g je tíhové zrychlení. Jak musíme přibližně změnit délku kyvadla dlouhého 20 cm, aby se doba kmitu zvětšila o 0,05 s? (Uvažujte g D 981 cm � s<sup>�2</sup> .) 

15.2. Určete diferenciál funkce 



<!-- Start of picture text -->
f .x/ D arcsin x a ¤ 0<br>a ;<br><!-- End of picture text -->

15.3. Pomocí předchozího výsledku určete přibližně hodnotu arcsin 0;2. 

15.4. Určete druhý diferenciál funkce 



<!-- Start of picture text -->
f .x/ D ln x<br>x :<br><!-- End of picture text -->

_Výsledky._ 15.1. Kyvadlo je potřeba prodloužit o 2,23 cm. 15.2. df .x/.h/ D ~~p~~ asg<sup>2</sup> n� ax<sup>2h, jxj < jaj. 15.3.</sup> 0,2. 15.4. d<sup>2</sup> f .x/.h/ D<sup><u>2 ln</u></sup> x<sup><u>x3�3</u></sup> h<sup>2</sup> , x > 0. 

### 16 Obecné vˇety o derivaci 

■ Vˇeta 16.1 — Rolleova<sup>2</sup> . _Nechť funkce_ f _splňuje předpoklady:_ 

- (i) _je spojitá na_ ha; bi _;_ 

- (ii) _má vlastní nebo nevlastní derivaci v každém bodě_ .a; b/ _;_ 

(iii) f .a/ D f .b/ _._ 

_Pak existuje bod_ c 2 .a; b/ _tak, že_ f<sup>0</sup> .c/ D 0 _._ 

_Důkaz._ Je-li f konstantní, stačí za c vzít libovolný bod z .a; b/. Nechť f není konstantní a předpokládejme nejprve, že f .a/ D f .b/ ¤ maxff .x/ W x 2 ha; big. Podle 2. Weierstrassovy věty existuje c 2 .a; b/ takové, že f .c/ D maxff .x/ W x 2 ha; big. Podle (ii) existuje f<sup>0</sup> .c/ 2 R<sup>�</sup> . Připusťme f<sup>0</sup> .c/ > 0, tedy limx!c<sup><u>f.x</u></sup> x<sup><u>/�</u></sup> �<sup><u>f</u></sup> c<sup><u>.c/</u></sup> > 0. To znamená, že existuje O<sup>�</sup> .c/ takové, že pro x 2 O<sup>�</sup> .c/ je<sup><u>f.x</u></sup> x<sup><u>/�</u></sup> �<sup><u>f</u></sup> c<sup><u>.c/</u></sup> > 0. Zvolme x1 2 ha; bi \ O<sup>�</sup> .c/, x1 > c. Pak x1 � c > 0, f .x1/ � f .c/ � 0, tedy<sup><u>f.x</u></sup> x<sup><u>/�</u></sup> �<sup><u>f</u></sup> c<sup><u>.c/</u></sup> � 0, což je spor. Analogicky vyloučíme možnost f<sup>0</sup> .c/ < 0. Je tedy f<sup>0</sup> .c/ D 0. Pokud f .a/ D f .b/ D maxff .x/ W x 2 ha; big, existuje c 2 .a; b/ takové, že f .c/ D minff .x/ W x 2 ha; big a provedeme analogické úvahy. 

Poznámka 16.2. Z důkazu plyne, že za c lze volit bod, ve kterém f nabývá svého maxima nebo minima. Neplyne z něho ale, že jiné body, ve kterých je nulová derivace, neexistují. 

- Vˇeta 16.3 — Lagrangeova<sup>3</sup> vˇeta o stˇrední hodnotˇe, vˇeta o pˇrír˚ustku funkce. _Nechť funkce_ f _splňuje:_ (i) _je spojitá na_ ha; bi _,_ 

(ii) _v každém bodě_ .a; b/ _má vlastní nebo nevlastní derivaci. Pak existuje_ c 2 .a; b/ _takové, že platí_ 



<!-- Start of picture text -->
f 0 .c/ D f .b/ � f .a/ :<br>b � a<br><!-- End of picture text -->

> 2Michel Rolle 1652–1719, Francouz 

> 3Joseph-Louis Lagrange 1736–1813, Francouz italského původu 

16 Obecné vˇety o derivaci 

69 

_Důkaz._ Položme F.x/ D .b � a/f .x/ � .f .b/ � f .a//x pro x 2 ha; bi. Díky předpokladům na f splňuje F předpoklady Rolleovy věty (ověřte), a tedy existuje c 2 .a; b/ tak, že F<sup>0</sup> .c/ D 0. Derivace F je F<sup>0</sup> .x/ D .b � a/f<sup>0</sup> .x/ � .f .b/ � f .a//, a tedy F<sup>0</sup> .c/ D .b � a/f<sup>0</sup> .c/ � .f .b/ � f .a// D 0. Vyjádříme-li odtud f<sup>0</sup> .c/, dostáváme požadované tvrzení. 

Poznámka 16.4. Z věty 16.3 plyne f .b/ � f .a/ D f<sup>0</sup> .c/.b � a/. Levá strana představuje přírůstek funkční hodnoty mezi body a; b, odtud druhý název věty. _Důkaz věty 14.10._ Nechť x 2 Oı<sup>�C</sup> .x0/. Protože podle předpokladu je f spojitá na Oı<sup>C.x0/, a tedy i na</sup> hx0; xi, podle Lagrangeovy věty o střední hodnotě existuje v intervalu .x0; x/ bod x0 C #.x � x0/, # 2 .0; 1/, takový, že platí 



<!-- Start of picture text -->
f .x/ � f .x0/<br>D f 0 .x0 C #.x � x0//:<br>x � x0<br><!-- End of picture text -->

Podle dalšího předpokladu existuje limita limx!x0C f<sup>0</sup> .x/ D a. Uvažujme nejprve případ, kdy je tato limita vlastní, tj. a 2 R. To znamená, že k libovolnému " > 0 existuje ı<sup>�</sup> < ı takové, že pro každé x 2 Oı<sup>�C�.x0/ je jf0.x/ �aj < ". Pokud tedy x2 O</sup> ı<sup>�C�.x0/, pak</sup> 



<!-- Start of picture text -->
f .x/ � f .x0/<br>� a<br>ˇˇf 0.x0 C #.x � x0// � aˇˇ < ";<br>ˇˇˇˇ x � x0 ˇˇˇˇ D<br><!-- End of picture text -->

což ale znamená, že fC<sup>0.x0/ D a.</sup> 

Pokud je limx!x0C f<sup>0</sup> .x/ D 1, pak k libovolnému h 2 R existuje ı<sup>�</sup> < ı takové, že pro každé x 2 Oı<sup>�C�.x0/ je f0.x/ > h. Pro takové xtedy máme</sup> 



<!-- Start of picture text -->
f .x/ � f .x0/<br>D f 0 .x0 C #.x � x0// > h;<br>x � x0<br><!-- End of picture text -->



<!-- Start of picture text -->
tj. fC 0 .x0/ D 1. Analogicky by se ukázala rovnost pro nevlastní limitu limx!x 0 C f 0.x/ D �1.<br>Stejným postupem by se tvrzení dokázalo i pro levostrannou limitu.<br><!-- End of picture text -->

■ Vˇeta 16.5 — Cauchyova vˇeta o stˇrední hodnotˇe, vˇeta o podílu pˇrír˚ustk˚u funkcí. _Nechť funkce_ f; g _splňují:_ 

(i) _jsou spojité na_ ha; bi _,_ 

(ii) _pro každé_ x 2 .a; b/ _existuje vlastní nebo nevlastní derivace_ f<sup>0</sup> .x/ _a vlastní nebo nevlastní derivace_ g<sup>0</sup> .x/ ¤ 0 _._ 

_Pak existuje_ c 2 .a; b/ _takové, že_ 



<!-- Start of picture text -->
fg.b/.b/ � � fg.a/.a/ D f g 00 .c/ .c/ :<br><!-- End of picture text -->

_Důkaz._ Funkce g splňuje předpoklady Lagrangeovy věty o střední hodnotě a tedy existuje d 2 .a; b/ takové, že<sup><u>g.b</u></sup> b<sup><u>/�</u></sup> �<sup><u>g.</u></sup> a<sup>a/</sup> D g<sup>0</sup> .d/ ¤ 0, z čehož plyne g.b/ � g.a/ ¤ 0, takže zlomek na levé straně tvrzení věty má smysl. Položme F.x/ D .g.b/ � g.a//f .x/ � .f .b/ � f .a//g.x/ pro x 2 ha; bi. Protože tato funkce splňuje předpoklady Rolleovy věty, existuje c 2 .a; b/ takové, že F<sup>0</sup> .c/ D 0. Tedy 0 D .g.b/ � g.a//f<sup>0</sup> .c/ � .f .b/ � f .a//g<sup>0</sup> .c/, z čehož plyne požadované tvrzení. 

Poznámka 16.6. Důkaz Lagrangeovy věty využívá Rolleovu větu. Důkaz Cauchyovy věty využívá Lagrangeovu a Rolleovu větu. Bezprostředně je ale vidět, že Lagrangeova věta je důsledkem Cauchyovy věty a Rolleova věta je důsledkem Lagrangeovy věty. Všechny tři věty jsou tedy ekvivalentní. 

■ Vˇeta 16.7 — l’Hospitalovo<sup>4</sup> pravidlo. _Nechť_ f; g _jsou funkce,_ x0 2 R<sup>�</sup> _a nechť_ 



<!-- Start of picture text -->
xlim!x0 f .x/ D x lim !x0 g.x/ D 0<br><!-- End of picture text -->

4Guillaume Francois de l’Hospital 1661–1704, Francouz, skutečným autorem je však Johann Bernoulli 1667–1748, Švýcar 

Kapitola 2. Diferenciální poˇcet 

70 

_nebo_ 



<!-- Start of picture text -->
xlim!x0 f .x/ D ˙1; xlim!x0 g.x/ D ˙1:<br><!-- End of picture text -->

_Existuje-li_ 



<!-- Start of picture text -->
f 0 .x/<br>lim<br>x!x0 g 0 .x/ 2 R�;<br><!-- End of picture text -->

_pak existuje i_ 



<!-- Start of picture text -->
f .x/ f .x/ f 0 .x/<br>lim a platí lim<br>x!x0 g.x/ x!x0 g.x/ D x lim !x0 g 0 .x/ :<br><!-- End of picture text -->

_Stejné tvrzení platí i pro jednostranné limity._ 

_Důkaz._ Důkaz provedeme pouze pro případ nulových limit funkcí f , g (druhý případ je o něco složitější). Nechť tedy existuje vlastní nebo nevlastní limita 



<!-- Start of picture text -->
f 0 .x/<br>L WD lim<br>x!x0 g 0 .x/ :<br><!-- End of picture text -->

Uvažujme nejprve limitu zprava x ! x0C, kde x0 2 R (tj. x0 je vlastní bod). Existence limity L implikuje, že funkce f<sup>0</sup> , g<sup>0</sup> a f<sup>0</sup> =g<sup>0</sup> jsou definovány v nějakém pravém okolí bodu x0, tj. na intervalu .x0; x0 C ı/ (ı > 0). Podle věty 14.3 jsou pak f , g spojité v každém bodě tohoto intervalu. Pokud navíc položíme f .x0/ D g.x0/ D 0 (to můžeme, protože existence limity nezávisí na hodnotách funkce v bodě x0), pak f , g budou spojité zprava v bodě x0, tj. celkově máme spojitost těchto funkcí na intervalu hx0; x0 C ı/. Zvolme nyní číslo x1 2 .x0; x0 C ı/ libovolně. Pak funkce f , g jsou spojité na intervalu hx0; x1i, přičemž g<sup>0</sup> .x/ ¤ 0 pro každé x 2 .x0; x1/ (kdyby nastal opak, nemohl by výraz f<sup>0</sup> =g<sup>0</sup> být definován v intervalu .x0; x0 C ı/). Funkce f , g tedy splňují předpoklady Cauchyovy věty o střední hodnotě (viz věta 16.5), a proto existuje � 2 .x0; x1/ takové, že 



<!-- Start of picture text -->
f .x1/ � f .0/ f .x1/ � 0 f .x1/<br>) )<br>g.x1/ � g.0/ D f g 00 .�/ .�/ g.x1/ � 0 D f g 00 .�/ .�/ g.x1/ D f g 00 .�/ .�/ :<br><!-- End of picture text -->

Poslední rovnost platí nezávisle na volbě bodu x1 (přesněji, pro každé x1 2 .x0; x0 C ı/ existuje � 2 .x0; x1/ takové, že platí poslední rovnost), pro x1 ! x0C tedy máme i � ! x0C (viz věta o 3 limitách), přičemž 



<!-- Start of picture text -->
f .x1/ f 0 .�/ f .x/<br>lim lim tj. lim<br>x1!x0C g.x1/ D �!x0C g 0 .�/ ; x!x0C g.x/ D L:<br><!-- End of picture text -->

Analogicky bychom ukázali případ limx!x0�, kdy opět 



<!-- Start of picture text -->
f .x/<br>lim<br>x!x0� g.x/ D L:<br><!-- End of picture text -->

Pokud je x0 nevlastní bod, např. x0 D 1, použijeme právě dokázané tvrzení na limitu 



<!-- Start of picture text -->
f .1=x/<br>lim<br>x!0C g.1=x/ ;<br><!-- End of picture text -->

která se rovná (pokud existuje) limitě 



<!-- Start of picture text -->
f .x/<br>lim<br>x!1 g.x/ :<br><!-- End of picture text -->

Poznámka 16.8. a) l’Hospitalovo pravidlo lze při zachování uvedených předpokladů opakovat. 

b) Limity vedoucí k neurčitým výrazům 0 �1, 1 �1, 0<sup>0</sup> , 1<sup>0</sup> a 1<sup>1</sup> lze řešit pomocí l’Hospitalova pravidla zprostředkovaně: 

17 Taylor˚uv polynom 

71 



<!-- Start of picture text -->
f .x/<br>(i) Typ 0 �1 W xlim!x0 f .x/ D 0, x lim !x0 g.x/ D ˙1 ) x lim !x0 f .x/g.x/ D x lim !x0 1 .<br>g.x/<br>1 1<br>(ii) Typ 1�1 W xlim!x0 f .x/ D x lim !x0 g.x/ D 1 ) x lim !x0�f .x/�g.x/� D xlim!x0 1 � 1 D<br>f .x/ g.x/ !<br>1 1<br>g.x/ � f .x/<br>xlim!x0 f .x/1 � g.x/1 .<br>(iii) Typy 0 0 , 1 0 , 1 1 W xlim!x0 .f .x//g.x/ D elimx!x0 g.x/ ln f .x/, kde vnitřní limita je typu 0 �1.<br><!-- End of picture text -->



<!-- Start of picture text -->
Pˇríklad 16.9. Vypočítejte limitu limx!0C �cotg x � x 1 �.<br><!-- End of picture text -->

_Řešení._ Dvojí aplikací l’Hospitalova pravidla máme 



<!-- Start of picture text -->
x cos x � sin x<br>lim cotg x � 1 D lim D lim<br>x!0C � x � x!0C � cossin x x � x 1 � x!0C x sin x<br>�x sin x �.sin x C x cos x/<br>D lim lim D 0:<br>x!0C sin x C x cos x D x!0C 2 cos x � x sin x<br><!-- End of picture text -->

#### Pˇríklady k procviˇcení 

16.1. Pomocí l’Hospitalova pravidla vyšetřete následující limity: 



<!-- Start of picture text -->
x � sin x<br>a) lim ;<br>x!0 x 3<br>b) x!lim0C .cos x/1=x;<br>1<br>c) lim ;<br>x!0C � x1 3 � sin 3 x �<br>d) x!lim0C x2 ln x;<br>e) x!lim�=2� .tg x/2x�� ;<br>1<br>f) lim .<br>x!0� � x1 � e x �1 �<br><!-- End of picture text -->

16.2. Odůvodněte, proč nelze použít l’Hospitalova pravidla k výpočtu limit 



<!-- Start of picture text -->
a) lim x 2 sin x 1 I b) lim 4 � cos x<br>x!0C sin x x!1 2 C cos x :<br><!-- End of picture text -->

_Výsledky._ 16.1. a)<sup>1</sup> =6; b) 1; c) �1; d) 0; e) 1; f)<sup>1</sup> =2. 

### 17 Taylor˚uv polynom 

Definice 17.1 — Taylorova polynomu. Nechť f má v bodě x0 2 D.f / derivace až do n-té včetně. Polynom 



<!-- Start of picture text -->
Tn;x f 0 .x/ D f .x 0 / C f 0.x0/ .x � x0/ C f 00.x0/ .x � x0/ 2 C ���C f .n/.x0/ .x � x0/ n<br>1Š 2Š nŠ<br><!-- End of picture text -->

se nazývá _Taylorův_<sup>_5_</sup> _polynom funkce_ f _se středem v bodě_ x0. Pokud nemůže dojít k nedorozumění, budeme psát stručně Tn.x/. Je-li x0 D 0, nazývá se tento polynom _Maclaurinův_<sup>_6_</sup> . 

Kapitola 2. Diferenciální poˇcet 

72 

Maclaurinovy polynomy nˇekterých elementárních funkcí 1. f .x/ D e<sup>x</sup> , .e<sup>x</sup> /<sup>.n/</sup> D e<sup>x</sup> , f<sup>.n/</sup> .0/ D e<sup>0</sup> D 1 a tedy 



<!-- Start of picture text -->
n x k<br>Tn.x/ D 1 C 1Š x C x 2Š 2 C ���C x nŠ n D X kŠ :<br>kD0<br><!-- End of picture text -->

2. f .x/ D sin x, f .0/ D 0, f<sup>0</sup> .x/ D cos x ) f<sup>0</sup> .0/ D 1, f<sup>00</sup> .x/ D � sin x ) f<sup>00</sup> .0/ D 0, f<sup>000</sup> .x/ D � cos x ) f<sup>000</sup> .0/ D �1, f<sup>.4/</sup> D sin x ) f<sup>.4/</sup> .0/ D 0, . . . . Celkem f<sup>.2n�1/</sup> .0/ D .�1/<sup>n�1</sup> , f<sup>.2n/</sup> .0/ D 0. Odtud 



<!-- Start of picture text -->
T2n�1.x/ D T2n.x/ D x � x 3Š 3 C x 5Š 5 ����C .�1/n�1 .2n x2n  � � 1/Š 1 D Xn .�1/ k�1 .2k x2k  � � 1/Š 1 :<br>kD1<br><!-- End of picture text -->

3. f .x/ D cos x, f .0/ D 1, f<sup>0</sup> .x/ D � sin x ) f<sup>0</sup> .0/ D 0, f<sup>00</sup> .x/ D � cos x ) f<sup>00</sup> .0/ D �1, f<sup>000</sup> .x/ D sin x ) f<sup>000</sup> .0/ D 0, f<sup>.4/</sup> D cos x ) f<sup>.4/</sup> .0/ D 1, . . . . Celkem f<sup>.2n�1/</sup> .0/ D 0, f<sup>.2n/</sup> .0/ D .�1/<sup>n</sup> . Odtud 



<!-- Start of picture text -->
T2n.x/ D T2nC1.x/ D 1 � x 2Š 2 C x 4Š 4 ����C .�1/n .2n/Š x2n D Xn .�1/ k .2k/Š x2k :<br>kD0<br><!-- End of picture text -->

4. f .x/ D ln.1 C x/, f .0/ D 0, f<sup>0</sup> .x/ D 1C1 x<sup>)f0.0/D1,f00.x/D�</sup> .1C1x/<sup>2)f00.0/D�1,</sup> f<sup>000</sup> .x/ D .1C2x/<sup>3,f000.0/D2,f.4/.x/D�</sup> .1C2�x/3<sup>4,f.4/.0/D�2 �3,. . . .Celkemf.n/.x/D</sup> .�1/<sup>n�1</sup> .1<sup><u>.n</u></sup> C<sup>�</sup> x/<sup>1/nŠ) f.n/.0/ D .�1/n�1.n �1/Š. Odtud</sup> 



<!-- Start of picture text -->
Tn.x/ D x � x 2 2 C x 3 3 ����C .�1/n�1 x n n D Xn .�1/ k�1 x k k :<br>kD1<br><!-- End of picture text -->



<!-- Start of picture text -->
5. f .x/ D .1 C x/ ˛ , ˛ 2 R, f .0/ D 1, f 0 .x/ D ˛.1 C x/ ˛�1 ) f 0 .0/ D ˛, f 00 .x/ D ˛.˛ � 1/.1 C<br>x/ ˛�2 ) f 00 .0/ D ˛.˛ � 1/, f 000 .x/ D ˛.˛ � 1/.˛ � 2/.1 C x/ ˛�3 ) f 000 .0/ D ˛.˛ � 1/.˛ � 2/,<br>. . . . Celkem f .n/ .x/ D ˛.˛ � 1/ : : : .˛ � n C 1/.1 C x/ ˛�n ) f .n/ .0/ D ˛.˛ � 1/ : : : .˛ � n C 1/.<br>Definujeme-li �˛k� D ˛.˛�1/::: kŠ .˛�kC1/ , k D 1; 2; : : : , �˛0� D 1, pak<br>n<br>˛ ˛ ˛ ˛<br>Tn.x/ D 1 C 1 x C 2 x 2 C ���C n x n D X k x k :<br>! ! ! kD0 !<br><!-- End of picture text -->

Pro ˛ 2 N, ˛ � n, je Maclaurinův polynom rozepsáním výrazu .1 C x/<sup>˛</sup> podle binomické věty. 

■ Vˇeta 17.2 — Taylorova. _Buď_ f _funkce,_ x0 2 D.f / _,_ n 2 N _. Nechť existuje_ O.x0/ _takové, že_ f _má_ .n C 1/ _-ní derivaci v každém bodě z_ O.x0/ _a nechť_ x 2 O.x0/ _. Pak v otevřeném intervalu s krajními body_ x0 _a_ x _existuje číslo_ � 2 R _takové, že platí_ 



<!-- Start of picture text -->
f .x/ D f .x0/ C f 0.x0/ .x � x0/ C f 00.x0/ .x � x0/ 2 C ���<br>1Š 2Š<br>C f .n/.x0/ .x � x0/ n C f .nC1/.�/<br>nŠ .n C 1/Š .x � x0/nC1:<br><!-- End of picture text -->

_Důkaz._ Nechť xQ 2 O<sup>�C</sup> .x0/ je libovolné. Položme 



<!-- Start of picture text -->
K D f .x Q / � Tn. Qx/ tj. f .x/ Q  D Tn. Qx/ C K.x Q � x0/ nC1 :<br>.x Q � x0/ nC1 ;<br><!-- End of picture text -->

> 5Brook Taylor 1685–1731, Angličan 

> 6Colin Maclaurin 1698–1746, Skot 

17 Taylor˚uv polynom 

73 

Dále položíme F.x/ D f .x/ � Tn.x/ � K.x � x0/<sup>nC1</sup> pro x 2 hx0; xQ i. Funkce F má na hx0; xQ i spojité derivace až do řádu n, protože f má na tomto intervalu .n C 1/-ní derivaci (viz věta 14.3) a Tn, .x � x0/<sup>nC1</sup> mají derivace všech řádů. Dosazením x D x0 do F (s využitím definice Tn) je snadné ověřit, že F.x0/ D F<sup>0</sup> .x0/ D F<sup>00</sup> .x0/ D ���D F<sup>.n/</sup> .x0/ D 0. Dále F.x/ Q D 0. Tedy F splňuje na hx0; xQ i předpoklady Rolleovy věty (viz věta 16.1). Odtud plyne, že existuje �1 2 .x0; x/Q takové, že F<sup>0</sup> .�1/ D 0. 

To dále znamená, že funkce F<sup>0</sup> splňuje předpoklady Rolleovy věty na hx0; �1i, z čehož plyne, že existuje �2 2 hx0; �1i takové, že F<sup>00</sup> .�2/ D 0. 

Takto pokračujeme dále, až v n-tém kroku ukážeme, že existuje �n 2 .x0; x/Q takové, že F<sup>.n/</sup> .�n/ D 0. Protože i F<sup>.n/</sup> splňuje předpoklady Rolleovy věty, existuje � 2 .x0; �n/ � .x0; x/Q takové, že F<sup>.nC1/</sup> .�/ D 0. Přitom 



<!-- Start of picture text -->
F .nC1/ .�/ D f .nC1/ .�/ � 0 � K.n C 1/Š D 0:<br><!-- End of picture text -->

Odtud plyne K D f<sup>.nC1/</sup> .�/=.n C 1/Š. Dokázali jsme tedy vzorec pro x D xQ . Protože ale xQ 2 O<sup>�C</sup> .x0/ bylo libovolné, platí vzorec na celém pravém okolí O<sup>�C</sup> .x0/. Jeho platnost na levém okolí bodu by se ukázala analogicky. 

Poznámka 17.3. a) Rovnost ve větě lze obecně napsat jako f .x/ D Tn.x/ C Rn.x/, kde funkce Rn se nazývá _Taylorův zbytek_ . V našem případě je 



<!-- Start of picture text -->
Rn.x/ D f .nC1/.�/<br>.n C 1/Š .x � x0/nC1<br><!-- End of picture text -->

a toto vyjádření se nazývá _Lagrangeův tvar Taylorova zbytku_ . Existují i jiné tvary Taylorova zbytku, např. _Cauchyův tvar_ 



<!-- Start of picture text -->
Rn.x/ D f .nC1/.�/ .x � x0/.x � �/ n ;<br>nŠ<br><!-- End of picture text -->

kde � je reálné číslo ležící někde uvnitř intervalu s krajními body x0 a x. 

b) Číslo � lze napsat ve tvaru � D x0 C #.x � x0/, kde # 2 .0; 1/ závisí na zvoleném x. 

c) Lagrangeovu větu o střední hodnotě (věta 16.3) lze chápat jako speciální případ Taylorovy věty (pro n D 1). 

Zbytky Maclaurinových polynom˚u vybraných elementárních funkcí 



<!-- Start of picture text -->
e #x<br>1. f .x/ D e x , Rn.x/ D .n C 1/Š xnC1;<br>2. f .x/ D sin x, R2n�1.x/ D sin.#x C n�/ x 2n ;<br>.2n/Š<br>3. f .x/ D cos x, R2n.x/ D cos �#x C 2n 2 C1 �� x 2nC1 ;<br>.2n C 1/Š<br>x nC1<br>4. f .x/ D ln.x C 1/, Rn.x/ D .�1/ n<br>.n C 1/.1 C #x/ nC1 ;<br>˛<br>5. f .x/ D .1 C x/ ˛ , Rn.x/ D .1 C #x/ ˛�n�1 x nC1 .<br>n C 1<br>!<br><!-- End of picture text -->

Pˇríklad 17.4. Určete Maclaurinův polynom, který na intervalu .��=2; �=2/ aproximuje funkci f .x/ D sin x s přesností 10<sup>�5</sup> . 

_Řešení._ Pro Taylorův zbytek funkce sin na zadaném intervalu platí 



<!-- Start of picture text -->
sin.#x C n�/ 2 /2n<br>jR2n�1.x/j D x 2n<br>ˇˇˇˇ .2n/Š ˇˇˇˇ � .2n/Šx2n � . .2n/Š � :<br><!-- End of picture text -->

Protože jR9.x/j � 0;00002 a jR11j � 0;0000005 < 10<sup>�5</sup> , stačí vzít 



<!-- Start of picture text -->
T11.x/ D x � x 6 3 C 120 x5 � 5 040x 7 C 362 880x 9 � 39 916 800x 11 :<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet 

74 

#### Pˇríklady k procviˇcení 

17.1. V mocninách dvojčlenu .x C 1/ vyjádřete polynom P.x/ D x<sup>4</sup> � 4x<sup>3</sup> C 7x � 2. 

17.2. Napište Maclaurinův polynom stupně 3 funkce f .x/ D tg x. 



<!-- Start of picture text -->
17.3. Napište Maclaurinův polynom stupně 4 funkce f .x/ D 1<br>p 3 1Cx .<br><!-- End of picture text -->

17.4. Užitím Taylorovy věty určete přibližně hodnoty 



<!-- Start of picture text -->
a) cos 9 ı I b) p 3 30<br><!-- End of picture text -->

tak, aby chyba aproximace byla menší než 10<sup>�5</sup> . 

_Výsledky._ 17.1. P.x/ D �4 � 9.x C 1/ C 18.x C 1/<sup>2</sup> � 8.x C 1/<sup>3</sup> C .x C 1/<sup>4</sup> . 17.2. T3.x/ D x C<sup><u>1</u></sup> 3<sup>x3.</sup> 17.3. T4.x/ D 1 �<sup><u>1</u></sup> 3<sup>x C</sup><sup><u>2</u></sup> 9<sup>x2 �</sup><sup><u>14</u></sup> 81<sup>x3 C</sup> 243<sup><u>35</u>x4. 17.4. a) 0;98769; b) 3;107233.</sup> 

### 18 Pr˚ubˇeh funkce 

■ Vˇeta 18.1. _Nechť_ f _je spojitá na intervalu_ I _a má zde vlastní nebo nevlastní derivaci. Pak_ f _je rostoucí (resp. klesající) na_ I , f<sup>0</sup> .x/ � 0 _(resp._ f<sup>0</sup> .x/ � 0 _)_ 8x 2 I _, přičemž_ f<sup>0</sup> _není nulová na žádném podintervalu intervalu_ I _._ 

_Důkaz._ „)“ Nechť f je rostoucí na I , tj. pro všechny dvojice x1; x2 2 I , x1 < x2, platí f .x1/ < f .x2/. Nechť x0 2 I je libovolný bod. Pak pro každé x < x0 platí f .x/ < f .x0/, tj. 



<!-- Start of picture text -->
f .x/ � f .x0/ f .x/ � f .x0/<br>> 0; a tedy f 0 .x0/ D f� 0 .x0/ D lim � 0;<br>x � x0 x!x0� x � x0<br><!-- End of picture text -->

neboť dle předpokladu má f v bodě x0 vlastní nebo nevlastní derivaci. Analogicky, pro každé x > x0 je f .x/ > f .x0/, a tedy také 



<!-- Start of picture text -->
f .x/ � f .x0/ f .x/ � f .x0/<br>> 0; z čehož plyne f 0 .x0/ D fC 0 .x0/ D lim � 0:<br>x � x0 x!x0� x � x0<br><!-- End of picture text -->

(v případě, kdy x0 2 I je krajní bod I , uvažujeme pouze jednostrannou derivaci). Zbývá ukázat, že nulová hodnota derivace nemůže nastat na intervalu J � I . Kdyby tomu tak bylo, tak by funkce musela být na J konstantní (tato vlastnost je jednoduchým důsledkem Lagrangeovy věty o střední hodnotě, viz Lemma 19.2), což je spor s tím, že f je rostoucí. 

Analogicky bychom ukázali, že v případě klesající funkce musí být f<sup>0</sup> .x/ � 0 pro všechna x 2 I . 

„(“ Nechť f<sup>0</sup> .x/ � 0 8x 2 I , přičemž tato derivace není nulová na žádném podintervalu intervalu I . Nechť x1; x2 2 I jsou libovolné body takové, že x1 < x2. Potom podle Lagrangeovy věty o střední hodnotě existuje c 2 .x1; x2/ takové, že f .x2/ � f .x1/ D f<sup>0</sup> .c/.x2 � x1/, a tedy f .x2/ � f .x1/, protože f<sup>0</sup> .c/ � 0 a x2 � x1 > 0. To znamená, že f je neklesající na I . Předpokládejme, že na nějakém intervalu J � I je f konstantní. Potom ale na tomto intervalu je f<sup>0</sup> .x/ D 0, což je spor s předpokladem. Funkce f tedy musí být rostoucí. 

Analogicky bychom ukázali, že předpoklad f<sup>0</sup> .x/ � 0 8x 2 I vede na klesající funkci. 

- Definice 18.2 — lokálních a globálních extrém˚u. 1. Řekneme, že f má v bodě x0 2 D.f / _lokální maximum_ (resp. _minimum_ ), jestliže existuje O.x0/ � D.f / takové, že pro každé x 2 O.x0/ platí f .x/ � f .x0/ (resp. f .x/ � f .x0/). 

2. Lokální maximum (resp. minimum) se nazývá _ostré_ , jestliže existuje O<sup>�</sup> .x0/ � D.f / takové, že pro každé x 2 O<sup>�</sup> .x0/ platí f .x/ < f .x0/ (resp. f .x/ > f .x0/). 

3. Lokální maxima a minima souhrnně nazýváme _lokální extrémy_ , případně _ostré lokální extrémy_ . 

4. Řekneme, že funkce f má na množině M � D.f / v bodě x0 2 M _globální (absolutní) maximum_ (resp. _minimum_ ), jestliže pro každé x 2 M platí f .x/ � f .x0/ (resp. f .x/ � f .x0/). 

18 Pr˚ubˇeh funkce 

75 

5. Globální maximum (resp. minimum) se nazývá _ostré_ , jestliže příslušné nerovnosti jsou ostré pro x ¤ x0. 

6. Globální maxima a minima souhrnně nazýváme _globální extrémy_ . 

Poznámka 18.3. Okolí bodu x0 z předchozí definice leží celé v D.f /. To znamená, že je-li x0 krajním bodem D.f /, o lokálním extrému v tomto bodě neuvažujeme, např. funkce f .x/ D<sup>~~p~~</sup> x v bodě 0 lokální extrém nemá. V některé literatuře je podmínka oslabena tak, že se v definici požaduje O.x0/ \ D.f /. V tomto případě by f .x/ D<sup>~~p~~</sup> x v bodě 0 měla lokální minimum. 

Bezprostředním důsledkem 2. Weierstrassovy věty je následující tvrzení: 

■ Vˇeta 18.4 — o globálních extrémech. _Funkce_ f _spojitá na_ ha; bi _zde nabývá svých globálních extrémů, a to buď v bodech lokálního extrému, nebo v krajních bodech_ a; b _._ 

■ Vˇeta 18.5 — Fermatova<sup>7</sup> vˇeta o nutné podmínce pro lokální extrém. _Má-li funkce v bodě_ x0 2 D.f / _lokální extrém a existuje_ f<sup>0</sup> .x0/ _, pak_ f<sup>0</sup> .x0/ D 0 _._ 

_Důkaz._ Nechť f má v bodě x0 lokální extrém (tj. na nějakém okolí bodu x0 platí f .x/ � f .x0/ nebo f .x/ � f .x0/) a má v tomto bodě derivaci. Připusťme, že 



<!-- Start of picture text -->
f .x/ � f .x0/<br>f 0 .x0/ D lim > 0:<br>x!0 x � x0<br><!-- End of picture text -->

Pak existuje okolí O<sup>�</sup> .x0/, na kterém je 



<!-- Start of picture text -->
f .x/ � f .x0/<br>> 0:<br>x � x0<br><!-- End of picture text -->

Pro x z tohoto okolí ležící nalevo od x0 je x � x0 < 0, tudíž musí být f .x/ � f .x0/ < 0, neboli f .x/ < f .x0/. Pro x ležící napravo od x0 je naopak x � x0 > 0, takže musí být f .x/ � f .x0/ > 0, tj. f .x/ > f .x0/. To je spor s tím, že v bodě x0 je lokální extrém. 

Analogicky bychom vyloučili případ f<sup>0</sup> .x0/ < 0. 

Poznámka 18.6. a) Body, v nichž f<sup>0</sup> .x/ D 0 nazýváme _stacionární body funkce_ f . Stacionární bod může, ale nemusí být bodem lokálního extrému. Např. f .x/ D x<sup>3</sup> , f<sup>0</sup> .0/ D 0, f<sup>0</sup> .x/ D 3x<sup>2</sup> > 0 pro x ¤ 0. Tedy podle věty 18.1 je f rostoucí na R. 

b) Funkce může mít lokální extrém buď ve stacionárním bodě, nebo v bodě, kde neexistuje vlastní ani nevlastní derivace. Např. f .x/ D jxj má v bodě x0 D 0 ostré lokální minimum, ale derivace v tomto bodě neexistuje. 

■ Vˇeta 18.7. _Nechť_ f _je spojitá v bodě_ x0 2 D.f / _. Existuje-li_ O<sup>��</sup> .x0/ _, v němž je_ f _neklesající (resp. nerostoucí, resp. rostoucí, resp. klesající) a_ O<sup>�C</sup> .x0/ _, v němž je_ f _nerostoucí (resp. neklesající, resp. klesající, resp. rostoucí), pak má_ f _v bodě_ x0 _lokální maximum (resp. lokální minimum, resp. ostré lokální maximum, resp. ostré lokální minimum)._ 

_Důkaz._ Nechť f je v O<sup>��</sup> .x0/ neklesající a v O<sup>�C</sup> .x0/ nerostoucí. Protože f je spojitá v bodě x0, existují konečné limity limx!x0� f .x/ D limx!x0C f .x/ D f .x0/. Není těžké ověřit, že platí limx!x0� f .x/ D supff .x/ W x 2 O<sup>��</sup> .x0/g a limx!x0C f .x/ D supff .x/ W x 2 O<sup>�C</sup> .x0/g (existence limity implikuje ohraničenost funkce na nějakém okolí, a tedy existenci suprema), a tedy f .x0/ D supff .x/ W x 2 O<sup>��</sup> .x0/ [ O<sup>�C</sup> .x0/g. To znamená, že f .x/ � f .x0/ pro všechna x 2 O<sup>��</sup> .x0/ [ O<sup>�C</sup> .x0/ [ fx0g, tj. v bodě x0 je lokální maximum. 

Je-li f v O<sup>��</sup> .x0/ rostoucí a v O<sup>�C</sup> .x0/ klesající, pak pro libovolný bod x 2 O<sup>��</sup> .x0/ platí x1 2 .x; x0/ � O<sup>��</sup> .x0/ ) f .x/ < f .x1/ � f .x0/ D supff .x/ W x 2 O<sup>��</sup> .x0/g. Podobně by se ukázalo, že pro x 2 O<sup>�C</sup> .x0/ je f .x0/ > f .x/. Celkově tedy, v x0 je ostré lokální maximum. 

Analogicky ukážeme platnost tvrzení v ostatních případech. 

> 7Pierre de Fermat 1601–1665, Francouz 

Kapitola 2. Diferenciální poˇcet 

76 

Poznámka 18.8. a) Obrácená věta neplatí. Má-li funkce f v bodě x0 lokální extrém, nemusí být v žádném ryzím jednostranném okolí monotónní. 

b) Předpoklad o spojitosti f v bodě x0 je podstatný. 

Bezprostředním důsledkem vět 18.1 a 18:7 je: 

> ■ Vˇeta 18.9 — 1. vˇeta o postaˇcujících podmínkách pro lokální extrém. _Nechť funkce_ f _je spojitá v bodě_ x0 2 D.f / _a existují_ O<sup>��</sup> .x0/ _a_ O<sup>�C</sup> .x0/ _taková, že_ f _má na těchto okolích vlastní nebo nevlastní derivaci_ f<sup>0</sup> _, přičemž_ f<sup>0</sup> .x/ > 0 _(resp._ f<sup>0</sup> .x/ < 0 _)_ 8x 2 O<sup>��</sup> .x0/ _a_ f<sup>0</sup> .x/ < 0 _(resp._ f<sup>0</sup> .x/ > 0 _)_ 8x 2 O<sup>�C</sup> .x0/ _. Pak má_ f _v bodě_ x0 _ostré lokální maximum (resp. minimum)._ 

■ Vˇeta 18.10 — 2. vˇeta o postaˇcujících podmínkách pro lokální extrém. _Nechť funkce_ f _má v bodě_ x0 _vlastní nebo nevlastní druhou derivaci, přičemž platí_ f<sup>0</sup> .x0/ D 0 _. Je-li_ f<sup>00</sup> .x0/ < 0 _, pak má_ f _v bodě_ x0 _ostré lokální maximum, je-li_ f<sup>00</sup> .x0/ > 0 _, pak má_ f _v bodě_ x0 _ostré lokální minimum._ 

_Důkaz._ Nechť 



<!-- Start of picture text -->
f 0 .x/ � f 0 .x0/<br>f 00 .x0/ D lim > 0:<br>x!x0 x � x0<br><!-- End of picture text -->

To znamená, že existuje ryzí okolí O<sup>�</sup> .x0/, na kterém je 



<!-- Start of picture text -->
f 0 .x/ � f 0 .x0/ D f 0.x/ < 0:<br>x � x0 x � x0<br><!-- End of picture text -->

Tato nerovnost dává f<sup>0</sup> .x/ < 0 pro x 2 O<sup>��</sup> .x0/ a f<sup>0</sup> .x/ > 0 pro x 2 O<sup>�C</sup> .x0/. Funkce tedy má podle věty 18.9 v bodě x0 ostré lokální minimum. 

Pˇríklad 18.11. Ze čtvercového plechu o straně délky 2a (a > 0) máme zhotovit krabici bez víka tak, že v rozích vyřízneme stejně velké čtverce. Jak velké musí být strany těchto odříznutých čtverců, aby krabice měla maximální objem? 

_Řešení._ Označíme-li x stranu vyříznutých čtverců, objem krabice bude V.x/ D 4.a �x/<sup>2</sup> x, kde x 2 .0; a/. Pak V<sup>0</sup> D �8.a � x/x C 4.a � x/<sup>2</sup> D 4.a � x/.�2x C a � x/ D 4.a � x/.a � 3x/. Z rovnice V<sup>0</sup> .x/ D 0 dostaneme dva stacionární body x1 D a a x2 D a=3. Kořen x1 nevyhovuje, protože krabice by měla podstavu 2a � 2a D 0. Stačí proto vyšetřit případ x2 D<sup>a</sup> =3. Protože V<sup>00</sup> .x/ D �4.a � 3x/ � 12.a � x/ D 24x � 16a, V<sup>00</sup> .x2/ D 8a � 16a D �8a < 0, jde o lokální (a zároveň globální) maximum. Je tedy Vmax D 4.2a=3/<sup>2</sup> a=3 D 16a<sup>3</sup> =27 a strana vyříznutého čtverce je a=3. 

> ■ Vˇeta 18.12 — 3. vˇeta o postaˇcujících podmínkách pro lokální extrém. _Nechť funkce_ f _má na_ O.x0/ _spojitou_ n _-tou derivaci (_ n � 3 _) a_ 



<!-- Start of picture text -->
f 0 .x0/ D f 00 .x0/ D ���D f .n�1/ .x0/ D 0; f .n/ .x0/ ¤ 0:<br><!-- End of picture text -->

_Pak, je-li_ n _liché, nenastane v_ x0 _lokální extrém (_ x0 _je inflexní bod, viz definice 18.15 níže). Je-li_ n _sudé, nastane v_ x0 _ostré lokální maximum při_ f<sup>.n/</sup> .x0/ < 0 _a ostré lokální minimum při_ f<sup>.n/</sup> .x0/ > 0 _._ 

_Důkaz._ Podle Taylorovy věty na uvažovaném okolí O.x0/ platí 



<!-- Start of picture text -->
f .x/ D f .x0/ C f .n/.x0 C #.x � x0// .x � x0/ n ;<br>nŠ<br><!-- End of picture text -->

kde # 2 .0; 1/ závisí na x. Protože funkce f<sup>.n/</sup> je spojitá na O.x0/, existuje určité okolí O.x<sup>e</sup> 0/, na kterém je sgn f<sup>.n/</sup> .x/ D sgn f<sup>.n/</sup> .x0/ (sgn značí znaménko výrazu). Zvolíme-li x 2 O.x<sup>e</sup> 0/, pak také x0 C #.x � x0/ 2 O.x<sup>e</sup> 0/ pro libovolné � 2 .0; 1/, a tedy sgn f<sup>.n/</sup> .x0 C #.x � x0// D sgn f .x0/. Odtud sgn�f .x/ � f .x0/� D sgn f<sup>.n/</sup> .x0/.x � x0/<sup>n</sup> pro každé x 2 O.x<sup>e</sup> 0/. 

Je-li n liché, pak hodnota .x � x0/<sup>n</sup> mění znaménko (je záporná pro x < x0 a kladná pro x > x0). Důsledkem toho také změní znaménko výraz f .x/ � f .x0/ (tj. f .x/ > f .x0/ pro x nalevo od x0 a f .x0/ > f .x/ pro x napravo od x0, nebo naopak), a tudíž v bodě x0 nenastává lokální extrém. 

18 Pr˚ubˇeh funkce 

77 

Je-li n sudé, pak hodnota .x �x0/<sup>n</sup> nemění znaménko, přesněji, je kladná pro všechna x 2 O.x<sup>e</sup> 0/nfx0g. To znamená, že pro f<sup>.n/</sup> .x0/ < 0 je f .x/ � f .x0/ < 0 pro všechna x 2 O.x<sup>e</sup> 0/ n fx0g, tj. f .x/ < f .x0/, takže v bodě x0 je ostré lokální maximum. Pro f<sup>.n/</sup> .x0/ < 0 naopak dostaneme f .x/ > f .x0/ pro x 2 O.x<sup>e</sup> 0/ n fx0g, tj. v bodě x0 je ostré lokální minimum. 

■ Vˇeta 18.13. _Nechť funkce_ f _má na intervalu_ I _derivaci_ f<sup>0</sup> _. Pak funkce_ f _je konvexní (resp. konkávní, resp. ryze konvexní, resp. ryze konkávní) na intervalu_ I , f<sup>0</sup> _je na_ I _neklesající (resp. nerostoucí, resp. rostoucí, resp. klesající)._ 

_Důkaz._ Ukažme nejprve, že když f je na intervalu I konvexní a má zde derivaci, pak platí f .x0/ C f<sup>0</sup> .x0/.x � x0/ � f .x/, kde x0 a x jsou libovolné dva různé body v intervalu I . Tato podmínka říká, že funkční hodnota f .x/ je vždy nad tečnou v libovolném bodě (nebo na ní). Konvexnost na I znamená, že pro libovolná dvě x1; x3 2 I a libovolné � 2 h0; 1i platí f .x1.1 � �/ C x3�/ � .1 � �/f .x1/ C �f .x3/, viz definice 8.19. Je-li x1 < x3 a x2 je libovolný bod mezi x1 a x3 (tj. x2 D .1 � �/x1 C �x3 pro nějaké � 2 .0; 1/), pak lze nerovnost napsat ve tvaru 



<!-- Start of picture text -->
f .x2/ � f .x1/ C f .x3/ � f .x1/ .x2 � x1/<br>x3 � x1<br><!-- End of picture text -->

(tento tvar dostaneme ihned, pokud si vyjádříme hodnotu parametru � ze vztahu x2 D .1 � �/x1 C �x3 a dosadíme do první nerovnosti). Odečtením f .x1/ od obou stran nerovnosti a vydělením členem x2 � x1 dostaneme 



<!-- Start of picture text -->
f .x2/ � f .x1/ � f .x3/ � f .x1/ ; x1 < x2 < x3: (?)<br>x2 � x1 x3 � x1<br><!-- End of picture text -->

Bude se nám hodit ještě jedna nerovnost, která je rovnosti (?) ekvivalentní, a to 



<!-- Start of picture text -->
f .x2/ � f .x1/ � f .x3/ � f .x2/ ; x1 < x2 < x3 (??)<br>x2 � x1 x3 � x2<br><!-- End of picture text -->

(to že jsou obě nerovnosti ekvivalentní lze ověřit velmi snadno tak, že nerovnost (?) vynásobíme faktorem .x2 � x1/.x3 � x1/, nerovnost (??) faktorem .x2 � x1/.x3 � x2/ a upravíme). 

Nechť nyní x0 a x jsou libovolné různé body intervalu I a nechť nejprve x0 < x. Pak pro libovolné t 2 .x0; x/ nerovnost (?) dává 



<!-- Start of picture text -->
f .t/ � f .x0/<br>� f .x/ � f .x0/ :<br>t � x0 x � x0<br><!-- End of picture text -->

Limitním přechodem t ! x0C dostaneme f<sup>0</sup> .x0/ �<sup><u>f.x</u></sup> x<sup><u>/�</u></sup> �<sup><u>f</u></sup> x0<sup><u>.x0/</u></sup> (limita existuje díky předpokladu existence derivace f<sup>0</sup> na I – ta se v každém bodě rovná jednostranným derivacím), tj. f .x0/ C f<sup>0</sup> .x0/.x � x0/ � f .x/. Je-li naopak x < x0 a t 2 .x; x0/, pak máme 



<!-- Start of picture text -->
f .x0/ � f .x/ � f .x0/ � f .t/<br>x0 � x x0 � t<br><!-- End of picture text -->

a limitním přechodem t ! x0� dostaneme f .x/ � f .x0/ C f<sup>0</sup> .x0/.x � x0/. 

Dále ukažme, že když f je navíc ryze konvexní na I , pak pro libovolné dva různé vnitřní body x0 a x intervalu platí f .x0/ C f<sup>0</sup> .x0/.x � x0/ < f .x/. Protože ryze konvexní funkce je zároveň konvexní, podle již dokázaného je f .x0/ C f<sup>0</sup> .x0/.x � x0/ � f .x/. Připusťme, že rovnost nastane, tj. existují body x1; x3 2 I , x1 < x3 takové, že f .x3/ D f .x1/ C f<sup>0</sup> .x1/.x3 � x1/. Ryzí konvexnost na I je (analogicky nerovnosti (?)) ekvivalentní nerovnosti 



<!-- Start of picture text -->
f .x2/ � f .x1/ < f .x3/ � f .x1/ ;<br>x2 � x1 x3 � x1<br><!-- End of picture text -->

pro libovolnou trojici bodů x1; x2; x3 takovou, že x1 < x2 < x3, přičemž dosazením f .x3/ D f .x1/ C f<sup>0</sup> .x1/.x3 � x1/ dostaneme 



<!-- Start of picture text -->
f .x2/ � f .x1/ < f .x1/ C f 0.x1/.x3 � x1/ � f .x1/ D f 0 .x1/:<br>x2 � x1 x3 � x1<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet 

78 

Odtud f .x2/ < f .x1/ C f<sup>0</sup> .x1/.x2 � x1/, což je spor s již dokázaným (při přeznačení x WD x2, x0 WD x1). 

Pro konkávnost (resp. ryzí konkávnost) funkce bychom analogicky ukázali nerovnost f .x0/ C f<sup>0</sup> .x0/.x � x0/ � f .x/ (resp. f .x0/ C f<sup>0</sup> .x0/.x � x0/ > f .x/). 

Nyní již můžeme dokázat uvedenou ekvivalenci ve větě. 

„)“ Nechť x1; x2 2 I , x1 < x2, jsou libovolné body a f je konvexní na I . Pak podle prvního odstavce je f .x2/ � f .x1/ C f<sup>0</sup> .x1/.x2 � x1/ a zároveň f .x1/ � f .x2/ C f<sup>0</sup> .x2/.x1 � x2/. Odtud 



<!-- Start of picture text -->
f 0 .x1/ � f .x2/ � f .x1/ � f 0 .x2/;<br>x2 � x1<br><!-- End of picture text -->

tj. f<sup>0</sup> je neklesající na I . 

„(“ Sporem. Nechť f<sup>0</sup> je neklesající na I a připusťme, že f není konvexní. Pak, vzhledem k nerovnosti (??), existují x1; x2; x3 2 I , x1 < x2 < x3, taková, že 



<!-- Start of picture text -->
f .x2/ � f .x1/ > f .x3/ � f .x2/ :<br>x2 � x1 x3 � x2<br><!-- End of picture text -->

Podle Lagrangeovy věty o střední hodnotě (viz věta 16.3) existují �1 2 .x1; x2/ a �2 2 .x2; x3/ taková, že 



<!-- Start of picture text -->
f .x2/ � f .x1/ f .x3/ � f .x2/<br>D f 0 .�1/ a D f 0 .�2/:<br>x2 � x1 x3 � x2<br><!-- End of picture text -->

Máme tedy f<sup>0</sup> .�1/ > f<sup>0</sup> .�2/ při �1 < �2. To je spor s tím, že f<sup>0</sup> je na I neklesající, a tedy f musí být na I konvexní. 

Analogicky bychom ukázali případ konkávnosti funkce a s využitím druhého odstavce důkazu také případ ryzí konvexnosti a ryzí konkávnosti. 

■ D˚usledek 18.14. _Nechť funkce_ f _má na intervalu_ I _spojitou první derivaci a vlastní nebo nevlastní druhou derivaci. Pak_ f _je ryze konvexní (resp. konkávní) na_ I , f<sup>00</sup> .x/ � 0 _(resp._ f<sup>00</sup> .x/ � 0 _)_ 8x 2 I _, přičemž_ f<sup>00</sup> _není nulová na žádném podintervalu intervalu_ I _._ 

Definice 18.15 — inflexního bodu. Nechť funkce f je spojitá v bodě x0 2 D.f / a nechť existuje vlastní nebo nevlastní derivace f<sup>0</sup> .x0/. Řekneme, že x0 je _inflexním bodem funkce_ f , jestliže existují O<sup>��</sup> .x0/ a O<sup>�C</sup> .x0/ taková, že f je ryze konvexní na O<sup>��</sup> .x0/ a ryze konkávní na O<sup>�C</sup> .x0/, nebo naopak f je ryze konvexní na O<sup>�C</sup> .x0/ a ryze konkávní na O<sup>��</sup> .x0/. 

Poznámka 18.16. a) Je-li x0 inflexní bod funkce f a f<sup>0</sup> je spojitá v bodě x0, pak f<sup>0</sup> má v bodě x0 ostrý lokální extrém. 

b) Je-li x0 inflexní bod funkce f a existuje vlastní nebo nevlastní druhá derivace f<sup>00</sup> .x0/, pak f<sup>00</sup> .x0/ D 0. Opačné tvrzení neplatí. Z f<sup>00</sup> .x0/ D 0 neplyne, že by x0 byl inflexní bod f . Např. f .x/ D x<sup>4</sup> , f<sup>00</sup> .x/ D 12x<sup>2</sup> , f<sup>00</sup> .0/ D 0, ale v bodě x0 D 0 není inflexní bod. 

Definice 18.17 — asymptot. 1. Řekneme, že přímka p W x D x0 je _asymptotou bez směrnice funkce_ f , jestliže f má v x0 alespoň jednu nevlastní jednostrannou limitu. 

2. Řekneme, že přímka p W y D kx C q je _asymptotou se směrnicí funkce_ f , jestliže f je definována v okolí 1 (resp. �1) a platí limx!1.kx C q � f .x// D 0 (resp. limx!�1.kx C q � f .x// D 0). 

Libovolná funkce může mít nejvýše dvě asymptoty se směrnicí, muže však mít libovolný počet asymptot bez směrnice. 

■ Vˇeta 18.18. _Přímka_ y D kx C q _je asymptotou se směrnicí funkce_ f , 



<!-- Start of picture text -->
f .x/<br>lim D k; lim<br>x!1 x x!1 .f .x/ � kx/ D q<br><!-- End of picture text -->

18 Pr˚ubˇeh funkce 

79 

##### _nebo_ 



<!-- Start of picture text -->
f .x/<br>x!�1lim x D k; x!�1lim .f .x/ � kx/ D q:<br><!-- End of picture text -->



<!-- Start of picture text -->
Důkaz. „)“ Pokud limx!1.kx C q � f .x// D 0 pak také<br><!-- End of picture text -->



<!-- Start of picture text -->
kx C q � f .x/ f .x/ f .x/<br>lim D 0; tedy 0 D k � lim ; tj. lim D k:<br>x!1 x x!1 x x!1 x<br><!-- End of picture text -->

Dále z limx!1.kxCq�f .x// D 0 plyne 0 D limx!1.kx�f .x//Cq, a tedy limx!1.f .x/�kx/ D q. Pokud limx!�1.kx C q � f .x// D 0, postupuje se analogicky. 

„(“ Jestliže limx!1.f .x/�kx/ D q, pak limx!1.kxCq�f .x// D limx!1.kx�f .x//Cq D �q C q D 0. 

##### Postup pˇri vyšetˇrování pr˚ubˇehu funkce 

1. Určíme D.f /, nulové body (intervaly kladnosti a zápornosti f ), případně sudost a lichost, periodičnost, spojitost a poruchy spojitosti. 

2. Vypočítáme f<sup>0</sup> , určíme nulové body f<sup>0</sup> (stacionární body) a intervaly kladnosti a zápornosti f<sup>0</sup> , body, v nichž f<sup>0</sup> neexistuje (lokální extrémy). 

3. Vypočítáme f<sup>00</sup> , určíme nulové body f<sup>00</sup> (podezření na inflexní bod) a intervaly kladnosti a zápornosti f<sup>00</sup> (konvexnost a konkávnost). 

4. Vypočítáme příslušné jednostranné limity v „hraničních bodech“ D.f / (tj. najdeme všechny asymptoty bez směrnice). Najdeme obě asymptoty se směrnicí (pokud existují). 

5. Vypočítáme funkční hodnoty ve význačných bodech (stacionárních, inflexních), případně v několika dalších bodech. V inflexních bodech muže být užitečné vypočítat hodnotu derivace. 

6. Na základě informací z předchozích pěti bodů načrtneme graf. 

Pˇríklad 18.19. Vyšetřete průběh funkce f .x/ D x<sup>2</sup> <u>2xC1</u><sup>.</sup> 

_Řešení._ Funkce je lichá, má nulový bod x0 D 0 (na R<sup>C</sup> je kladná, na R<sup>�</sup> záporná). Platí 



<!-- Start of picture text -->
x 2 � 1<br>f 0 .x/ D �2<br>.x 2 C 1/ 2 :<br><!-- End of picture text -->

Z rovnice f<sup>0</sup> .x/ D 0 pak dostáváme stacionární body s1;2 D ˙1, přičemž není těžké ověřit, že v bodě s1 D 1 je ostré lokální maximum a v bodě s2 D �1 je ostré lokální minimum (viz věta 18.9). Druhá derivace pak je 



<!-- Start of picture text -->
f 00 .x/ D 4x.x2 � 3/<br>.x 2 C 1/ 3 ;<br><!-- End of picture text -->

přičemž z rovnice f<sup>00</sup> .x/ D 0 (s přihlédnutím ke znaménku f<sup>00</sup> na příslušných intervalech) dostaneme 3 inflexní body x1 D 0, x2;3 D ˙ ~~p~~ 3. Protože 



<!-- Start of picture text -->
f .x/ 2 2x<br>k D lim D lim lim �f .x/ � kx� D lim<br>x!˙1 x x!˙1 x 2 C 1 D 0; x!˙1 x!˙1 x 2 C 1 D 0;<br><!-- End of picture text -->

přímka y D 0 (osa x) je jedinou asymptotou se směrnicí (asymptoty bez směrnice funkce nemá). Získané informace jsou vyznačeny v grafu funkce, viz obrázek 18.1. 

#### Pˇríklady k procviˇcení 

18.1. Nalezněte lokální extrémy následujících funkcí: 



<!-- Start of picture text -->
a) f .x/ D x � p x � 1; b) f .x/ D 1 C x2 c) f .x/ D x 5 C x 3 C 1<br>1 � x 2 ;<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet 

80 



<!-- Start of picture text -->
y<br>1<br>0 . 5<br>− √ 3 x<br>− 4 − 3 − 2 − 1 1 √ 3 2 3 4<br>− 0 . 5<br>− 1<br>Obrázek 18.1: Graf funkce 2x<br>x 2 C1<br><!-- End of picture text -->

18.2. Nalezněte globální (absolutní) extrémy následujících funkcí na intervalu I : 



<!-- Start of picture text -->
a) f .x/ D sin x C sin 2 x C 1; I D h0; �i ; b) f .x/ D q 3 .x 2 � x/ 2 ; I D .�3; 2/:<br><!-- End of picture text -->

18.3. Určete intervaly, na kterých je funkce 



<!-- Start of picture text -->
f .x/ D x C jsin 2xj<br><!-- End of picture text -->

rostoucí, resp. klesající. 

18.4. Hodláme koupit obdélníkovou parcelu o rozloze 200 m<sup>2</sup> , jejíž jedna strana bude ohraničena již hotovou zdí, zatímco ze zbývajících tří stran bude nutné parcelu oplotit. Ukažte, že obdélník lze zvolit tak, aby plot měl minimální délku, a najděte délky příslušných stran. 

18.5. Kouli o poloměru R opište rotační kužel s nejmenším objemem. Jaké jsou jeho rozměry? 

18.6. Vyšetřete průběh následujících funkcí: 



<!-- Start of picture text -->
a) f .x/ D x 2 2x� 1 C x; b) f .x/ D p 3 x 3 C x 2 ;<br>c) f .x/ D e �2x sin 3x; d) f .x/ D cos x � ln cos x:<br><!-- End of picture text -->

_Výsledky._ 18.1. a) xmin D<sup>5</sup> =4, f .xmin/ D<sup>3</sup> =4, b) xmin D 0, f .xmin/ D 1, c) nemá lokální extrémy. 18.2. a) xmax D �=2, f .xmax/ D 3, xmin<sup>1D0, x</sup> min<sup>2D�, f .x</sup> min<sup>1/D0Df .x</sup> min<sup>2/, b) x</sup> min<sup>1D0, x</sup> min<sup>2D1,</sup> f .xmin<sup>1/ D f .x</sup> min<sup>2/ D 0. 18.2. Na .k�=2; k�=2C�=3/, k2 Z, je rostoucí, na .k�=2C�=3; k�=2C�=2/,</sup> k 2 Z, je klesající. 18.4. Kratší strana 10 m, delší strana 20 m. 18.5. r D ~~p~~ 2R, h D 4R, Vmin D<sup><u>8</u></sup> 3<sup>�R3.</sup> 18.6. Správnost závěrů ověřte softwarově (např. Wolfram Alpha, Geogebra, Desmos). 

## Kapitola 3 

# Integrální poˇcet 

### 19 Primitivní funkce 

Definice 19.1 — primitivní funkce. Buď I interval (omezený nebo neomezený) a f; F funkce definované na I . Jestliže 8x 2 I je F<sup>0</sup> .x/ D f .x/, pak F se nazývá _primitivní funkce k funkci_ f _na intervalu_ I . 

■ Lemma 19.2. _Funkce_ f _je na intervalu_ I _konstantní_ , f<sup>0</sup> .x/ D 0 8x 2 I _._ 

_Důkaz._ „)“ Je-li f .x/ D c 2 R 8x 2 I , pak f<sup>0</sup> .x/ D 0 8x 2 I . 

„(“ Nechť f<sup>0</sup> .x/ D 0 8x 2 I . Pak pro libovolná x1; x2 2 I , x1 < x2, existuje podle Lagrangeovy věty o střední hodnotě � 2 .x1; x2/ takové, že f .x2/ � f .x1/ D f<sup>0</sup> .�/.x2 � x1/ D 0.x2 � x1/ D 0. Odtud f .x1/ D f .x2/ a tedy f musí být konstantní, protože hodnoty x1; x2 byly libovolné. 

- Vˇeta 19.3 — o množinˇe všech primitivních funkcí. a) _Je-li_ F _primitivní funkce k funkci_ f _na intervalu_ I _, pak také_ F C c _, kde_ c 2 R _je libovolná konstanta, je primitivní funkce k_ f _na_ I _._ 

- b) _Jsou-li_ F _a_ G _primitivní funkce k funkci_ f _na_ I _, pak existuje konstanta_ c _taková, že_ F.x/ D G.x/ C c 8x 2 I _._ 

- c) _Je-li_ F _funkce primitivní k_ f _na_ I _, pak_ fF C c W c 2 Rg _je množina všech funkcí primitivních k funkci_ f _na I._ 

_Důkaz._ ad a) .F.x/ C c/<sup>0</sup> D F<sup>0</sup> .x/ C c<sup>0</sup> D F<sup>0</sup> .x/ C 0 D f .x/ na I . 

ad b) Z předpokladu plyne .F.x/ � G.x//<sup>0</sup> D F<sup>0</sup> .x/ � G<sup>0</sup> .x/ D f .x/ � f .x/ D 0 na I , a tedy podle Lemmatu 19.2 je F.x/ � G.x/ D c, neboli F.x/ D G.x/ C c. 

Tvrzení c) je důsledkem prvních dvou. 

■ Vˇeta 19.4 — o existenci primitivní funkce. _Ke každé funkci spojité na intervalu_ I _existuje primitivní funkce._ 

Důkaz tvrzení využívá poznatků z teorie určitého integrálu, věta tedy bude dokázána později, viz strana 103. 

Definice 19.5. Množina všech primitivních funkcí se nazývá _neurčitý integrál_ a značí se R f .x/ dx. 

##### Základní integrály 

1. 0 dx D c na R. Z 

2. Pro ˛ ¤ �1 je Z x<sup>˛</sup> dx D ˛<sup>x</sup> C<sup>˛C</sup> 1<sup>1C c</sup> na R, je-li ˛ 2 N0; na každém podintervalu R n f0g, je-li �˛ 2 N; na R<sup>C</sup> , je-li ˛ 2 R n Z. 

Kapitola 3. Integrální poˇcet 

82 

1 3. Z x<sup>dxD ln jxj C c</sup> na každém podintervalu R n f0g. 4. e<sup>x</sup> dx D e<sup>x</sup> Cc na R. Z 5. Pro a > 0, a ¤ 1 je Z a<sup>x</sup> dx D ln<sup>ax</sup> a<sup>C c</sup> na R. 6. R sin x dx D � cos x C c na R. 7. R cos x dx D sin x C c na R. 1 8. na každém �.2k � 1/<sup><u>�</u></sup> 2<sup>; .2k C 1/</sup><sup><u>�</u></sup> 2 �, k 2 Z. Z cos<sup>2</sup> x<sup>dxD tg x C c</sup> 1 9. dx D � cotg x C c na každém .k�; .k C 1/�/, k 2 Z. Z sin<sup>2</sup> x 1 10. na .�1; 1/. Z ~~p~~ 1 � x<sup>2dxD arcsin x C c1D �arccos x C c2</sup> 1 11. dx D ln ~~p~~ x<sup>2</sup> � 1 na každém podintervalu R n h�1; 1i (D argcosh x C c Z ~~p~~ x<sup>2</sup> � 1 ˇˇˇx C <u>ˇˇˇ C c</u> na .1; 1/). 1 12. dx D ln.x C ~~p~~ x<sup>2</sup> C 1/ C c D argsinh x C c na R. Z ~~p~~ x<sup>2</sup> C 1 1 13. Z x<sup>2</sup> C 1<sup>dxD arctg x C c1D �arccotg x C c2</sup> na R. 1 1 C x 14. Z 1 � x<sup>2dxD</sup> 2<sup>1ln</sup> ˇˇˇˇ 1 � x ˇˇˇˇ C c na každém podintervalu R n f�1; 1g (D argtgh x C c1 na .�1; 1/, D argcotgh x C c1 na každém podintervalu R n h�1; 1i). 15. sinh x dx D cosh x C c na R. Z 16. cosh x dx D sinh x C c na R. Z 1 17. dx D � cotgh x C c na každém podintervalu R n f0g. Z sinh<sup>2</sup> x 1 18. dx D tgh x C c na R. Z cosh<sup>2</sup> x 19. na každém intervalu, kde je f<sup>0</sup> =f spojitá. Z <u>ff .x/0.x/</u><sup>dxD ln jf .x/j C c</sup> 

Všechny výše uvedené integrály by se ověřily zpětným derivováním primitivní funkce. 

■ Vˇeta 19.6 — základní vlastnosti. _Existují-li na intervalu_ I _neurčité integrály funkcí_ f; g _, pak na_ I _existují také neurčité integrály z funkce_ 

a) kf _, kde_ k 2 R _je libovolná konstanta, a platí_ 



<!-- Start of picture text -->
kf .x/ dx D k f .x/ dx;<br>Z Z<br><!-- End of picture text -->



<!-- Start of picture text -->
b) f C g  a platí<br>Œf .x/ C g.x/� dx D f .x/ dx C g.x/ dx:<br>Z Z Z<br><!-- End of picture text -->

_Důkaz._ Plyne ihned z pravidel pro derivovaní a definice primitivní funkce. 

Poznámka 19.7. a) Z předchozí věty plyne, že integrace je lineární operací. b) Pozor, R f .x/g.x/ dx ¤ R f .x/ dx � R g.x/ dx! Stejně tak, integrál podílu není podíl integrálů. 



<!-- Start of picture text -->
■ Vˇeta 19.8. Nechť na intervalu  I platí R f .x/ dx D F.x/ C c . Pak<br><!-- End of picture text -->



<!-- Start of picture text -->
Z f .ax C b/ dx D a 1 F.ax C b/ C c na J D fx 2 R W ax C b 2 I g:<br>Důkaz. Platí � a1 F.ax C b/ �0 D a1 F 0.ax C b/.ax C b/0 D F 0.ax C b/ D f .ax C b/.<br><!-- End of picture text -->

19 Primitivní funkce 

83 

Pˇríklad 19.9. Vypočítejte neurčitý integrál R sin<sup>2</sup> x dx. _Řešení._ 



<!-- Start of picture text -->
sin 2 x dx D dx D 1 .1 � cos 2x/ dx D 1 x � 1 C c:<br>Z Z 1 � cos2  2x 2 Z 2 � 2 sin 2x �<br><!-- End of picture text -->

■ Vˇeta 19.10 — integrace po ˇcástech. _Nechť_ u; v _jsou funkce, které mají na intervalu_ I _derivaci. Existuje-li na_ I _primitivní funkce k jedné z funkcí_ u<sup>0</sup> v _,_ uv<sup>0</sup> _, pak existuje také ke druhé z nich a platí_ 



<!-- Start of picture text -->
u 0 .x/v.x/ dx D u.x/v.x/ � u.x/v 0 .x/ dx:<br>Z Z<br><!-- End of picture text -->

_Důkaz._ Protože u; v mají derivaci na I , má zde také derivaci uv, přičemž platí .uv/<sup>0</sup> .x/ D u<sup>0</sup> .x/v.x/ C u.x/v<sup>0</sup> .x/ (viz věta 14.5). Integrací tohoto vztahu dostaneme R .uv/<sup>0</sup> .x/ dx D u.x/v.x/ C c D R .u<sup>0</sup> .x/v.x/ C u.x/v<sup>0</sup> .x// dx na I , tj. integrál R .u<sup>0</sup> .x/v.x/ C u.x/v<sup>0</sup> .x// dx na I existuje. Pokud existuje primitivní funkce k alespoň jedné z funkcí u<sup>0</sup> v, uv<sup>0</sup> , nechť je to např. funkce uv<sup>0</sup> , pak podle věty 19.6 existuje integrál z rozdílu R �u<sup>0</sup> .x/v.x/ C u.x/v<sup>0</sup> .x// � u.x/v<sup>0</sup> .x/� dx D R u<sup>0</sup> .x/v.x/ dx, což je druhý integrál. Platí tedy uv C c D R u<sup>0</sup> v dx C R uv<sup>0</sup> dx. Odtud již dostáváme vzorec věty. 



<!-- Start of picture text -->
Pˇríklad 19.11. Vypočítejte neurčitý integrál arctg x dx:<br>Z<br><!-- End of picture text -->

_Řešení._ Položíme-li u<sup>0</sup> .x/ D 1 a v.x/ D arctg x, pak u.x/ D x a v<sup>0</sup> .x/ D 1=.1 C x<sup>2</sup> /. Podle věty 19.10 platí 



<!-- Start of picture text -->
x 2x<br>arctg x dx D x arctg x �<br>Z Z 1 C x 2 dx D x arctg x � 2 1 Z 1 C x 2 dx D x arctg x � 2 1 ln.1 C x2/ C c:<br><!-- End of picture text -->

Pˇríklad 19.12. Vypočítejte neurčitý integrál 1 C x<sup>2</sup> dx. <u>Z</u> ~~p~~ 



<!-- Start of picture text -->
Řešení. Položíme-li u 0 .x/ D 1 a v.x/ D p 1 C x 2 , pak u.x/ D x, v 0 .x/ D p 1xCx 2 a věta 19.10 dává<br>x 2<br>Z p 1 C x 2 dx D x p 1 C x 2 � Z p 1 C x 2 dx D x p 1 C x 2 � Z 1 p  C1 x C2 � x 2 1 dx<br>1<br>D x p 1 C x 2 � Z p 1 C x 2 dx C Z p 1 C x 2 dx:<br><!-- End of picture text -->

Vidíme, že hledaný integrál vystupuje s opačným znaménkem také na pravé straně rovnosti. Jeho přičtením dostaneme novou rovnost 



<!-- Start of picture text -->
1<br>2 Z p 1 C x 2 dx D x p 1 C x 2 C Z p 1 C x 2 dx<br><!-- End of picture text -->

a podle výše uvedeného 12. bodu přehledu základních integrálů máme 



<!-- Start of picture text -->
1 C x 2 dx D 1 p 1 C x 2 C 1 �x C p 1 C x 2 � C c:<br>Z p 2 x 2 ln<br><!-- End of picture text -->

■ Vˇeta 19.13 — integrace substituˇcní metodou **t D '.x/** . _Nechť_ F _je primitivní funkce k funkci_ f _na intervalu_ I _a nechť funkce_ ' _má derivaci na intervalu_ J _, přičemž platí_ '.J / � I _. Potom na_ J _platí_ 



<!-- Start of picture text -->
f .'.x//' 0 .x/ dx D F.'.x// C c :<br>Z „ ƒ‚ …<br>R f .t/ dtjtD'.x/<br><!-- End of picture text -->

_Důkaz._ Protože F a ' splňují předpoklady věty o derivaci složené funkce (věta 14.6), platí �F.'.x//�0 D F<sup>0</sup> .'.x//'<sup>0</sup> .x/ D f .'.x//'<sup>0</sup> .x/ 8x 2 J , tj. F ı ' je primitivní k .f ı '/'<sup>0</sup> . 

Kapitola 3. Integrální poˇcet 

84 

Pˇríklad 19.14. Vypočítejte neurčitý integrál x<sup>2</sup><sup>~~p~~</sup> x<sup>3</sup> C 1 dx. Z 

_Řešení._ 



<!-- Start of picture text -->
Z x 2 p x 3 C 1 dx D ˇˇˇˇˇ 3x 2 dx Dx d 3 tC) 1 d Dx tD 3x1 2 dt ˇˇˇˇˇ D 31 Z t 1=2 dt D 9 2 t 3=2 C c<br>D 2<br>9 .x3 C 1/3=2 C c:<br><!-- End of picture text -->

■ Vˇeta 19.15 — integrace substituˇcní metodou **x D '.t/** . _Nechť_ f _je funkce definovaná na intervalu_ I _,_ ' _je funkce definovaná na intervalu_ J _, která zde má nenulovou derivaci (tj._ ' _musí být spojitá a ryze monotónní na_ J _) a_ '.J / D I _. Je-li_ F _primitivní funkce k_ .f ı '/'<sup>0</sup> _na_ J _, pak na_ I _platí_ 



<!-- Start of picture text -->
f .x/ dx D F.' �1 .x// C c<br>Z „ ƒ‚ …<br>R f .'.t//' 0 .t/ dtjtD'�1.x/<br><!-- End of picture text -->

_Důkaz._ Předpoklady věty vyhovují předpokladům vět o derivaci složené a inverzní funkce (věty 14.6 a 14.7). Máme tedy �F.'<sup>�1</sup> .x//�0 D F 0.'�1.x//�'<sup>�1</sup> .x/�0 D f .'.'�1.x///'0.'�1.x// '<sup><u>0</u></sup> <u>1.t/</u><sup>D</sup> f .x/'<sup>0</sup> .t/ '<sup><u>0</u></sup> <u>1.t/</u><sup>D f .x/ 8x2 I.</sup> 

Pˇríklad 19.16. Vypočítejte neurčitý integrál 



<!-- Start of picture text -->
1 � x 2 dx.<br>Z p<br><!-- End of picture text -->

_Řešení._ 



<!-- Start of picture text -->
x D sin t<br>1 � x 2 dx D cos 2 t dt D 1 .1 C cos 2t/ dt D t<br>Z p ˇˇˇˇ dx D cos t dt ˇˇˇˇ D Z 2 Z 2 C 1 4 sin 2t C c<br>D 2 t C 2 1 sin t cos t Cc D 1 2 arcsin x C 1 2 x cos.arcsin x/Cc D 1 2 arcsin x C 1 2 x q 1 � sin 2 .arcsin x/Cc<br>D 1 2 arcsin x C 1 2 x p 1 � x 2 C c:<br><!-- End of picture text -->



<!-- Start of picture text -->
Pˇríklad 19.17. Vypočítejte neurčitý integrál 1 C x 2 dx.<br>Z p<br><!-- End of picture text -->

_Řešení._ 



<!-- Start of picture text -->
x D sinh t<br>1 C x 2 dx D 1 C sinh 2 t cosh t dt D cosh 2 t dt<br>Z p ˇˇˇˇ dx D cosh t dt ˇˇˇˇ D Z q Z<br>D 1 e t C e �t �2 dt D 1 e 2t C2 C e �2t � dt D 1 �e 2t � e �2t � C 1<br>4 Z � 4 Z � 4 � 1 2 2 t C c<br>D 4 1 sinh 2t C 1 2 t C c D 1 2 sinh t cosh t C 1 2 t C c D 1 2 sinh t q 1 C sinh 2 t C 1 2 t C c<br>D 1 p 1 C x 2 C 1 p 1 C x 2 C 1 �x C p 1 C x 2 � C c:<br>2 x 2 argsinh x C c D 1 2 x 2 ln<br><!-- End of picture text -->

Srovnejte s řešením příkladu 19.12. 

#### Pˇríklady k procviˇcení 

19.1. Určete příslušné neurčité integrály: 



<!-- Start of picture text -->
a) x dxI b) x 2 c) 1 � 1 x p x dx:<br>Z � p 3x � x p 4 � Z 1 C x 2 dxI Z � x 2 � q<br><!-- End of picture text -->

20 Speciální substituce (integraˇcní metody) 

85 

19.2. Pomocí metody per-partes spočítejte následující neurčité integrály: 



<!-- Start of picture text -->
a) x 2 e �2x dxI b) x 2 cos x dxI c) sin x ln.tg x/ dx:<br>Z Z Z<br><!-- End of picture text -->

19.3. Pomocí substituce vypočtěte neurčité integrály: 



<!-- Start of picture text -->
sin 2x 1<br>a) dxI b) dxI c) x 2 p 3 1 � x dx:<br>Z p 1 C sin 2 x Z p .1 � x 2 / arcsin x Z<br><!-- End of picture text -->

_Výsledky._ 19.1. a) 6<sup>~~p~~</sup> x �<sup>x2</sup><sup>~~p~~</sup> x=10Cc; b) x �arctg x Cc; c) 4.x<sup>2</sup> C7/=7<sup>~~p~~4</sup> x Cc. 19.2. a) �<sup>e�2x</sup> =2�x<sup>2</sup> Cx C 1=2� C c; b) x<sup>2</sup> sin x C 2x cos x � 2 sin x C c; c) ln�tg<sup>x</sup> =2� � cos x ln.tg x/ C c. 19.3. a) 2 ~~p~~ 1 C sin<sup>2</sup> x C c; b) ln j arcsin xj C c; c) �<sup>3</sup> =140.9 C 12x C 14x<sup>2</sup> /.1 � x/<sup>4=3</sup> C c. 

### 20 Speciální substituce (integraˇcní metody) 

Integrace racionálních lomených funkcí 

V rozkladu racionální lomené funkce vystupují parciální zlomky ve tvaru 



<!-- Start of picture text -->
A Bx C C<br>.x � ˛/ k ; �.x � a/ 2 C b 2�` :<br><!-- End of picture text -->

Tyto integrujeme následovně: 



<!-- Start of picture text -->
8 1 1<br>1 k ¤ 1;<br>Z .x � ˛/ k dx D ˆ< 1 � k .x � ˛/ k�1 C c;<br>ˆ:ln jx � ˛j C c; k D 1:<br><!-- End of picture text -->



<!-- Start of picture text -->
Bx C C 2.x � a/ aB C C<br>Œ.x � a/ 2 C b 2 � ` D B 2 Œ.x � a/ 2 C b 2 � ` C Œ.x � a/ 2 C b 2 � ` ;<br>2.x � a/ .x � a/ 2 C b 2 D t<br>Z Œ.x � a/ 2 C b 2 � ` dx D ˇˇˇˇ dx D dt=.2.x � a// ˇˇˇˇ<br>8 1 1 1 1<br>1 ` > 1<br>D Z t ` dt D ˆ< 1 � ` t `�1 C c D 1 � ` ..x � a/ 2 C b 2 / `�1 C c;<br>ˆ:ln t C c D ln..x � a/ 2 C b 2 / C c; ` D 1:<br>1 b 1 1<br>Z ..x � a/ 2 C b 2 / ` dx D jx � a D btj D Z .b 2 t 2 C b 2 / ` dt D b 2`�1 Z .t 2 C 1/ ` dt:<br>1<br>Označme K` D<br>Z .t 2 C 1/ ` dt . Pak K1 D arctg t C c a pro ` > 1 dostaneme<br>1<br>u D .t 2 C1/ ` v 0 D 1 t t 2 t<br>K` D ˇˇˇˇˇ u 0 D .t 2 �C2`t1/ `C1 v D t ˇˇˇˇˇ D .t 2 C 1/ ` C 2` Z .t 2 C 1/ `C1 dt D .t 2 C 1/ `<br>1 1 t<br>C2` D<br>�Z .t 2 C 1/ ` dt � Z .t 2 C 1/ `C1 dt � .t 2 C 1/ ` C 2`.K` � K`C1/;<br>tedy K` D .t 2 Ct 1/ ` C 2`K` � 2`K`C1. Odtud K`C1 D 2`.t 2 tC1/ ` C 2` 2` �1 K`. Pokud přeznačíme<br>(píšeme ` namísto ` C 1), dostáváme<br><!-- End of picture text -->



<!-- Start of picture text -->
t<br>K` D 2.` � 1/.t 2 C 1/ `�1 C 2` 2`  �  � 2 3 K`�1:<br><!-- End of picture text -->

Kapitola 3. Integrální poˇcet 

86 

Poznámka 20.1. R R.f .x//f<sup>0</sup> .x/ dx – substituce t D f .x/ převede na R R.t/ dt , R R.e<sup>ax</sup> / dx – substituce t D e<sup>ax</sup> převede na a<sup><u>1</u></sup> R Rt.t/ dt . 

Definice 20.2 — polynomu dvou promˇenných. _Polynomem dvou proměnných_ nazýváme zobrazení P W R<sup>2</sup> ! R tvaru 

P.x; y/ D an;0x<sup>n</sup> C an�1;1x<sup>n�1</sup> y C an�2;2x<sup>n�2</sup> y<sup>2</sup> C ���C a0;ny<sup>n</sup> C : : : C a2;0x<sup>2</sup> C a1;1xy C a0;2y<sup>2</sup> C a1;0x C a0;1y C a0;0: _Racionální funkce ve dvou proměnných_ je funkce R W R<sup>2</sup> ! R tvaru R.x; y/ D<sup>P</sup><sup><u>.x; y/</u></sup> Q.x; y/<sup>;</sup> 

kde P; Q jsou polynomy dvou proměnných. 

##### Integrály, které lze transformovat na integrály z racionální funkce 



<!-- Start of picture text -->
1. R 0 n ax C b 1<br>Z s cx C d cx C d D t n.<br>@x; A dx, kde a; b; c; d 2 R, ad � bc ¤ 0 – substituce ax C b<br>2. R�x; p ax 2 C bx C c� dx, a ¤ 0 a kvadratický trojčlen ax 2 C bx C c nemá dvojnásobný kořen –<br>Z<br><!-- End of picture text -->

Eulerovy substituce, přičemž lze uvažovat tyto varianty: 

a) Je-li a > 0, pak je možné klást ~~<u>p</u>~~ ax<sup>2</sup> <u>C bx C c</u> D ˙<sup>~~p~~</sup> ax C t ; b) Je-li c � 0, pak je možné klást ~~p~~ ax<sup>2</sup> C bx C c D xt ˙<sup>~~p~~</sup> c; 

   - c) Pokud lze kvadratický trojčlen psát jako ax<sup>2</sup> C bx C c D a.x � ˛1/.x � ˛2/, kde ˛1; ˛2 2 R, ˛1 < ˛2, pak klademe ~~p~~ ax<sup>2</sup> C bx C c D ˙t.x � ˛1/, t � 0, kde znaménko „C“ bereme, je-li a > 0 a uvažujeme interval h˛2; 1/ a znaménko „�“ bereme, je-li a > 0 a uvažujeme interval .�1; ˛1i. V případě a < 0 pak klademe znaménko „C“. 

3. Binomické integrály R x<sup>m</sup> .a C bx<sup>n</sup> /<sup>p</sup> dx, kde m; n; p 2 Q, a; b 2 R: 



<!-- Start of picture text -->
p 2 Z W x D t N ; kde N je společný jmenovatel čísel m; n;<br>m C 1<br>2 Z W a C bx n D t N ; kde N je jmenovatel zlomku p;<br>n<br>m C 1<br>C p 2 Z W a C bx n D x n t N ; kde N je jmenovatel zlomku p:<br>n<br><!-- End of picture text -->

4. R R.cos x; sin x/ dx – substituce t D tg<sup><u>x</u></sup> 2<sup>, v některých případech lze volit jednodušší substituci:</sup> 



<!-- Start of picture text -->
R.sin x; � cos x/ D �R.sin x; cos x/ W sin x D t;<br>R.� sin x; cos x/ D �R.sin x; cos x/ W cos x D t;<br>R.� sin x; � cos x/ D R.sin x; cos x/ W tg x D t:<br><!-- End of picture text -->



<!-- Start of picture text -->
dx<br>Pˇríklad 20.3. Vypočtěte neurčitý integrál .<br>Z x C p x 2 � x C 1<br><!-- End of picture text -->



<!-- Start of picture text -->
Řešení. Integrand je funkcí spojitou na celé reálné ose (protože jmenovatel g.x/ D x C p x 2 � x C 1 je<br>rostoucí funkce s limx!�1 g.x/ D 1=2). Ze substituce x C p x 2 � x C 1 D t, t > 1=2 (viz Eulerova<br>substituce pro a > 0), máme x D .t 2 � 1/=.2t � 1/, dx D 2.t 2 � t C 1/=.2t � 1/ 2 dt. Integrál se tedy<br>transformuje:<br>dx 1 1<br>Z x C p x 2 � x C 1 D Z 2.t.2tt 2 ��t 1/C 2  1/ dt D 2 Z 1t dt C 3 Z .2t � 1/ 2 dt � 3 Z 2t � 1 dt<br><!-- End of picture text -->

20 Speciální substituce (integraˇcní metody) 

87 



<!-- Start of picture text -->
3<br>D 2 ln t � 2.2t � 1/ � 2 3 ln.2t � 1/ C c<br>D 3 ln �x C p x 2 � x C 1�4=3 � 1 C c:<br>2 2�x C p x 2 � x C 1� � 1 2.x C p x 2 � x C 1/ � 1 !<br><!-- End of picture text -->

Pˇríklad 20.4. Vypočtěte neurčitý integrál 



<!-- Start of picture text -->
1 C x 2 dx.<br>Z p<br><!-- End of picture text -->

_Řešení._ Jedná se binomický integrál, kde (vzhledem ke značení výše) je m D 0, n D 2 a p D 1=2 (a D 1, b D 1). Protože .m C 1/=n C p D 1 2 Z, pomůže substituce 1 C x<sup>2</sup> D x<sup>2</sup> t<sup>2</sup> , tj. 1=x<sup>2</sup> C 1 D t<sup>2</sup> , x ¤ 0. Pro x > 0 pak z posledního vyjádření máme x D 1= ~~p~~ t<sup>2</sup> � 1, přičemž zvolíme jednu monotónní větev, např. tu pro t > 1. Protože platí dx D � .t<sup>2</sup> �t1/<sup>3=2dt, integrál se transformuje na</sup> 



<!-- Start of picture text -->
t t t 2<br>1 C x 2 dx D �<br>Z p Z .t 2 � 1/ 1=2 � .t 2 � 1/ 3=2 dt D � Z .t 2 � 1/ 2 dt;<br><!-- End of picture text -->

což je racionální lomená funkce v proměnné t . Rozkladem na parciální zlomky dále máme 



<!-- Start of picture text -->
t 2 1 1 1 1<br>� Z .t 2 � 1/ 2 dt D � 4 1 Z .t C 1/ 2 dt � 4 1 Z .t � 1/ 2 dt C 1 4 Z t C 1 dt � 1 4 Z t � 1 dt<br>D 1 1 1<br>4 � t C 1 C 4 1 � t � 1 C 4 1 ln t t C �  1 1 C c:<br><!-- End of picture text -->

Návratem k původní proměnné skrze t D ~~p~~ 1 C x<sup>2</sup> =x dostaneme 



<!-- Start of picture text -->
1 C x 2 dx D 1 x C x C 1 p 1 C x 2 C c<br>Z p 4 � p 1 C x 2 C x p 1 C x 2 � x � 4 ln x p  C 1 C x 2 � x<br>D 1 p 1 C x 2 � x/ C x. p 1 C x 2 C x/ C 1 x C p 1 C x 2 � p 1 C x 2 C x C c<br>4 � x. 1 4 ln p 1 C x 2 � x p 1 C x 2 C x !<br>D 1 p 1 C x 2 C 1 �x C p 1 C x 2 � C c:<br>2 x 2 ln<br><!-- End of picture text -->

Ke stejnému závěru bychom došli, kdybychom uvažovali x < 0 (a vybrali jednu monotónní větev substituční funkce). Konečně, není těžké ověřit, že derivací výsledku v bodě x D 0 dostaneme hodnotu integrandu v tomto bodě, a tedy nalezená funkce je primitivní funkcí k integrandu na celé reálné ose. Srovnejte s řešením příkladů 19.12 a 19.17. 

Pˇríklad 20.5. Vypočtěte neurčitý integrál 



<!-- Start of picture text -->
1 C x 2 dx.<br>Z p<br><!-- End of picture text -->

_Řešení._ Integrand lze chápat jako speciální případ funkce R.x; ~~p~~ ax<sup>2</sup> C bx C x/, kde a D 1, b D 0, c D 1. Lze tedy použít například substituci ~~p~~ 1 C x<sup>2</sup> D �x C t, ze které vyjádříme x D<sup><u>t</u>2</sup> 2t<sup>�1, t>0,</sup> <u>1�t</u><sup>2</sup> dx D � 2t<sup>2C 1</sup> �dt . Integrál se tedy transformuje na 



<!-- Start of picture text -->
1 C x 2 dx D 1 � t 2 C t 1 � t 2 C 1 dt D 1 dt<br>Z p Z 2t !  2t 2 ! 4 Z 1 C 2tt 3 2 C t 4<br>D 1 dt D � 1<br>4 Z � t1 3 C 2 t C t � 8t 2 C 2 1 ln t C 1 8 t 2 C c<br>1<br>D 1 8 � �x C p 1 C x 2 �2 C �x C p 1 C x 2 �2 ! C 1 2 ln �x C p 1 C x 2 � C c<br>D 1 8 �1 C �x C p 1 C x 2 �4 � � p 1 C x 2 � x�2 C 2 1 ln �x C p 1 C x 2 � C c<br>�x C p 1 C x 2 �2 � p 1 C x 2 � x�2 !<br><!-- End of picture text -->

Kapitola 3. Integrální poˇcet 

88 



<!-- Start of picture text -->
D 1 p 1 C x 2 C 1 �x C p 1 C x 2 � C c:<br>2 x 2 ln<br><!-- End of picture text -->

Poslední vyjádření opět souhlasí se závěry příkladů 19.12, 19.17 a 20.4. 

Pˇríklad 20.6. Vypočtěte neurčitý integrál 



<!-- Start of picture text -->
1 C x 2 dx.<br>Z p<br><!-- End of picture text -->

_Řešení._ Integrál nejprve transformujme pomocí substituce x D tg t , ��=2 < t < �=2: 



<!-- Start of picture text -->
1 1<br>Z p 1 C x 2 dx D Z q 1 C tg 2 t � cos 2 t dt D Z cos 3 t dt:<br><!-- End of picture text -->

Vidíme, že vzniklý integrand je typu R.sin t; cos t/, přičemž R.sin t; cos t/ D �R.sin t; cos t/. Pro převod na racionální lomenou funkci tedy zabere (podle čtvrtého bodu výše) substituce sin t D u, �1 < u < 1, odkud máme dt D du= cos t a 



<!-- Start of picture text -->
1 1 1 1<br>Z cos 3 t dt D Z cos 4 t du D Z .1 � sin 2 t/ 2 du D Z .1 � u 2 / 2 du<br>D 1 1 1 1 1<br>4 Z u C 1 du � 4 1 Z u � 1 du C 1 4 Z .u � 1/ 2 du C 4 1 Z .u C 1/ 2 du<br>D 1 1 1 C c<br>4 ln u u  C  �  1 1 � 1 4 � u � 1 C u C 1 �<br><!-- End of picture text -->

S využitím identity u D sin.arctg x/ D x= ~~p~~ 1 C x<sup>2</sup> dostaneme po úpravě 



<!-- Start of picture text -->
1 C x 2 dx D 1 p 1 C x 2 C 1 �x C p 1 C x 2 � C c:<br>Z p 2 x 2 ln<br><!-- End of picture text -->

Jedná se tedy již o pátý způsob, jak určit primitivní funkci k funkci ~~p~~ 1 C x<sup>2</sup> , viz příklady 19.12, 19.17, 20.4 a 20.5. 

Poznámka 20.7. Primitivní funkce k funkci elementární nemusí být elementární, může to být vyšší transcendentní funkce. Vyššími funkcemi jsou zejména 



<!-- Start of picture text -->
Si.x/ D dx „sinusintegrál“; Ci.x/ D dx „kosinusintegrál“;<br>Z sinx x Z cosx x<br>Li.x/ D Z ln1 x dx „logaritmusintegrál“; Z e �x2 dx integrál z Gaussovy funkce;<br>sin x 2 dx; cos x 2 dx Fresnelovy integrály;<br>Z Z<br><!-- End of picture text -->

binomické integrály R x<sup>m</sup> .a C bx<sup>n</sup> /<sup>p</sup> dx, kdy žádné žádné z čísel p;<sup><u>m</u></sup> n<sup><u>C1</u></sup> ;<sup><u>m</u></sup> n<sup><u>C1</u></sup> C p není celé. Není známo obecné pravidlo, které by umožnilo rozhodnout, zda primitivní funkci neumíme vyjádřit jako elementární v důsledku neznámých integračních metod, nebo zda skutečně vyjadřuje vyšší transcendentní funkci. 

#### Pˇríklady k procviˇcení 

20.1. Pomocí Eulerových substitucí určete následující integrály: 



<!-- Start of picture text -->
dx p 1 C x C x 2 x 2 C 4x<br>a) b) dx; c) dx:<br>Z .1 C x/ p 1 C x C x 2 ; Z 1 �x p 1 C x C x 2 Z p x 2<br>xC p 1CxCx 2 p 1CxCx 2<br>Výsledky. 20.1. a) ln ˇˇˇ 2CxC p 1CxCx 2 ˇˇˇ C c, b) ln ˇˇˇ 2Cx�2 x 2 ˇˇˇ C c, c) lnˇˇx C 2 C p x 2 C 4xˇˇ �<br>8<br>xC p x 2 C4x C c.<br><!-- End of picture text -->

21 Urˇcitý (Riemann˚uv) integrál 

89 

### 21 Urˇcitý (Riemann˚uv) integrál 

Z elementární geometrie víme, jak určit obsah (plošnou míru) základních geometrických útvarů jakými jsou např. trojúhelník, obdélník či obecněji mnohoúhelník. Přirozenou otázkou je, jak přiřadit obsah rovinnému obrazci, který nelze rozložit na mnohoúhelníky. Příkladem takového geometrického útvaru je obrazec ohraničený přímkami x D a, x D b, y D 0 a grafem spojité nezáporné funkce f , tj. množina 

M<sup>C</sup> D ˚Œx; y� 2 R<sup>2</sup> W a � x � b; 0 � y � f .x/�; 

takové množině se říká _křivočarý lichoběžník (určený funkcí_ f _a intervalem_ ha; bi _)_ . Přiřazení obsahu libovolnému křivočarému lichoběžníku M<sup>C</sup> (případně jinému rovinnému obrazci) pak lze chápat jako zobrazení, které těmto rovinným obrazcům přiřazuje nezáporné reálné číslo (obsah), a to by mělo mít stejné vlastnosti, jaké známe z elementární geometrie (např. když A � B, pak obsah.A/ � obsah.B/). 

Zmíněná úvaha slouží jako základní motivace k zavedení pojmu určitého integrálu. Jinak řečeno, určitý (Riemannův) integrál bude definovat obsah křivočarého lichoběžníku M<sup>C</sup> z předchozího odstavce. Nebude-li řečeno jinak, tak v celé kapitole bude funkce f ohraničená a definovaná na uzavřeném intervalu ha; bi (na rozdíl od úvodního odstavce tedy dále nepožadujeme spojitost funkce ani její nezápornost). 

Definice 21.1 — pojm˚u potˇrebných pˇri konstrukci Riemannova<sup>1</sup> integrálu. _Dělením uzavřeného intervalu_ ha; bi rozumíme množinu D D fx0; x1; : : : ; xng takovou, že a D x0 < x1 < x2 < ��� < xn�1 < xn D b. Číslo �.D/ D maxfxi �xi�1 W i D 1; 2; : : : ; ng nazýváme _normou dělení_ D. Symbolem _D_ .ha; bi/ označíme množinu všech dělení intervalu ha; bi. Jsou-li D1 2 _D_ .ha; bi/, D2 2 _D_ .ha; bi/ taková, že D1 � D2 (tj. každý dělící bod D1 je současně dělícím bodem D2), řekneme, že dělení D2 je _zjemněním dělení_ D1. 

Definice 21.2 — dolního a horního souˇctu. Buďte D 2 _D_ .ha; bi/ a mi D infff .x/ W x 2 hxi �1; xi ig, Mi D supff .x/ W x 2 hxi�1; xi ig pro i 2 f1; : : : ; ng. Číslo 



<!-- Start of picture text -->
n<br>s.D; f / D X mi .xi � xi�1/<br>i D1<br><!-- End of picture text -->

nazveme _dolním součtem_ a číslo 



<!-- Start of picture text -->
n<br>S.D; f / D X Mi .xi � xi�1/<br>iD1<br><!-- End of picture text -->

nazveme _horním součtem_ příslušným k funkci f a dělení D. 

Poznámka 21.3. Existence čísel mi a Mi je zaručena ohraničeností f . 

- Lemma 21.4. (i) _Pro libovolné_ D 2 _D_ .ha; bi/ _platí_ s.D; f / � S.D; f / _._ 

- (ii) _Je-li_ D2 2 _D_ .ha; bi/ _zjemněním_ D1 2 _D_ .ha; bi/ _, pak_ s.D1; f / � s.D2; f / _a_ S.D1; f / � S.D2; f / _(tj. při zjemnění dělení se dolní součet nezmenší a horní součet nezvetší)._ 

- (iii) _Nechť_ m D infff .x/ W x 2 ha; big _,_ M D supff .x/ W x 2 ha; bi/ _. Pak pro každé_ D 2 _D_ .ha; bi/ _platí_ m.b � a/ � s.D; f / � S.D; f / � M.b � a/ _._ 

_Důkaz._ ad (i) Plyne ihned z toho, že mi � Mi a xi � xi�1 > 0 pro každé i 2 f1; : : : ; ng. ad (ii) Nechť D2 má o jeden dělící bod více, než D1, tj. existuje k 2 f1; : : : ; ng takové, že 

D1 D fx0; x1; : : : ; xk�1; xk; : : : ; xng; D2 D fx0; x1; : : : ; xk�1; z; xk; : : : ; xng: 

Označme mi D infff .x/ W x 2 hxi �1; xi ig, i D 1; 2; : : : ; n, m<sup>�</sup> k<sup>Dinfff .x/Wx2hxk�1; zig,</sup> m<sup>��</sup> k D infff .x/ W x 2 hz; xkig. Pak zřejmě mk � m<sup>�</sup> k<sup>, mk�m��</sup> k a tedy mk.xk � xk�1/ D mk.xk � z/ C mk.z � xk�1/ � m<sup>��</sup> k<sup>.xk�z/ C m�</sup> k<sup>.z �xk�1/:</sup> 

1Bernhard Riemann 1826–1866, Němec 

Kapitola 3. Integrální poˇcet 

90 

Odtud plyne 



<!-- Start of picture text -->
k�1 n<br>s.D1; f / D X mi .xi � xi �1/ C mk.xk � xk�1/ C X mi .xi � xi �1/<br>i D1 iDkC1<br>k�1 n<br>� X mi .xi � xi�1/ C m �� k .xk � z/ C m� k .z � xk�1/ C X mi .xi � xi�1/ D s.D2; f /:<br>iD1 i DkC1<br><!-- End of picture text -->

Analogicky ukážeme, že S.D1; f / � S.D2; f /. Pokud D2 má o p dělících bodů více než D1, ukážeme platnost tvrzení p-násobným opakováním téže úvahy. 

ad (iii) Plyne z (i) a (ii), neboť fa; bg 2 _D_ .ha; bi/ a každé jiné dělení je zjemněním fa; bg. 

Definice 21.5 — dolního a horního integrálu. Číslo 



<!-- Start of picture text -->
f .x/ dx WD supfs.D; f / W D 2  D .ha; bi/g<br>Zab<br> f na intervalu ha; bi a číslo ha; bi a čísloa; bi a čísloi a číslo a číslo<br>f .x/ dx WD inffS.D; f / W D 2  D .ha; bi/g<br>Zab<br><!-- End of picture text -->

nazýváme _dolní integrál funkce_ f na intervalu ha; bi a číslo ha; bi a čísloa; bi a čísloi a číslo a číslo 

nazýváme _horní integrál funkce_ f na intervalu ha; bi. 

Poznámka 21.6. Uvedená definice je korektní, protože množiny fs.D; f / W D 2 _D_ .ha; bi/g a fS.D; f / W D 2 _D_ .ha; bi/g jsou podle bodu (iii) z předchozího lemmatu ohraničené a neprázdné a tedy sup i inf existují. Tato definice spolu s vlastností (iii) z předchozího lemmatu ihned dávají: 

■ Vˇeta 21.7. _Nechť_ m D infff .x/ W x 2 ha; big _,_ M D supff .x/ W x 2 ha; big _. Pak platí_ 



<!-- Start of picture text -->
m.b � a/ � f .x/ dx � f .x/ dx � M.b � a/:<br>Zab Zab<br><!-- End of picture text -->

Definice 21.8 — integrovatelnosti a Riemannova integrálu. Řekneme, že f _je na_ ha; bi _integrovatelná (integrabilní, integrace schopna) v Riemannově smyslu_ , jestliže 



<!-- Start of picture text -->
f .x/ dx D f .x/ dx:<br>Zab Zab<br>V tomto případě definujeme její  Riemannův integrál<br>f .x/ dx WD f .x/ dx D f .x/ dx:<br>Zab Zab Zab<br>Jestliže<br>f .x/ dx < f .x/ dx;<br>Zab Zab<br>řekneme, že f není na  ha; bi  integrovatelná v Riemannově smyslu .<br><!-- End of picture text -->

Poznámka 21.9. Protože v celé kapitole uvažujeme integrovatelnost pouze v Riemannově smyslu, budeme dále hovořit stručně o integrovatelnosti funkce. 

Pˇríklad 21.10. Rozhodněte o integrovatelnosti funkcí a) f .x/ D c na ha; bi, b) f .x/ D �.x/ na ha; bi. 

21 Urˇcitý (Riemann˚uv) integrál 

91 

_Řešení._ ad a) Je-li f .x/ D c pro x 2 ha; bi, pak m D M D c a podle věty 21.7 



<!-- Start of picture text -->
c.b � a/ � f .x/ dx � f .x/ dx � c.b � a/;<br>Zab Zab<br><!-- End of picture text -->

z čehož plyne 



<!-- Start of picture text -->
f .x/ dx D f .x/ dx D c.b � a/:<br>Zab Zab<br><!-- End of picture text -->

Ad b) Pro libovolné D D fx0; x1; : : : ; xng 2 _D_ .ha; bi/ je mi D 0, Mi D 1, i 2 f1; 2; : : : ; ng, a tedy 



<!-- Start of picture text -->
n n<br>s.D; f / D X mi .xi � xi �1/ D X 0.xi � xi �1/ D 0 D f .x/ dx;<br>i D1 i D1 Zab<br>n n<br>S.D; f / D X Mi .xi � xi �1/ D X 1.xi � xi�1/ D xn � x0 D b � a D f .x/ dx<br>i D1 i D1 Zab<br><!-- End of picture text -->

a tedy � není integrovatelná. 

Definice 21.11 — integrálního souˇctu. Nechť D D fx0; x1; : : : ; xng 2 _D_ .ha; bi/ je dělení intervalu ha; bi, �i 2 hxi �1; xi i pro i 2 f1; : : : ; ng. Množina � D f�1; �2; : : : ; �ng se nazývá _výběr reprezentantů dělících intervalů dělení_ D. Číslo 



<!-- Start of picture text -->
n<br>�.D; f; �/ WD X f .�i /.xi � xi�1/<br>iD1<br><!-- End of picture text -->

se nazývá _integrální součet příslušný k dělení_ D _, funkci_ f _a výběru reprezentantů_ � . 

Poznámka 21.12. Poněvadž mi � f .�i / � Mi , platí s.D; f / � �.D; f; �/ � S.D; f / pro každé dělení D a každý výběr reprezentantů � . 

Poznámka 21.13. _Posloupností v širším smyslu_ rozumíme zobrazení množiny N do libovolné množiny. Lze tedy mluvit o posloupnosti dělení daného intervalu jakožto zobrazení N ! _D_ .ha; bi/. Řekneme, že posloupnost dělení fDng<sup>1</sup> nD1<sup>�</sup><sup>_D_.ha; bi/ je</sup><sup>_nulová_, jestliže limn!1 �.Dn/D0. Ke každému ı>0</sup> existuje D 2 _D_ .ha; bi/ takové, že �.D/ < ı (stačí položit n D � <u>b�ı a</u> ˘ C 1 a interval rozdělit na n stejně dlouhých dělících intervalů). 

■ Vˇeta 21.14. _Buď_ fDng<sup>1</sup> nD1<sup>_libovolná nulová posloupnost dělení intervalu_ha; bi</sup><sup>_. Pak platí_</sup> 



<!-- Start of picture text -->
nlim!1 s.Dn; f / D Zab f .x/ dx a nlim!1 S.Dn; f / D Zab f .x/ dx:<br><!-- End of picture text -->

_Je-li navíc_ f _integrovatelná na_ ha; bi _a_ �n _je libovolný výběr reprezentantů dělících intervalů dělení_ Dn _, pak platí_ 



<!-- Start of picture text -->
nlim!1 s.Dn; f / D n lim !1 S.Dn; f / D n lim !1 �.Dn; f; �n/ D Zab f .x/ dx:<br><!-- End of picture text -->

_Důkaz._ Dokažme nejdříve pomocné tvrzení: 

■ Lemma 21.15. _Ke každému_ " > 0 _existuje_ ı > 0 _takové, že pro každé_ D 2 _D_ .ha; bi/ _,_ �.D/ < ı _, platí_ 



<!-- Start of picture text -->
S.D; f / < f .x/ dx C ":<br>Zab<br><!-- End of picture text -->

Kapitola 3. Integrální poˇcet 

92 

_Důkaz lemmatu._ Poněvadž f je ohraničená, existuje h 2 R, h > 0 takové, že jf .x/j � h pro všechna x 2 ha; bi. Z definice horního integrálu ihned máme Ra b<sup>f .x/ dx�S.D; f / pro libovolné D2</sup><sup>_D_.ha; bi/.</sup> Dále existuje dělení D1 D fy0; y1; : : : ; ypg 2 _D_ .ha; bi/ takové, že S.D1; f / < R ba<sup>f .x/ dx C</sup> 2<sup><u>"</u>(kdyby</sup> takové dělení neexistovalo, nemohl by horní integrál být infimem horních součtů S.D; f / přes všechna dělení, viz analogickou argumentaci v příkladu 6.4). Celkově tedy máme 



<!-- Start of picture text -->
f .x/ dx � S.D1; f / < f .x/ dx C "<br>Zab Zab 2 :<br><!-- End of picture text -->

Položme ı D "=.4hp/. Pak ı > 0. Buď D D fx1; x2; : : : ; xng 2 _D_ .ha; bi/ libovolné takové, že �.D/ < ı. Dále položme D2 D D [ D1 D fz1; z2; : : : ; zmg. Podle lemmatu 21.4(ii) je S.D2; f / � S.D; f /. Dělící intervaly hxi �1; xi i dělení D rozdělíme na dva druhy: intervaly 1. druhu, jestliže uvnitř intervalu neleží žádný dělící bod yj dělení D1, intervaly 2. druhu v opačném případě. Každý dělící interval 1. druhu je rovněž dělícím intervalem dělení D2. Tento interval přispívá k S.D; f / i k S.D2; f / týmž sčítancem Mi .xi � xi�1/, tedy v rozdílu S.D; f / � S.D2; f / se neprojeví. Uvnitř každého intervalu hxi �1; xi i 2. druhu leží alespoň jedno z čísel y1; y2; : : : ; yp�1, což znamená, že intervalů 2. druhu je nejvýše p � 1. Interval druhého druhu přispívá k S.D; f / sčítancem Mi .xi � xi�1/, který je v absolutní hodnotě menší nebo roven jak číslo h�.D/ (protože Mi � h a �.D/ D maxi .xi � xi�1/), a protože �.D/ < ı, máme h�.D/ < hı. Absolutní hodnota příspěvku všech intervalů 2. druhu k S.D; f / je tedy menší než hıp. V D2 je každý interval hxi�1; xi i 2. druhu rozdělen dělícími body xi �1 D zr < zrC1 < ��� < zs D xi . Označme Mk<sup>�Dsupff .x/Wx2hzk�1; zkig.OpětjM</sup> k<sup>�j�hatedyabsolutníhodnotapříspěvku</sup> intervalu hxi�1; xi i do součtu S.D2; f / je 



<!-- Start of picture text -->
s s<br>X Mk �.zk � zk�1/ � X h.zk � zk�1/ D h.zs � zr / D h.xi � xi �1/ � h�.D/ < hı:<br>ˇˇˇˇˇˇkDrC1 ˇˇˇˇˇˇ kDrC1<br><!-- End of picture text -->

Absolutní hodnota příspěvků všech intervalů 2. druhu k S.D2; f / je tedy menší než hıp. Odtud plyne, že S.D; f / � S.D2; f / < 2hıp D 2<sup><u>"</u>,neboliS.D; f /<S.D2; f / C</sup> 2<sup><u>"</u>.Podlelemmatu21.4(ii)je</sup> S.D2; f / � S.D1; f /, a tedy 



<!-- Start of picture text -->
S.D; f / < S.D2; f / C 2 " � S.D1; f / C 2 " < Zab f .x/ dx C 2 " C 2 " ;<br><!-- End of picture text -->

což je tvrzení lemmatu. 

Buď nyní " > 0 libovolné. Podle výše uvedeného lemmatu existuje ı > 0 takové, že pro každé D 2 _D_ .ha; bi/, �.D/ < ı platí 



<!-- Start of picture text -->
S.D; f / < f .x/ dx C ":<br>Zab<br><!-- End of picture text -->

Poněvadž 



<!-- Start of picture text -->
S.D; f / � f .x/ dx;<br>Zab<br><!-- End of picture text -->

platí 



<!-- Start of picture text -->
f .x/ dx<br>Zab<br>ˇˇˇˇˇS.D; f / � ˇˇˇˇˇ < ":<br><!-- End of picture text -->

Dále, protože posloupnost fDng je nulová, k ı > 0 existuje n0 2 N takové, že pro každé n � n0 platí �.Dn/ < ı. To znamená, že pro každé n � n0 platí 



<!-- Start of picture text -->
Zab f .x/ dx a proto nlim!1 S.Dn; f / D Zab f .x/ dx:<br>ˇˇˇˇˇS.Dn; f / � ˇˇˇˇˇ < ";<br><!-- End of picture text -->

Analogicky bychom dokázali limn!1 s.Dn; f / D <u>R ba</u><sup>f .x/ dx.</sup> 

21 Urˇcitý (Riemann˚uv) integrál 

93 

Je-li f integrovatelná na ha; bi, je <u>Ra b</u><sup>f .x/ dxD</sup> Ra b<sup>f .x/ dxD</sup> Ra b<sup>f .x/ dx, takže</sup> nlim!1<sup>s.Dn; f / D</sup> n<sup>lim</sup> !1<sup>S.Dn; f / D</sup> Zab f .x/ dx: 

Poslední tvrzení věty plyne z nerovnosti s.D; f / � �.D; f; �/ � S.D; f / a z věty o 3 posloupnostech. 

Poznámka 21.16. Určitý integrál definovaný skrz definice 21.1–21.8 je ve skutečnosti Darbouxův integrál (Jean-Gaston Darboux 1842–1917, Francouz), i když jsme jej nazvali Riemannův (někdy se také hovoří o Darbouxově definici Riemannova integrálu). Původní Riemannova definice pracuje právě s integrálními součty �.D; f; �/ z definice 21.11. Lze dokázat, že Darbouxův a Riemannův integrál jsou ekvivalentní (tj. když existuje jeden, existuje i druhý a dávají stejnou hodnotu). Důkaz implikace „Darboux ) Riemann“ využívá předchozí větu. Darbouxova definice se považuje za lepší z didaktického hlediska, Riemannova zase z praktického hlediska. 

■ Vˇeta 21.17 — Nutná a postaˇcující podmínka integrovatelnosti. _Funkce_ f _je na_ ha; bi _integrovatelná_ , _ke každému_ " > 0 _existuje_ D 2 _D_ .ha; bi/ _takové, že_ 



<!-- Start of picture text -->
S.D; f / � s.D; f / < ":<br><!-- End of picture text -->

_Důkaz._ „)“ Nechť f je integrovatelná, " > 0 je libovolné a nechť fDng<sup>1</sup> nD1<sup>�</sup><sup>_D_.ha; bi/ je libovolná</sup> nulová posloupnost dělení intervalu ha; bi. Podle věty 21.14 existuje n0 2 N takové, že 



<!-- Start of picture text -->
f .x/ dx f .x/ dx<br>Zab 2 ; Zab 2 :<br>ˇˇˇˇˇs.Dn0 ; f / � ˇˇˇˇˇ < " ˇˇˇˇˇS.Dn0 ; f / � ˇˇˇˇˇ < "<br><!-- End of picture text -->

Tedy pro Dn0 platí 

S.Dn0 ; f / � s.Dn0 ; f / D jS.Dn0 ; f / � s.Dn0 ; f /j 



<!-- Start of picture text -->
� f .x/ dx f .x/ dx � s.Dn0 ; f /<br>Zab Zab 2 C 2 " D ":<br>ˇˇˇˇˇS.Dn0 ; f / � ˇˇˇˇˇ C ˇˇˇˇˇ ˇˇˇˇˇ < "<br><!-- End of picture text -->

„(“ Nechť pro libovolné " > 0 existuje takové dělení D 2 _D_ .ha; bi/, že S.D; f / � s.D; f / < ". Z této nerovnosti a z nerovností 



<!-- Start of picture text -->
f .x/ dx � S.D; f /; f .x/ dx � s.D; f /; s.D; f / � S.D; f /<br>Zab Zab<br><!-- End of picture text -->

plyne, že 



<!-- Start of picture text -->
0 � f .x/ dx � f .x/ dx < ":<br>Zab Zab<br><!-- End of picture text -->

Protože ale " > 0 je libovolné, musí nutně být R ba<sup>f .x/ dx�</sup> <u>R ba</u><sup>f .x/ dxD0,neboli</sup> Ra b<sup>f .x/ dxD</sup> <u>R ba</u><sup>f .x/ dx, tj. fje integrovatelná.</sup> 

■ Vˇeta 21.18 — 1. postaˇcující podmínka pro integrovatelnost. _Je-li funkce_ f _monotónní na_ ha; bi _, pak je na tomto intervalu integrovatelná._ 

_Důkaz._ Nechť je f pro určitost na ha; bi např. neklesající. Je-li f .a/ D f .b/, pak je f na ha; bi konstantní a podle příkladu 21.10 je integrovatelná. Nechť tedy f .a/ < f .b/. Buď " > 0 libovolné a D D fx0; x1; : : : ; xng 2 _D_ .ha; bi/ takové, že �.D/ < f .b/�" f .a/<sup>. Protože fje neklesající, platí</sup> 

mi D infff .x/ W x 2 hxi �1; xi ig D f .xi�1/; Mi D supff .x/ W x 2 hxi�1; xi ig D f .xi /: 

Kapitola 3. Integrální poˇcet 

94 

##### Odtud 



<!-- Start of picture text -->
n n<br>S.D; f / � s.D; f / D X f .xi /.xi � xi �1/ � X f .xi �1/.xi � xi �1/<br>iD1 iD1<br>n n<br>D<br>X�f .xi / � f .xi�1/�.xi � xi �1/ � X�f .xi / � f .xi�1/��.D/<br>iD1 i D1<br>D �.D/�f .x1/ � f .x0/ C f .x2/ � f .x1/ C ���C f .xn/ � f .xn�1/�<br>D �.D/�f .xn/ � f .x0/� D �.D/�f .b/ � f .a/�<br>"<br>< �f .b/ � f .a/� D ":<br>f .b/ � f .a/<br><!-- End of picture text -->

Podle věty 21.17 je tedy f integrovatelná na ha; bi. 

■ Vˇeta 21.19 — 2. postaˇcující podmínka pro integrovatelnost. _Je-li funkce_ f _spojitá na_ ha; bi _, pak je zde integrovatelná._ 

_Důkaz._ Buď f spojitá a " > 0 libovolné. Podle Heineho–Cantorovy věty (viz věta 13.20) je f na ha; bi spojitá stejnoměrně, a tedy k b�" a<sup>>0existujeı>0takové,žeprovšechnax; y2ha; bi</sup> taková, že jx � yj < ı, je jf .x/ � f .y/j < b�" a<sup>. Buď DDfx0; x1; : : : ; xng2</sup><sup>_D_.ha; bi/, �.D/<ı,</sup> mi D infff .x/ W x 2 hxi �1; xi ig, Mi D supff .x/ W x 2 hxi �1; xi ig. Podle 2. Weierstrassovy věty existují yi 2 hxi�1; xi i, zi 2 hxi�1; xi i takové, že f .yi / D mi , f .zi / D Mi . Protože dělení D splňuje �.D/ < ı, platí také jyi � zi j < ı, a tedy f .zi / � f .yi / D Mi � mi < b�" a<sup>. Odtud</sup> 



<!-- Start of picture text -->
n n<br>S.D; f / � s.D; f / D X f .zi /.xi � xi�1/ � X f .yi /.xi � xi �1/<br>iD1 i D1<br>n n<br>" "<br>D<br>XŒf .zi / � f .yi /�.xi � xi�1/ < b � a X.xi � xi �1/ D b � a .b � a/ D ":<br>iD1 iD1<br><!-- End of picture text -->

Podle věty 21.17 je tedy f integrovatelná na ha; bi. 

Definice 21.20 — nulové množiny. Množina M � R se nazývá _nulová_ , jestliže ke každému " > 0 existuje konečný počet otevřených intervalů .a1; b1/, .a2; b2/; : : : ; .an; bn/ takových, že<sup>Pn</sup> i D1<sup>.bi�ai/<"</sup> a M � .a1; b1/ [ .a2; b2/ [ ���[ .an; bn/. 

Platí: 

- (i) Každá konečná množina je nulová. 

- (ii) Sjednocení konečně mnoha nulových množin je nulová množina. 

- (iii) Množina členů konvergentní posloupnosti je nulová. 

- (iv) Množina členů posloupnosti, která má konečný počet hromadných bodu, je nulová. 

■ Vˇeta 21.21 — 3. postaˇcující podmínka pro integrovatelnost. _Je-li množina bodů nespojitosti funkce_ f _na_ ha; bi _nulová, pak je_ f _integrovatelná na_ ha; bi _._ 

_Důkaz._ Bude dokázano později, viz strana 100. 

Pˇríklad 21.22. Zjistěte, zda je na intervalu h0; 1i integrovatelná funkce 



<!-- Start of picture text -->
1<br>f .x/ D .�1/ n pro x 2 � 2 nC1 ; 2 1n E; n D 0; 1; : : : ;<br>(0 pro x D 0:<br><!-- End of picture text -->

_Řešení._ Množina bodů nespojitosti M D f1=2<sup>n</sup> g tvoří konvergentní posloupnost, je to tedy nulová množina a podle předchozí věty je f integrovatelná (lze ukázat, že R 10<sup>f .x/ dxD</sup><sup><u>1</u></sup> 3<sup>).</sup> 

22 Výpoˇcet a vlastnosti Riemannova integrálu 

95 

### 22 Výpoˇcet a vlastnosti Riemannova integrálu 

Z praktického hlediska je pro výpočet Riemannova integrálu stěžejní následující tvrzení. 

■ Vˇeta 22.1 — Newtonova<sup>2</sup> –Leibnizova<sup>3</sup> formule. _Nechť funkce_ f _je integrovatelná na_ ha; bi _a nechť_ F _je spojitá funkce na_ ha; bi _a primitivní k_ f _na_ .a; b/ _. Pak_ 



<!-- Start of picture text -->
f .x/ dx D F.b/ � F.a/:<br>Zab<br><!-- End of picture text -->

_Důkaz._ Buď D 2 _D_ .ha; bi/. Protože funkce F je primitivní k f na .a; b/, má zde derivaci. Je navíc spojitá na ha; bi, tudíž splňuje oba předpoklady Lagrangeovy věty o střední hodnotě (věta 16.3). Pro každé i 2 f1; : : : ; ng tedy existuje �i 2 .xi�1; xi / takové, že F.xi / � F.xi �1/ D F<sup>0</sup> .�i /.xi � xi�1/ D f .�i /.xi � xi �1/. Označme � D f�1; �2; : : : ; �ng. Pak 



<!-- Start of picture text -->
n n<br>�.D; f; �/ D X f .�i /.xi � xi�1/ D X�F.xi / � F.xi �1/� D F.b/ � F.a/:<br>iD1 iD1<br><!-- End of picture text -->

To znamená, že pro libovolné D existuje výběr reprezentantů � takový, že �.D; f; �/ D F.b/ � F.a/. Nechť fDng<sup>1</sup> nD1<sup>je nyní libovolná nulová posloupnost dělení intervalu ha; bi. Ke každému Dnexistuje</sup> výběr reprezentantů �n takový, že �.Dn; f; �n/ D F.b/ � F.a/. Podle věty 21.14 



<!-- Start of picture text -->
Zab f .x/ dx D nlim!1 �.Dn; f; �n/ D n lim !1�F.b/ � F.a/� D F.b/ � F.a/:<br><!-- End of picture text -->

Poznámka 22.2. V dalším budeme používat označení ŒF.x/�<sup>b</sup> a<sup>WD F.b/ �F.a/. Jsou-li F; Gprimitivní</sup> funkce k f , pak podle věty 19.3 je G.x/ D F.x/ C c a tedy ŒG.x/�<sup>b</sup> a<sup>DŒF.x/ C c�b</sup> a<sup>D.F.b/ C c/ �</sup> .F.a/ C c/ D F.b/ � F.a/ D ŒF.x/�<sup>b</sup> a<sup>. To znamená, že formule z věty 22.1 nezávisí na výběru primitivní</sup> funkce. 



<!-- Start of picture text -->
Pˇríklad 22.3. Určete hodnotu integrálu R� 11 p 1 � x 2 dx.<br><!-- End of picture text -->

_Řešení._ Podle příkladu 19.16 je (po drobné úpravě) F.x/ D F.x/ D D<sup><u>1</u></sup> 2 



<!-- Start of picture text -->
Podle příkladu 19.16 je (po drobné úpravě) F.x/ D F.x/ D D 1 2 arcsin x C 4 1 sin.2 arcsin x/ a tedy<br>Z�11 p 1 � x 2 dx D � 12 arcsin x C 1 4 sin.2 arcsin x/ �1�1 D � 4 C 0 � �� � 4 � � 0 D � 2 :<br><!-- End of picture text -->

Poznámka 22.4. 1. (Integrace per-partes pro určitý integrál) Mají-li funkce u; v v intervalu ha; bi spojité derivace u<sup>0</sup> ; v<sup>0</sup> pak platí 



<!-- Start of picture text -->
u 0 .x/v.x/ dx D Œu.x/v.x/� b a � u.x/v 0 .x/ dx:<br>Zab Zab<br><!-- End of picture text -->

2. (Substituční metody pro určité integrály) 

- (i) Nechť funkce ' má spojitou derivaci na ha; bi, zobrazuje tento interval do intervalu I , platí '.a/ < '.b/ a funkce f je spojitá na I . Potom platí 



<!-- Start of picture text -->
f .'.x//' 0 .x/ dx D f .t/ dt:<br>Zab Z'.a/'.b/<br><!-- End of picture text -->

- (ii) Nechť f je spojitá funkce na intervalu ha; bi a nechť funkce ' má spojitou derivaci na uzavřeném intervalu I , je zde rostoucí a zobrazuje I na ha; bi. Pak platí 



<!-- Start of picture text -->
f .x/ dx D f .'.t//' 0 .t/ dt:<br>Zab Z'' � � 1 .a/1.b/<br><!-- End of picture text -->

> 2Isaac Newton 1643–1727, Angličan 

> 3Gottfried Wilhelm Leibniz 1646–1716, Němec 

Kapitola 3. Integrální poˇcet 

96 

Pˇríklad 22.5. Určete hodnotu integrálu R 1�1 ~~p~~ 1 � x<sup>2</sup> dx. _Řešení._ 



<!-- Start of picture text -->
x D sin t; dx D cos t dt<br>p 1 � x 2 dx D cos 2 t dt<br>Z�11 ˇˇˇˇ �1 ! ��=2; 1 ! �=2 ˇˇˇˇ D Z��=2�=2<br>D 2 1 Z��=2�=2.1 C cos 2t/ dt D 2 1 �t C 1 2 sin 2t ��=2��=2 D � 4 � �� � 4 � D � 2 :<br><!-- End of picture text -->

Vlastnosti Riemannova integrálu 

■ Vˇeta 22.6. _Nechť_ f _je integrovatelná na_ ha; bi _,_ c; d 2 R _,_ c � f .x/ � d _pro každé_ x 2 ha; bi _. Pak_ 



<!-- Start of picture text -->
c.b � a/ � f .x/ dx � d.b � a/:<br>Zab<br><!-- End of picture text -->

_Důkaz._ Tvrzení plyne ihned z věty 21.7, protože c � infff .x/ W x 2 ha; big, d � supff .x/ W x 2 ha; big. 

■ D˚usledek 22.7. a) _Je-li_ f _integrovatelná na intervalu_ ha; bi _a platí_ f .x/ � 0 _pro_ 8x 2 ha; bi _, pak_ 



<!-- Start of picture text -->
f .x/ dx � 0:<br>Zab<br><!-- End of picture text -->

b) _Je-li_ f _integrovatelná na_ ha; bi _a platí_ jf .x/j � c 8x 2 ha; bi _, pak_ 



<!-- Start of picture text -->
f .x/ dx<br>Zab<br>ˇˇˇˇˇ ˇˇˇˇˇ � c.b � a/:<br><!-- End of picture text -->

> ■ Vˇeta 22.8 — aditivita vzhledem k integrovaným funkcím. _Jsou-li_ f _a_ g _integrovatelné na_ ha; bi _, pak je i_ f C g _integrovatelná na_ ha; bi _a platí_ 



<!-- Start of picture text -->
�f .x/ C g.x/� dx D f .x/ dx C g.x/ dx:<br>Zab Zab Zab<br><!-- End of picture text -->

_Důkaz._ Nechť D D fx0; x1; x2; : : : ; xng 2 _D_ .ha; bi/ libovolné a označme mi D infff .x/ W x 2 hxi �1; xi ig, ni D inffg.x/ W x 2 hxi�1; xi ig, pi D infff .x/ C g.x/ W x 2 hxi�1; xi ig. Na intervalu hxi �1; xi i platí mi C ni � f .x/ C g.x/ a tedy mi C ni � pi , což znamená, že mi .xi � xi �1/ C ni .xi � xi �1/ � pi .xi � xi �1/ pro každé i 2 f1; dots; ng. Sečtením těchto nerovností pro i od 1 do n dostaneme s.D; f / C s.D; g/ � s.D; f C g/. Buď nyní fDng<sup>1</sup> nD1<sup>libovolná nulová posloupnost dělení intervalu</sup> ha; bi. Pak platí s.Dn; f / C s.Dn; g/ � s.Dn; f C g/ a limitním přechodem n ! 1 dostaneme podle věty 21.14, poznámky a) pod větou 7.6 a věty 7.9(ii) 



<!-- Start of picture text -->
f .x/ dx C g.x/ dx � �f .x/ C g.x/� dx:<br>Zab Zab Zab<br><!-- End of picture text -->

Analogicky odvodíme 

<u>�f .x/ C g.x/�</u> dx � f .x/ dx C g.x/ dx; Zab Zab Zab tedy musí být <u>R ba</u> �f .x/ C g.x/� dx D R ba <u>�f .x/ C g.x/�</u> dx D Ra b�f .x/ C g.x/� dx D R ba<sup>f .x/ dx C</sup> Ra b<sup>g.x/ dx.</sup> 

■ Vˇeta 22.9 — homogenita vzhledem k integrovaným funkcím. _Je-li_ f _integrovatelná na_ ha; bi _a_ c 2 R _, pak_ cf _je integrovatelná na_ ha; bi _a platí_ 



<!-- Start of picture text -->
cf .x/ dx D c f .x/ dx:<br>Zab Zab<br><!-- End of picture text -->

22 Výpoˇcet a vlastnosti Riemannova integrálu 

97 

_Důkaz._ Nechť D D fx0; x1; x2; : : : ; xng 2 _D_ .ha; bi/ libovolné a označme mi D infff .x/ W x 2 hxi�1; xi ig, Mi D supff .x/ W x 2 hxi �1; xi ig, ni D inffcf .x/ W x 2 hxi�1; xi ig, Ni D supfcf .x/ W x 2 hxi �1; xi ig. Pro c D 0 je tvrzení zřejmé. 

Nechť c > 0. Pak je ni D cmi , Ni D cMi , a tedy s.D; cf / D cs.D; f /, S.D; cf / D cS.D; f /. Vzhledem k větě 21.14 pro libovolnou nulovou fDng<sup>1</sup> nD1<sup>�</sup><sup>_D_.ha; bi/ platí</sup> 



<!-- Start of picture text -->
Zab cf .x/ dx D nlim!1 s.Dn; cf / D c n lim !1 s.Dn; f / D c Zab f .x/ dx;<br>Zab cf .x/ dx D nlim!1 S.Dn; cf / D c n lim !1 S.Dn; f / D c Zab f .x/ dx;<br><!-- End of picture text -->

z čehož plyne tvrzení věty. 

Nechť c < 0. Pak ni D cMi , Ni D cmi a tedy s.D; cf / D cS.D; f /, S.D; cf / D cs.D; f / a důkaz dokončíme analogicky s využitím nulové posloupnosti fDng<sup>1</sup> nD1<sup>�</sup><sup>_D_.ha; bi/.</sup> 

Poznámka 22.10. Riemannův integrál je tedy lineární transformací (funkcionálem) na lineárním prostoru všech riemannovsky integrovatelných funkcí do vektorového prostoru R. 

■ Vˇeta 22.11 — monotonie vzhledem k integrovaným funkcím. _Nechť_ f _a_ g _jsou integrovatelné na_ ha; bi _. Jestliže pro každé_ x 2 ha; bi _platí_ f .x/ � g.x/ _, pak_ 



<!-- Start of picture text -->
f .x/ dx � g.x/ dx:<br>Zab Zab<br><!-- End of picture text -->

_Důkaz._ Pro každé x 2 ha; bi je g.x/ � f .x/ � 0. Podle důsledku 22.7 a vět 22.8, 22.9 je 0 � R ba<sup>g.x/ �f .x/ dxD</sup> R ba<sup>g.x/ dx �</sup> R ba<sup>f .x/ dx.</sup> 

■ Vˇeta 22.12. (i) _Nechť_ f _a_ g _jsou integrovatelné na_ ha; bi _. Pak je také_ fg _integrovatelná na intervalu_ ha; bi _._ 

(ii) _Je-li navíc_ jg.x/j � c > 0 _pro každé_ x 2 ha; bi _, pak je také integrovatelná_ f=g _na_ ha; bi _._ 

_Důkaz._ ad (i) Nechť nejprve f .x/ � 0, g.x/ � 0 pro všechna x 2 ha; bi. Poněvadž funkce f a g jsou integrovatelné, jsou ohraničené, a tedy existuje k > 0 takové, že f .x/ � k, g.x/ � k pro x 2 ha; bi. Buď " > 0 libovolné. K číslu 2k"<sup>> 0 existují podle věty 21.17 dělení D1, D2intervalu ha; bi taková, že</sup> S.D1; f / � s.D1; f / < 2k"<sup>, S.D2; g/ �s.D2; g/ <</sup> 2k"<sup>. Položme DD fx0; x1; : : : ; xng D D1 [ D2.</sup> Podle lemmatu 21.4(ii) platí s.D1; f / � s.D; f /, S.D1; f / � S.D; f / a tedy S.D; f / � s.D; f / � S.D1; f / � s.D1; f / < 2k"<sup>. Podobně: S.D; g/ �s.D; g/ <</sup> 2k"<sup>. Označme</sup> 



<!-- Start of picture text -->
mi D infff .x/ W x 2 hxi�1; xi ig; Mi D supff .x/ W x 2 hxi�1; xi ig;<br>ni D inffg.x/ W x 2 hxi�1; xi ig; Ni D supfg.x/ W x 2 hxi�1; xi ig;<br>pi D infff .x/g.x/ W x 2 hxi �1; xi ig; Pi D supff .x/g.x/ W x 2 hxi �1; xi ig:<br><!-- End of picture text -->

Na intervalu hxi�1; xi i platí 0 � mi � f .x/ � Mi , 0 � ni � g.x/ � Ni a tedy mi ni � f .x/g.x/ � Mi Ni . Odtud dále plyne mi ni � pi � Pi � Mi Ni , neboli Pi � pi � Mi Ni � mi ni D Ni .Mi � mi / C mi .Ni � ni /. Poněvadž Ni � k, mi � k, platí Pi � pi � k..Mi � mi / C .Ni � ni //. Poslední nerovnost vynásobíme členem .xi � xi �1/ a takto vzniklé nerovnosti sečteme pro i D 1; 2; : : : ; n. Tím dostaneme S.D; fg/ � s.D; fg/ � k�S.D; f / � s.D; f / C S.D; g/ � s.D; g/� � k � 2k"<sup>C</sup> 2k" � D ", a tedy podle věty 21.17 je fg integrovatelná. 

Nechť nyní jsou f; g libovolné. Opět existuje k 2 R takové, že f .x/ � k, g.x/ � k pro všechna x 2 ha; bi. Podle vět 22.8 a 22.9 jsou funkce k � f .x/, k � g.x/ integrovatelné a nezáporné, a podle první části důkazu je integrovatelná i funkce h.x/ D .k � f .x//.k � g.x//. Poněvadž f .x/g.x/ D h.x/ C kf .x/ C kg.x/ � k<sup>2</sup> , je funkce fg podle vět 22.8 a 22.9 integrovatelná na ha; bi. 

ad (ii) Nechť g.x/ � c > 0 pro každé x 2 ha; bi. Buď " > 0 libovolné. K číslu c<sup>2</sup> " > 0 existuje podle věty 21.17 D D fx0; x1; : : : ; xng 2 _D_ .ha; bi/ takové, že S.D; g/ � s.D; g/ < c<sup>2</sup> ". Označme 

Kapitola 3. Integrální poˇcet 

98 

mi D inffg.x/ W x 2 hxi �1; xi ig, Mi D supfg.x/ W x 2 hxi�1; xi ig, ni D inf˚ g.x/1<sup>Wx2hxi�1; xii</sup> �, Ni D supf g.x/1<sup>Wx2hxi�1; xiig.PlatíniD</sup> M1i<sup>,NiD</sup> m1i<sup>,mi�c,Mi�c.Odtuddostaneme</sup> <u>1 1 1</u> Ni � ni D mi<sup>�</sup> Mi<sup>DM</sup> m<sup><u>i</u></sup> i<sup>�</sup> M<sup>m</sup> i<sup><u>i</u></sup> � c<sup>2.Mi�mi/.Tytonerovnicevynásobímečlenem.xi�xi�1/</sup> a sečteme pro i D 1; 2; : : : ; n. Dostaneme 



<!-- Start of picture text -->
S �D; g 1 � � s�D; g 1 � � c 12 .S.D; g/ � s.D; g// < ":<br><!-- End of picture text -->

Podle věty 21.17 je funkce g<sup><u>1</u>integrovatelná na ha; bi.</sup> 

Je-li g.x/ ��c < 0 pro každé x 2 ha; bi, je podle první části důkazu funkce �1=g integrovatelná na ha; bi, a tedy podle věty 22.9 je také 1=g integrovatelná na ha; bi. 

Tvrzení věty je nyní důsledkem výše dokázané části (i), neboť<sup><u>f</u></sup> g<sup>D f</sup> g<sup><u>1</u>.</sup> 

■ Vˇeta 22.13. _Je-li_ f _integrovatelná funkce na_ ha; bi _, pak také_ jf j _je integrovatelná na_ ha; bi _a platí_ 



<!-- Start of picture text -->
f .x/ dx jf .x/j dx:<br>Zab Zab<br>ˇˇˇˇˇ ˇˇˇˇˇ �<br><!-- End of picture text -->

_Důkaz._ Bud " > 0 libovolné. Protože f je integrovatelná, existuje podle věty 21.17 dělení D D fx0; x1; : : : ; xng 2 _D_ .ha; bi/ takové, že S.D; f / � s.D; f / < ". Označme mi D infff .x/ W x 2 hxi �1; xi ig, Mi D supff .x/ W x 2 hxi�1; xi ig, ni D inffjf .x/j W x 2 hxi �1; xi ig, Ni D supfjf .x/j W x 2 hxi �1; xi ig. Nechť x; y 2 hxi �1; xi i. Pak jf .x/j �jf .y/j �jf .x/ � f .y/j � Mi � mi . Odtud plyne, že pro pevně zvolené yi 2 hxi �1; xi i je jf .x/j �jf .yi /j C Mi � mi pro každé x 2 hxi �1; xi i. Z vlastností suprema plyne Ni �jf .yi /jCMi �mi , neboli jf .yi /j � Ni �.Mi �mi /. Z vlastností infima nyní plyne ni � Ni � .Mi � mi /, neboli Ni � ni � Mi � mi . Poslední nerovnost vynásobíme členem .xi � xi�1/ a sečteme přes i D 1; 2; : : : ; n. Dostaneme S.D; jf j/ � s.D; jf j/ � S.D; f / � s.D; f / < ", a tedy podle věty 21.17 je funkce jf j integrovatelná. 

Dále pro x 2 ha; bi platí f .x/ �jf .x/j, �f .x/ �jf .x/j a tedy podle věty 22.11 platí 

což znamená, že 



<!-- Start of picture text -->
�<br>f .x/ dx � jf .x/j dx; f .x/ dx � jf .x/j dx;<br>Zab Zab Zab Zab<br>�<br>jf .x/j dx � f .x/ dx � jf .x/j dx;<br>Zab Zab Zab<br><!-- End of picture text -->

a to je nerovnost v tvrzení věty. 

■ Vˇeta 22.14 — 1. vˇeta o stˇrední hodnotˇe integrálního poˇctu. _Nechť_ f _a_ g _jsou integrovatelné funkce na_ ha; bi _,_ g.x/ � 0 _pro každé_ x 2 ha; bi _,_ m D infff .x/ W x 2 ha; big _,_ M D supff .x/ W x 2 ha; big _. Pak existuje_ � 2 hm; M i _takové, že_ 



<!-- Start of picture text -->
f .x/g.x/ dx D � g.x/ dx:<br>Zab Zab<br><!-- End of picture text -->

_Důkaz._ Poněvadž m � f .x/ � M a g.x/ � 0, platí mg.x/ � f .x/g.x/ � Mg.x/ pro každé x 2 ha; bi, a tedy podle vět 22.11 a 22.9 je 



<!-- Start of picture text -->
m g.x/ dx � f .x/g.x/ dx � M g.x/ dx:<br>Zab Zab Zab<br><!-- End of picture text -->

Je-li Ra b<sup>g.x/ dxD 0, pak podle vět 22.11 a 22.9 je</sup> 



<!-- Start of picture text -->
0 � f .x/g.x/ dx � 0<br>Zab<br><!-- End of picture text -->

22 Výpoˇcet a vlastnosti Riemannova integrálu 

99 

a tedy R ba<sup>f .x/g.x/ dxD 0. Rovnost v tvrzení věty je splněna pro libovolné �2 R.</sup> Je-li R ba<sup>g.x/ dx> 0, položíme</sup> 



<!-- Start of picture text -->
R ba f .x/g.x/ dx<br>� D :<br>Ra b g.x/ dx<br><!-- End of picture text -->

Pak 



<!-- Start of picture text -->
m D m Ra b g.x/ dx � R ba f .x/g.x/ dx D � D R ba f .x/g.x/ dx � M R ba g.x/ dx D M:<br>R ba g.x/ dx R ba g.x/ dx R ba g.x/ dx R ba g.x/ dx<br><!-- End of picture text -->

■ D˚usledek 22.15. 1. _Nechť navíc k předpokladu věty 22.14 je funkce_ f _spojitá. Pak existuje_ c 2 ha; bi _takové, že_ 



<!-- Start of picture text -->
f .x/g.x/ dx D f .c/ g.x/ dx:<br>Zab Zab<br><!-- End of picture text -->

2. _Mají-li_ m _a_ M _stejný význam jako v předchozí větě, pak existuje_ � 2 hm; M i _takové, že_ 



<!-- Start of picture text -->
f .x/ dx D �.b � a/:<br>Zab<br><!-- End of picture text -->

_Důkaz._ ad 1. Tvrzení plyne ihned z druhé Bolzanovy věty, viz věta 13.15. 

ad 2. Tvrzení plyne ihned volbou g.x/ D 1 ve větě 22.14. 

■ Vˇeta 22.16 — aditivita vzhledem k integraˇcnímu oboru. _Nechť_ a; b; c 2 R _,_ a < c < b _a_ f _je funkce definovaná a ohraničená na_ ha; bi _. Pak platí_ 



<!-- Start of picture text -->
f .x/ dx D f .x/ dx C f .x/ dx; f .x/ dx D f .x/ dx C f .x/ dx:<br>Zab Zac Zcb Zab Zac Zcb<br><!-- End of picture text -->

_Je-li navíc_ f _integrovatelná na_ ha; ci _a_ hc; bi _, pak je integrovatelná i na_ ha; bi _a platí_ 



<!-- Start of picture text -->
f .x/ dx D f .x/ dx C f .x/ dx:<br>Zab Zac Zcb<br><!-- End of picture text -->

_Důkaz._ Nechť fDn<sup>�g1</sup> nD1<sup>jenulováposloupnostděleníintervaluha; ciafD</sup> n<sup>��gjenulováposloupnost</sup> dělení intervalu hb; ci. Pro každé n 2 N položme Dn D Dn<sup>�[ D</sup> n<sup>��. Pak je Dn2</sup><sup>_D_.ha; bi/, �.Dn/ D</sup> maxf�.Dn<sup>�/; �.D</sup> n<sup>��/g.Toznamená,želimn!1 �.Dn/D0,nebolifDng1</sup> nD1<sup>jenulováposloupnost</sup> dělení intervalu ha; bi. Dále s.Dn; f / D s.Dn<sup>�; f / C s.D</sup> n<sup>��; f /, S.Dn; f / D S.D</sup> n<sup>�; f / C S.D</sup> n<sup>��; f /,</sup> z čehož limitním přechodem pro n ! 1 s využitím věty 21.14 dostaneme první tvrzení. 

Je-li funkce f integrovatelná na intervalech ha; ci, hc; bi, pak podle první části platí 



<!-- Start of picture text -->
f .x/ dx D f .x/ dx C f .x/ dx D f .x/ dx;<br>Zab Zac Zcb Zab<br><!-- End of picture text -->

odkud okamžitě plyne druhé tvrzení. 

Poznámka 22.17. Větu lze indukcí zobecnit na libovolný konečný počet intervalů. 

■ Vˇeta 22.18 — monotonie vzhledem k integraˇcnímu oboru. _Nechť funkce_ f _je integrovatelná na_ ha; bi _a nechť_ hc; d i �ha; bi _. Pak je_ f _integrovatelná i na_ hc; d i _._ 

_Důkaz._ Předpokládejme, že hc; d i � .a; b/. Nechť fDn<sup>�g, resp. fD</sup> n<sup>��g, resp. fD</sup> n<sup>���</sup> g je nulová posloupnost dělení intervalu ha; ci, resp. hc; d i, resp. hd; bi. Pro každé n 2 N položme Dn D Dn<sup>�[ D</sup> n<sup>��</sup> [ Dn<sup>���</sup> . Pak je fDng<sup>1</sup> nD1<sup>nulová posloupnost dělení intervalu ha; bi a platí s.Dn; f / D s.D</sup> n<sup>�; f / C s.D</sup> n<sup>��; f / C</sup> 

Kapitola 3. Integrální poˇcet 

100 

s.Dn<sup>���</sup> ; f /, S.Dn; f / D s.Dn<sup>�; f /CS.D</sup> n<sup>��; f /CS.D</sup> n<sup>���</sup> ; f /. Odtud dostaneme limitním přechodem pro n ! 1 s využitím věty 21.14 



<!-- Start of picture text -->
f .x/ dx D f .x/ dx C f .x/ dx C f .x/ dx;<br>Zab Zac Zcd Zdb<br>f .x/ dx D f .x/ dx C f .x/ dx C f .x/ dx:<br>Zab Zac Zcd Zdb<br>Odečtením těchto rovností dostaneme<br>0 D f .x/ dx � f .x/ dx C f .x/ dx � f .x/ dx C f .x/ dx � f .x/ dx :<br>�Zac Zac � Zcd Zcd ! Zdb Zdb !<br><!-- End of picture text -->

Protože všechny sčítance jsou nekladné, musí být nulové, tj. máme <u>R dc</u><sup>f .x/ dxD</sup> Rc d<sup>f .x/ dx.</sup> Je-li c D a nebo d D b, vypadne pouze interval ha; ci nebo hc; d i, jinak je důkaz veden stejně. 

_Důkaz věty 21.21 (3. postačující podmínka pro integrovatelnost)._ Buď " > 0 libovolné. Poněvadž funkce f je na intervalu ha; bi ohraničená, existuje k > 0 takové, že �k � f .x/ � k pro každé x 2 ha; bi. Buď M množina bodů nespojitosti funkce f . Protože je tato množina nulová, existují čísla a1; a2; : : : ; an; b1; b2; : : : ; bn 2 R, a1 < b1 < a2 < b2 < ��� < an < bn taková, že M � .a1; b1/ [ .a2; b2/ [ ���[ .an; bn/ a<sup>Pn</sup> iD1<sup>.bi�ai/ <</sup> 2k"<sup>.</sup> 

Předpokládejme nejprve, že a < a1, bn < b. V takovém případě nespojitost funkce nemůže nastat v krajních bodech intervalu ha; bi. Na každém z intervalů ha; a1i ; hb1; a2i ; : : : ; hbn�1; ani ; hbn; bi je funkce f spojitá a tedy podle věty 21.19 integrovatelná. Na každém intervalu hai ; bi i, i D 1; 2; : : : ; n platí podle věty 21.7 



<!-- Start of picture text -->
�k.bi � ai / � f .x/ dx � f .x/ dx � k.bi � ai /:<br>Zabi i Zabi i<br><!-- End of picture text -->

Podle věty 22.16 (tvrzení můžeme indukcí zobecnit na libovolný konečný počet intervalů) je 



<!-- Start of picture text -->
n�1 n<br>f .x/ dx D f .x/ dx C f .x/ dx C X f .x/ dx C X f .x/ dx<br>Zab Zaa1 Zbnb iD1 Zbiai C1 i D1 Zabi i<br>n�1 n<br>� f .x/ dx C f .x/ dx C X f .x/ dx � k X.bi � ai /<br>Zaa1 Zbnb iD1 Zbiai C1 iD1<br>n�1<br>> Zaa1 f .x/ dx C Zbnb f .x/ dx C iXD1 Zbiai C1 f .x/ dx � k 2k "<br>n�1<br>D<br>Zaa1 f .x/ dx C Zbnb f .x/ dx C iXD1 Zbiai C1 f .x/ dx � 2 " :<br><!-- End of picture text -->

Analogicky ukážeme, že 

Odtud 



<!-- Start of picture text -->
n�1<br>Zab f .x/ dx < Zaa1 f .x/ dx C Zbnb f .x/ dx C iXD1 Zbiai C1 f .x/ dx C 2 " :<br>0 � f .x/ dx � f .x/ dx < ":<br>Zab Zab<br><!-- End of picture text -->

Protože ale " bylo libovolné, musí být R ba<sup>f .x/ dxD</sup> <u>R ba</u><sup>f .x/ dx.</sup> Pokud a D a1 (resp. bn D b), pak ve vyjádření <u>R ba</u><sup>f .x/ dx a</sup> R ba<sup>f .x/ dx vypadnou členy</sup> R aa 1 f .x/ dx (resp. Rb bn<sup>f .x/ dx), jinak je důkaz veden stejně.</sup> 

22 Výpoˇcet a vlastnosti Riemannova integrálu 

101 

Dále, je-li a1 < a < b1 a an < b < bn (jedná se o případ, kdy krajní body intervalu ha; bi jsou body nespojitosti funkce f ), pak platí na ha; b1i platí 



<!-- Start of picture text -->
�k.b1 � a1/ < �k.b1 � a/ � f .x/ dx � f .x/ dx � k.b1 � a/ < k.b1 � a1/<br>Zab1 Zab1<br><!-- End of picture text -->

a na han; bi platí 



<!-- Start of picture text -->
�k.bn � an/ < �k.b � an/ � f .x/ dx � f .x/ dx � k.b � an/ < k.bn � an/;<br>Zabn Zabn<br><!-- End of picture text -->

přičemž podobně jako výše je 



<!-- Start of picture text -->
n�1 n�1<br>f .x/ dx D X f .x/ dx C X f .x/ dx C f .x/ dx C f .x/ dx<br>Zab iD1 Zbiai C1 iD2 Zabi i Zab1 Zabn<br>n�1<br>> iXD1 Zbiai C1 f .x/ dx � 2 " ;<br>n�1<br>Zab f .x/ dx < iXD1 Zbiai C1 f .x/ dx C 2 " :<br><!-- End of picture text -->

Odtud opět dostaneme, že musí být Ra b<sup>f .x/ dxD</sup> <u>Ra b</u><sup>f .x/ dx.</sup> 

Konečně, pokud jeden z krajních bodů intervalu ha; bi je bodem nespojitosti a druhý není, jednalo by se o kombinaci výše uvedených případů. 

■ Vˇeta 22.19. _Nechť_ f; g _jsou ohraničené na_ ha; bi _a množina_ M D fx 2 ha; bi W f .x/ ¤ g.x/g _je nulová. Je-li jedna z funkcí_ f; g _integrovatelná na_ ha; bi _, je integrovatelná i druhá z nich a platí_ 



<!-- Start of picture text -->
f .x/ dx D g.x/ dx:<br>Zab Zab<br><!-- End of picture text -->

_Důkaz._ Nechť funkce f je integrovatelná a nechť " > 0 je libovolné. Buď k 2 R, k > 0 takové, že �k � g.x/ � k pro x 2 ha; bi (takové k jistě existuje, neboť f je podle předpokladu ohraničená). Poněvadž M je nulová, existují reálná čísla a1 < b1 < a2 < b2 < ��� < an < bn taková, že M � .a1; b1/ [ .a2; b2/ [ ���[ .an; bn/,<sup>Pn</sup> iD1<sup>.bi�ai/ <</sup> 2k"<sup>.</sup> 

Předpokládejme, že a < a1, b > bn (v ostatních případech by se důkaz mírně modifikoval jako v důkazu předchozí věty). Podle věty 22.18 je funkce f na každém z intervalu ha; a1i, hb1; a2i, hb2; a3i ; : : : ; hbn; bi integrovatelná. Na každém z těchto intervalů jsou funkce f; g shodné, tedy i g je na nich integrovatelná a platí 



<!-- Start of picture text -->
f .x/ dx D g.x/ dx; f .x/ dx D g.x/ dx; : : : ; f .x/ dx D g.x/ dx:<br>Zaa1 Zaa1 Zb1a2 Zb1a2 Zbnb Zbnb<br>Analogicky jako v důkazu věty 22.18 ukážeme, že<br>n�1<br>Zab g.x/ dx > Zaa1 f .x/ dx C Zbnb f .x/ dx C iXD1 Zbiai C1 f .x/ dx � 2 " ;<br>n�1<br>Zab g.x/ dx > Zaa1 f .x/ dx C Zbnb f .x/ dx C iXD1 Zbiai C1 f .x/ dx C 2 " ;<br><!-- End of picture text -->

Analogicky jako v důkazu věty 22.18 ukážeme, že 

z čehož plyne Ra b<sup>g.x/ dxD</sup> <u>Ra b</u><sup>g.x/ dxD</sup> Ra b<sup>f .x/ dx.</sup> 

Poznámka 22.20. Díky předchozí větě není při úvahách o Riemannově integrálu nutné předpokládat, že ohraničená funkce je definovaná na celém intervalu ha; bi. Stačí, je-li definovaná na ha; bi s výjimkou nulové množiny. Zejména lze tedy hovořit o funkci integrovatelné na otevřeném intervalu .a; b/. 

Kapitola 3. Integrální poˇcet 

102 

#### Pˇríklady k procviˇcení 

22.1. Vypočítejte určité integrály 



<!-- Start of picture text -->
dx dx p 3 x 2<br>a) Z02 x 2 C 4x C 5 I b) Z13 p 3 C 2x � x 2 I c) Z127 3 C p 3 x 2 dx:<br>Vypočítejte určitý integrál<br>1<br>Z�11 4 C x 2 dx<br><!-- End of picture text -->

22.2. Vypočítejte určitý integrál 

a poté jej zkuste spočítat ještě jednou pomocí substituce x D 1=t. Proč je výsledek jiný (kde nastala chyba)? 

_Výsledky._ 22.1. a) arctg<sup>2</sup> =9, b)<sup>�</sup> =6, c) 8 C<sup>3</sup> ~~p~~ 3�=2. 

### 23 Integrál jako funkce horní meze 

Integrovatelností funkce budeme v této kapitole stále myslet integrovatelnost v Riemannově smyslu. Rozšiřme nejprve pojem Riemannova integrál o případ, kdy se interval ha; bi, přes který integrujeme, degeneruje v bod, a o případ, kdy horní mez integrace je menší než dolní mez. 

Definice 23.1 — rozšíˇrená definice Riemannova integrálu. a) Nechť funkce f je definována v bodě a 2 R. Pak klademe 



<!-- Start of picture text -->
f .x/ dx WD 0:<br>Zaa<br><!-- End of picture text -->

b) Nechť a; b 2 R, a > b, a nechť f je integrovatelná na intervalu hb; ai. Pak klademe 



<!-- Start of picture text -->
f .x/ dx WD � f .x/ dx:<br>Zab Zba<br><!-- End of picture text -->

Při takto rozšířené definici všechny vlastnosti Riemannova integrálu zůstávají v platnosti. 

Poznámka 23.2. Vraťme se ještě k substituční metodě v určitém integrálu. V bodě 2(ii) poznámky 22.4 jsme předpokládali, že substituční funkce ' je rostoucí. Pokud je (při zachování zbývajících předpokladů) klesající, tak '<sup>�1</sup> .a/ > '<sup>�1</sup> .b/, a vzhledem k části b) předchozí definice dostaneme 



<!-- Start of picture text -->
f .x/ dx D f .'.t//' 0 .t/ dt D � f .'.t//' 0 .t/ dt:<br>Zab Z'' � � 1 .a/1.b/ Z'' � � 1 .b/1.a/<br><!-- End of picture text -->

Uvědomíme-li si navíc, že musí být '<sup>0</sup> .t/ � 0 pro každé t 2 I (a tedy �'<sup>0</sup> .t/ D j'<sup>0</sup> .t/j pro každé t 2 I ), lze oba případy sloučit do jednoho a tvrzení o substituci formulovat takto: 

Nechť f je funkce spojitá na intervalu ha; bi, ' je funkce, která zobrazuje interval h˛; ˇi na interval ha; bi, má na h˛; ˇi spojitou derivaci, přičemž '<sup>0</sup> .t/ ¤ 0 pro každé t 2 h˛; ˇi (tento předpoklad zaručí, že ' je na h˛; ˇi buď rostoucí, nebo klesající). Potom platí 



<!-- Start of picture text -->
f .x/ dx D f .'.t//j' 0 .t/j dt:<br>Zab Z˛ˇ<br><!-- End of picture text -->

Definice 23.3 — integrálu jako funkce horní meze. Nechť funkce f je integrovatelná na ha; bi. Funkci F definovanou pro x 2 ha; bi vztahem F.x/ D R xa<sup>f .t/ dtnazýváme</sup><sup>_integrál jako funkce horní meze_.</sup> 

Poznámka 23.4. Definice je korektní, protože je-li f integrovatelná na ha; bi, pak je podle věty 22.18 je funkce integrovatelná také na ha; xi, tj. hodnota F.x/ existuje. 

23 Integrál jako funkce horní meze 

103 

■ Vˇeta 23.5. _Nechť funkce_ f _je integrovatelná na_ ha; bi _. Pak_ F.x/ D R xa<sup>f .t/ dt</sup><sup>_je spojitá na_ha; bi</sup><sup>_._</sup> 

_Důkaz._ Nechť nejprve x0 2 .a; b/ (tj. x0 je vnitřní bod intervalu ha; bi) a " > 0 je libovolné. Protože f je integrovatelná, je ohraničená, tj. existuje c 2 R takové, že jf .x/j � c. K uvažovanému " vezměme ı tak, aby zároveň platilo ı < "=c, x0 C ı < b, a < x0 � ı (tedy platí Oı .x0/ �ha; bi). Nechť dále x 2 Oı .x0/ je libovolné. Pak 



<!-- Start of picture text -->
jF.x/ � F.x0/j D f .t/ dt � f .t/ dt f .t/ dt<br>ˇˇˇˇZax Zax0 ˇˇˇˇ D ˇˇˇˇZxx0 ˇˇˇˇ � cjx � x0j < cı < "<br><!-- End of picture text -->

(první nerovnost plyne z důsledku 22.7), tedy F je spojitá v bodě x0, a protože x0 bylo v intervalu .a; b/ voleno libovolně, je F spojitá na .a; b/. Zbývá ukázat, že F je spojitá v bodě a zprava, resp. v bodě b zprava. To by se provedlo analogicky jako v případě vnitřního bodu x0, pracujeme nyní pouze s pravým ı-okolím bodu a, resp. levým ı-okolím bodu b. 

■ Vˇeta 23.6. _Nechť funkce_ f _je integrovatelná na_ ha; bi _a spojitá v_ x0 2 ha; bi _. Pak_ F.x/ D R xa<sup>f .t/ dt</sup> _má derivaci v_ x0 _a platí_ F<sup>0</sup> .x0/ D f .x0/ _(je-li_ x0 D a _nebo_ x0 D b _, jedná se o příslušnou jednostrannou derivaci)._ 

_Důkaz._ Buď, stejně jako v předchozím důkazu, x0 vnitřní bod intervalu ha; bi a " > 0 libovolné. Protože f je podle předpokladu spojitá v x0, k " > 0 existuje ı > 0 takové, že platí Oı .x0/ �ha; bi a pro x 2 Oı .x0/ platí jf .x/ � f .x0/j < "=2. Tedy pro x 2 Oı<sup>�.x0/ platí</sup> 



<!-- Start of picture text -->
F .x/ � F .x0/ 1 � f .x0/.x � x0/<br>� f .x0/ f .t/ dt � f .t/ dt<br>ˇˇˇˇ x � x0 ˇˇˇˇ D ˇˇˇˇ x � x0 �Zax Zax0 � x � x0 ˇˇˇˇ<br>D 1 � f .x0/.x � x0/<br>f .t/ dt C f .t/ dt � f .t/ dt<br>ˇˇˇˇ x � x0 �Zax0 Zxx0 Zax0 � x � x0 ˇˇˇˇ<br>1<br>D<br>f .t/ dt � f .x0/ dt<br>ˇˇˇˇ x � x0 �Zxx0 Zxx0 �ˇˇˇˇ<br>1 1<br>D<br>.f .t/ � f .x0// dt jf .t/ � f .x0/j dt<br>jx � x0j ˇˇˇˇZxx0 ˇˇˇˇ � jx � x0j ˇˇˇˇZxx0 ˇˇˇˇ<br>1 " 1<br>� jx � x0j ˇˇˇˇZxx0 2 dt ˇˇˇˇ D jx � x0j jx � x0j 2 " < ";<br><!-- End of picture text -->

kde první nerovnost na posledním řádku plyne z důsledku 22.7. To znamená, že 



<!-- Start of picture text -->
F .x/ � F .x0/<br>lim D f .x0/:<br>x!x0 x � x0<br><!-- End of picture text -->

Podobně bychom ukázali existenci derivace zprava v bodě x0 D a a derivaci zleva v bodě x0 D b. 

Poznámka 23.7. Předchozí dvě tvrzení zůstanou v platnosti, i když zaměníme dolní mez integrace a za libovolné c 2 ha; bi, tj. F.x/ D R xc<sup>f .t/ dtjespojitánaha; biaje-lifspojitávx02ha; bi,pak</sup> F<sup>0</sup> .x0/ D f .x0/. 

■ D˚usledek 23.8. _Je-li_ f _spojitá na_ ha; bi _, pak_ F.x/ D Ra x<sup>f .t/ dt</sup><sup>_má na_ha; bi</sup><sup>_derivaci a platí zde_</sup> F<sup>0</sup> D f _._ 

_Důkaz věty 19.4._ Je-li interval I uzavřený, plyne tvrzení ihned z předchozího důsledku. Nechť tedy nyní I není uzavřený. Zvolme pevně c 2 I a položme F.x/ D R xc<sup>f .t/ dt. Funkce Fje definována na celém</sup> I , protože pro x 2 I je f spojitá na uzavřeném intervalu s krajními body c a x a tedy podle věty 21.19 integrovatelná. Bud nyní x0 2 I libovolné. Zvolme a; b 2 I tak, že a � minfc; x0g, b � maxfc; x0g. Pak c 2 ha; bi, x0 2 ha; bi a f je spojitá na ha; bi. Podle předchozí poznámky tedy platí F<sup>0</sup> .x0/ D f .x0/. Poněvadž x0 2 I byl libovolný, platí F<sup>0</sup> .x/ D f .x/ pro každé x 2 I . 

Kapitola 3. Integrální poˇcet 

104 

Poznámka 23.9. Je-li f integrovatelná na ha; bi, lze analogicky uvažovat integrál jako funkci dolní meze G.x/ D R bx<sup>f .t/ dt, nebo obecněji G.x/ D</sup> R cx<sup>f .t/ dtpro c2 ha; bi. Je-li fje integrovatelná na ha; bi,</sup> c 2 ha; bi, pak je G.x/ D R xc<sup>f .t/dtje spojitá na ha; bi. Je-li fspojitá v bodě x02 ha; bi, pak G v tomto</sup> bodě derivaci a platí G<sup>0</sup> .x0/ D �f .x0/. 

#### Pˇríklady k procviˇcení 

23.1. Určete funkci zadanou integrálem 



<!-- Start of picture text -->
1<br>a) Z1x t dt; b) Zx0 sin t dt; c) Zax t 2 dt; a 2 R:<br><!-- End of picture text -->

23.2. Napište derivaci funkce 



<!-- Start of picture text -->
sin t 1<br>a) F.x/ D dt; b) F.x/ D c) F.x/ D<br>Z0x t Z1ln x t dt; Zx1 2 t dt:<br><!-- End of picture text -->

23.3. Nalezněte lokální extrémy funkce 



<!-- Start of picture text -->
sin t<br>dt; x > 0:<br>Z0x t<br><!-- End of picture text -->

_Výsledky._ 23.1. a) ln x, b) cos x � 1, c) .x<sup>2</sup> � a<sup>3</sup> /=3. 23.2. a) .sin x/=x, b) 1=.x ln x/, c) �2x<sup>3</sup> . 23.3. Lokální maximum v bodech x D .2k C 1/�, lokální minimum v bodech x D 2k�, k 2 N. 

### 24 Nevlastní integrály 

Doposud jsme v případě Riemannova integrálu předpokládali: 

- (i) a; b 2 R, tj. interval ha; bi má konečnou délku, 

- (ii) f je ohraničená na ha; bi. 

Půjde o rozšíření na případ, kdy některý z těchto předpokladů není splněn. 

Nevlastní integrál I. druhu (vlivem meze) 

Definice 24.1 — nevlastního integrálu I. druhu. Nechť a 2 R a f je funkce definovaná na ha; 1/, přičemž je integrovatelná na každém intervalu ha; bi, kde b > a. Položme F.t/ D Ra t<sup>f .x/ dxpro</sup> t > a. Existuje-li vlastní limita limt !1 F.t/, pak říkáme, že _nevlastní integrál_ R 1a f .x/ dx _konverguje_ a klademe Ra 1 f .x/ dx D limt!1 F.t/. Pokud je tato limita nevlastní nebo neexistuje, tak říkáme, že _nevlastní integrál_ R 1a f .x/ dx _diverguje_ . 

Poznámka 24.2. Analogicky definujeme nevlastní integrál R a�1<sup>f .x/ dxpro funkci zadanou na .�1; ai</sup> a integrovatelnou na každém hb; ai, b < a. Je-li f integrovatelná na každém uzavřeném intervalu, pak definujeme R 1�1<sup>f .x/ dxWD</sup> R�1 a<sup>f .x/ dx C</sup> Ra 1 f .x/ dx, pokud oba integrály konvergují pro nějaké a 2 R (není těžké rozmyslet si, že hodnota integrálu nezávisí na volbě bodu a). 

Pˇríklad 24.3. Rozhodněte o konvergenci následujících integrálů. 



<!-- Start of picture text -->
1 1<br>a) Z11 x p dxI p 2 R; b) Z�11 1 C x 2 dxI c) Z01 cos x dx:<br><!-- End of picture text -->

_Řešení._ ad a) 



<!-- Start of picture text -->
1<br>Z11 x p dx<br><!-- End of picture text -->

24 Nevlastní integrály 

105 



<!-- Start of picture text -->
8t!1lim Œln x� 1 t D t!1 lim .ln t � ln 1/ D 1 pro p D 1;<br>1<br>D t !1lim Z1t x p dx D ˆˆˆ< lim x 1�p D lim t 1�p 1 D p�1 1 pro p > 1;<br>ˆˆˆ:t!1 " 1 � p #t1 t !1 1 � p � 1 � p ! (1 pro p < 1:<br><!-- End of picture text -->

Integrál tedy konverguje pro p > 1 a diverguje pro p � 1. 



<!-- Start of picture text -->
ad b) Pišme daný integrál jako I1 C I2, kde I1 D R 0�1 1C1x 2 dx a I2 D R 10 1C1x 2 dx. Potom<br>I1 D x!�1lim Zx0 1 C1 t 2 dt D x!�1lim Œarctg t� x 0 D � x!�1lim arctg x D 0 � �� � 2 � D � 2 :<br><!-- End of picture text -->

Protože integrand je sudou funkcí, musí být také I2 D<sup><u>�</u></sup> 2<sup>. Celkově tedy zadaný integrál konverguje a platí</sup> 



<!-- Start of picture text -->
1<br>Z�11 1 C x 2 dx D I1 C I2 D �:<br><!-- End of picture text -->



<!-- Start of picture text -->
ad c)<br><!-- End of picture text -->



<!-- Start of picture text -->
Z01 cos x dx D xlim!1 Z0x cos t dx D xlim!1 Œsin t� 0 x D x lim !1 sin x:<br><!-- End of picture text -->

Protože limx!1 sin x neexistuje, zadaný integrál diverguje. 



<!-- Start of picture text -->
■ Vˇeta 24.4 — srovnávací kritérium. Nechť platí  0 � f .x/ � g.x/  pro každé  x 2 ha; 1/ .<br>a) Konverguje-li Ra 1 g.x/ dx , pak konverguje i R 1a f .x/ dx .<br>b) Diverguje-li R 1a f .x/ dx , pak diverguje i Ra 1 g.x/ dx .<br><!-- End of picture text -->

_Důkaz._ Položíme-li F.x/ D Ra x<sup>f .t/ dtaG.x/D</sup> R xa<sup>g.t/ dt,pakprokaždéx2ha; 1/platí0�</sup> F.x/ � G.x/; to plyne ihned z důsledku 22.7 a věty 22.11. Funkce F a G jsou navíc na ha; 1/ neklesající. Skutečně, je-li x1; x2 2 ha; 1/, x1 < x2, pak 



<!-- Start of picture text -->
F.x2/ D f .t/ dt D f .t/ dt C f .t/ dt � f .t/ dt D F.x1/<br>Zax2 Zax1 Zxx12 Zax1<br><!-- End of picture text -->

(využili jsme zde vlastnosti z věty 22.16 a nezápornosti integrálu R xx12<sup>f .t/ dt). Analogicky pro funkci</sup> G. Díky monotonii funkcí F , G existují limity limx!1 F.x/ a limx!1 G.x/ (vlastní nebo nevlastní). Jedná se o analogickou vlastnost, kterou známe z posloupností, kdy monotónní ohraničená posloupnost má vlastní limitu a monotónní neohraničená posloupnost má nevlastní limitu. Přejdeme-li tedy k limitě v nerovnosti 0 � F.x/ � G.x/, dostáváme ihned tvrzení věty. 

■ Vˇeta 24.5 — nutná podmínka konvergence. _Nechť_ R 1a f .x/ dx _konverguje a nechť existuje_ limx!1 f .x/ D c 2 R _. Pak_ c D 0 _._ 

_Důkaz._ Sporem. Připusťme c > 0. Protože limx!1 f .x/ D c > 0, existují x0 � a a k > 0 taková, že pro 8x � x0 je f .x/ � k. Platí R 1x0<sup>k dxDlimt!1 k.x�x0/D1.Podlevěty24.4</sup> Rx 10<sup>f .x/ dx</sup> diverguje a tedy i R 1a f .x/ dx diverguje, což je spor s předpokladem. Je-li c < 0, postupujeme analogicky. 

Poznámka 24.6. V příkladu 24.3a) pro p � 0 nutná podmínka konvergence splněna není. 

Nevlastní integrál II. druhu (vlivem funkce) 

Definice 24.7 — singulárního bodu. Nechť a; b 2 R, a < b, a nechť funkce f je definována na ha; b/. Řekneme, že b je _singulární bod funkce_ f , jestliže f není ohraničená na ha; b/ a pro každé t 2 .a; b/ je integrovatelná na ha; ti. 

Kapitola 3. Integrální poˇcet 

106 

Definice 24.8 — nevlastního integrálu II. druhu. Nechť a; b 2 R, a < b, a nechť funkce f je definována na ha; b/, integrovatelná na každém ha; ti, kde t 2 .a; b/, a nechť b je jejím singulárním bodem. Položme F.t/ D R ta<sup>f .x/ dx. Existuje-li vlastní limita limt!b�F.t/, pak říkáme, že</sup><sup>_nevlastní integrál_</sup> R ba<sup>f .x/ dx</sup> _konverguje_ a klademe R ba<sup>f .x/ dxDlimt!b�F.t/ pro t2ha; b/. Pokud je tato limita nevlastní nebo</sup> neexistuje, říkáme, že _nevlastní integrál_ R ba<sup>f .x/ dx</sup><sup>_diverguje_.</sup> 

Poznámka 24.9. a) Analogicky definujeme singulární bod a pro funkci definovanou na intervalu .a; bi a konvergenci nebo divergenci nevlastního integrálu R ba<sup>f .x/ dx.</sup> 

b) Srovnávací kritérium lze analogicky formulovat i pro nevlastní integrály II. druhu. 



<!-- Start of picture text -->
Pˇríklad 24.10. Rozhodněte o konvergenci integrálu R 10 x1 p dx, p 2 R.<br><!-- End of picture text -->

_Řešení._ Pro p D 1 máme 



<!-- Start of picture text -->
1 1<br>Z01 x dx D t !lim0C Zt 1 x dx D t !lim0C Œln x�1 t D ln 1 � t ! lim 0C ln t D 0 � .�1/ D 1:<br><!-- End of picture text -->

Pro p ¤ 1 pak je 



<!-- Start of picture text -->
1<br>Z01 x p dx<br>1 1 1 1 pro p > 1;<br>D lim lim t D 1 � lim D 1<br>t !0C Zt 1 x p dx D 1 � p t!0C Œx1�p�1 1 � p � t !0C t 1�p � ( 1�p pro p < 1:<br><!-- End of picture text -->

Vidíme tedy, že integrál konverguje pro p < 1 a diverguje pro p � 1. 

#### Pˇríklady k procviˇcení 

24.1. Vyšetřete konvergenci následujících nevlastních integrálů prvního druhu a v případě, že integrál konverguje, určete jeho hodnotu: 



<!-- Start of picture text -->
a) Z01 x e �x2 dx; b) Z11 1arct C xg x 2 dx; c) Z�11 4 C1 x 2 dx:<br><!-- End of picture text -->

24.2. Vyšetřete konvergenci následujících integrálů druhého druhu a v případě, že integrál konverguje, určete jeho hodnotu: 



<!-- Start of picture text -->
1 e 1=x x<br>a) Z01 p 1 � x 2 dx; b) Z01 x 3 dx; c) Z12 p x � 1 dx:<br><!-- End of picture text -->

24.3. Pomocí srovnávacího kritéria rozhodněte, zda konverguje integrál 



<!-- Start of picture text -->
1<br>Z01 e x � cos x dx:<br><!-- End of picture text -->

_Výsledky._ 24.1. a)<sup>1</sup> =2, b)<sup>3�2</sup> =32, c)<sup>�</sup> =2. 24.2. a)<sup>�</sup> =2, b) diverguje, c)<sup>8</sup> =3. 24.3. Diverguje. 

### 25 Aplikace urˇcitého integrálu 

Prumˇerná hodnota (integrální pr˚umˇer) veliˇciny na intervalu 



<!-- Start of picture text -->
1<br>f D f .x/ dx (kde f je integrovatelná funkce):<br>b � a Zab<br><!-- End of picture text -->

25 Aplikace urˇcitého integrálu 

107 

Obsah rovinného obrazce 

1. Již víme (viz úvod kapitoly 21), že obsah křivočarého lichoběžníka 



<!-- Start of picture text -->
M C D ˚Œx; y� 2 R 2 W a � x � b; 0 � y � f .x/�;<br><!-- End of picture text -->

kde f je spojitá nezáporná funkce na ha; bi, je dán Riemannovým integrálem z funkce f přes interval ha; bi, tj. 



<!-- Start of picture text -->
S D f .x/ dx:<br>Zab<br><!-- End of picture text -->

Pokud bychom uvažovali křivočarý lichoběžník s nekladnou spojitou funkcí f , tj. množinu 



<!-- Start of picture text -->
M � D ˚Œx; y� 2 R 2 W a � x � b; f .x/ � y � 0�;<br><!-- End of picture text -->

pak integrál z funkce f přes interval ha; bi bude nekladné číslo, což znamená, že obsah množiny M<sup>�</sup> je dán jako 



<!-- Start of picture text -->
S D � f .x/ dx:<br>Zab<br><!-- End of picture text -->

Oba integrály lze chápat jako speciální případy, kdy obsah obecnějšího křivočarého lichoběžníka 

M D ˚Œx; y� 2 R<sup>2</sup> W a � x � b; f .x/ � y � g.y/�; 

kde f; g jsou spojité funkce na ha; bi, je dán integrálem 



<!-- Start of picture text -->
S D �g.x/ � f .x/� dx:<br>Zab<br><!-- End of picture text -->

2. Křivočarý lichoběžník určený nerovnostmi a � x � b, 0 � y � .t/, kde x D '.t/ je ryze monotónní na h˛; ˇi, má zde spojitou derivaci, a zobrazuje tento interval na ha; bi: 



<!-- Start of picture text -->
S D  .t/j' 0 .t/j dt:<br>Z˛ˇ<br> ˛ � ' � ˇ s hraniční křivkou �<br>S D 1 � 2 .'/ d':<br>2 Z˛ˇ<br><!-- End of picture text -->

3. Rovinný sektor v polárních souřadnicích vymezený ˛ � ' � ˇ s hraniční křivkou � D �.'/ (� spojitá): 

Pˇríklad 25.1. Určete obsah smyčky Descartesova listu x<sup>3</sup> C y<sup>3</sup> D 3axy, a > 0 (viz obrázek 25.1). 

_Řešení._ Převedeme úlohu do polárních souřadnic. Vztah mezi kartézskými a polárnímí souřadnicemi je x D � cos ', y D � sin '. Dosadíme-li toto vyjádření do rovnice křivky, dostaneme 

�<sup>3</sup> .cos<sup>3</sup> ' C sin<sup>3</sup> '/ D 3a�<sup>2</sup> cos ' sin ': 

Odtud 



<!-- Start of picture text -->
cos ' sin '<br>� D 3a ; 0 < ' < �<br>cos 3 ' C sin 3 ' 2<br>a podle vzorce 3 je obsah dán integrálem<br>9a 2 cos 2 ' sin 2 ' cos 2 ' sin 2 '<br>2 Z0�=2 .cos 3 ' C sin 3 '/ 2 d' D 9a 2 2 Z0�=2 cos 6 ' .1 C tg 3 '/ 2 d':<br><!-- End of picture text -->

a podle vzorce 3 je obsah dán integrálem 

Všimněme si, že integrand má singularitu v horní mezi, jedná se tedy o nevlastní integrál II. druhu. Substituce 1 C tg<sup>3</sup> ' D t převede integrál na nevlastní integrál I. druhu 



<!-- Start of picture text -->
3a 2 1 � 1 D 3a2 lim �1 C 1 D 3a2<br>2 Z11 t 2 dt D 3a 2 2 � t �11 2 �t !1 t � 2 :<br><!-- End of picture text -->

Obsah smyčky Descartesova listu tedy je S D<sup>3a2</sup> =24. 

Kapitola 3. Integrální poˇcet 

108 



<!-- Start of picture text -->
y<br>−a x<br>−a<br><!-- End of picture text -->

Obrázek 25.1: Smyčka Descartesova listu 

###### Délka rovinné kˇrivky 

1. Křivka je grafem funkce y D f .x/ na intervalu ha; bi (přičemž derivace f<sup>0</sup> je zde spojitá): 



<!-- Start of picture text -->
` D q 1 C .f 0 .x// 2 dx:<br>Zab<br><!-- End of picture text -->

2. Křivka op parametrizaci x D '.t/, y D .t/ na intervalu h˛; ˇi (přičemž '<sup>0</sup> ,<sup>0</sup> jsou zde spojité): 



<!-- Start of picture text -->
` D q .' 0 .t// 2 C .  0 .t// 2 dt:<br>Z˛ˇ<br><!-- End of picture text -->

3. Křivka je dána v polárních souřadnicích rovnicí � D �.'/, ˛ � ' � ˇ (přičemž �<sup>0</sup> je zde spojitá): 



<!-- Start of picture text -->
` D q � 2 .'/ C .� 0 .'// 2 d':<br>Z˛ˇ<br><!-- End of picture text -->

Předpoklady na derivace příslušných funkcí budou dále analogické. 

Objem tˇelesa vzniklého rotací kˇrivky 

1. Těleso vzniklé rotací křivky y D f .x/, a � x � b kolem osy x: 



<!-- Start of picture text -->
V D � f 2 .x/ dx:<br>Zab<br><!-- End of picture text -->

2. Těleso vzniklé rotací křivky o parametrických rovnicích x D '.t/, y D .t/, ˛ � t � ˇ kolem osy x: 



<!-- Start of picture text -->
V D � 2 .t/j' 0 .t/j dt:<br>Z˛ˇ<br><!-- End of picture text -->

Plocha pláštˇe rotaˇcního tˇelesa 

1. Těleso vzniklé rotací křivky y D f .x/, a � x � b kolem osy x: 



<!-- Start of picture text -->
P D 2� jf .x/j q 1 C Œf 0 .x/� 2 dx:<br>Zab<br><!-- End of picture text -->

2. Těleso vzniklé rotací křivky o parametrických rovnicích x D '.t/, y D .t/, ˛ � t � ˇ kolem osy x: 



<!-- Start of picture text -->
P D 2� j .t/j q Œ' 0 .t/� 2 C Œ  0 .t/� 2 dx:<br>Z˛ˇ<br><!-- End of picture text -->

25 Aplikace urˇcitého integrálu 

109 

#### Pˇríklady k procviˇcení 

25.1. Určete obsah rovinného obrazce ohraničeného křivkami: 



<!-- Start of picture text -->
a) y D 6x � x 2 ; y D 0I b) y D x 2 � 2x; y D xI c) y D x2 x:<br>4 ; y D 2 p<br><!-- End of picture text -->

25.2. Určete obsah rovinného obrazce ohraničeného křivkami: 

a) x D 3t<sup>2</sup> ; y D 3t � t<sup>3</sup> ; t 2 ˝� ~~p~~ 3; ~~p~~ 3˛I b) x D a.cos t C t sin t/; y D a.sin t � t cos t/; t 2 h0; 2�i ; polopřímka x D a, y � 0 .a > 0/: 

25.3. Určete obsah obrazce ohraničeného křivkou, jejíž rovnice v polárních souřadnicích je: 



<!-- Start of picture text -->
� �<br>a) � D a cos '; ' 2 .a > 0/I b) � D 3j sin.3'/j; ' 2 h0; 2�i :<br>D 2 ; � 2 E<br><!-- End of picture text -->

25.4. Určete délku křivky: 

a) y D ln x; x 2 ˝ ~~p~~ 3; ~~p~~ 8˛I b) y D arcsin x C ~~p~~ 1 � x<sup>2</sup> ; x 2 h�1; 1i : 

25.5. Určete délku jednoho oblouku epicykloidy, resp. hypocykloidy, jejíž parametrické rovnice jsou dány viz a), resp. viz b) (a > 0 je parametr): 

x D a�.n C 1/ cos t � cos..n C 1/t/�; x D a�.n � 1/ cos t C cos..n � 1/t/�; a) b) y D a�.n C 1/ sin t � sin..n C 1/t/�I y D a�.n � 1/ sin t � sin..n � 1/t/�: 

25.6. Určete délku a) oblouku hyperbolické spirály, b) prvního závitu logaritmické spirály: 



<!-- Start of picture text -->
a) � D a ; a > 0I b) � D a e ' ; ' 2 h0; 2�i :<br>' ; ' 2 D 32 ; 4 3 E<br><!-- End of picture text -->

_Výsledky._ 25.1. a) 36; b)<sup>9</sup> =2; c)<sup>16</sup> =3. 25.2. a)<sup>72</sup> ~~p~~ 3=5; b) .4�<sup>3</sup> C 3�/a<sup>2</sup> =3. 25.3. a) �a<sup>2</sup> =4; b) 9�=2. 25.4. a) 1C<sup>1</sup> =2 ln<sup>3</sup> =2; b) 4. 25.5. a)<sup>8a.nC1/</sup> =n; b)<sup>8a.n�1/</sup> =n. 25.6. a) a�.<sup>3</sup> ~~p~~ 13�10/=6Cln 6�ln.2C ~~p~~ 13/�; b) a ~~p~~ 2.e<sup>2�</sup> �1/. 

# Literatura 

- [1] Blaško, R., _Matematická analýza I_ , text UNIZA, 2014. 

- [2] Děmidovič, B. P., _Sbírka úloh a cvičení z matematické analýzy_ , Fragment, 2003. 

- [3] Došlá, Z., J. Kuben, J., _Diferenciální počet funkcí jedné proměnné_ , MUNI, Brno, 2004. 

- [4] Došlý, O., Zemánek, P., _Integrální počet v_ R, MUNI, Brno, 2011. 

- [5] Drábek, P., Míka, S., _Matematická analýza I_ , FAV ZČU, Plzeň, 1992. 

- [6] Eliaš, J., Horváth, J., Kajan, J., _Zbierka úloh z vyššej matematiky 2_ , 3. vyd., Alfa, Bratislava, 1996. 

- [7] Jarník, V., _Diferenciální počet I_ , 7. vyd., Academia, Praha, 1984. 

- [8] Jarník, V., _Integrální počet I_ , 6. vyd., Academia, Praha, 1984. 

- [9] Jirásek, F., Kriegelstein, E., Tichý, Z., _Sbírka řešených příkladů z matematiky_ , 3. vyd., SNTL, Praha, 1987. 

- [10] Kuben, J., Šarmanová, P., _Diferenciální počet funkcí jedné proměnné_ , VŠB TU, Ostrava, 2006. 

- [11] Novák, V., _Integrální počet v_ R, 3. vyd., MUNI, Brno, 2001. 

- [12] Pospíšil, Z., Půža, B., _Základy matematické analýzy v reálném oboru_ , text PřF MUNI, 2004. 

- [13] Škrášek, J., Tichý, Z., _Základy aplikované matematiky I_ , SNTL, Praha, 1983. 

- [14] Škrášek, J., Tichý, Z., _Základy aplikované matematiky II_ , SNTL, Praha, 1986. 

- [15] Tomeček, J., _Matematická analýza 1_ , PřF UPOL, Olomouc, 2020. 

- [16] Tomiczek, P., _Matematická analýza I_ , text FAV ZČU, 2006. 

- [17] Veselý, J., _Základy matematické analýzy I_ , 2. vyd., MatfyzPress, Praha, 2019. 

