

# Matematická analýza II 

Ludˇek Nechvátal 

Verze: 2025–02–21 

Pˇredmluva 

Předkládaný text slouží jako studijní opora k předmětu Matematická analýza II, který bezprostředně navazuje na předmět Matematická analýza I. Oba jsou vyučovány na Fakultě strojního inženýrství VUT v Brně pro studenty prvního ročníku oborů Matematické inženýrství a Fyzikální inženýrství. 

Látka se věnuje především diferenciálnímu a integrálnímu počtu funkce více proměnných (tedy zobrazení R<sup>n</sup> ! R, případně R<sup>n</sup> ! R<sup>m</sup> ). Uvedeny budou také základní poznatky z teorie křivkového a plošného integrálu. 

Proč se zabývat funkcemi více proměnných? V praxi je často třeba uvažovat veličiny, které závisejí na více než jedné proměnné, např. objem rotačního kužele závisí na poloměru podstavy r a výšce h, teplota v kovovém prutu může záviset na místě x a čase t, hustota tělesa se může měnit v závislosti na bodu X o souřadnicích Œx; y; z�, vektor síly f<sup>E</sup> D .f1; f2/ v rovině může záviset na souřadnicích bodu v rovině (tj. máme f<sup>E</sup> D �f1.x; y/; f2.x; y/�), apod. Uvedené naznačuje, že nám půjde o geometricko-fyzikální popis situace. 

Připomeňme, že v Matematické analýze I jsme množinu R chápali nejenom jako množinu nějakých prvků (reálných čísel), ale byla zde jasně dána algebraická struktura (sčítání, násobení, R je vybavena relací uspořádání, klíčový byl také axiom o suprému). Podobně, R<sup>n</sup> WD R � R ����� R (n-krát) nebude chápána pouze jako množina uspořádaných n-tic, ale jako množina, na které je zavedena určitá struktura. Zejména, součet každých dvou prvků X D Œx1; : : : ; xn� 2 R<sup>n</sup> , Y D Œy1; : : : ; yn� 2 R<sup>n</sup> je definován jako 



<!-- Start of picture text -->
X C Y D Œx1 C y1; : : : ; xn C yn� 2 R n<br><!-- End of picture text -->

a násobek libovolným skalárem c 2 R je pro každé X 2 R<sup>n</sup> definován jako 



<!-- Start of picture text -->
cX D Œcx1; : : : ; cxn� 2 R n :<br><!-- End of picture text -->

Lze ukázat, že R<sup>n</sup> s takto definovanými operacemi tvoří vektorový prostor dimenze n (viz předmět Lineární algebra). Prvky R<sup>n</sup> budeme nazývat buď body, nebo vektory (podle situace). Interpretujeme-li prvky X a Y jako body, pak rozdíl Y � X bude chápán jako vektor (to je v souladu s tím, co známe z analytické geometrie). 

Další podstatnou vlastností je, že v R<sup>n</sup> umíme měřit vzdálenosti bodů. Matematická abstrakce pojmu vzdálenosti dvou prvků nějaké množiny vedla ke vzniku teorie metrických prostorů, velmi stručný úvod do této teorie je obsahem první kapitoly. 

Pokud si čtenář bude chtít znalosti doplnit nad rámec probíraných statí nebo bude potřebovat více příkladů k procvičení, lze se inspirovat literaturou uvedenou na konci tohoto textu. 

Brno, únor 2023 

Autor 

# Obsah 

|**1**<br>**Úvo**|**d do metrických prostorů**|**7**|
|---|---|---|
|1|Metrika a metrický prostor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>7|
|2|Podmnožiny metrického prostoru . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>11|
|3|Konvergence v metrickém prostoru . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>12|
|4|Úplné a kompaktní metrické prostory . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>14|
|5|Zobrazení metrických prostorů . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|**2**<br>**Dife**|**renciální počet funkce více proměnných**|**21**|
|6|Funkce více proměnných, spojitost a limita<br>. . . . . . . . . . . . . . . . . . . . .|. . .<br>21|
|7|Parciální a směrová derivace, gradient . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>25|
|8|Totální diferenciál . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>29|
|9|Derivace složené funkce, Taylorův polynom . . . . . . . . . . . . . . . . . . . . .|. . .<br>33|
|10|Lokální a globální extrémy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>36|
|11|<br>Implicitní funkce, diferencovatelná zobrazení mezi prostory vyšší dimenze . . . . .|. . .<br>47|
|12|Vázané extrémy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>58|
|**3**<br>**Inte**|**grální počet funkce více proměnných**|**65**|
|13|Dvojný integrál . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>65|
|14|Alternativní přístup k definování dvojného integrálu . . . . . . . . . . . . . . . . .|. . .<br>70|
|15|Trojný integrál<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>74|
|16|Substituce (transformace) ve dvojném a trojném integrálu . . . . . . . . . . . . . .|. . .<br>76|
|17|Aplikace dvojného a trojného integrálu v mechanice . . . . . . . . . . . . . . . . .|. . .<br>81|
|**4**<br>**Kři**|**vkové a plošné integrály**|**83**|
|18|Křivky v rovině a prostoru . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>83|
|19|Křivkový integrál . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>85|
|20|<br>Nezávislost křivkového integrálu na integrační cestě . . . . . . . . . . . . . . . . .|. . .<br>92|
|21|Plochy v prostoru . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>97|
|22|Plošný integrál<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>98|



## Kapitola 1 

# Úvod do metrických prostor˚u 

### 1 Metrika a metrický prostor 

Definice 1.1 — metriky a metrického prostoru. Buď M ¤ ; libovolná množina a � W M � M ! h0; 1/ zobrazení, které pro všechna x; y; z 2 M splňuje 

(m1) �.x; y/ D 0 () x D y (axiom totožnosti), (m2) �.x; y/ D �.y; x/ (axiom symetrie), (m3) �.x; y/ � �.x; z/ C �.z; y/ (trojúhelníková nerovnost) Zobrazení � nazýváme _metrika na_ M , prvky množiny M nazýváme _body metrického prostoru_ .M; �/, číslo �.x; y/ nazýváme _vzdálenost bodů_ x; y. 



<!-- Start of picture text -->
1 pro x ¤ y<br>Pˇríklad 1.2. 1. Je-li M libovolná množina a �.x; y/ D , pak .M; �/ je metrický prostor<br>(0 pro x D y<br><!-- End of picture text -->

(nazývá se _diskrétní_ ). 

2. Je-li M D R, pak �.x; y/ D jx � yj je metrika. 

3. Je-li M D R<sup>n</sup> , x D Œx1; x2; : : : ; xn�, y D Œy1; y2; : : : ; yn� 2 R<sup>n</sup> , pak 



<!-- Start of picture text -->
�1.x; y/ D jx1 � y1j C jx2 � y2j C ���C jxn � ynj,<br>�2.x; y/ D p .x1 � y1/ 2 C .x2 � y2/ 2 C ���C .xn � yn/ 2 ,<br>�1.x; y/ D maxfjx1 � y1j; jx2 � y2j; : : : ; jxn � ynjg<br><!-- End of picture text -->

jsou metriky. Metrika �1 se nazývá _součtová (manhattanská, taxíkářská)_ , metrika �2 se nazývá _eukleidovská_<sup>1</sup> , metrika �1 se nazývá _maximální (šachovnicová, Čebyševova_<sup>2</sup> ). Axiomy (m1), (m2) zřejmě platí. Ověřme (m3). 

> � V případě metriky �1 máme 



<!-- Start of picture text -->
n n n<br>�1.x; z/ C �1.z; y/ D X jxi � zi j C X jzi � yi j D X.jxi � zi j C jzi � yi j/<br>iD1 i D1 i D1<br>n<br>� X jxi � zi C zi � yi j D �1.x; y/:<br>i D1<br><!-- End of picture text -->

- V případě metriky �2 vyjdeme z Cauchyho–Schwarzovy<sup>3</sup> nerovnosti (ta se někdy též nazývá Cauchyho–Buňakovského<sup>4</sup> –Schwarzova) 



<!-- Start of picture text -->
n v u n v u n<br>X ui vi � uX u 2 i � uX vi 2:<br>i D1 tiD1 ti D1<br><!-- End of picture text -->

> 1Eukleidés 3. stol. př.n.l., Řek žijící v Alexandrii v Egyptě 

> 2Pafnutij Lvovič Čebyšev 1821–1894, Rus 

Kapitola 1. Úvod do metrických prostor˚u 

8 

Položme ui D pi C qi , vi D qi . Potom 



<!-- Start of picture text -->
n v u n v u n<br>X.pi C qi /qi � uX.pi C qi / 2 � uX qi 2:<br>i D1 tiD1 tiD1<br><!-- End of picture text -->

Pokud naopak ui D pi , vi D pi C qi , tak 



<!-- Start of picture text -->
n v u n v u n<br>X pi .pi C qi / � uX pi 2 � uX.pi C qi / 2 :<br>iD1 tiD1 ti D1<br><!-- End of picture text -->

Sečtením pak dostaneme 



<!-- Start of picture text -->
n v u n v u n v u n<br>u 0u u 1<br>X.pi C qi / 2 � X.pi C qi / 2 � X pi 2 C X qi 2<br>i D1 tiD1 @tiD1 ti D1 A ;<br><!-- End of picture text -->

tj. 



<!-- Start of picture text -->
v u n v u n v u n<br>uX.pi C qi / 2 � uX pi 2 C uX qi 2 .Minkowského 5 nerovnost/:<br>tiD1 ti D1 tiD1<br><!-- End of picture text -->

Dosazením pi D xi � zi , qi D zi � yi máme 



<!-- Start of picture text -->
v u n v u n v u n<br>uX.xi � yi / 2 � uX.xi � zi / 2 C uX.zi � yi / 2 ; tj. �2.x; y/ � �2.x; z/ C �2.z; y/:<br>ti D1 ti D1 tiD1<br><!-- End of picture text -->

- Konečně, v případě metriky �1 označme j , resp. k, resp. `, ten index, pro který nastane maximum z hodnot jxi � zi j, resp. jzi � yi j, jxi � yi j, tj. 



<!-- Start of picture text -->
�1.x; z/ D maxfjxi � zi j W i D 1; 2; : : : ; ng D jxj � zj j;<br><!-- End of picture text -->



<!-- Start of picture text -->
�1.z; y/ D maxfjzi � yi j W i D 1; 2; : : : ; ng D jzk � ykj;<br>�1.x; y/ D maxfjxi � yi j W i D 1; 2; : : : ; ng D jx` � y`j:<br><!-- End of picture text -->

Potom 



<!-- Start of picture text -->
�1.x; z/ C �1.z; y/ D jxj � zj j C jzk � ykj<br><!-- End of picture text -->



<!-- Start of picture text -->
�jx` � z`j C jz` � y`j �jx` � z` C z` � y`j D jx` � y`j D �1.x; y/;<br><!-- End of picture text -->

tedy 



<!-- Start of picture text -->
�1.x; z/ C �1.z; y/ � �1.x; y/:<br><!-- End of picture text -->

4. Je-li M D C.ha; bi/ (množina všech funkcí spojitých na ha; bi), pak 



<!-- Start of picture text -->
�C .f; g/ D maxfjf .x/ � g.x/j W x 2 ha; big (metrika stejnoměrné konvergence);<br>�I .f; g/ D jf .x/ � g.x/j dx (integrální metrika)<br>� ab<br><!-- End of picture text -->

jsou metriky. Ověření axiomů (m1) a (m2) je opět triviální. Axiom (m3) lze v případě �C lze ověřit podobně jako v případě �1 na R<sup>n</sup> . V případě �I máme 



<!-- Start of picture text -->
�I .f; g/ D jf .x/ � g.x/j dx D jf .x/ � h.x/ C h.x/ � g.x/j dx<br>� ab � ab<br><!-- End of picture text -->

3Karl Hermann Amandus Schwarz 1843–1921, Němec 

> 4Viktor Jakovlevič Buňakovskij 1804–1889, Rus 

5Hermann Minkowski 1864–1909, německý Žid 

1 Metrika a metrický <u>prostor</u> 

9 



<!-- Start of picture text -->
� �jf .x/ � h.x/j C jh.x/ � g.x/j� dx<br>� ab<br>D<br>jf .x/ � h.x/j dx C jh.x/ � g.x/j dx D �I .f; h/ C �I .h; f /;<br>� ab � ab<br><!-- End of picture text -->

kde jsme využili trojúhelníkovou nerovnost pro absolutní hodnotu, monotonii vzhledem k integrovaným funkcím (viz věta 21.10 v Matematické analýze I) a aditivitu integrálu (integrál součtu je součet integrálů, viz věta 21.7 v Matematické analýze I). 

5. Je-li M D `<sup>1</sup> (množina všech ohraničených posloupností), pak 



<!-- Start of picture text -->
�1.fang; fbng/ D supfjan � bnj W n 2 Ng<br><!-- End of picture text -->

je metrika. Splnění axiomů (m1), (m2) je opět zřejmé. Axiom (m3) by se dokázal analogicky jako u �1 na R<sup>n</sup> . 

Definice 1.3 — otevˇrené a uzavˇrené koule, okolí. Nechť .M; �/ je metrický prostor, a 2 M , r 2 R<sup>C</sup> . Pak množina 



<!-- Start of picture text -->
Br .a/ WD fx 2 M W �.a; x/ < rg<br><!-- End of picture text -->

se nazývá _otevřená koule se středem_ a _a poloměrem_ r („ball“) a množina 



<!-- Start of picture text -->
Br Œa� WD fx 2 M W �.a; x/ � rg<br><!-- End of picture text -->

se nazývá _uzavřená koule se středem_ a _a poloměrem_ r. Speciálně: O".a/ WD B".a/ se nazývá _(epsilonové) okolí bodu_ a a O"<sup>�.a/ WD O".a/ n fag se nazývá</sup><sup>_ryzí (epsilonové) okolí bodu_a.</sup> 

Poznámka 1.4. Platí: " � ı H) O".a/ � Oı .a/. Není-li podstatná velikost poloměru ", budeme psát stručně O.a/. 

Pˇríklad 1.5. Načrtněte O".a/ v R<sup>2</sup> s metrikami �1, �2 a �1. Viz obrázek 1.1 (voleno a D Œ0; 0� a " D 1). 



<!-- Start of picture text -->
x 2 x 2 x 2<br>0 , 5 0 , 5 0 , 5<br>− 0 , 5 0 0 , 5 x 1 − 0 , 5 0 0 , 5 x 1 − 0 , 5 0 0 , 5 x 1<br>− 0 , 5 − 0 , 5 − 0 , 5<br><!-- End of picture text -->

Obrázek 1.1: Jednotková koule (se středem v počátku) v R<sup>2</sup> s metrikou �1, resp. �2, resp. �1 

Poznámka 1.6. Metriku na R<sup>n</sup> lze (obecněji) zavést pro libovolné p 2 h1; 1/ vztahem 



<!-- Start of picture text -->
�p.x; y/ D X jxi � yi j p :<br>iDn1 !1=p<br><!-- End of picture text -->

Jednotková „kružnice“ se středem v počátku pro případ n D 2 (tj. množina všech bodů mající jednotkovou vzdálenost od počátku v metrice �p) je načrtnuta pro několik hodnot parametru p na obrázku 1.2. Z tohoto obrázku je pak zřejmé, proč se maximální metrika značí indexem 1. 

Pozor, pro p < 1 výše uvedená funkce �p nepředstavuje metriku! 

Kapitola 1. Úvod do metrických prostor˚u 

10 



<!-- Start of picture text -->
x 2<br>0 , 5<br>− 0 , 5 0 0 , 5 x 1<br>p  = 10<br>p  = 4<br>− 0 , 5 p  = 2 , 5<br>p  = 1 , 5<br><!-- End of picture text -->

Obrázek 1.2: Jednotkové „kružnice“ v R<sup>2</sup> se středem v počátku pro p D 1:5, p D 2:5, p D 4 a p D 10 

Definice 1.7 — vzdálenosti dvou množin a pr˚umˇeru množiny. Nechť .M; �/ je metrický prostor. Pro neprázdné A; B � M definujeme: �.A; B/ WD inff�.a; b/ W a 2 A; b 2 Bg – _vzdálenost množin_ A; B, d.A/ WD supf�.x; y/ W x; y 2 Ag – _průměr množiny_ A. 

Jestliže množina f�.x; y/ W x; y 2 Ag není shora ohraničená, klademe d.A/ D 1. Vzdálenost bodu x od množiny A definujeme jako �.x; A/ WD �.fxg; A/. 

Poznámka 1.8. Je-li A \ B ¤ ;, pak zřejmě �.A; B/ D 0 (vzdálenost však může být nulová i pro A; B disjunktní). Je-li alespoň jedna z množin A; B prázdná, pak klademe jejich vzdálenost rovnu 1. Naopak průměr prázdné množiny klademe nulový, tj. d.;/ D 0. Tato konvence je přirozená vzhledem k vlastnosti U � V � R ) inf.U / � inf.V / a sup.U / � sup.V /. 

Definice 1.9. Buď .M; �/ metrický prostor, A � M . Řekneme, že A je _ohraničená_ , jestliže d.A/ < 1. 

Poznámka 1.10. Množina A je zřejmě ohraničená, jestliže existuje bod a a číslo r > 0 tak, že A � Br .a/. 

#### Pˇríklady k procviˇcení 

1.1. Nechť � je metrika na množině M . Ukažte, že pro každé x; y; z 2 M platí 



<!-- Start of picture text -->
j�.x; y/ � �.y; z/j � �.x; z/:<br><!-- End of picture text -->

1.2. Ověřte platnost axiomu (m3) pro metriku �C ze 4. bodu příkladu 1.2 a pro metriku �1 z 5. bodu příkladu 1.2. 

1.3. Ukažte, že zobrazení � definované jako 



<!-- Start of picture text -->
1<br>�.x; y/ D<br>ˇˇˇˇ x � y 1 ˇˇˇˇ<br><!-- End of picture text -->

je metrikou na R n f0g. 

1.4. Pomocí Cauchyho–Schwarzovy nerovnosti ukažte, že pro libovolný bod X D Œx1; x2; : : : ; xn� 2 R<sup>n</sup> platí 



<!-- Start of picture text -->
.x1 C x2 C ���C xn/ 2 � n.x1 2 C x 2 2 C ���C x n 2/:<br><!-- End of picture text -->



<!-- Start of picture text -->
1.5. Ukažte, že zobrazení � W R 2 ! R C 0 definované<br><!-- End of picture text -->



<!-- Start of picture text -->
�.x; y/ D �jx1 � y1j p C jx2 � y2j p�1=p<br><!-- End of picture text -->

2 Podmnožiny metrického prostoru 

11 

není metrikou na R<sup>2</sup> pro 0 < p < 1. 



<!-- Start of picture text -->
1.6. Určete vzdálenost posloupností a D f2 �n g 1 nD1 a b D f.�2/�ng1 nD1 v metrice<br><!-- End of picture text -->



<!-- Start of picture text -->
0 pro a D b;<br>�.a; b/ D<br>(1=k pro a ¤ b; kde k je nejmenší index takový, že ak ¤ bk:<br><!-- End of picture text -->

Ukažte také, že � je skutečně metrikou na množině všech posloupností. 

1.7. Pro x 2 h0; 1i určete hodnotu a 2 R tak, aby funkce f .x/ D ax měla nejmenší vzdálenost od funkce g.x/ D x<sup>2</sup> v integrální metrice �I . _Nápověda._ Pozor, integrand obsahuje absolutní hodnotu, je tedy potřeba provést diskuzi znaménka! 

1.8. Určete průměr množiny A D ff 2 C.h0; 1i/ W f .x/ D ax C b; jaj < 1; jbj < 1g v metrickém prostoru .C.h0; 1i/; �C /, resp. .C.h0; 1i/; �I /. 

_Výsledky._ 1.6. �.a; b/ D 1. 1.7. a D ~~p~~ 2=2. 1.8. d.A/ D 4 v metrice �C a d.A/ D 3 v metrice �I . 

### 2 Podmnožiny metrického prostoru 

Definice 2.1 — význaˇcných bod˚u v metrickém prostoru. Nechť .M; �/ je metrický prostor a A � M . Bod a 2 M se nazývá 

_vnitřní bod množiny_ A, jestliže existuje " > 0 takové, že O".a/ � A, _hraniční bod množiny_ A, jestliže pro každé " > 0 platí O".a/ \ A ¤ ; a zároveň O".a/ \ .M n A/ ¤ ;, _bod uzávěru množiny_ A, jestliže �.a; A/ D 0, _hromadný bod množiny_ A, jestliže pro každé " > 0 platí O"<sup>�.a/ \ A ¤ ;,</sup> _izolovaný bod množiny_ A, jestliže existuje " > 0 takové, že O".a/ \ A D fag. 

Definice 2.2 — vnitˇrku, hranice, uzávˇeru a derivace množiny. Nechť .M; �/ je metrický prostor a A � M . 

1. Množina všech vnitřních bodů množiny A se nazývá _vnitřek množiny_ A a značí se A<sup>ı</sup> , někdy int A (interior), 

2. Množina všech hraničních bodů množiny A se nazývá _hranice množiny_ A a značí se @A, někdy fr A (frontier), 

3. Množina všech bodů uzávěru množiny A se nazývá _uzávěr množiny_ A a značí se A, někdy cl A (closure), 

4. Množina všech hromadných bodů množiny A se nazývá _derivace množiny_ A a značí se A<sup>0</sup> . 

Pˇríklad 2.3. Uvažujte R s metrikou <u>�.x; y/</u> D jx � yj a množiny a) A D .0; 1/, b) A D h0; 1/ \ Q, c) A D h0; 1i [ f2g. Napište A<sup>ı</sup> , @A, A a A<sup>0</sup> . 

_Řešení._ ad a) A<sup>ı</sup> D A D .0; 1/, @A D f0; 1g, A D h0; 1i, A<sup>0</sup> D h0; 1i. ad b) A<sup>ı</sup> D ;, @A D h0; 1i, A D h0; 1i, A<sup>0</sup> D h0; 1i. ad c) A<sup>ı</sup> D .0; 1/, @A D f0; 1; 2g, A D h0; 1i [ f2g, A<sup>0</sup> D h0; 1i. 

Definice 2.4 — otevˇrené a uzavˇrené množiny v metrickém prostoru. Buď .M; �/ metrický prostor, A � M . Množina A se nazývá _otevřená_ , jestliže A<sup>ı</sup> D A, množina A se nazývá _uzavřená_ , jestliže A D A. 

■ Vˇeta 2.5. _Buď_ .M; �/ _metrický prostor,_ A � M _. Množina_ A _je otevřená_ () M n A _je uzavřená. Množina_ A _je uzavřená_ () M n A _je otevřená._ 

_Důkaz._ Ukažme nejprve, že pro každou A � M platí A<sup>ı</sup> D M n M n A. Skutečně, x 2 M n M n A () x … M n A () " WD �.x; M n A/ > 0 () .y 2 M n A/.�.x; y/ � "/ () O".x/ \ .M n A/ D ; () O".x/ � A () x 2 A<sup>ı</sup> . 

Kapitola 1. Úvod do metrických prostor˚u 

12 

Nechť A je otevřená, tj. A D A<sup>ı</sup> . Podle výše dokázaného tedy platí A D M n M n A. Odtud plyne, že M n A D M n .M n M n A/. Protože pro každou podmnožinu B � M platí M n .M n B/ D B, platí z předchozí rovnosti, že M n A D M n A, tj. M n A je uzavřená. 

Nechť naopak M n A je uzavřená, tj. M n A D M n A. Pak podle první části máme A<sup>ı</sup> D M n M n A D M n .M n A/ D A. 

Platnost druhého tvrzení by se ukázala analogicky. 

Poznámka 2.6. a) V každém metrickém prostoru .M; �/ pro libovolnou A <u>�</u> M zřejmě platí A<sup>ı</sup> � A � A. D Navíc lze ukázat, že <u>.A</u><sup>ı</sup> /<sup>ı</sup> D A<sup>ı</sup> , A A, a tedy A<sup>ı</sup> je vždy otevřená a A je vždy uzavřená. 

b) Obecně Br .a/ ¤ Br Œa�, např. je-li .M; �/ diskrétní, a 2 M , r D 1, potom B1.a/ D fag a tedy B1.a/ D fag, avšak B1Œa� D M . 

c) Platí ;<sup>ı</sup> D ;, protože když je množina prázdná, nemůže obsahovat žádné okolí bodu množiny M . Podobně platí ; D ;, protože kdyby existoval bod a 2 M s nulovou vzdáleností od ;, pak bychom byli ve sporu s poznámkou 1.8, kdy vzdálenost prázdné množiny od libovolné množiny je 1. Celkově tedy, ; je v jakémkoliv metrickém prostoru otevřená i uzavřená zároveň. Podle předchozí věty je pak celá M také otevřená i uzavřená zároveň. 

Definice 2.7 — indukované metriky a metrického podprostoru. Nechť .M; �/ je metrický prostor a A � M . Metriku �A, definovanou jako �A.x; y/ D �.x; y/ pro 8x; y 2 A, nazýváme _metrikou indukovanou na množině_ A _metrikou_ �. Metrický prostor .A; �A/ nazýváme _podprostorem metrického prostoru_ .M; �/. Píšeme .A; �A/ � .M; �/. 

Pˇríklad 2.8. Uvažujeme-li R jako podmnožinu R<sup>2</sup> (tj. reálná čísla ztotožníme s dvojicemi .a; 0/), pak každá z metrik �i (i D 1; 2; 1) na R<sup>2</sup> indukuje metriku �.x; y/ D jx � yj na R. 

#### Pˇríklady k procviˇcení 

2.1. Uveďte příklad takové množiny A � R, pro kterou jsou množiny A, A<sup>ı</sup> , A, ~~�~~ A ~~�~~ ı a A<sup><u>ı</u></sup> v metrickém prostoru .R; jx � yj/ vzájemně různé. 

2.2. Rozhodněte, zda množina A D ff 2 C.ha; bi/ W jf .x/j < 1 8x 2 ha; big je otevřená v metrickém prostoru .C.ha; bi/; �C /. 

_Výsledky._ 2.2. Ano. 

### 3 Konvergence v metrickém prostoru 

Definice 3.1 — konvergentní posloupnosti v metrickém prostoru. Buď .M; �/ metrický prostor a fxng<sup>1</sup> nD1<sup>posloupnost bodů z M(tj. zobrazení N ! M). Řekneme, že posloupnost fxng1</sup> nD1<sup>_konverguje_</sup> _k bodu_ x 2 M ( _je konvergentní v M_ ), jestliže limn!1 �.xn; x/ D 0 (zapisujeme limn!1 xn D x, stručně lim xn D x nebo xn ! x). 

Pˇríklad 3.2. 1. .M; �/ diskrétní (viz příklad 1.2.1): xn ! x () .9n0 2 N/.n � n0 H) xn D x/. 2. .R<sup>2</sup> ; �1/ (viz příklad 1.2.3): Œxn; yn� ! Œx; y� () xn ! x, yn ! y v R s metrikou �.x; y/ D jx � yj. 

_Důkaz._ 0 D lim.jxn � xj C jyn � yj/ D lim jxn � xj C lim jyn � yj. Protože, ale lim jxn � xj � 0, lim jyn � yj � 0, musí být lim jxn � xj D 0, lim jyn � yj D 0. 

Analogické tvrzení platí pro všechny metrické prostory z příkladu 1.2.3. 

3. .C.ha; bi/; �C / (viz příklad 1.2.4): 

   - fn ! f () .8" > 0/.9n0 2 N/.8n � n0/.8x 2 ha; bi/ W jfn.x/ � f .x/j < ". 

3 Konvergence v metrickém prostoru 

13 

Má-li posloupnost funkcí definovaných na intervalu ha; bi vlastnost uvedenou na pravé straně ekvivalence, řekneme, že posloupnost funkcí ffng<sup>1</sup> nD1<sup>_konverguje stejnoměrně_na ha; bi k funkci f .</sup> 

_Důkaz._ Konvergence fn ! f v .C.ha; bi/; �C / znamená: 

.8" > 0/.9n0 2 N/.8n � n0/ W �C .fn; f / < " () .8" > 0/.9n0 2 N/.8n � n0/ W maxfjfn.x/ � f .x/j W x 2 ha; big < " () .8" > 0/.9n0 2 N/.8n � n0/.8x 2 ha; bi/ W jfn.x/ � f .x/j < ". 

Definice 3.3 — ohraniˇcenosti posloupnosti. Buď .M; �/ metrický prostor a fxng<sup>1</sup> nD1<sup>posloupnost bodů</sup> z M . Řekneme, že posloupnost fxng<sup>1</sup> nD1<sup>_je ohraničená_, jestliže množina fxnW n 2 Ng je ohraničená ve</sup> smyslu definice 1.9. 

■ Vˇeta 3.4. _Buď_ .M; �/ _metrický prostor. Pak platí_ 

1. _Každá posloupnost_ fxng � M _má nejvýše jednu limitu v_ M _._ 

2. _Posloupnost konvergentní v_ .M; �/ _je ohraničená v_ .M; �/ _._ 

3. limn!1 xn D x 2 M () _pro každou posloupnost_ fxnk g _vybranou z_ fxng _platí_ limk!1 xnk D x _._ 

_Důkaz._ Plyne z příslušných tvrzení v kapitole o posloupnostech, viz Matematická analýza I. 

Definice 3.5 — cauchyovské posloupnosti. Buď .M; �/ metrický prostor a fxng<sup>1</sup> nD1<sup>posloupnost bodů</sup> z M . Řekneme, že posloupnost fxng<sup>1</sup> nD1<sup>je</sup><sup>_cauchyovská_,jestližekekaždému">0existujen02N</sup> takové, že pro všechna m; n � n0 je �.xm; xn/ < ". 

■ Vˇeta 3.6. _Nechť_ .M; �/ _je metrický prostor a_ fxng<sup>1</sup> nD1<sup>_posloupnost bodů z_M</sup><sup>_. Je-li_fxng1</sup> nD1<sup>_konvergentní_</sup> _v_ .M; �/ _, pak je cauchyovská._ 

- ZK _Důkaz._ Nechť xn ! x a " > 0 je libovolné. K 2<sup><u>"</u>existujen02Ntakové,žeprovšechnan�n0je</sup> �.xn; x/ < 2<sup><u>"</u>. Pro libovolné m �n0a libovolné n �n0tedy s využitím trojúhelníkové nerovnosti platí</sup> �.xm; xn/ � �.xm; x/ C �.xn; x/ < 2<sup><u>"</u>C</sup> 2<sup><u>"</u>D ".</sup> 

Poznámka 3.7. Obrácené tvrzení obecně neplatí. Např. pro M D .0; 1/, �.x; y/ D jx � yj, fxng<sup>1</sup> nD1<sup>D</sup> f1=ng<sup>1</sup> nD1<sup>je cauchyovská, ale není konvergentní (protože 0 … M).</sup> 

> ■ Vˇeta 3.8. _Nechť_ .M; �/ _je metrický prostor a_ A � M _. Množina_ A _je uzavřená v_ .M; �/ () _pro každou konvergentní posloupnost_ fxng � A _takovou, že_ xn ! x _, platí_ x 2 A _._ 

_Důkaz._ „H)“ Nechť A je uzavřená, tj. A D A a nechť fxng je libovolná posloupnost konvergující k x 2 M . Kdyby x … A, pak by " WD �.x; A/ > 0 a tedy pro každé xn by platilo �.xn; x/ � ", což by bylo ve sporu s xn ! x. 

„(H“ Nechť pro každou posloupnost fxng � A, pro kterou xn ! x, platí x 2 A. Buď y 2 A libovolný bod, tj. platí �.y; A/ D 0. Ke každému n<sup><u>1</u>>0 existuje xn2A takové, že �.xn; y/<</sup> n<sup><u>1</u>. To</sup> znamená, že pro takto vytvořenou posloupnost fxng <u>platí</u> lim �.xn; <u>y/</u> D 0, tj. xn ! y. Z podmínky plyne, že y 2 A. Tedy A � A. Protože však také A � A, máme A D A, tj. A je uzavřená. 

Definice 3.9 — ekvivalentních metrik. Nechť M je množina a �, � metriky na M . Řekneme, že � a � jsou _ekvivalentní metriky na_ M , jestliže pro každou posloupnost fxng<sup>1</sup> nD1<sup>�Mplatí: xn! x v .M; �/</sup> () xn ! x v .M; �/. 

Pˇríklad 3.10. a) Metriky �1, �2 a �1 na R<sup>n</sup> jsou ekvivalentní, protože pro každou z těchto metrik platí, že xk ! x () xi<sup>k! xiv .R; jx �yj/. To znamená, že xk! xv .Rn; �j /, kde j2 f1; 2; 1g ()</sup> .8" > 0/.9k0 2 N/.8k � k0/.8i 2 f1; 2; : : : ; ng/ W jxi<sup>k�xij < ".</sup> 

b) Metriky �I a �C na C.ha; bi/ nejsou ekvivalentní. 

Kapitola 1. Úvod do metrických prostor˚u 

14 

Poznámka 3.11. Jsou-li �; � ekvivalentní metriky na M , pak množina A � M je uzavřená v .M; �/ () je uzavřená v .M; �/ a je otevřená v .M; �/ () je otevřená v .M; �/. 

■ Vˇeta 3.12. _Buďte_ �; � _metriky na_ M _. Jestliže existují kladné konstanty_ a; b _takové, že pro všechny dvojice bodů_ Œx; y� 2 M<sup>2</sup> _je_ a�.x; y/ � �.x; y/ � b�.x; y/ _, pak jsou metriky ekvivalentní._ 

- ZK _Důkaz._ Nechť je splněna podmínka věty, x 2 M , a nechť fxng � M je taková posloupnost, že lim �.xn; x/ D 0. Pak a�.xn; x/ � �.xn; x/ � b�.xn; x/ a z věty o 3 posloupnostech (viz věta 7.13 v Matematické analýze I) plyne lim �.xn; x/ D 0. Pokud bychom vyšli z posloupnosti, pro kterou lim �.xn; x/ D 0, pak se důkaz provede stejně s využitím nerovnosti b<sup><u>1</u>�.x; y/��.x; y/�</sup> a<sup><u>1</u>�.x; y/,</sup> která je ekvivalentní s nerovností v podmínce věty. 

Poznámka 3.13. Pozor, obrácené tvrzení neplatí, tj. pokud jsou metriky � a � na M ekvivalentní, tak ještě nemusí platit vlastnost z věty 3.12. Např., metriky �, � na R definované �.x; y/ D jx � yj a �.x; y/ D minfjx � yj; 1g jsou ekvivalentní, ale neexistují kladné konstanty a; b takové, aby byla splněna podmínka věty 3.12. 

#### Pˇríklady k procviˇcení 

3.1. Na základě věty 3.8 ukažte, že množina A D ff 2 C.ha; bi/ W jf .x/j < 1 8x 2 ha; big nemůže být v metrickém prostoru .C.ha; bi/; �C / uzavřená (viz také cvičení 2.2) 

3.2. Na základě věty 3.12 rozhodněte, zda metriky �1, �2 a �1 jsou na R<sup>n</sup> vzájemně ekvivalentní. 

_Výsledky._ 3.2. Jsou, viz také příklad 3.10. 

### 4 Úplné a kompaktní metrické prostory 

Z předchozí sekce víme, že cauchyovská posloupnost v metrickém prostoru nemusí mít limitu v tomto prostoru. Jinak řečeno, obecně neplatí Cauchyovo–Bolzanovo kritérium konvergence. Prostory, ve kterých každá cauchyovská posloupnost konvergentní je, se nazývají úplné. 

Definice 4.1 — úplného metrického prostoru. Metrický prostor .M; �/ se nazývá _úplný_ , jestliže v něm každá cauchyovská posloupnost má limitu. 

Pˇríklad 4.2. 1. Prostor R s metrikou �.x; y/ D jx � yj je úplný. 

_Důkaz._ Tvrzení plyne ihned z Cauchyova–Bolzanova kritéria konvergence, viz věta 7.34 v Matematické analýze I. 

2. Prostory .R<sup>n</sup> ; �1/, .R<sup>n</sup> ; �2/, .R<sup>n</sup> ; �1/ jsou úplné. 

- _Důkaz._ V případě .R<sup>n</sup> ; �1/ cauchyovskost znamená, že pro k; m � k0 je<sup>Pn</sup> iD1<sup>jx</sup> i<sup>k�x</sup> i<sup>mj < ", z čehož</sup> plyne, že jxi<sup>k�x</sup> i<sup>mj<"8i2f1; 2; : : : ; ngatedykaždáfx</sup> i<sup>kg,iD1; 2; : : : ; n,jecauchyovská</sup> v .R; �1/. Podle Cauchyho–Bolzanova kritéria konvergence je však každá fxi<sup>kg také konvergentní, tj.</sup> lim xi<sup>kDxi, iD1; 2; : : : ; n. Odtud plyne, že limk!1 xkDxD.x1; x2; : : : ; xn/2Rn. Protože</sup> metriky �1; �2 a �1 jsou ekvivalentní, jsou úplné také prostory .R<sup>n</sup> ; �2/ a .R<sup>n</sup> ; �1/. 

- 3. Q s metrikou �.x; y/ D jx � yj není úplný. Např. ˚�1 C n<sup><u>1</u></sup> �n�1nD1<sup>je cauchyovská, ale konverguje</sup> k e … Q. 

4. Prostor �C.ha; bi/; �C � je úplný. 

_Důkaz._ Nechť ffng je cauchyovská posloupnost v prostoru .C.ha; bi/; �C /, tj. k "=2 (" > 0 je libovolné) existuje n0 2 N takové, že 8m; n � n0 platí 

max ˇˇfm.x/ � fn.x/ˇˇ < " a tedy ˇˇfm.x/ � fn.x/ˇˇ < " 8x 2 ha; bi : (�) x2ha;bi 2<sup>;</sup> 2 

4 Úplné a kompaktní metrické prostory 

15 

Jinými slovy, posloupnost funkčních hodnot ffn.x/g je cauchyovská pro každé x 2 ha; bi. Podle Cauchyho–Bolzanova kritéria pak ffn.x/g konverguje; limitu označme f .x/. Tím máme definovánu funkci f W ha; bi ! R, přičemž platí odhad 



<!-- Start of picture text -->
ˇˇfn.x/ � f .x/ˇˇ � " 8x 2 ha; bi :<br>2 < "<br><!-- End of picture text -->

Tuto nerovnost dostaneme tak, že v nerovnosti (�) provedeme limitní přechod m ! 1 (využíváme zde vlastnosti an < bn ) lim an � lim bn, pokud obě limity existují). Tato nerovnost nám tedy dává 



<!-- Start of picture text -->
max<br>ˇˇfn.x/ � f .x/ˇˇ < ";<br>x2ha;bi<br><!-- End of picture text -->

tj. posloupnost ffng konverguje v metrice �C (konverguje stejnoměrně na ha; bi). Zbývá ověřit, že limitní funkce f je na intervalu ha; bi spojitá, tj. že f 2 C.ha; bi/. Už víme, že posloupnost ffng konverguje stejnoměrně, tj. k "=3 existuje n1 2 N takové, že pro každé n � n1 a každé x 2 ha; bi platí jfn.x/ � f .x/j < "=3. Zároveň pro libovolně zvolené x0 2 ha; bi existuje ı > 0 takové, že pro jx � x0j < ı máme jfn.x/ � fn.x0/j < "=3, protože fn je spojitá v bodě x0. Celkově tedy 



<!-- Start of picture text -->
jf .x/ � f .x0/j D jf .x/ � fn.x/ C fn.x/ � fn.x0/ C fn.x0/ � f .x0/j<br>�jf .x/ � fn.x/j C jfn.x/ � fn.x0/j C jfn.x0/ � f .x0/j < 3 " C 3 " C 3 " D ":<br><!-- End of picture text -->

To ale znamená, že f je spojitá v bodě x0, a protože bod x0 byl volen libovolně, f je spojitá na ha; bi. 5. Prostor �C.ha; bi/; �I � není úplný. Stačí vzít např. posloupnost funkcí 



<!-- Start of picture text -->
8�1 pro x 2 h�1; �1=n/ ;<br>fn.x/ D nx pro x 2 h�1=n; 1=ni ;<br>ˆ<<br>ˆ:1 pro x 2 .1=n; 1i ;<br><!-- End of picture text -->

která je cauchyovská v �C.h�1; 1i/; �I �, ale limita není spojitá funkce, a tedy nepatří do C.h�1; 1i/. 

> ■ Vˇeta 4.3. _Je-li metrický prostor_ .M; �/ _úplný a množina_ A � M _je uzavřená, pak metrický prostor_ .A; �A/ _(_ �A _je metrika indukovaná metrikou_ � _) je úplný._ 

_Důkaz._ Buď fxng � A libovolná cauchyovská posloupnost. Poněvadž .M; �/ je úplný, existuje nlim!1<sup>xnD</sup> x 2 M . Podle věty 3.8 je však x 2 A. 

Podíváme-li se na důkaz I. Weierstrassovy věty (viz věta 12.11 v Matematické analýze I), stěžejním krokem bylo, že z posloupnosti bodů v uzavřeném intervalu je možné vybrat konvergentní podposloupnost. Tato vlastnost je podstatou tzv. kompaktních metrických prostorů. 

Definice 4.4 — kompaktního metrického prostoru a kompaktní množiny v metrickém prostoru. Řekneme, že metrický prostor .M; �/ je _kompaktní_ , jestliže z každé posloupnosti jeho bodů lze vybrat posloupnost konvergentní. Řekneme, že množina A � M je _kompaktní_ , jestliže podprostor .A; �A/ je kompaktní. 

■ Vˇeta 4.5. _Je-li_ A _kompaktní množina v metrickém prostoru_ .M; �/ _, pak je_ A _uzavřená a ohraničená v tomto prostoru._ 

_Důkaz._ Uzavřenost sporem: Připusťme, že A není uzavřená, tj. A ¤ A, tedy že existuje x 2 A n A. Protože �.x; A/ D 0, existuje posloupnost fxng � A tak, že �.xn; x/ ! 0, neboli xn ! x. Pro každou vybranou posloupnost fxnk g z posloupnosti fxng je podle věty 3.4.3 limk!1 xnk D x … A, což je spor s kompaktností A. 

Ohraničenost sporem: Připusťme, že A není ohraničená, tj. d.A/ D 1. Sestrojme posloupnost fxng takto. Bod x1 2 A vybereme libovolně a nechť x2 2 A je takové, že �.x1; x2/ � 1 (takové x2 jistě existuje, protože A je neohraničená). Bod x3 2 A vybereme tak, aby jeho vzdálenost od obou x1 a x2 byla 

Kapitola 1. Úvod do metrických prostor˚u 

16 

větší nebo rovna 1 (tento bod opět existuje z důvodu neohraničenosti). Pokračujeme tak, aby bod xn měl vzdálenost větší nebo rovnu jedna od všech předchozích bodů. Posloupnost fxng i každá posloupnost z ní vybraná není cauchyovská, neboť �.xn; xm/ � 1 pro 8m; n 2 N, m ¤ n, a tedy podle věty 3.6 nemůže být konvergentní. To je ale spor s kompaktností A. 

■ Vˇeta 4.6. _V prostorech_ .R<sup>n</sup> ; �i / _, kde_ i D 1; 2; 1 _, platí i opačné tvrzení. Máme tedy:_ A � R<sup>n</sup> _je kompaktní_ () _je v tomto prostoru uzavřená a ohraničená._ 

_Důkaz._ Nutnost podmínky plyne z věty 4.5. Dokažme její dostatečnost. Uvažujme nejprve metriku �1. Buď 



<!-- Start of picture text -->
fxkg 1 kD1 D ˚.x1 k; x 2 k; : : : ; x n k/ �1kD1<br><!-- End of picture text -->

libovolná posloupnost bodů z A. Poněvadž A je ohraničená, je každá z číselných posloupností 



<!-- Start of picture text -->
fxi kg1 kD1 ; i D 1; 2; : : : ; n<br><!-- End of picture text -->

také ohraničená, a tedy lze z každé z nich vybrat konvergentní podposloupnost 



<!-- Start of picture text -->
k`i<br>fxi g 1 `i D1<br><!-- End of picture text -->

konvergující k xi<sup>02 R, iD 1; 2; : : : ; n (viz věta 7.27 v Matematické analýze I). To znamená, že každá</sup> posloupnost fxkg<sup>1</sup> kD1<sup>�A má podvýběr konvergující k bodu x0D .x</sup> 1<sup>0; x</sup> 2<sup>0; : : : ; x</sup> n<sup>0/ 2 Rn. Protože však</sup> A je uzavřená, musí podle věty 3.8 být x<sup>0</sup> 2 A. Jinak řečeno, každá posloupnost z A obsahuje konvergentní podposloupnost s limitou v A, což je požadavek v definici kompaktnosti. Z ekvivalence metrik �1; �2 a �1 plyne tvrzení i pro prostory .R<sup>n</sup> ; �2/ a .R<sup>n</sup> ; �1/. 

■ Vˇeta 4.7. _Je-li metrický prostor_ .M; �/ _kompaktní, pak je úplný._ 

_Důkaz._ Buď fxng libovolná cauchyovská posloupnost v .M; �/. Poněvadž .M; �/ je kompaktní, existuje posloupnost fxnk g vybraná z fxng taková, že limk!1 xnk D x 2 M . Ukažme, že x D limn!1 xn. Buď " > 0 libovolné. Posloupnost fxnk g konverguje k x, což znamená, že k 2<sup><u>"</u>existuje k02N takové,</sup> že pro k � k0 je �.xnk ; x/ < 2<sup><u>"</u>. Protože fxng je cauchyovská, k</sup> 2<sup><u>"</u>> 0 existuje n12 N takové, že pro</sup> 8n; m � n1 platí �.xn; xm/ < 2<sup><u>"</u>. Položme n0D maxfn1; nk</sup> 0<sup>g a nechť n �n0a k�k0jsou libovolná</sup> čísla. Pak také nk � n0. S využitím trojúhelníkové nerovnosti dostaneme 



<!-- Start of picture text -->
�.xn; x/ � �.xn; xnk / C �.xnk ; x/ < 2 " C 2 " D ";<br><!-- End of picture text -->

což znamená, že nlim!1<sup>xnD x.</sup> 

#### Pˇríklady k procviˇcení 

4.1. Nechť � je metrika na R definována: 



<!-- Start of picture text -->
81 je-li jx � yj iracionální;<br>�.x; y/ D 1=2 je-li jx � yj racionální nenulové;<br>ˆ<<br>ˆ:0 je-li x D y:<br><!-- End of picture text -->

Rozhodněte, zda .R; �/ je úplný (rozmyslete si také, proč � je skutečně metrikou). 

4.2. Dokažte, že diskrétní metrický prostor .M; �/ je kompaktní () M je konečná. _Nápověda._ Implikaci „H)“ dokazujte sporem (připusťte, že M není konečná). 

_Výsledky._ 4.1. Je úplný. 

5 Zobrazení metrických prostor˚u 

17 

### 5 Zobrazení metrických prostor˚u 

Definice 5.1 — izometrického zobrazení. Nechť .M; �/ a .N; �/ jsou metrické prostory a F W M ! N je zobrazení (s D.F / D M , tj. zobrazení množiny M do N ). Zobrazení F se nazývá _izometrické_ , jestliže 8x; y 2 M platí 

�.F.x/; F.y// D �.x; y/: 

Poznámka 5.2. Izometrické zobrazení je vždy prosté (kdyby existovaly v M body x ¤ y takové, že F.x/ D F.y/, pak by podle (m1) a definice izometrie platilo 0 D �.F.x/; F.y// D �.x; y/ ¤ 0, což je spor). Je-li zobrazení také surjekce, pak existuje inverzní zobrazení F<sup>�1</sup> W N ! M (s D.F<sup>�1</sup> / D N ), které je opět izometrické (v takovém případě řekneme, že .M; �/ a .N; �/ jsou _izometrické prostory_ ). Např. všechna shodná zobrazení R<sup>2</sup> ! R<sup>2</sup> (posunutí, osová či středová souměrnost, otočení) jsou izometrická zobrazení. 

Definice 5.3 — spojitého zobrazení mezi metrickými prostory. Buďte .M; �/, .N; �/ metrické prostory a F W M ! N zobrazení. Řekneme, že F je _spojité v bodě_ x0 2 M , jestliže ke každému " > 0 existuje ı > 0 takové, že pro všechna x 2 Oı .x0/ v .M; �/ platí F.x/ 2 O".F.x0// v .N; �/. Řekneme, že zobrazení F _je spojité na_ M , jestliže je spojité v každém bodě x 2 M . 

■ Vˇeta 5.4 — Heineho podmínka. _Nechť_ .M; �/ _,_ .N; �/ _jsou metrické prostory. Zobrazení_ F W M ! N _je spojité v bodě_ x0 2 M () _pro každou posloupnost_ fxng<sup>1</sup> nD1<sup>_bodů z_M</sup><sup>_takovou, že_xn! x0</sup><sup>_v_.M; �/</sup><sup>_,_</sup> _platí_ F.xn/ ! F.x0/ _v_ .N; �/ _._ 

_Důkaz._ „H)“ Nechť F je spojité v bodě x0 a fxng � M je libovolná posloupnost konvergující k x0. Potřebujeme dokázat, že �.F.xn/; F.x0// ! 0. Nechť " > 0 je libovolné. Podle definice spojitosti zobrazení F v bodě x0 k "-ovému okolí bodu F.x0/ existuje ı-okolí bodu x0 takové, že pro každé x z tohoto okolí platí �.F.x/; F.x0// < ". Protože �.xn; x0/ ! 0, k číslu ı existuje n0 2 N takové, že pro každé n � n0 je �.xn; x0/ < ı, a tedy �.F.xn/; F.x0// < ". To znamená, že k libovolnému " > 0 jsme našli n0 2 N takové, že pro každé n � n0 platí �.F.xn/; F.x0// < ", tedy F.xn/ ! F.x0/. 

„(H“ Nechť x0 je libovolný bod a pro libovolnou posloupnost xn ! x0 platí F.xn/ ! F.x0/. Sporem: předpokládejme, že zobrazení f není spojité v bodě x0, tj. že existuje okolí O".F.x0// takové, že v každém okolí Oı .x0/ existuje x splňující F.x/ … O".F.x0//. Klademe-li postupně ı D<sup>1</sup> =n, pak v okolí Oı existuje bod xn takový, že F.xn/ … O".F.x0//. Tímto způsobem jsme sestrojili posloupnost fxng konvergující k x0, pro kterou F.xn/ nekonverguje k F.x0/ (neboť F.xn/ … O".F.x0// pro každé n 2 N), což je spor. Zobrazení F tedy musí být spojité v bodě x0. 

■ Vˇeta 5.5. _Nechť_ .M; �/ _,_ .N; �/ _jsou metrické prostory,_ A � M _a_ F W M ! N _spojité zobrazení na_ M _. Je-li množina_ A _kompaktní (v_ .M; �/ _), pak je i množina_ F.A/ _kompaktní (v_ .N; �/ _)._ 

_Důkaz._ Nechť A je kompaktní a buď fyng libovolná posloupnost bodů z F.A/. Ke každému yn 2 F.A/ existuje xn 2 A takové, že F.xn/ D yn. Poněvadž A je kompaktní, lze z posloupnosti fxng vybrat konvergentní podposloupnost fxnk g, tj. limk!1 xnk D x0 2 A v .M; �/. Označme y0 D F.x0/. Pak y0 2 F.A/ a podle Heineho podmínky limk!1 ynk D limk!1 F.xnk / D F.x0/ D y0 v .N; �/. Našli jsme tedy posloupnost fynk g vybranou z fyng konvergující k y0 2 F.A/. To znamená, že F.A/ je kompaktní množina. 

■ D˚usledek 5.6 — I. a II. Weierstrassova vˇeta. _Reálná funkce_ f _spojitá na uzavřeném intervalu je zde ohraničená a nabývá svého maxima a minima._ 

_Důkaz._ Uzavřený interval ha; bi je podle věty 4.6 kompaktní v .R; jx � yj/ a podle věty 5.5 je kompaktní také obraz f .ha; bi/. I. Weierstrassova věta nyní plyne z faktu, že kompaktní množina v každém metrickém prostoru je ohraničená (viz věta 4.5). II. Weierstrassova věta (tj. skutečnost, že f za daných předpokladů nabývá svého maxima a minima) plyne z následující úvahy. Protože f .ha; bi/ je ohraničená, existuje 

Kapitola 1. Úvod do metrických prostor˚u 

18 

supremum množiny f .ha; bi/. Z vlastnosti suprema plyne, že k 1=n existuje yn 2 f .ha; bi/ takové, že sup f .ha; bi/ � 1=n < yn, a tedy limn!1 yn D sup f .ha; bi/. Protože množina f .ha; bi/ je (opět podle věty 4.5) uzavřená, platí podle věty 3.8, že sup f .ha; bi/ 2 f .ha; bi/, tj. sup f .ha; bi/ D max f .ha; bi/. Analogicky by se ukázalo, že f nabývá na ha; bi i své nejmenší hodnoty. 

Definice 5.7 — stejnomˇernˇe spojitého zobrazení. Nechť .M; �/, .N; �/ jsou metrické prostory a F W M ! N zobrazení. Řekneme, že F je _stejnoměrně spojité na_ M , jestliže ke každému " > 0 existuje ı > 0 takové, že pro 8x; y 2 M splňující �.x; y/ < ı platí �.F.x/; F.y// < ". 

Poznámka 5.8. Stejnoměrně spojité zobrazení je spojité. 

> ■ Vˇeta 5.9 — Heineova–Cantorova. _Buď_ .M; �/ _kompaktní metrický prostor,_ .N; �/ _metrický prostor a_ F W M ! N _spojité zobrazení. Pak_ F _je stejnoměrně spojité._ 

_Důkaz._ Nechť .M; �/ je kompaktní a F W M ! N spojité. Sporem: připusťme, že F není stejnoměrně spojité. Pak existuje "0 > 0 takové, že ke každému ı > 0 existují x; y 2 M taková, že �.x; y/ < ı a �.F.x/; F.y// � "0. Položíme-li ı D n<sup><u>1</u>, pak to znamená, že existují xn; yntaková, že �.xn; yn/ < ı</sup> a �.F.xn/; F.yn// � "0. Protože M je kompaktní, lze z posloupnosti fxng<sup>1</sup> nD1<sup>vybrat podposloupnost</sup> fxnk g<sup>1</sup> kD1<sup>tak,želimk!1 xnkDx02M.Dáleplatí�.x0; ynk/��.x0; xnk/ C �.xnk; ynk/!0</sup> pro k ! 1, a tedy také limk!1 ynk D x0. Podle Heineho podmínky platí �.F.xnk /; F.ynk // � �.F.xnk /; F.x0// C �.F.x0/; F.ynk // ! 0 pro k ! 1, což je spor s �.F.x/; F.y// � "0. 

Definice 5.10 — lipschitzovského zobrazení a kontrakce. Buďte .M; �/, .N; �/ metrické prostory a F W M ! N zobrazení. Řekneme, že F je _lipschitzovské_ , jestliže existuje konstanta L > 0 taková, že pro 8x; y 2 M je �.F.x/; F.y// � L�.x; y/. Konstanta L se nazývá _Lipschitzova_<sup>6</sup> _konstanta_ . Řekneme, že zobrazení F je _kontrakce_ , je-li lipschitzovské s konstantou L < 1. 

■ Vˇeta 5.11. _Nechť_ .M; �/ _,_ .N; �/ _jsou metrické prostory a_ F W M ! N _zobrazení. Je-li_ F _lipschitzovské, pak je stejnoměrně spojité (a tedy také spojité)._ 

- ZK _Důkaz._ Nechť F je lipschitzovské s konstantou L. Buď " > 0 libovolné. Položme ı D "=L. Jsou-li x; y 2 M libovolné body takové, že �.x; y/ < ı, pak �.F.x/; F.y// � L�.x; y/ < Lı D L"=L D ". 

Pˇríklad 5.12. Buď f spojitá funkce na intervalu ha; bi, která má derivaci na .a; b/. Pak f je lipschitzovská na ha; bi () f<sup>0</sup> je na .a; b/ ohraničená. 

_Důkaz._ „(H“: Podle Lagrangeovy věty o střední hodnotě (viz věta 15.3 v Matematické analýze I) ke každým dvěma x; y 2 ha; bi existuje � 2 .x; y/ takové, že f .x/ � f .y/ D f<sup>0</sup> .�/.x � y/. Odtud jf .y/ � f .x/j D jf<sup>0</sup> .�/jjy � xj � Ljy � xj. 

„H)“: Protože f je lipschitzovská na ha; bi, platí jf .y/ � f .x/j � Ljy � xj pro x; y 2 ha; bi. Buď x 2 .a; b/ libovolné a y pišme ve tvaru y D x C h, kde h 2 .a � x; b � x/. Potom lze podmínku přepsat jako jf .x C h/ � f .x/j � Ljx C h � xj D Ljhj, což je v případě h ¤ 0 ekvivalentní podmínce 



<!-- Start of picture text -->
f .x C h/ � f .x/<br>ˇˇˇˇ h ˇˇˇˇ � L:<br>Odtud<br>f .x C h/ � f .x/ f .x C h/ � f .x/<br>lim<br>h!0 ˇˇˇˇ h ˇˇˇˇ D ˇˇˇˇh lim!0 h ˇˇˇˇ D jf 0.x/j � hlim!0 L D L;<br><!-- End of picture text -->

tj. f<sup>0</sup> je na .a; b/ ohraničená. 

6Rudolf Lipschitz 1832–1903, Němec 

5 Zobrazení metrických prostor˚u 

19 

Definice 5.13 — limity zobrazení mezi metrickými prostory. Buďte .M; �/, .N; �/ metrické prostory, F W M ! N zobrazení a x0 2 M hromadný bod množiny M . Řekneme, že zobrazení F má v bodě x0 2 M _limitu_ y0 2 N a píšeme limx!x0 F.x/ D y0, jestliže ke každému " > 0 existuje ı > 0 takové, že pro všechna x 2 Oı<sup>�.x0/ v .M; �/ platí F.x/ 2 O".y0/ v .N; �/.</sup> 

Poznámka 5.14. a) Pozor, limitu lze (narozdíl od spojitosti) uvažovat pouze v hromadných bodech množiny M ! 

b) Jestliže má zobrazení F v bodě x0 2 M limitu F.x0/, pak je v tomto bodě spojité. 

Definice 5.15 — pevného bodu zobrazení. Nechť M je množina a F W M ! M . Bod x 2 M se nazývá _pevný bod zobrazení_ F , jestliže F.x/ D x. 

■ Vˇeta 5.16 — Banachova<sup>7</sup> vˇeta o pevném bodu. _Nechť_ .M; �/ _je úplný metrický prostor a_ F W M ! M _kontrakce. Pak existuje jediný pevný bod zobrazení_ F _. Navíc, tento pevný bod je limitou posloupnosti_ fxng<sup>1</sup> nD1<sup>_, kde_x12 M</sup><sup>_je libovolný bod a_xnC1D F.xn/</sup><sup>_,_n D 1; 2; : : :</sup><sup>_._</sup> 

ZK _Důkaz._ a) Nejdříve ukažme, že posloupnost fxng je cauchyovská. Pro libovolné n 2 N platí 



<!-- Start of picture text -->
�.xn; xnC1/ D �.F.xn�1/; F.xn// � L�.xn�1; xn/<br>D L�.F.xn�2/; F.xn�1// � L 2 �.xn�2; xn�1/ D ���� L n�1 �.x1; x2/:<br><!-- End of picture text -->

Odtud a z (m3) plyne, že pro libovolná n; m 2 N platí 



<!-- Start of picture text -->
�.xn; xnCm/ � �.xn; xnC1/ C �.xnC1; xnC2/ C ���C �.xnCm�1; xnCm/<br>� L n�1 �.x1; x2/ C L n �.x1; x2/ C L nC1 �.x1; x2/ C ���C L nCm�2 �.x1; x2/<br>D .L n�1 C L n C L nC1 C ���C L nCm�2 /�.x1; x2/<br>D .1 C L C L 2 C ���C L m�1 /L n�1 �.x1; x2/ D 1 1  �  � L L m Ln�1�.x1; x2/ � Ln�1 �. 1 x  � 1; x L 2/ ! 0<br><!-- End of picture text -->

pro n ! 1, neboť L<sup>n�1</sup> ! 0 pro n ! 1, tj. fxng je cauchyovská. b) Protože .M; �/ je úplný, existuje limn!1 xn D x� 2 M . c) Ukažme, že x� je pevný bod F . Platí 



<!-- Start of picture text -->
�.x�; F.x�// � �.x�; xn/ C �.xn; F.x�//<br>D �.x�; xn/ C �.F.xn�1/; F.x�// � �.x�; xn/ C L�.xn�1; x�/ ! 0<br><!-- End of picture text -->

pro n ! 1, neboť 



<!-- Start of picture text -->
nlim!1 �.x�; xn/ D n lim !1 �.xn�1; x�/ D 0<br><!-- End of picture text -->

pro n ! 1. Tedy �.x�; F.x�// D 0 a podle (m1) je F.x�/ D x�. 

d) Jako poslední krok ukažme jednoznačnost pevného bodu. Předpokládejme, že existuje pevný bod x�� ¤ x� zobrazení F . Pak �.x��; x�/ D �.F.x��/; F.x�// � L�.x��; x�/. Odtud plyne, že .1 � L/�.x��; x�/ � 0 a poněvadž 0 < L < 1, musí být �.x��; x�/ D 0, tj. x�� D x�. 

#### Pˇríklady k procviˇcení 

5.1. Uvažujte metrické prostory .C.h�1; 1i/; �I / a .C.h�1; 1i/; �/, kde 



<!-- Start of picture text -->
�.f; g/ D x 2 jf .x/ � g.x/j dx:<br>� �11<br><!-- End of picture text -->

7Stefan Banach 1892–1945, Polák 

Kapitola 1. Úvod do metrických prostor˚u 

20 

Dále, nechť F W C.h�1; 1i/ ! C.h�1; 1i/ je zobrazení definované 



<!-- Start of picture text -->
F.f /.x/ D kf .x 3 /:<br><!-- End of picture text -->

Určete konstantu k tak, aby F bylo izometrické. 

5.2. Uvažujte metrické prostory .C.ha; bi/; �C /, .R; jx � yj/ a zobrazení F W C.ha; bi/ ! R definované 



<!-- Start of picture text -->
F.f / D f :<br>� a C2  b �<br><!-- End of picture text -->

Ukažte, že F je na C.ha; bi/ spojité. 

5.3. Ukažte, že Newtonova metoda 



<!-- Start of picture text -->
xnC1 D xn � f .xn/ n D 1; 2; : : :<br>f 0 .xn/ ;<br><!-- End of picture text -->

(tato metoda hledá numericky kořen rovnice f .x/ D 0) konverguje ke kořenu x� D ~~p~~ 3 pro funkci f .x/ D x<sup>2</sup> � 3 a libovolný startovací bod x1 2 h ~~p~~ 3; 1/. 

_Výsledky._ 5.1. k D ˙3. 

## Kapitola 2 

# Diferenciální poˇcet funkce více promˇenných 

### 6 Funkce více promˇenných, spojitost a limita 

Definice 6.1 — funkce n promˇenných. Zobrazení f W R<sup>n</sup> ! R nazveme _(reálnou) funkcí_ n _(reálných) proměnných_ . Množina D.f / WD fŒx1; x2; : : : ; xn� 2 R<sup>n</sup> W 9y 2 R tak, že Œx1; x2; : : : ; xn; y� 2 f g se nazývá _definiční obor_ funkce f , množina H.f / WD fy 2 R W 9Œx1; x2; : : : ; xn� 2 R<sup>n</sup> tak, že Œx1; x2; : : : ; xn; y� 2 f g se nazývá _obor hodnot_ . Zapisujeme: y D f .x1; x2; : : : ; xn/, stručně y D f .X/. Pro n D 2: z D f .x; y/, pro n D 3: u D f .x; y; z/, atp. _Grafem funkce_ n _proměnných_ nazveme množinu G.f / WD fŒX; f .X/� 2 R<sup>nC1</sup> W X 2 D.f /g. 

Poznámka 6.2. Není-li definiční obor zadán, považujeme za něj množinu všech X 2 R<sup>n</sup> , pro která má daný předpis smysl. 

Pˇríklad 6.3. Načrtněte D.f / funkce f .x; y/ D ~~p~~ sin.y � x/. 

_Řešení._ Jedinou podmínkou je nezápornost výrazu pod odmocninou, tj. definiční obor obdržíme z podmínky sin.y � x/ � 0. Ta je ekvivalentní podmínce 2k� � y � x � .2k C 1/�, k 2 Z. Máme tedy D.f / D fŒx; y� 2 R<sup>2</sup> W 2k� � y � x � .2k C 1/�; k 2 Zg, viz obrázek 6.1. 



<!-- Start of picture text -->
y<br>− 3 π −π π<br>− 2 π 0 2 π x<br><!-- End of picture text -->

Obrázek 6.1: Naznačení definičního oboru funkce f .x; y/ D ~~p~~ sin.y � x/ („pruhy“ se periodicky opakují) 

Pˇríklad 6.4. Načrtněte graf funkce f .x; y/ D ~~p~~ x<sup>2</sup> C y<sup>2</sup> . 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

22 

_Řešení._ Řezy plochy s rovinami rovnoběžnými se souřadnými rovinami xz a yz jsou hyperboly ležící (ve zmíněných souřadných rovinách pak přejdou v asymptoty těchto hyperbol). Řezy plochy s rovinami rovnoběžnými se souřadnou rovinou xy jsou pak kružnice se středem v počátku. Grafem je tedy polovina rotační kuželové plochy (hodnota z D f .x; y/ je podle zadání nezáporná) s osou rotace v ose z, viz obrázek 6.2. 



Obrázek 6.2: Kuželová plocha (graf funkce f .x; y/ D ~~p~~ x<sup>2</sup> C y<sup>2</sup> ) 

Uvažujeme-li na množině R<sup>n</sup> některou z ekvivalentních metrik �1, �2, �1 a na množině D.f / potom příslušnou indukovanou metriku, pak funkci n proměnných lze považovat za zobrazení metrického prostoru (D.f /; �i / na metrický prostor .H.f /; jx � yj/. O funkci f řekneme, že je spojitá (resp. stejnoměrně spojitá, resp. lipschitzovská), je-li toto zobrazení spojité (resp. stejnoměrně spojité, resp. lipschitzovské). Lze použít všechna tvrzení z předchozí kapitoly. Nebude-li řečeno jinak, budeme používat maximální metriku �1. V tomto případě 



<!-- Start of picture text -->
O.X/ D .x1 � "; x1 C "/ � .x2 � "; x2 C "/ ����� .xn � "; xn C "/<br><!-- End of picture text -->



<!-- Start of picture text -->
a O � .X/ D O.X/ n fX g.<br><!-- End of picture text -->

Limitu funkce n proměnných bychom zavedli jako v definici 5.13. Pokud chceme pojem rozšířit i na „nevlastní případ“, je potřeba uvažovat také okolí nevlastních bodů (nevlastním bodem rozumíme bod X D Œx1; : : : ; xn�, kde alespoň jedna složka xi D ˙1). Je-li X D Œx1; x2; : : : ; xn� 2 .R<sup>�</sup> /<sup>n</sup> nevlastní bod, pak klademe 



<!-- Start of picture text -->
O � .X/ D .a1; b1/ � .a2; b2/ ����� .an; bn/;<br><!-- End of picture text -->

kde 



<!-- Start of picture text -->
8xi � " pro xi 2 R 8xi C " pro xi 2 R<br>ai D �1 pro xi D �1 ; bi D 1 pro xi D 1; :<br>ˆ< ˆ<<br>ˆ:c 2 R pro xi D 1 ˆ:c 2 R pro xi D �1<br><!-- End of picture text -->

Okolí nevlastního bodů je vždy ryzí. Pokud X je nevlastní bod a pro každé okolí O.X/ platí O.X/\D.f / ¤ ;, pak X lze považovat za hromadný bod D.f /. 

Definice 6.5 — limity funkce **n** promˇenných. Nechť f W R<sup>n</sup> ! R je funkce a X0 je hromadný bod D.f /. Řekneme, že f má v bodě X0 limitu a 2 R<sup>�</sup> (píšeme limX!X0 f .X/ D a), jestliže ke každému okolí O.a/ existuje okolí O<sup>�</sup> .X0/ takové, že pro každé X 2 O<sup>�</sup> .X0/ \ D.f / platí f .X/ 2 O.a/. 

> ■ Vlastnosti . 1 _. Funkce_ f _má v_ X0 _nejvýše jednu limitu._ 

> 2 _. Má-li_ f _v bodě_ X0 _limitu_ a 2 R _, pak existuje_ O<sup>�</sup> .X0/ _takové, že_ f _je na_ O<sup>�</sup> .X0/ \ D.f / _ohraničená (funkci nazveme ohraničenou na množině_ A � D.f / _, je-li ohraničená množina_ f .A/ _coby podmnožina_ R _)._ 

> 3 _. Nechť_ lim f .X/ D 0 _a existuje_ O<sup>�</sup> .X0/ _takové, že funkce_ g _je na_ O<sup>�</sup> .X0/ \ D.f / _ohraničená. Pak_ X!X0 

lim f .X/g.X/ D 0: X!X0 

6 Funkce více promˇenných, spojitost a limita 

23 

- 4 _. Nechť_ lim f .X/ D a 2 R _,_ lim g.X/ D b 2 R _. Pak platí:_ lim jf .X/j D jaj _,_ lim .f .X/˙ X!X0 X!X0 X!X0 X!X0 

- g.X// D a ˙ b _,_ 

   - <u>f .X/</u> 

   - lim f .X/g.X/ D ab _, je-li navíc_ b ¤ 0 _, pak_ lim a � b _, je-li_ f .X/ � g.X/ 

   - X!X0 X !X0 g.X/<sup>Da</sup> b<sup>_,_</sup> _na nějakém_ O<sup>�</sup> .X0/ \ D.f / _._ 

- 5 _. Nechť existuje okolí_ O<sup>�</sup> .X0/ _takové, že pro každé_ X 2 O<sup>�</sup> .X0/ \ D.f / \ D.g/ \ D.h/ _platí_ f .X/ � g.X/ � h.X/ _. Jestliže_ lim f .X/ D lim h.X/ D a 2 R _, pak_ lim g.X/ D a _._ X!X0 X!X0 X!X0 

- 6 _. Limita složené funkce I: Nechť_ ' W R<sup>n</sup> ! R _,_ f W R ! R _jsou funkce a nechť_ X0 2 .R<sup>�</sup> /<sup>n</sup> _je hromadný bod definičního oboru složené funkce_ f ı ' _, přičemž_ lim '.X/ D a 2 R _a_ f _je spojitá v bodě_ a _._ X!X0 

- _Potom_ 



<!-- Start of picture text -->
lim f .'.X// D f � lim '.X/� D f .a/:<br>X!X0 X!X0<br><!-- End of picture text -->

- 7 _. Limita složené funkce II: Nechť_ ' W R<sup>n</sup> ! R _,_ f W R ! R _jsou funkce a_ X0 2 .R<sup>�</sup> /<sup>n</sup> _je hromadný bod definičního oboru složené funkce_ f ı ' _. Nechť dále_ limX!X0 '.X/ D b 2 R<sup>�</sup> _a existuje ryzí okolí_ O<sup>�</sup> .X0/ _takové, že_ '.X/ ¤ b _pro každé_ X 2 O<sup>�</sup> .X0/ \ D.'/ _. Konečně, předpokládejme, že_ limt !b f .t/ D a _. Potom_ 



<!-- Start of picture text -->
lim f .'.X// D a:<br>X!X0<br><!-- End of picture text -->

- 8 _. Heineho podmínka:_ lim f .X/ D a () 8fXng � D.f / _,_ Xn ! X0 _,_ Xn ¤ X0 _, platí_ f .Xn/ ! a _._ X!X0 

Výpočet limity funkce dvou a více proměnných obvykle není jednoduchý, zejména nemáme analogii l’Hospitalova pravidla! 

Pˇríklad 6.6. Vypočítejte 



<!-- Start of picture text -->
x C 7 x 2 � y 2 sin.x 2 C y 2 /<br>a) lim b) lim c) lim :<br>Œx;y�!Œ2;3� x � y C 2 ; Œx;y�!Œ1;1� x 3 � y 3 ; Œx;y�!Œ0;0� x 2 C y 2<br><!-- End of picture text -->

_Řešení._ a) Přímým dosazením (jedná se o podíl dvou polynomů prvního stupně) máme 



<!-- Start of picture text -->
x C 7<br>lim<br>Œx;y�!Œ2;3� x � y C 2 D 9:<br><!-- End of picture text -->

b) Úpravou výrazu: 



<!-- Start of picture text -->
x 2 � y 2 .x C y/.x � y/ x C y<br>lim lim lim<br>Œx;y�!Œ1;1� x 3 � y 3 D Œx;y�!Œ1;1� .x � y/.x 2 C xy C y 2 / D Œx;y�!Œ1;1� x 2 C xy C y 2 D 3 2 :<br><!-- End of picture text -->

c) V tomto případě lze danou limitu převést na limitu funkce jedné proměnné (k tomu nás opravňuje sedmý bod vlastností limity): 



<!-- Start of picture text -->
sin.x 2 C y 2 / sin t<br>lim D lim D 1:<br>Œx;y�!Œ0;0� x 2 C y 2 ˇˇˇ x2t C! y 02CD t ˇˇˇ D t !0C t<br><!-- End of picture text -->

xy x<sup>3</sup> <u>y</u> Pˇríklad 6.7. Dokažte, že limity a) lim b) lim Œx;y�!Œ0;0� x<sup>2</sup> C y<sup>2,</sup> Œx;y�!Œ0;0� x<sup>6</sup> C y<sup>2neexistují.</sup> _Řešení._ a) Uvažujeme-li funkci pouze nad svazkem přímek y D kx, k 2 R, pak limity funkce nad jednotlivými přímkami vedou na 



<!-- Start of picture text -->
kx 2 k k<br>lim<br>x!0 x 2 C k 2 x 2 D x lim !0 1 C k 2 D 1 C k 2 :<br><!-- End of picture text -->

Nad každou přímkou by tedy hodnota limity byla jiná, což je spor s jednoznačností limity. Limita tedy neexistuje. 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

24 

b) Vyzkoušíme-li podobně jako v příkladu a) svazek přímek y D kx, zjistíme, že všechny limity funkce nad těmito přímkami jsou nulové. To nám existenci limity nevyvrátí, ale ani nepotvrdí. Podobně, svazek parabol y D kx<sup>2</sup> také vede na nulové limity. Až svazek kubických parabol y D kx<sup>3</sup> , k 2 R vede na 



<!-- Start of picture text -->
kx 6 k k<br>lim<br>x!0 x 6 C k 2 x 6 D x lim !0 1 C k 2 D 1 C k 2 ;<br><!-- End of picture text -->

což existenci limity vyloučí. 

Pˇríklad 6.8. Vyšetřte limitu 



<!-- Start of picture text -->
3x 2<br>lim<br>Œx;y�!Œ0;0� y 2 � 5x C 3y :<br><!-- End of picture text -->

_Řešení._ Metodou svazku přímek y D kx, k 2 R dostaneme 



<!-- Start of picture text -->
3x 2 3x 0 pro k ¤ 5=3;<br>lim<br>x!0 k 2 x 2 � 5x C 3kx D x lim !0 k 2 x � 5 C 3k D (27=25 pro k D 5=3:<br><!-- End of picture text -->

Protože pro jednu přímku vychází hodnota limity jinak než pro ostatní, limita zadané funkce neexistuje. 

Pˇríklad 6.9. Vyšetřete limitu 



<!-- Start of picture text -->
Œx;y�!limŒ1;1� .x2 C y2/ e�.xCy/ :<br><!-- End of picture text -->

_Řešení._ Platí 

0 � .x<sup>2</sup> C y<sup>2</sup> / e<sup>�.xCy/</sup> D x<sup>2</sup> e<sup>�x</sup> e<sup>�y</sup> Cy<sup>2</sup> e<sup>�x</sup> e<sup>�y</sup> � x<sup>2</sup> e<sup>�x</sup> Cy<sup>2</sup> e<sup>�y</sup> 8x � 0; 8y � 0: 

Protože 



<!-- Start of picture text -->
t 2 2t 2<br>t!1lim t 2 e�t D t!1 lim e t D t !1 lim e t D t !1 lim e t D 0 .použili jsme 2x l’Hospitalovo pravidlo/;<br><!-- End of picture text -->

funkce x<sup>2</sup> e<sup>�x</sup> Cy<sup>2</sup> e<sup>�y</sup> na pravé straně druhé nerovnosti konverguje k nule pro Œx; y� ! Œ1; 1�. Podle věty o třech limitách je tedy limita zadané funkce také nula. 

■ Vˇeta 6.10. _Funkce_ f W R<sup>2</sup> ! R _má v bodě_ Œx0; y0� _limitu_ a 2 R _, jestliže existuje_ r<sup>�</sup> > 0 _a funkce_ g W .0; 1/ ! h0; 1/ _taková, že_ limr!0C g.r/ D 0 _a_ jf .x0 C r cos '; y0 C r sin '/ � aj � g.r/ _pro každé_ r 2 .0; r<sup>�</sup> / _a každé_ ' 2 h0; 2�/ _._ 

ZK _Důkaz._ Buď " > 0 libovolné. Protože limr!0C g.r/ D 0, existuje 0 < ı < r<sup>�</sup> takové, že pro 8r 2 .0; ı/ platí 0 � g.r/ < ". Uvažujeme-li na R<sup>2</sup> metriku �2, pak také 8Œx; y� 2 Oı<sup>�.Œx0; y0�/ platí jf .x; y/�aj <</sup> ", tj. 



<!-- Start of picture text -->
Œx;y�!limŒx0;y0� f .x; y/ D a:<br><!-- End of picture text -->



<!-- Start of picture text -->
x 2 C .y � 1/ 2 y<br>Pˇríklad 6.11. Vyšetřete lim<br>Œx;y�!Œ0;1� x 2 C .y � 1/ 2 .<br><!-- End of picture text -->

_Řešení._ Máme 

Odtud, 



<!-- Start of picture text -->
x 2 C .y � 1/ 2 y D r 2 C r 3 sin3 ' D 1 C r sin 3 ':<br>x 2 C .y � 1/ 2 ˇˇˇˇˇxDr cos '; yD1Cr sin ' r 2<br>ˇˇ 1„ C rƒ‚ sin 3 …' � „ƒ‚…1 ˇˇ � „ƒ‚…r ! 0 pro r ! 0:<br>f .r cos ';1Cr sin '/ a g.r/<br><!-- End of picture text -->

Hledanou limitou je tedy číslo 1. 

7 Parciální a smˇerová derivace, gradient 

25 

Poznámka 6.12. Vztah spojitosti a limity v bodě je nyní následující. Funkce f W R<sup>n</sup> ! R je v bodě X0 2 D.f / spojitá, jestliže limX!X0 f .X/ D f .X0/. Jsou-li všechny body D.f / hromadné, tak platí i opačné tvrzení. 

#### Pˇríklady k procviˇcení 

6.1. Načrtněte D.f / funkcí 



<!-- Start of picture text -->
a) f .x; y/ D p 4 � x 2 C q 1 � y 2 ; b) f .x; y/ D q 1 � .x 2 C y/ 2 ;<br>c) f .x; y; z/ D q 1 � x 2 � y 2 � z 2 :<br><!-- End of picture text -->

6.2. Pomocí metody řezů načrtněte G.f / funkcí 



<!-- Start of picture text -->
1<br>a) f .x; y/ D b) f .x; y/ D 2 � q x 2 C y 2 :<br>2x 2 C 3y 2 ;<br><!-- End of picture text -->

6.3. Vyšetřete následující limity: 



<!-- Start of picture text -->
4x 2 � 3y 2 .x C y/ 2 � 4<br>a) lim b) lim<br>Œx;y�!Œ0;0� 2x 2 C 3y 2 ; Œx;y�!Œ�1;�1� x C y C 2 ;<br>x 2 � y 2 x C y<br>c) lim d) lim<br>Œx;y�!Œ2;2� x 2 C 3x � 3y � xy ; Œx;y�!Œ1;1� x 2 � xy C y 2<br>(využijte nejprve substituce u D 1=x, v D 1=y a poté substituci do polárních souřadnic);<br><!-- End of picture text -->



<!-- Start of picture text -->
1 sin xy<br>e) lim f) lim ;<br>Œx;y�!Œ0;0� xy2 cos x 2 y ; Œx;y�!Œ0;2� x<br>1 � cos.x 2 C y 2 /<br>g) lim<br>Œx;y�!Œ0;0� .x 2 C y 2 /x 2 y 2 ;<br><!-- End of picture text -->

6.4. Zjistěte, zda funkce f je spojitá v bodě Œ0; 0�: 



<!-- Start of picture text -->
xy 2<br>pro Œx; y� ¤ Œ0; 0�;<br>f .x; y/ D x 2 Cy 2<br>(0 pro Œx; y� D Œ0; 0�:<br><!-- End of picture text -->

_Výsledky._ 6.3. a) neexistuje; b) �4; c) 4=5; d) 0; e) 0; f) 2; g) 1. 6.4. Je. 

### 7 Parciální a smˇerová derivace, gradient 

Definice 7.1 — parciálních derivací funkce dvou promˇenných. Nechť f W R<sup>2</sup> ! R je funkce a Œx0; y0� je vnitřní bod D.f /. Položme '.x/ D f .x; y0/. Má-li funkce ' derivaci v bodě x0, nazýváme tuto derivaci _parciální derivací funkce_ f _podle proměnné_ x _v bodě_ Œx0; y0� (značíme fx<sup>0.x0; y0/ nebo fx.x0; y0/ nebo</sup> @f @x<sup>.x0; y0/. To znamená, že</sup> 



<!-- Start of picture text -->
'.x0 C h/ � '.x0/ f .x0 C h; y0/ � f .x0; y0/<br>fx 0 .x0; y0/ D lim D lim :<br>h!0 h h!0 h<br><!-- End of picture text -->

Podobně, má-li funkce .y/ D f .x0; y/ derivaci v bodě y0, nazýváme tuto derivaci _parciální derivací funkce_ f _podle proměnné_ y _v bodě_ Œx0; y0� (značíme fy<sup>0.x0; y0/ nebo fy.x0; y0/ nebo@</sup> @y<sup><u>f</u>.x0; y0/).</sup> Má-li funkce f parciální derivace podle x ve všech bodech nějaké množiny M � D.f /, je tato parciální derivace sama funkcí (značíme fx<sup>0, fx,@</sup> @x<sup><u>f</u>), analogicky pro f</sup> y<sup>0.</sup> 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

26 



<!-- Start of picture text -->
Poznámka 7.2. a) Analogicky pro f W R n ! R definujeme fx 0 i .X0/ WD ' i 0 .x i 0/, kde<br>'i .xi / WD f .x1 0; x 2 0; : : : ; x i 0 �1 ; xi ; x i 0 C1 ; : : : ; x n 0/:<br><!-- End of picture text -->

b) Pravidlo pro výpočet je snadné, derivujeme jako funkci jedné proměnné, ostatní proměnné považujeme za parametry. 

c) Lze tedy použít všechna pravidla pro derivování jako u funkce jedné proměnné. 

d) Pozor, v případě funkce jedné proměnné platilo, že funkce mající derivaci v bodě musí být spojitá v tomto bodě. Toto pravidlo pro funkce dvou a více proměnných obecně neplatí, např. 



<!-- Start of picture text -->
1 pro xy D 0<br>f .x; y/ D<br>(0 pro xy ¤ 0<br><!-- End of picture text -->

má v bodě Œ0; 0� parciální derivace fx<sup>0.0; 0/ D 0 D f</sup> y<sup>0.0; 0/, ale funkce v tomto bodě není spojitá.</sup> 

Pˇríklad 7.3. Určete parciální derivace funkce f .x; y; z/ D x<sup>y</sup> ln.x C z<sup>2</sup> /. _Řešení._ 



<!-- Start of picture text -->
1 2z<br>fx 0 D yxy�1 ln.x C z/ C xy fy 0 D xy ln x ln.x C z2/; fz 0 D xy<br>x C z 2 ; x C z 2 :<br><!-- End of picture text -->

■ Vˇeta 7.4 — o stˇrední hodnotˇe. _Nechť funkce_ f W R<sup>2</sup> ! R _má obě parciální derivace ve všech bodech množiny_ ha1; b1i �ha2; b2i � D.f / _. Pak existují čísla_ � 2 .a1; b1/ _,_ � 2 .a2; b2/ _taková, že_ 



<!-- Start of picture text -->
f .b1; b2/ � f .a1; a2/ D fx 0 .�; a2/.b1 � a1/ C f y 0.b1; �/.b2 � a2/:<br><!-- End of picture text -->

_Důkaz._ S využitím Lagrangeovy věty o střední hodnotě pro funkci jedné proměnné (viz věta 15.3 v Matematické analýze I) dostaneme 



<!-- Start of picture text -->
f .b1; b2/ � f .a1; a2/ D f .b1; b2/ � f .b1; a2/ C f .b1; a2/ � f .a1; a2/<br>D fy 0.b1; �/.b2 � a2/ C f x 0 .�; a2/.b1 � a1/:<br><!-- End of picture text -->

Definice 7.5 — druhých parciálních derivací. Nechť funkce f W R<sup>2</sup> ! R má obě parciální derivace na otevřené množině M � D.f / a Œx0; y0� 2 M . Existuje-li parciální derivace funkce fx<sup>0podle proměnné x</sup> v bodě Œx0; y0�, nazveme tuto derivaci _druhou parciální derivací (nebo parciální derivací 2. řádu) funkce_ f _podle_ x _v bodě_ Œx0; y0� a značíme fxx<sup>00.x0; y0/, nebo fxx.x0; y0/, nebo@</sup> @x<sup>2f2.x0; y0/. Existuje-li parciální</sup> derivace funkce fx<sup>0podle yv bodě Œx0; y0�, nazveme tuto derivaci</sup><sup>_druhou smíšenou parciální derivací_</sup> _funkce_ f _v bodě_ Œx0; y0� a značíme fxy<sup>00.x0; y0/, nebo fxy.x0; y0/, nebo</sup> @x@y<sup>@2f.x0; y0/. Analogicky pro</sup> derivace funkce fy<sup>0.</sup> 

Poznámka 7.6. a) Podobně bychom definovali druhé parciální derivace funkce tří a více proměnných, jejich počet je n<sup>2</sup> , kde n je počet proměnných. 

b) Parciální derivace m-tého řádu (m � 3) definujeme jako parciální derivace derivací .m � 1/-tého řádu. Jejich počet je n<sup>m</sup> (variace s opakováním). 

Pˇríklad 7.7. Určete všechny druhé parciální derivace funkce f .x; y/ D sin y<sup><u>x</u>.</sup> 

_Řešení._ fx<sup>0Dcos</sup> y<sup><u>x</u>�</sup> y<sup><u>1</u>,f</sup> y<sup>0Dcos</sup> y<sup><u>x</u>��</sup> y<sup>2x,f</sup> xx<sup>00D�sin</sup> y<sup><u>x</u>�</sup> y1<sup>2,f</sup> xy<sup>00D�sin</sup> y<sup><u>x</u>��</sup> y<sup>3xC cos</sup> y<sup><u>x</u>��</sup> y<sup>21,</sup> fyx<sup>00D �sin</sup> y<sup><u>x</u>��</sup> y<sup>3xC cos</sup> y<sup><u>x</u>��</sup> y<sup>21, f</sup> yy<sup>00D �sin</sup> y<sup><u>x</u>�</sup> y<sup><u>x24</u>C cos</sup> y<sup><u>x</u>�</sup> y<sup><u>2x3</u>. Vidíme, že smíšené derivace f</sup> xy<sup>00</sup> a fyx<sup>00se rovnají, to není náhoda, ale také to nenastane úplně vždy, viz následující věta.</sup> 

7 Parciální a smˇerová derivace, gradient 

27 

■ Vˇeta 7.8 — Schwarzova. _Nechť funkce_ f W R<sup>2</sup> ! R _má parciální derivace_ fxy<sup>00</sup><sup>_,_f</sup> yx<sup>00</sup><sup>_na okolí bodu_</sup> Œx0; y0� _, které jsou v bodě_ Œx0; y0� _spojité. Pak jsou tyto derivace záměnné, tj. platí_ fxy<sup>00.x0; y0/D</sup> fyx<sup>00.x0; y0/</sup><sup>_._</sup> 

_Důkaz._ Dle předpokladu existuje ı-okolí Oı .Œx0; y0�/ D .x0 � ı; x0 C ı/ � .y0 � ı; y0 C ı/, v němž jsou parciální derivace fxy<sup>00a f</sup> yx<sup>00definovány (a tedy zde musí být definovány i f</sup> x<sup>0, f</sup> y<sup>0a sama funkce f ).</sup> Pro 0 < h < ı položme 



<!-- Start of picture text -->
F.h/ D f .x0 C h; y0 C h/ � f .x0 C h; y0/ � f .x0; y0 C h/ C f .x0; y0/<br>h 2<br><!-- End of picture text -->

a označme '.y/ D f .x0 C h; y/ � f .x0; y/, .x/ D f .x; y0 C h/ � f .x; y0/. Pak funkci F můžeme psát 



<!-- Start of picture text -->
F.h/ D 1 �'.y0 C h/ � '.y0/� D 1 � .x0 C h/ �  .x0/�: (�)<br>h 2 h 2<br><!-- End of picture text -->

Podle Lagrangeovy věty o střední hodnotě existuje �1 2 .0; 1/ takové, že 

'.y0 C h/ � '.y0/ D h'<sup>0</sup> .y0 C �1h/ D h�fy<sup>0.x0 C h; y0 C �1h/ �f</sup> y<sup>0.x0; y0 C �1h/</sup> �: Označme ještě g.x/ D fy<sup>0.x; y0 C �1h/. Pak g0.x/ D f</sup> yx<sup>00.x; y0 C �1h/ a rozdíl v hranatých závorkách</sup> je (opět podle Lagrangeovy věty o střední hodnotě) 



<!-- Start of picture text -->
g.x0 C h/ � g.x0/ D hg 0 .x0 C �2h/ D hfyx 00 .x0 C �2h; y0 C �1h/; �2 2 .0; 1/:<br><!-- End of picture text -->

Dosadíme-li odtud do .�/, dostáváme F.h/ D fyx<sup>00.x0 C �2h; y0 C �1h/. Provedeme-li stejné úvahy pro</sup> funkci , dostaneme rovnost 

F.h/ D fxy<sup>00.x0 C �3h; y0 C �4h/;</sup> �3; �4 2 .0; 1/: Poslední vztahy a spojitost fxy<sup>00, f</sup> yx<sup>00v bodě Œx0; y0�implikují</sup> 



<!-- Start of picture text -->
hlim!0 F.h/ D f xy 00 .x0; y0/ a současně hlim!0 F.h/ D f yx 00 .x0; y0/;<br><!-- End of picture text -->

tj. fxy<sup>00.x0; y0/ D f</sup> yx<sup>00.x0; y0/.</sup> 

Poznámka 7.9. Bez předpokladu spojitosti rovnost smíšených derivací obecně neplatí, např. pro funkci f definovanou 



<!-- Start of picture text -->
8xy x2 � y2 pro Œx; y� ¤ Œ0; 0�;<br>f .x; y/ D x 2 C y 2<br>ˆ<<br>ˆ:0 pro Œx; y� D Œ0; 0�;<br><!-- End of picture text -->

dostaneme fxy<sup>00.0; 0/D�1 a f</sup> yx<sup>00.0; 0/D1 (smíšené derivace na okolí bodu Œ0; 0�existují, ale nejsou</sup> v bodě Œ0; 0� spojité). 

■ D˚usledek 7.10. _Má-li funkce_ f W R<sup>2</sup> ! R _spojité parciální derivace až do druhého řádu na otevřené množině_ M � D.f / _, pak jsou zde smíšené derivace záměnné, tj._ fxy<sup>00.x; y/Df</sup> yx<sup>00.x; y/</sup><sup>_prokaždé_</sup> Œx; y� 2 M _._ 

Poznámka 7.11. Tvrzení platí i pro smíšené derivace funkce tří a více proměnných a matematickou indukcí jej můžeme rozšířit i pro derivace vyšších řádů: Má-li funkce f spojité parciální derivace až do řádu m na otevřené množině M � D.f /, pak hodnota parciální derivace řádu m v libovolném bodě z množiny M závisí pouze na tom, kolikrát se derivovalo podle i-té proměnné (i D 1; 2; : : : ; n/, nikoliv na pořadí, v jakém se derivovalo. Považujeme-li smíšené derivace za totožné, pak se počet parciálních derivací redukuje na �nCmm�1� (kombinace s opakováním). 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

28 

Definice 7.12 — smˇerové derivace. Nechť f W R<sup>2</sup> ! R je funkce, Œx0; y0� je vnitřní bod množiny D.f / a sE D .s1; s2/ je vektor v R<sup>2</sup> . Položme '.t/ D f .x0 C ts1; y0 C ts2/. Má-li funkce ' derivaci v bodě 0, nazýváme ji _směrovou derivací funkce_ f _v bodě_ Œx0; y0� _ve směru vektoru_ sE a označujeme fsE<sup>0.x0; y0/ nebo fsE.x0; y0/ nebo@</sup> @<sup><u>f</u></sup> sE<sup>.x0; y0/. To znamená, že</sup> 



<!-- Start of picture text -->
'.t/ � '.0/ f .x0 C ts1; y0 C ts2/ � f .x0; y0/<br>fsE 0.x0; y0/ D t lim !0 t D tlim!0 t :<br><!-- End of picture text -->

Poznámka 7.13. a) Analogicky bychom zavedli směrovou derivaci pro funkci tří a více proměnných. 

b) Někdy se v definici navíc požaduje, aby směrový vektor Es byl jednotkový, tj. jEsj D 1. Směrovou derivaci pak lze interpretovat, viz obrázek na přednášce. 

c) Jelikož je směrová derivace obyčejnou derivací funkce ', platí pro počítání tato pravidla: Nechť existují fsE<sup>0, g</sup> sE<sup>0v bodě X2 Rn. Potom</sup> (i) pro 8c 2 R existuje fc<sup>0</sup> sE<sup>.X/ a platí f</sup> c<sup>0</sup> sE<sup>.X/ D cf</sup> sE<sup>0.X/,</sup> (ii) .f ˙ g/<sup>0</sup> sE<sup>.X/ D f</sup> sE<sup>0.X/ ˙ g</sup> sE<sup>0.X/,</sup> (iii) .fg/<sup>0</sup> sE<sup>.X/ D f</sup> sE<sup>0.X/g.X/ C f .X/g</sup> sE<sup>0.X/,</sup> fsE<sup>0.X/g.X/ �f .X/g</sup> <u>sE</u><sup>0.X/</sup> (iv) je-li g.X/ ¤ 0, pak .X/ D . � <u>fg</u> �0sE g<sup>2</sup> .X/ 

d) Naopak neplatí aditivita směrových derivací vzhledem ke směrům. Jestliže existují frE<sup>0, f</sup> sE<sup>0, nemusí</sup> existovat frE<sup>0</sup> CEs<sup>, a pokud existuje f</sup> rE<sup>0</sup> CEs<sup>, může být f</sup> rE<sup>0</sup> CEs<sup>¤ f</sup> rE<sup>0C f</sup> sE<sup>0(tato vlastnost platí v případě, kdy je</sup> alespoň jedna z frE<sup>0, f</sup> sE<sup>0spojitá na nějakém okolí bodu X).</sup> 

e) Parciální derivace lze považovat za směrové derivace ve směrech vektorů standardní báze R<sup>n</sup> , tj. fx<sup>0</sup> i<sup>D f</sup> eE<sup>0</sup> i<sup>.</sup> f) Z existence směrové derivace v bodě ve směru libovolného vektoru neplyne spojitost funkce v tomto bodě. 

Pˇríklad 7.14. Spočítejte směrovou derivaci f .x; y; z/ D x<sup>2</sup> C yz v bodě Œ1; 2; �1� ve směru vektoru sE D .�1; 1; 2/. 

_Řešení._ 

'.t/ D f .1 � t; 2 C t; �1 C 2t/ D .1 � t/<sup>2</sup> C .2 C t/.�1 C 2t/ D 1 � 2t C t<sup>2</sup> � 2 C 4t � t C 2t<sup>2</sup> D �1 C t C 3t<sup>2</sup> H) '<sup>0</sup> .t/ D 1 C 6t H) '<sup>0</sup> .0/ D 1: 

Definice 7.15 — gradientu funkce. Buď f W R<sup>n</sup> ! R funkce a X0 2 D.f /. Nechť pro 8i D 1; 2; : : : ; n existuje fx<sup>0</sup> i<sup>.X0/.Pakvektorgrad f .X0/D.f</sup> x<sup>0</sup> 1<sup>.X0/; f</sup> x<sup>0</sup> 2<sup>.X0/; : : : ; f</sup> x<sup>0</sup> n<sup>.X0//senazývá</sup><sup>_gradient_</sup> _funkce_ f _v bodě_ X0. Existují-li parciální derivace na množině M � D.f /, pak vektorovou funkci grad f D .fx<sup>0</sup> 1<sup>; f</sup> x<sup>0</sup> 2<sup>; : : : ; f</sup> x<sup>0</sup> n<sup>/ nazveme</sup><sup>_gradientem funkce_f(jedná se tedy o zobrazení Mdo Rn).</sup> 

Poznámka 7.16. a) Namísto grad f se používá též značení rf (operátor „nabla“). 

b) Později ukážeme, že pokud všechny parciální derivace funkce f existují na okolí bodu X0 a jsou spojité v X0, pak směrová derivace v tomto bodě existuje pro libovolný směrový vektor a platí fsE<sup>0.X0/ D grad f .X0/ �Es(standardní skalární součin1). Platí grad f�EsD j grad f .X0/j �jEsj cos ˛, kde</sup> ˛ je úhel, který tyto dva vektory svírají. Odtud plyne, že hodnota směrové derivace bude největší, je-li cos ˛ D 1, tj. ˛ D 0, tj. oba vektory mají stejný směr. Geometricky lze tedy gradient interpretovat jako směr, ve kterém je přírůstek funkční hodnoty funkce f největší. 

> 1 _Standardní (eukleidovský) skalární součin_ „�“ vektorů uE D .u1; u2; : : : ; un/, vE D .v1; v2; : : : ; vn/ v Rn je definován jako uE �Ev D u1v1 C u2v2 C ���C unvn. 

8 Totální diferenciál 

29 

#### Pˇríklady k procviˇcení 

- 7.1. Spočítejte parciální derivace funkcí v bodě A: 

   - a) f .x; y/ D x ~~p~~ 1 � x<sup>2</sup> C y ~~p~~ 1 � x<sup>2</sup> , A D Œ0; 0�; b) f .u; v/ D<sup><u>u</u></sup> v<sup>C</sup> u<sup><u>v</u>,</sup> A D Œ1; 1�; c) f .x; y/ D 3x<sup>2</sup> y C e<sup>xy</sup> , A D Œ3; 2�; d) f .˛; ˇ/ D<sup>˛ cos</sup><sup><u>ˇ</u>�ˇ cos ˛</sup> A D Œ0; 0�; 1Ccos ˛Csin <u>ˇ</u><sup>,</sup> 

   - e) f .x; y/ D xy ~~p~~ 1 � x<sup>2</sup> � y<sup>2</sup> , A D Œ0; 0�. 

- 7.2. Určete parciální derivace funkcí: 

   - a) f .x; y/ D sin<sup><u>x</u></sup> y<sup>2;</sup> b) f .�; ı/ D arctg<sup><u>�Cı</u></sup> � �ı<sup>;</sup> 

   - c) f .x; y; z/ D ln.cos<sup>2</sup> .x<sup>2</sup> � z<sup>2</sup> y//. 

- 7.3. Ukažte, že ze stavové rovnice ideálního plynu pV D nRT (p je tlak, V objem, T absolutní teplota a n, R jsou konstanty) vyplývá 



<!-- Start of picture text -->
@p @V @T<br>@V @T @p D �1:<br><!-- End of picture text -->

- 7.4. Určete všechny druhé parciální derivace funkcí 

   - a) f .x; y; z/ D xy C xz C yz; b) f .x; y/ D ln<sup><u>x2C1</u></sup> y<sup>2</sup> �1<sup>.</sup> 

<u>@</u><sup>2</sup> 7.5. Ukažte, že funkce u.x; y/ D ln ~~p~~ x<sup>2</sup> C y<sup>2</sup> vyhovuje Laplaceově rovnici �u D 0, kde � D @x<sup>2C</sup> @y<sup><u>@22</u></sup> (tzv. Laplaceův operátor). 



<!-- Start of picture text -->
7.6. Ukažte, že funkce u.x; t/ D 1 4a 2 t (a; b 2 R, a ¤ 0) splňuje rovnici vedení tepla<br>2a p �t e� .x�b/2<br>u 0 t D a2u xx 00 .<br><!-- End of picture text -->

- 7.7. Předpokládejme, že funkce f W R<sup>5</sup> ! R je dostatečně mnohokrát derivovatelná. 

   - a) Jaký je počet derivací čtvrtého řádu? 

b) Jaký je počet derivací čtvrtého řádu, považujeme-li příslušné smíšené derivace za jednu? 

7.8. Pomocí definice vypočtěte směrovou derivaci funkce f .x; y; z/ D 4.x � 1/ C 3y<sup>2</sup> C 5z<sup>2</sup> v bodě A D Œ2; �1; 3� ve směru vektoru Es D .1; 4; �2/. Určete dále gradient funkce v bodě A. 

_Výsledky._ 7.1. a) fx<sup>0.A/D1,f</sup> y<sup>0.A/D1;b)f</sup> u<sup>0.A/D0,f</sup> v<sup>0.A/D0;c)f</sup> x<sup>0.A/D36C2 e6,</sup> fy<sup>0.A/ D 27 C 3 e6; d) f</sup> ˛<sup>0.A/ D</sup><sup><u>1</u></sup> 2<sup>, f</sup> ˇ<sup>0.A/ D �</sup> 2<sup><u>1</u>; e) f</sup> x<sup>0.A/ D 0, f</sup> y<sup>0.A/ D 0. 7.2. a) f</sup> x<sup>0D</sup><sup><u>2x</u></sup> y<sup>cos</sup><sup><u>x</u></sup> y<sup>2,</sup> fy<sup>0D �</sup> y<sup><u>x22</u>cos</sup><sup><u>x</u></sup> y<sup>2; b) f</sup> �<sup>0D �</sup> �<sup>2</sup> Cı ı<sup>2, f</sup> ı<sup>0D</sup> �<sup>2</sup> C� ı<sup>2; c) f</sup> x<sup>0D �4xtg .x2�z2y/, f</sup> y<sup>0D 2z2 tg.x2�z2y/,</sup> fz<sup>0D 4yz tg.x2 �z2y/. 7.4. a) f</sup> xx<sup>00D f</sup> yy<sup>00D f</sup> zz<sup>00D 0, f</sup> xy<sup>00D f</sup> yx<sup>00D f</sup> yz<sup>00D f</sup> zy<sup>00D f</sup> xz<sup>00D f</sup> zx<sup>00D 1;</sup> 2.y<sup>2</sup> <u>C1/</u> b) fxx<sup>00D�</sup> .x<sup>2.x2</sup> C<sup>2�</sup> 1/<sup>12/,f</sup> xy<sup>00Df</sup> yx<sup>00D0,f</sup> yy<sup>00D</sup> .y<sup>2</sup> �1/<sup>2.7.7.a)625;b)70.7.8.f</sup> sE<sup>0.A/D�80,</sup> rf .A/ D .4; �6; 30/. 

### 8 Totální diferenciál 

Definice 8.1 — totálního diferenciálu. Řekneme, že funkce f W R<sup>2</sup> ! R definovaná v okolí bodu 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

30 

Œx0; y0� je v tomto bodě _diferencovatelná_ , jestliže existují a; b 2 R taková, že platí 



<!-- Start of picture text -->
f .x0 C h; y0 C k/ � f .x0; y0/ � .ah C bk/<br>lim D 0:<br>Œh;k�!Œ0;0� p h 2 C k 2<br><!-- End of picture text -->

Lineární funkce ah C bk proměnných h; k se nazývá _totální (úplný) diferenciál funkce_ f _v bodě_ Œx0; y0� a značí se df .x0; y0/, případně df .x0; y0I h; k/, případně df .x0; y0/.h; k/. 

Poznámka 8.2. a) Analogicky bychom definovali totální diferenciál pro funkci tří a více proměnných. b) Podmínku z definice lze ekvivalentně formulovat: existují a; b 2 R a funkce � W R<sup>2</sup> ! R tak, že platí 



<!-- Start of picture text -->
f .x0 C h; y0 C k/ � f .x0; y0/ D ah C bk C p h 2 C k 2 �.h; k/; kde Œh;k�lim!Œ0;0� �.h; k/ D 0<br><!-- End of picture text -->

(srovnejte s definicí diferenciálu funkce jedné proměnné). 

c) Jmenovatel limity v definici je vzdálenost bodu Œh; k� od <u>počátku</u> v eukleidovské metrice �2. Lze použít i ekvivalentní metriky �1 nebo �1 (tj. výraz ~~p~~ h<sup>2</sup> C k<sup>2</sup> nahradit výrazem jhj C jkj nebo maxfjhj; jkjg). 

■ Vˇeta 8.3. _Je-li funkce_ f W R<sup>n</sup> ! R _diferencovatelná v bodě_ X0 _, pak je v tomto bodě spojitá._ 

ZK _Důkaz._ Pro n D 2: Protože f je diferencovatelná, platí podle předchozí poznámky b) 

lim �f .x0 C h; y0 C k/ � f .x0; y0/� D lim �ah C bk C ~~p~~ h<sup>2</sup> C k<sup>2</sup> �.h; k/� D 0 Œh;k�!Œ0;0� Œh;k�!Œ0;0� 

(protože limŒh;k�!Œ0;0� �.h; k/ D 0), což znamená, že limŒh;k�!Œ0;0� f .x0 C h; y0 C k/ D f .x0; y0/, tj. f je spojitá v Œx0; y0�. 

Poznámka 8.4. Obrácené tvrzení neplatí, např. funkce f .x; y/ D ~~p~~ x<sup>2</sup> C y<sup>2</sup> je spojitá v bodě Œ0; 0�, ale není zde diferencovatelná. 

■ Vˇeta 8.5. _Je-li funkce_ f W R<sup>2</sup> ! R _diferencovatelná v bodě_ Œx0; y0� _, pak má v tomto bodě parciální derivace a platí_ a D fx<sup>0.x0; y0/</sup><sup>_,_bD f</sup> y<sup>0.x0; y0/</sup><sup>_, tj._</sup> 



<!-- Start of picture text -->
df .x0; y0/ D fx 0 .x0; y0/ h C f y 0.x0; y0/ k:<br><!-- End of picture text -->

ZK _Důkaz._ Položme v definici totálního diferenciálu k D 0. Pak 



<!-- Start of picture text -->
0 D hlim!0 f .x0 C h; y0/ �jhjf .x0; y0/ � ah D (af �x 0 .x f 0 x 0; y.x00/; y �0a/ pro pro h < 0 h > 0 ;<br>tj. a D fx 0 .x0; y0/. Stejným obratem by se dokázala rovnost b D f y 0.x0; y0/.<br><!-- End of picture text -->

■ Vˇeta 8.6. _Má-li funkce_ f _na_ O.Œx0; y0�/ _parciální derivace_ fx<sup>0</sup><sup>_,_f</sup> y<sup>0</sup><sup>_, které jsou spojité v_Œx0; y0�</sup><sup>_, pak je_</sup> _v tomto bodě diferencovatelná._ 

_Důkaz._ Protože parciální derivace dle předpokladu existují v jistém okolí bodu Œx0; y0�, s využitím věty o střední hodnotě na tomto okolí platí 



<!-- Start of picture text -->
f .x0 C h; y0 C k/ � f .x0; y0/ � fx 0 .x0; y0/h � f y 0.x0; y0/k<br>lim<br>Œh;k�!Œ0;0� p h 2 C k 2<br>D lim fx 0 .x0 C �h; y0/h C f y 0.x0 C h; y0 C �k/k � f x 0 .x0; y0/h � f y 0.x0; y0/k<br>Œh;k�!Œ0;0� p h 2 C k 2<br>h<br>D lim �fx 0 .x0 C �h; y0/ � f x 0 .x0; y0/ �<br>Œh;k�!Œ0;0� p h 2 C k 2<br><!-- End of picture text -->

8 Totální diferenciál 

31 



<!-- Start of picture text -->
k<br>C lim �fy 0.x0 C h; y0 C �k/ � f y 0.x0; y0/ �<br>Œh;k�!Œ0;0� p h 2 C k 2 D 0:<br>Poslední rovnost plyne ze spojitosti fx 0 , f y 0 v Œx0; y0�, ohraničenosti<br>h k<br>ˇˇˇˇ p h 2 C k 2 ˇˇˇˇ � 1; ˇˇˇˇ p h 2 C k 2 ˇˇˇˇ � 1<br><!-- End of picture text -->

a vlastností limity. 

Poznámka 8.7. a) Poslední dvě tvrzení platí analogicky i pro funkce tří a více proměnných. 

b) Podobně jako u diferenciálu funkce jedné proměnné lze odůvodnit značení přírůstků h; k jako dx; dy, resp. přírůstků h1; h2; : : : ; hn jako dx1; dx2; : : : ; dxn. 

c) Rovina z D ax C by C c v R<sup>3</sup> se nazývá _tečnou rovinou ke grafu funkce_ z D f .x; y/ v bodě T D Œx0; y0; f .x0; y0/�, jestliže 



<!-- Start of picture text -->
f .x; y/ � ax � by � c<br>f .x0; y0/ D ax0 C by0 C c a lim<br>Œx;y�!Œx0;y0� p .x � x0/ 2 C .y � y0/ 2 D 0:<br><!-- End of picture text -->

Z těchto rovnic dostaneme 



<!-- Start of picture text -->
f .x; y/ � f .x0; y0/ C f .x0; y0/ � ax � by � c<br>0 D lim<br>Œx;y�!Œx0;y0� p .x � x0/ 2 C .y � y0/ 2<br>f .x; y/ � f .x0; y0/ � a.x � x0/ � b.y � y0/<br>D Œx;y�!limŒx0;y0� p .x � x0/ 2 C .y � y0/ 2 ;<br><!-- End of picture text -->

tj. df .x0; y0/.x � x0; y � y0/ D a.x � x0/ C b.y � y0/. Podle věty 8.5 platí a D fx<sup>0.x0; y0/,</sup> b D fy<sup>0.x0; y0/ a tedy cD f .x0; y0/ �x0f</sup> x<sup>0.x0; y0/ �y0f</sup> y<sup>0.x0; y0/. Celkově tedy</sup> 

z D f .x0; y0/ C fx<sup>0.x0; y0/.x �x0/ C f</sup> y<sup>0.x0; y0/.y �y0/;</sup> 

tj. 



<!-- Start of picture text -->
z D f .x0; y0/ C grad f .x0; y0/ � .x � x0; y � y0/;<br><!-- End of picture text -->

tj. z D f .x0; y0/ C df .x0; y0I x � x0; y � y0/. Odtud plyne geometrický význam totálního diferenciálu funkce dvou proměnných, je to přírůstek funkce měřený na tečné rovině. 

■ Vˇeta 8.8. _Nechť funkce_ f W R<sup>n</sup> ! R _je diferencovatelná v bodě_ X0 2 R<sup>n</sup> _a nechť_ Es 2 R<sup>n</sup> _je libovolný. Pak existuje směrová derivace_ fsE<sup>0.X0/</sup><sup>_a platí_f</sup> sE<sup>0.X0/ D grad f .X0/ �Es</sup><sup>_._</sup> 

ZK _Důkaz._ Pro n D 2: Nechť f je diferencovatelná v bodě Œx0; y0�. Potom 



<!-- Start of picture text -->
f .x0 C ts1; y0 C ts2/ � f .x0; y0/<br>fsE 0.x0; y0/ D t lim !0 t<br>df .x0; y0I ts1; ts2/ C q t 2 .s1 2 C s 2 2/ �.ts1; ts2/<br>D lim<br>t !0 t<br>D df .x0; y0I s1; s2/ ˙ tlim!0 q s1 2 C s 2 2 �.ts1; ts2/<br>D df .x0; y0I s1; s2/ D grad f .x0; y0/ �Es:<br><!-- End of picture text -->

Pˇríklad 8.9. Spočítejte směrovou derivaci f .x; y; z/ D x<sup>2</sup> C yz v bodě Œ1; 2; �1� ve směru vektoru sE D .�1; 1; 2/. 

_Řešení._ Platí grad f D .2x; z; y/, a tedy grad f .1; 2; �1/ D .2; �1; 2/, a tedy 

fsE<sup>0.1; 2; �1/ D .2; �1; 2/ �.�1; 1; 2/ D 1:</sup> 

Srovnejte s příkladem 7.14. 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

32 

Definice 8.10 — totálního diferenciálu m-ho ˇrádu. Nechť funkce f W R<sup>2</sup> ! R má na O.Œx0; y0�/ parciální derivace až do řádu m včetně, které jsou spojité v bodě Œx0; y0�. Pak _totálním diferenciálem_ m _-tého řádu funkce_ f _v bodě_ Œx0; y0� rozumíme funkci 



<!-- Start of picture text -->
m<br>m @ m f<br>d m f .x0; y0I h; k/ D X<br>j D0 j ! @x j @y m�j .x0; y0/hj km�j :<br><!-- End of picture text -->

Poznámka 8.11. a) Totální diferenciál m-tého řádu funkce f je přirozené definovat jako d<sup>m</sup> f D d.d<sup>m�1</sup> f /, m D 2; 3; : : : , což, vzhledem k větám 8.5 a 8.6, skutečně vede na vzorec v předchozí definici, např. 



<!-- Start of picture text -->
d 2 f D d.df / D d.fx 0 h C f y 0k/ D .f x 0 h C f y 0k/ x 0 h C .f x 0 h C f y 0k/ y 0 k<br>D fxx 00 h2 C f yx 00 hk C f xy 00 hk C f yy 00 k2 D f xx 00 h2 C 2f xy 00 hk C f yy 00 k2:<br><!-- End of picture text -->

b) V případě funkce tří a více proměnných se vzorec modifikuje na 



<!-- Start of picture text -->
d m f .X0I h1; h2; : : : ; hn/<br>mŠ @ m f<br>D X .X0/h m 1 1 hm 2 2 : : : h m n n :<br>m1Cm2C���CmnDm m1Šm2Š : : : mnŠ � @x1 m1 @x2 m2 : : : @xn mn<br><!-- End of picture text -->

Pˇríklady k procviˇcení 

8.1. Určete totální diferenciál funkce 



<!-- Start of picture text -->
f .x; y/ D arctg x<br>y<br><!-- End of picture text -->

v bodě A D Œ1; 1�. 

8.2. Určete hodnotu totálního diferenciálu funkce 



<!-- Start of picture text -->
f .x; y; z/ D 2 x .sin y/ arctg z<br><!-- End of picture text -->



<!-- Start of picture text -->
v bodě A D ��4; � 2 ; 0 � pro přírůstky h D 0;05, k D 0;06 a ` D 0;08.<br><!-- End of picture text -->

8.3. Pomocí totálního diferenciálu určete přibližně hodnotu 



<!-- Start of picture text -->
a) arcsin 1;05 0;48 I b) p 3 0;981;03 2 � 2 1;05 4 :<br><!-- End of picture text -->

8.4. Napište rovnici tečné roviny a normály ke grafu funkce f v bodě T : 



<!-- Start of picture text -->
f .x; y/ D x C y T D Œ2; 1; ‹�:<br>x � y ;<br><!-- End of picture text -->

8.5. Vypočtěte s přesností na dvě desetinná místa objem kužele V a určete odhad absolutní změny objemu, jestliže výška kužele je h D 15 ˙ 0; 3 cm a poloměr základny je r D 8 ˙ 0; 2 cm. Určete relativní změnu objemu. 

- 8.6. Najděte jednotkový vektor Es, pro nějž je směrová derivace fsE<sup>0funkce f .x; y/Dcotg.xy/ v bodě</sup> A D � <u>�2</u><sup>; 1</sup> � maximální a určete její hodnotu. 

8.7. Napište totální diferenciál druhého a třetího řádu funkce 



<!-- Start of picture text -->
f .x; y/ D ln.x C y/<br><!-- End of picture text -->

v bodě A D Œ2; 1�. 

9 Derivace složené funkce, Taylor˚uv polynom 

33 

_Výsledky._ 8.1. df .1; 1/.h; k/ D<sup><u>1</u></sup> 2<sup>h �</sup><sup><u>1</u></sup> 2<sup>k. 8.2. df</sup> ��4;<sup><u>�</u></sup> 2<sup>; 0</sup> �.0;05I 0;06I 0;08/ D 0;005. 8.3. a) 0,4716; b) 1. 8.4. � W 2x � 4y C z � 3 D 0, n W x D 2 C 2t, <u>y</u> D 1 � 4t, z D 3 C t (t 2 R/. 8.5. V D 1005;31 ˙ 70;37 cm<sup>3</sup> , 7%. 8.7. Es D .�2= ~~<u>p</u>~~ �<sup>2</sup> C 4; ��= ~~p~~ �<sup>2</sup> C 4/, ~~<u>p</u>~~ �<sup>2</sup> C 4=2. 8.7. d<sup>2</sup> f .2; 1/.h; k/ D �<sup><u>1</u></sup> 9<sup>h2 �</sup><sup><u>2</u></sup> 9<sup>hk �</sup><sup><u>1</u></sup> 9<sup>k2;d3f .2; 1/.h; k/ D</sup> 272<sup>h3 C</sup> 9<sup><u>2</u>h2k C</sup><sup><u>2</u></sup> 9<sup>hk2 C</sup> 27<sup><u>2</u>k3.</sup> 

### 9 Derivace složené funkce, Taylor˚uv polynom 

■ Vˇeta 9.1 — ˇretˇezové pravidlo. _Nechť funkce_ u; v W R<sup>2</sup> ! R _mají parciální derivace v bodě_ Œx0; y0� _a funkce_ f W R<sup>2</sup> ! R _je diferencovatelná v bodě_ Œu0; v0� D Œu.x0; y0/; v.x0; y0/� _. Potom složená funkce_ F.x; y/ D f .u.x; y/; v.x; y// _má parciální derivace v bodě_ Œx0; y0� _a platí_ 



<!-- Start of picture text -->
Fx 0 .x0; y0/ D f u 0.u0; v0/ u0 x .x0; y0/ C f v 0.u0; v0/ v x 0 .x0; y0/;<br>Fy 0 .x0; y0/ D f u 0.u0; v0/ u y 0 .x0; y0/ C f v 0.u0; v0/ v y 0 .x0; y0/;<br><!-- End of picture text -->

_stručně_ Fx<sup>0D f</sup> u<sup>0u0</sup> x<sup>C f</sup> v<sup>0v</sup> x<sup>0</sup><sup>_a_F</sup> y<sup>0D f</sup> u<sup>0u</sup> y<sup>0C f</sup> v<sup>0v</sup> y<sup>0</sup><sup>_._</sup> 

_Důkaz._ Podle definice je 



<!-- Start of picture text -->
F .x0 C h; y0/ � F .x0; y0/<br>Fx 0 .x0; y0/ D lim<br>h!0 h<br>f �u.x0 C h; y0/; v.x0 C h; y0/� � f �u.x0; y0/; v.x0; y0/�<br>D hlim!0 h :<br><!-- End of picture text -->

Protože f je diferencovatelná v bodě Œu0; v0�, existuje podle poznámky 8.2b) funkce � taková, že 



<!-- Start of picture text -->
Œh;k�lim!Œ0;0� �.h; k/ D 0<br><!-- End of picture text -->

a 

f �u.x0 C h; y0/; v.x0 C h; y0/� � f .u0; v0/ D fu<sup>0.u0; v0/</sup> <u>�u.x0 C h; y0/ �</u> u0� C fv<sup>0.u0; v0/</sup> �v.x0 C h; y0/ � v0� C ~~q~~ <u>�u.x0 C h; y0/ �</u> u0�2 C <u>�v.x0 C h; y0/ �</u> v0�2 ��u.x0 C h; y0/ � u0; v.x0 C h; y0/ � v0�; přičemž jsme využili větu 8.5. Označme 

!.h/ D ~~q~~ <u>�u.x0 C h; y0/ �</u> u0�2 C <u>�v.x0 C h; y0/ �</u> v0�2 ��u.x0 C h; y0/ � u0; v.x0 C h; y0/ � v0�: Pak 



<!-- Start of picture text -->
1<br>Fx 0 .x0; y0/ D lim �fu 0.u0; v0/ �u.x0 C h; y0/ � u0� C fv 0.u0; v0/ �v.x0 C h; y0/ � v0� C !.h/�<br>h!0 h<br>!.h/<br>D fu 0.u0; v0/u0 x .x0; y0/ C f v 0.u0; v0/v x 0 .x0; y0/ C lim :<br>h!0 h<br><!-- End of picture text -->

Jako poslední krok je potřeba ukázat, že 



<!-- Start of picture text -->
!.h/ �u.x0 C h; y0/ � u0�2 C �v.x0 C h; y0/ � v0�2<br>lim D lim �.h/ D 0:<br>h!0 h h!0 s h 2<br><!-- End of picture text -->

Skutečně, s využitím l’Hospitalova pravidla máme 



<!-- Start of picture text -->
�u.x0 C h; y0/ � u0�2 C �v.x0 C h; y0/ � v0�2<br>lim<br>h!0 h 2<br>2�u.x0 C h; y0/ � u0�u 0 x .x0 C h; y0/ C 2 �v.x0 C h; y0/ � v0�vx 0 .x0 C h; y0/<br>D lim<br>h!0 2h<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

34 



<!-- Start of picture text -->
D �u 0 x .x0; y0/ �2 C �vy 0 .x0; y0/ �2:<br><!-- End of picture text -->

Protože existuje konečná limita, funkce 



<!-- Start of picture text -->
�u.x0 C h; y0/ � u0�2 C �v.x0 C h; y0/ � v0�2<br>s h 2<br><!-- End of picture text -->

musí být ohraničená (viz vlastnosti limity, bod druhý s přihlédnutím k bodu šestému). Vztah 



<!-- Start of picture text -->
hlim!0 !.h/=h D 0<br><!-- End of picture text -->

pak plyne ihned z třetího bodu vlastností limity. 

Poznámka 9.2. a) Analogicky pro funkci tří a více proměnných f D f .u1; : : : ; un/, kde ui D ui .x1; : : : ; xn/, bychom pro složenou funkci 



<!-- Start of picture text -->
F.x1; : : : ; xn/ D f .u1.x1; : : : ; xn/; : : : ; un.x1; : : : ; xn//<br><!-- End of picture text -->

dostali 



<!-- Start of picture text -->
@F D Xn @f @uj ; i D 1; 2; : : : ; n:<br>@xi @uj @xi<br>j D1<br><!-- End of picture text -->

Princip řetězového pravidla dále zůstává stejný, i když počet proměnných vnitřních funkcí není stejný jako počet proměnných vnější funkce. 

b) Pro derivace druhého řádu by se tvrzení modifikovalo: mají-li funkce u a v parciální derivace do druhého řádu v bodě Œx0; y0� a funkce f má parciální derivace druhého řádu na okolí bodu Œu0; v0� D Œu.x0; y0/; v.x0; y0/�, které jsou v tomto bodě spojité, pak funkce F.x; y/ D f .u.x; y/; v.x; y// má druhé parciální derivace v bodě Œx0; y0� a platí 



<!-- Start of picture text -->
Fxx 00 D f uu 00 .u0 x /2 C 2f uv 00 u0 x v x 0 C f vv 00 .v x 0 /2 C f u 0u00 xx C f v 0v xx 0 ;<br>Fxy 00 D f uu 00 u0 x u y 0 C 2f uv 00 u0 x v y 0 C f vv 00 v x 0 v y 0 C f u 0u00 xy C f v 0v xy 0 ;<br>Fyy 00 D f uu 00 .u y 0 /2 C 2f uv 00 u y 0 v y 0 C f vv 00 .v y 0 /2 C f u 0u yy 00 C f v 0v yy 0 :<br><!-- End of picture text -->

Skutečně, např. pro Fxx<sup>00máme</sup> 



<!-- Start of picture text -->
Fxx 00 D .f u 0u0 x /0 x C .f v 0v x 0 /0 x D .f u 0/0 x u0 x C f u 0u00 xx C .f v 0/0 x v x 0 C f v 0v xx 00<br>D .fuu 0 u0 x C f uv 00 v x 0 /u0 x C f u 0u00 xx C .f vu 00 u0 x C f vv 00 v x 0 /v x 0 C f v 0v xx 0<br>D fuu 0 .u0 x /2 C 2f uv 00 u0 x v x 0 C f vv 00 .v x 0 /2 C f u 0u00 xx C f v 0v xx 0 ;<br><!-- End of picture text -->

přičemž jsme využili linearitu operace derivování a rovnost fuv<sup>00D f</sup> vu<sup>00.</sup> 

> ■ Vˇeta 9.3 — Taylorova. _Nechť funkce_ f W R<sup>n</sup> ! R _má v bodě_ X0 _a nějakém jeho okolí spojité parciální derivace až do řádu_ m C 1 _včetně. Pak pro libovolné_ X _z tohoto okolí platí_ 



<!-- Start of picture text -->
f .X/ D Tm.X/ C Rm.X/;<br><!-- End of picture text -->

_kde_ 



<!-- Start of picture text -->
Tm.X/ D f .X0/ C 1Š 1 df .X0I X � X0/ C 2Š 1 d2f .X0I X � X0/ C ���C mŠ 1 dmf .X0I X � X0/<br><!-- End of picture text -->

_se nazývá Taylorův polynom (stupně_ m _) a_ 



<!-- Start of picture text -->
1<br>Rm.X/ D .m C 1/Š dmC1f .X0 C #.X � X0/I X � X0/; # 2 .0; 1/<br><!-- End of picture text -->

_se nazývá_ m _-tý Taylorův zbytek v Lagrangeově tvaru._ 

9 Derivace složené funkce, Taylor˚uv polynom 

35 

_Idea důkazu._ Zavede se pomocná funkce F.t/ D f .X0 C t.X � X0//, pro kterou platí F.1/ D f .X/, a využije se Taylorova věta pro funkci jedné proměnné v bodě t D 0, tj. 



<!-- Start of picture text -->
F.1/ D F.0/ C 1Š 1 F 0.0/ C 2Š 1 F 00.0/ C ���C mŠ 1 F .m/.0/ C .m C1  1/Š F .mC1/.#/:<br><!-- End of picture text -->

Aplikujme-li pro výpočet derivací F<sup>.k/</sup> pravidlo pro parciální derivace složených funkcí, dostaneme vzorec věty. 

Poznámka 9.4. Nechť všechny parciální derivace řádu m C 1 funkce f jsou ohraničené stejnou konstantou c > 0 na úsečce X0 C tH , t 2 h0; 1i (H D Œh1; h2; : : : ; hn� 2 R<sup>n</sup> ), která leží v uvažovaném okolí. Pak pro odhad zbytku Rm platí: 



<!-- Start of picture text -->
c<br>jRm.X0 C H/j � �jh1j C jh2j C ���C jhnj�mC1:<br>.m C 1/Š<br><!-- End of picture text -->

Pˇríklad 9.5. Určete Taylorův polynom T2 funkce f .x; y/ D ~~p~~ 1 � x<sup>2</sup> � 4y<sup>2</sup> v bodě Œ0; 0�. Pomocí tohoto polynomu určete přibližně hodnotu f .1=4; 1=8/ a proveďte odhad chyby, které se aproximací dopustíme. 

_Řešení._ Máme f .0; 0/ D 1 a postupným napočítáním derivací až do druhého řádu snadno ověříme, že 



<!-- Start of picture text -->
df .0; 0/ D 0; d 2 f .0; 0/ D �h 2 � 4k 2 :<br><!-- End of picture text -->

Protože h D x � 0 D x, k D y � 0 D y, Taylorův polynom má tvar 



<!-- Start of picture text -->
T2.x; y/ D 1 � 1<br>2 x2 � 2y2<br><!-- End of picture text -->

(tento polynom spolu s původní funkcí jsou znázorněny na obrázku 9.1). Aproximace dané funkční hodnoty potom je 



<!-- Start of picture text -->
p 14<br>f D � 1 � 1 � 2 D 0; 9375:<br>� 41 ; 1 8 � 4 2 � 41 �2 � 18 �2<br>Pro odhad zbytku potřebujeme navíc třetí derivace. Platí:<br>000 3x.4y 2 � 1/ 000<br>fxxx D fxxy D 4y.4y2 � 2x2 � 1/<br>.1 � x 2 � 4y 2 / 5=2 ; .1 � x 2 � 4y 2 / 5=2 ;<br>000 000 48y.x 2 � 1/<br>fxyy D .1 4x  � .x x 22 � � 8 4y y22 � / 5=21/ ; fyyy D .1 � x 2 � 4y 2 / 5=2 :<br><!-- End of picture text -->

Pro odhad zbytku potřebujeme navíc třetí derivace. Platí: 

Protože nás zajímá ohraničenost derivací na úsečce x D t=4, y D t=8, t 2 h0; 1i, zaveďme funkce 



<!-- Start of picture text -->
000 3t 3 � 48t 000 t 3 C 16t<br>'1.t/ D fxxx � 4t ; 8 t � D 64.1 � t 2 =8/ 5=2 ; '2.t/ D fxxy � 4t ; 8 t � D � 32.1 � t 2 =8/ 5=2<br>000 t 3 C 16t 000 t 3 � 96t<br>'3.t/ D fxyy � 4t ; 8 t � D � 16.1 � t 2 =8/ 5=2 ; '4.t/ D fyyy � 4t ; 8 t � D 16.1 � t 2 =8/ 5=2 :<br><!-- End of picture text -->

Není těžké ověřit, že všechny čtyři funkce jsou v absolutní hodnotě na intervalu h0; 1i ohraničené číslem 8. Podle výše uvedeného vzorce tedy máme 



<!-- Start of picture text -->
9<br>D<br>ˇˇˇˇR2 � 41 ; 1 8 �ˇˇˇˇ � 3Š8 � 41 C 1 8 �3 128 D 0;0703125:<br><!-- End of picture text -->

Výpočtem na kalkulačce nebo počítači se lze přesvědčit, že skutečná chyba je výrazně menší (cca 0,002), odhad zbytku pomocí uvedeného vzorce bývá obvykle dosti pesimistický. 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

36 



Obrázek 9.1: Graf funkce f (horní polovina elipsoidu, tmavší šedá) a jejího Taylorova polynomu druhého stupně (eliptický paraboloid, světlejší šedá) z příkladu 9.5 

#### Pˇríklady k procviˇcení 

9.1. Transformujte funkci V.x; y/ D xfy<sup>0�yf</sup> x<sup>0do polárních souřadnic (tj. pomocí řetězového pravidla jej</sup> vyjádřete v proměnných � a '). O funkci f předpokládejme, že má spojité parciální derivace. Připomeňme, že vztah mezi kartézskými a polárními souřadnicemi je x D � cos ', y D � sin '. 

9.2. Napište Taylorův polynom třetího stupně funkce 



<!-- Start of picture text -->
x<br>f .x; y/ D arcsin<br>p x 2 C y 2<br><!-- End of picture text -->

v bodě A D Œ0; 1�. 

9.3. Určete přibližně hodnotu<sup>~~p~~</sup> 3 2 � 1; 02 � 0; 98 pomocí Taylorova polynomu druhého stupně (vhodné funkce ve vhodném bodě). Určete také odhad chyby, které se tuto aproximací dopustíme. 

_Výsledky._ 9.1. V<sup>�</sup> .�; '/ D F'<sup>0,kdeF.�; '/Df .�cos '; �sin '/.9.2.T3.x; y/Dx�x.y�1/ �</sup> <u>13</u><sup>x3C x.y�1/2.9.3.1; 0001</sup> 3, všechny parciální derivace třetího řádu jsou na úsečce 1 C 0;02t, 1 � 0;02t , t 2 h0; 1i, ohraničené číslem 1 (lze nalézt i o něco lepší konstantu), a tedy jR2.1;02I 0;98/j � <u>16</u><sup>.0; 02 C 0; 02/3�1;07 �10�5.</sup> 

### 10 Lokální a globální extrémy 

Definice 10.1 — lokálních extrém˚u. Řekneme, že funkce f W R<sup>n</sup> ! R nabývá v bodě X0 2 R<sup>n</sup> _lokálního maxima_ (resp. _minima_ ), jestliže existuje okolí O.X0/ takové, že O.X0/ � D.f / a pro každé X 2 O.X0/ platí f .X/ � f .X0/ (resp. f .X/ � f .X0/). Jsou-li tyto nerovnosti pro X ¤ X0 ostré, mluvíme o _ostrém_ lokálním maximu (resp. minimu). (Ostrá) lokální maxima a minima nazýváme souhrnně _(ostré) lokální extrémy_ . 

Pˇríklad 10.2. a) Funkce f .x; y/ D ~~p~~ x<sup>2</sup> C y<sup>2</sup> má v bodě Œ0; 0� ostré lokální minimum, protože f .x; y/ > 1 pro Œx; y� D Œ0; 0� 0 D f .0; 0/ pro 8Œx; y� ¤ Œ0; 0�. b) Funkce f .x; y/ D má v bodě Œ0; 0� ostré (0 pro Œx; y� ¤ Œ0; 0� lokální maximum. Příklad a) ukazuje, že funkce nemusí být v bodě lokálního extrému diferencovatelná, příklad b) ukazuje, že nemusí být ani spojitá. 

Definice 10.3 — stacionárního bodu. Řekneme, že bod S 2 R<sup>n</sup> je _stacionárním bodem funkce_ f W R<sup>n</sup> ! R, jestliže platí grad f .S/ D oE D .0; 0; : : : ; 0/. 

10 Lokální a globální extrémy 

37 

■ Vˇeta 10.4. _Nechť funkce_ f W R<sup>n</sup> ! R _má v bodě_ X<sup>�</sup> 2 R<sup>n</sup> _lokální extrém a nechť v tomto bodě existují všechny parciální derivace funkce_ f _. Pak_ X<sup>�</sup> _je stacionárním bodem funkce_ f _._ 

_Důkaz._ Kdyby fx<sup>0</sup> i<sup>.X�/ > 0, tj.</sup> 



<!-- Start of picture text -->
f .x1 �; : : : ; x i � �1 ; x i � C h; x i � C1 ; : : : ; x n �/ � f .x 1 �; : : : ; x i � �1 ; x i �; x i � C1 ; : : : ; x n �/<br>lim > 0;<br>h!0 h<br><!-- End of picture text -->

pak by existovalo ı > 0 takové, že pro každé h 2 .�ı; ı/ n f0g je také 



<!-- Start of picture text -->
f .x1 �; : : : ; x i � �1 ; x i � C h; x i � C1 ; : : : ; x n �/ � f .x 1 �; : : : ; x i � �1 ; x i �; x i � C1 ; : : : ; x n �/<br>> 0;<br>h<br><!-- End of picture text -->

viz vlastnosti limity. To znamená, že pro kladná h z .�ı; ı/ je 



<!-- Start of picture text -->
f .x1 �; : : : ; x i � �1 ; x i � C h; x i � C1 ; : : : ; x n �/ > f .x 1 �; : : : ; x i � �1 ; x i �; x i � C1 ; : : : ; x n �/;<br>a pro záporná h je<br>f .x1 �; : : : ; x i � �1 ; x i � C h; x i � C1 ; : : : ; x n �/ < f .x 1 �; : : : ; x i � �1 ; x i �; x i � C1 ; : : : ; x n �/;<br>což je spor s tím, že bod X � je bodem lokálního extrému. Analogicky vyloučíme možnost fx 0 i .X �/ < 0.<br><!-- End of picture text -->

Poznámka 10.5. Podobně jako u funkce jedné proměnné, stacionární bod nemusí být bodem lokálního extrému, např. funkce f .x; y/ D x<sup>2</sup> � y<sup>2</sup> má v bodě Œ0; 0� stacionární bod, ale není zde extrém (takovým stacionárním bodům říkáme sedlový bod). 

Definice 10.6 — kvadratické formy. Funkce K.X/ D<sup>Pn</sup> i;j D1<sup>bij xixj ,kdebij2RaX2Rn,se</sup> nazývá _kvadratická forma na_ R<sup>n</sup> (jedná se tedy o polynom druhého stupně n proměnných, ve kterém se nevyskytuje lineární a absolutní člen). 

Pokud bod X D Œx1; x2; : : : ; xn� identifikujeme s (vázaným) vektorem Ex D X �O D .x1; x2; : : : ; xn/, pak každé kvadratické formě lze jednoznačně přiřadit symetrickou matici A D .aij /<sup>n</sup> i;j D1<sup>tak, že platí</sup> K.X/ D xAE xE<sup>T</sup> . Prvky matice jsou dány aii D bii , aij D aji D 2<sup><u>1</u>.bijC bji/. Říkáme potom, že</sup><sup>_matice_</sup> A _reprezentuje kvadratickou formu_ K. 

Definice 10.7 — definitnosti kvadratické formy. Nechť A je symetrická matice. Řekneme, že kvadratická forma xAE xE<sup>T</sup> je _pozitivně definitní_ xAE xE<sup>T</sup> > 0 _negativně definitní_ xAE xE<sup>T</sup> < 0 , jestliže pro každý vektor xE ¤ oE platí , _pozitivně semidefinitní_ xAE xE<sup>T</sup> � 0 _negativně semidefinitní_ xAE xE<sup>T</sup> � 0 _indefinitní_ , existují-li vektory xE1; Ex2 tak, že xE1AxE1<sup>T< 0 axE2AxE</sup> 2<sup>T> 0 (tj. není-li definitní ani semidefi-</sup> nitní). 

Poznámka 10.8. Protože každá kvadratická forma je symetrickou maticí A určena jednoznačně, lze hovořit přímo o definitnosti matice (namísto formy). 

Definice 10.9 — hlavních minor˚u. Nechť A D .aij /<sup>n</sup> i;j D1<sup>je čtvercová matice (ne nutně symetrická). Pak</sup> _základními (rohovými) hlavními minory_ rozumíme determinanty 



<!-- Start of picture text -->
a11 a12 a13<br>a12 0 1<br>M1 D det.a11/; M2 D det ; M3 D det a21 a22 a23 : : : ; Mn D det.A/:<br>�aa2111 a22�<br>@a31 a32 a33A ;<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

38 

Základní hlavní minory tvoří podmnožinu všech hlavních minorů Mk<sup>`.</sup><sup>_Hlavníminoryřádu_kjsou</sup> determinanty čtvercových matic k � k (k D 1; : : : ; n), které vzniknou z matice A vynecháním n � k řádků a n � k sloupců, přičemž vynecháváme vždy odpovídající si sloupce a řádky (tj. i -tý řádek s i -tým sloupcem). Počet hlavních minorů řádu k je �kn�, tj. ` D 1; 2; : : : ; �kn�. Celkový počet hlavních minorů je pak �n1� C �n2� C ���C �nn� D 2<sup>n</sup> � 1. 

■ Vˇeta 10.10 — Sylvestrovo<sup>2</sup> kritérium. _Nechť_ A 2 R<sup>n�n</sup> _je symetrická matice,_ Mk _(_ k D 1; : : : ; n _) jsou její základní hlavní minory a_ Mk<sup>`</sup><sup>_(_kD 1; : : : ; n</sup><sup>_,_` D 1; : : : ;</sup> �kn� _) jsou její hlavní minory. Pak kvadratická_ 

_forma_ xAE xE<sup>T</sup> _je:_ 

- (i) _pozitivně definitní_ () _všechny základní hlavní minory_ Mk _(_ k D 1; : : : ; n _) jsou kladné,_ 

- (ii) _negativně definitní_ () _pro všechny základní hlavní minory_ Mk _platí_ sgn Mk D .�1/<sup>k</sup> _, tj._ M1 < 0 _,_ M2 > 0 _,_ M3 < 0 _, . . . ,_ 

(iii) _pozitivně semidefinitní_ () _všechny hlavní minory_ Mk<sup>`</sup><sup>_jsou nezáporné,_</sup> (iv) _negativně semidefinitní_ () _pro všechny hlavní minory_ Mk<sup>`</sup><sup>_platí_sgn M</sup> k<sup>`D .�1/k</sup><sup>_nebo_M `</sup> k<sup>D 0</sup><sup>_._</sup> 

_Nenastane-li ani jeden z předchozích případů, pak_ xAE xE<sup>T</sup> _je indefinitní._ 

Důkaz kritéria se opírá o několik poznatků z lineární algebry týkajících se symetrických matic, především pak o větu o hlavních osách. Postupně si potřebné vlastnosti uveďme a dokažme. 

■ Lemma 10.11. _Nechť_ A 2 R<sup>n�n</sup> _je symetrická matice. Potom vlastní vektory příslušné dvěma různým vlastním číslům_<sup>3</sup> _matice jsou ortogonální_<sup>4</sup> _._ 

_Důkaz._ Nechť � ¤ � jsou vlastní čísla matice A, vE D .v1; : : : ; vn/, resp. wE D .w1; : : : ; wn/, je vlastní vektor příslušný �, resp. �. Potom 



<!-- Start of picture text -->
.� � �/vE �Ew D �.vE �Ew/ � �.vE �Ew/ D w.�E vE T / �Ev.�wE T /<br>D w.AE vE T / �Ev.Aw E T / D .AvE T / T wE T �EvA Ew T<br>D vAE T wE T �Ev T Aw E T D vAE w E T �EvA Ew T (protože A T D A)<br>D 0:<br><!-- End of picture text -->

Protože podle předpokladu � ¤ �, musí být vE �Ew D 0, tj. vlastní vektory vE, wE jsou ortogonální. 

■ Lemma 10.12 — Gram˚uv–Schmidt˚uv ortogonalizaˇcní proces. _Je-li_ fEu1; Eu2; : : : ; Eung n _-tice lineárně nezávislých vektorů_<sup>5</sup> _v_ R<sup>n</sup> _(tj. báze), potom vektory_ vE1; Ev2; : : : ; Evn _dané rekursivně_ 



<!-- Start of picture text -->
vE1 D uE1;<br>vE2 D uE2 � uE2 �Ev1<br>jEv1j 2 vE1;<br>vE3 D uE3 � uE jE 3 v  �E 1j v21 vE1 �Eu jE 3 v  �E 2j v22 vE2;<br>: : :<br>vEn D uEn � uE jE n v  �E 1j v21 vE1 �Eu jE n v  �E 2j v22 vE2 � : : : �Eu jE n v  �E n� v 1 n j �21 vEn�1;<br><!-- End of picture text -->

_jsou nenulové a vzájemně ortogonální (_ n _-tice_ fv1; v2; : : : ; vng _tedy tvoří ortogonální bázi v_ R<sup>n</sup> _). Pokud navíc položíme_ wEi D vEi =jEvi j _,_ i D 1; 2; : : : ; n _, pak_ n _-tice_ f Ew1; wE2; : : : ; wEng _je ortonormální._ 

2James Joseph Sylvester 1814–1897, Angličan 

> 3Připomeňme, že � 2 C se nazývá _vlastní číslo_ čtvercové matice A 2 Rn�n, jestliže existuje nenulový vektor xE 2 Rn takový, že AxE D �xE. Vektor xE se pak nazývá _vlastní vektor_ příslušný vlastnímu číslu �. 

> 4Vektory u;E Ev 2 Rn nazveme _ortogonální_ , pokud uE �Ev D 0 („�“ značí standardní skalární součin, platí uE �Ev D uEvET ). Jsou li navíc vektory u;E Ev jednotkové, pak se nazývají _ortonormální_ . 

> 5Vektory uE1; Eu2; : : : ; Eun 2 Rn se nazývají _lineárně nezávislé_ , jestliže rovnost c1 Eu1 C c2 Eu2 C ���C cn Eun D 0 je splněna pouze v případě c1 D c2 D ���D cn D 0 (to implikuje, že žádný vektor nelze vyjádřit jako lineární kombinaci ostatních). 

10 Lokální a globální extrémy 

39 

_Důkaz._ Protože fEu1; Eu2; : : : ; Eung je množina lineárně nezávislých vektorů, platí vE1 D uE1 ¤ oE, a tedy j Ew1j D 1. Tvrzení dále dokážeme tak, že ověříme ortogonalitu vektoru vEk (a jeho nenulovost) ke každému z vektorů vE1; Ev2; : : : ; Evk�1 za předpokladu, že pro těchto k � 1 vektorů tvrzení platí. Jinak řečeno, použijeme matematickou indukci „k � 1 ) k “, kde k je libovolně zvolený index takový, že 2 � k � n (pro k D n pak dostaneme platnost lemmatu). Připusťme nejprve, že vEk je nulový. Pak 



<!-- Start of picture text -->
uEk D uE jE k v1 �E j v21 vE1 C uE jE k v2 �E j v22 vE2 C ���C uE jE k vk �E � v 1 k j �21 vEk�1;<br><!-- End of picture text -->

tj. uEk je lineární kombinací vektorů vE1; Ev2; : : : ; Evk�1 (které jsou podle indukčního předpokladu nenulové). Na druhou stranu, z prvních k � 1 řádků vidíme, že každý vektor vEi (i D 1; 2; : : : ; k � 1) je lineární kombinací vektorů uE1; Eu2; : : : ; Eui . To však znamená, že uEk je lineární kombinací předcházejících vektorů uE1; Eu2; : : : ; Euk�1, což je spor s lineární nezávislostí vektorů uE1; Eu2; : : : ; Eun. Vektor vEk je tedy nenulový. Spočítejme dále skalární součin vektorů vEk �Evi , kde vEi 2 fEv1; Ev2; : : : ; Evk�1g. S využitím definice vEk máme 



<!-- Start of picture text -->
vEk �Evi D uEk �Evi � uEk �Ev1 vE1 �Evi � uEk �Ev2 vE2 �Evi � : : : � uEk �Evk�1 vEk�1 �Evi :<br>jEv1j 2 jEv2j 2 jEvk�1j 2<br><!-- End of picture text -->

Všechny členy na pravé straně se znaménkem „minus“ jsou z důvodu ortogonality nulové vyjma i-tého, kdy 



<!-- Start of picture text -->
uEk �Evi vEi �Evi D uEk �Evi<br>jEvi j 2 jEvi j 2 jEvi j2 D uEk �Evi :<br><!-- End of picture text -->

Máme tedy Evk �Evi D uEk �Evi �Euk �Evi D 0, a protože Evi byl libovolný vektor z množiny fEv1; Ev2; : : : ; Evk�1g, vEk je ortogonální ke každému z vektorů vE1; Ev2; : : : ; Evk�1. Pro k D n pak dostáváme ortogonalitu pro celou n-tici vektorů. Protože každý z vektorů vEi , i D 1; 2; : : : ; n, je nenulový, můžeme jej znormalizovat vydělením jeho velikostí. Tím dostáváme ortonormální množinu vektorů. 

■ Vˇeta 10.13 — Vˇeta o hlavních osách. _Nechť_ A 2 R<sup>n�n</sup> _je symetrická matice. Potom_ A _je ortogonálně diagonalizovatelná, tj. existuje ortogonální matice_<sup>6</sup> Q 2 R<sup>n�n</sup> _a existuje diagonální matice_ D 2 R<sup>n�n</sup> _, přičemž platí_ Q<sup>T</sup> AQ D D _._ 

_Důkaz._ Tvrzení dokážeme opět principem matematické indukce. Pro n D 1 zřejmě platí, protože A D a 2 R je již diagonální (Q D Q<sup>T</sup> D 1). Nechť n D 2. Označme 



<!-- Start of picture text -->
b<br>A D b c ;<br>�a �<br><!-- End of picture text -->

kde a; b; c 2 R. Potom charakteristický polynom PA.�/ D det.�I � A/ má tvar 



<!-- Start of picture text -->
PA.�/ D � 2 � .a C c/� C ac � b 2 ;<br><!-- End of picture text -->

jehož diskriminant je .a C c/<sup>2</sup> � 4ac C 4b<sup>2</sup> D .a � c/<sup>2</sup> C b<sup>2</sup> � 0, což znamená, že PA má pro jakoukoliv symetrickou matici A pouze reálné kořeny. Tento diskriminant je nulový pouze v případě a D c, b D 0, neboli v případě, kdy A D aI , což je diagonální matice. Číslo a je zřejmě dvojnásobné vlastní číslo této matice. Tvrzení tedy platí s maticí Q D I (jednotková matice je ortogonální a její sloupce jsou dva ortonormální vlastní vektory příslušné vlastnímu číslu a). Předpokládejme druhý případ, tj. A ¤ aI . Potom PA má dva různé reálné kořeny, tj. matice A má dvě různá reálná vlastní čísla, označme je � a �. Nechť vE D .v1; v2/ a wE D .w1; w2/ jsou jednotkové vlastní vektory příslušné �, resp. � (protože vlastní čísla jsou reálná, tyto vlastní vektory musí být také reálné). Pak Q D .vE<sup>T</sup> ; wE<sup>T</sup> / je díky lemmatu 10.11 ortogonální matice, a protože AvE<sup>T</sup> D �vE<sup>T</sup> , Aw E<sup>T</sup> D �wE<sup>T</sup> , máme 



<!-- Start of picture text -->
Q T AQ D .vE T ; wE T / T A.vE T ; wE T / D .vE T ; wE T / T .AvE T ; Aw E T / D .vE T ; wE T / T .�vE T ; �wE T /<br>0 0 0<br>D .vE T ; wE T / T .vE T ; wE T / D I D :<br>0 � 0 � 0 �<br>�� � �� � �� �<br><!-- End of picture text -->

> 6 _Ortogonální matice_ je čtvercová matice, jejíž sloupce (a zároveň řádky) tvoří množinu ortonormálních vektorů (tj. vzájemně kolmých vektorů s jednotkovou velikostí). 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

40 

Tím je tvrzení dokázáno pro n D 2. Všimněme si, že vzniknuvší diagonální matice má na diagonále vlastní čísla matice A a ortogonální matice Q je tvořena sloupci vlastních vektorů příslušných k jednotlivým vlastním číslům. 

Předpokládejme nyní, že tvrzení platí pro symetrické matice řádu n D k � 1 (kde k > 3 je libovolně zvolené přirozené číslo) opět s diagonální maticí tvořenou reálnými vlastními čísly a ortogonální maticí tvořenou vlastními vektory (indukční předpoklad). Napišme matici A ve tvaru 



<!-- Start of picture text -->
B vE T<br>A D � vE c � ;<br><!-- End of picture text -->

kde B 2 R<sup>.k�1/�.k�1/</sup> je symetrická matice, vE D .v1; : : : ; vk�1/ 2 R<sup>k�1</sup> je vektor a c 2 R. Podle indukčního předpokladu existují ortogonální matice Q řádu k � 1 a diagonální matice D D diag.�1; �2; : : : ; �k�1/ takové, že Q<sup>T</sup> BQ D D. Uvažujeme-li nyní matici 



<!-- Start of picture text -->
Q oE T<br>W D � oE 1 � ;<br><!-- End of picture text -->

která je zřejmě ortogonální, pak 



<!-- Start of picture text -->
0�01 �02 : : :: : : 00 vv12 1<br>D vE T<br>W T AW D � vE c � D ::: ::: ::: ::: ::: :<br>0 0 : : : �n�1 vn�1<br>BBBBB@v1 v2 : : : vn�1 c CCCCCA<br><!-- End of picture text -->

Ortogonální matice W splňuje W<sup>T</sup> W D I . Protože determinant součinu je součin determinantů a determinant matice je roven determinantu transpozice této matice, platí .det.W //<sup>2</sup> D 1, a tedy det.W / D ˙1. Odtud 

PA.�/ D det.�I � A/ D det.W<sup>T</sup> .�I � A/W / D det.W<sup>T</sup> �W � W<sup>T</sup> AW / 



<!-- Start of picture text -->
0� �0�1 � �0�2 : : :: : : 00 ��vv12 1<br>D det.�I � W T AW / D det ::: ::: ::: ::: ::: :<br>0 0 : : : � � �k�1 �vk�1<br>BBBBB@ �v1 �v2 : : : �vk�1 � � c CCCCCA<br><!-- End of picture text -->

Je známo, že přičtení násobku řádku matice k jinému řádku této matice nemění determinant. Gaussovou eliminační metodou tedy převedeme matici na dolní trojúhelníkovou tak, že k poslednímu řádku přičteme postupně vi =.� � �i /-násobek i-tého řádku (i D 1; 2; : : : ; k � 1). To vede na 



<!-- Start of picture text -->
0� �0�1 � �0�2 : : :: : : 00 ��vv21 1<br>�I � W T AW � ::: ::: ::: ::: ::: ;<br>0 0 : : : � � �k�1 �vk�1<br>BBBBB@ 0 0 : : : 0 x CCCCCA<br><!-- End of picture text -->

kde 



<!-- Start of picture text -->
x D � � c � � �v1 2 �1 � � �v2 2 �2 � : : : � � �vk 2 ��k1�1 :<br><!-- End of picture text -->

Protože determinant trojúhelníkové matice je roven součinu prvků na hlavní diagonále, máme 



<!-- Start of picture text -->
PA.�/ D det.�I � W T AW / D .� � �1/.� � �2/ ��� .� � �k�1/.� � c/<br>� v1 2.� � �2/.� � �3/ : : : .� � � k�1 /<br><!-- End of picture text -->

10 Lokální a globální extrémy 

41 



<!-- Start of picture text -->
� v2 2.� � �1/.� � �3/ : : : .� � � k�1 /<br>� : : :<br><!-- End of picture text -->



<!-- Start of picture text -->
� vk 2 �1 .� � �1/.� � �2/ : : : .� � �k�2/:<br><!-- End of picture text -->

Nechť j je nyní ten index, pro který je �j největší ze všech vlastních čísel �1; : : : ; �k�1. Potom 



<!-- Start of picture text -->
PA.�j / D �vj 2.�j � �1/ ��� .�j � �j �1/.�j � �j C1/ ��� .�max � �k�1// � 0;<br><!-- End of picture text -->

tj. funkční hodnota charakteristického polynomu v bodě �j je nezáporná. Protože navíc lim�!1 PA.�/ D 1, tak to znamená, že PA má reálný kořen �<sup>�</sup> . Pro PA.�j / D 0 je tímto kořenem opět číslo �j , pro PA.�j / < 0 je existence reálného kořene zaručena I. Bolzanovou větou, protože PA je spojitá funkce na R (z vlastnosti lim�!1 PA.�/ D 1 plyne existence čísla b < 1 takového, že PA.b/ > 0, viz definice nevlastní limity). Protože �<sup>�</sup> je reálným vlastním číslem matice A, existuje reálný jednotkový vlastní vektor wE D .w1; : : : ; wk/ 2 R<sup>k</sup> takový, že A Ew<sup>T</sup> D �<sup>�</sup> wE<sup>T</sup> . Pomocí tohoto vektoru je možné vytvořit reálnou ortogonální matici U (např. tak, že k tomuto vektoru přidáme k � 1 vektorů, aby vzniklá k-tice byla lineárně nezávislá a aplikujeme Gramův–Schmidtův ortogonalizační proces (viz lemma 10.12). Navíc platí 



<!-- Start of picture text -->
0uEwE21 0uEwE21 oE<br>U T AU D ::: 2 ; : : : ; EuT k / D ::: � „ƒ‚…A Ew T ; AuE T 2 ; : : : ; AuET k � D �o�E T � C � ;<br>D� � wE T<br>BBB@uEkCCCA A.w E T ; EuT BBB@uEkCCCA<br><!-- End of picture text -->

kde C je nějaká symetrická matice řádu k � 1. Podle indukčního předpokladu existuje ortogonální matice V (řádu k � 1) taková, že V<sup>T</sup> CV je reálná diagonální matice (diagonála obsahuje vlastní čísla matice C ). Pokud nyní položíme 



<!-- Start of picture text -->
oE<br>S D U �oE1 T V � ;<br><!-- End of picture text -->

tak S je symetrická a ortogonální matice (součin dvou ortogonálních matic je opět ortogonální matice<sup>7</sup> ). Navíc, 



<!-- Start of picture text -->
oE oE oE oE oE<br>S T AS D U T AU D<br>�oE1 T V �T �oE1 T V � �oE1 T V T ��o�E T � C ��oE1 T V �<br>oE oE<br>D D<br>D diag.� � ; �1; : : : ; �k�1/;<br>�o�E T � V T CV � �o�E T � D�<br><!-- End of picture text -->

což jsme chtěli dokázat. 

Princip matematické indukce pak říká, že tvrzení platí pro libovolné n 2 N. 

Z důkazu věty je patrno, že diagonální matice D má na diagonále vlastní čísla matice A a sloupce ortogonální matice Q tvoří vlastní vektory matice A. I kdybychom důkaz k dispozici neměli, tato vlastnost z věty jednoduše vyplývá. Skutečně, vynásobením rovnosti Q<sup>T</sup> AQ D D D diag.d1; : : : ; dn/ maticí Q zleva dostáváme 

Q.Q<sup>T</sup> AQ/ D QD ) .QQ<sup>T</sup> /AQ D QD ) AQ D QD: 

Označíme-li i -tý sloupec matice Q jako qEi , pak poslední rovnost lze rozepsat 



<!-- Start of picture text -->
0d01 d02 : : :: : : 00 1<br>A�qE1; Eq2; : : : ; Eqn� D �qE1; Eq2; : : : ; Eqn�<br>::: ::: ::: :::<br>BBB@ 0 0 : : : dnCCCA ;<br><!-- End of picture text -->

> 7Jsou-li dvě čtvercové matice A a B ortogonální, pak .AB/T .AB/ D .B T AT /AB D B T .AT A/B D B T IB D B T B D I , a tedy AB je ortogonální. 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

42 

tj. 



<!-- Start of picture text -->
�AqE1; AqE2; : : : ; AqEn� D �d1qE1; d2qE2; : : : ; dnqEn�:<br><!-- End of picture text -->

Platí tedy AqEi D d1qEi pro každé i D 1; : : : ; n. Jinými slovy, di je vlastní číslo matice a qEi je příslušný vlastní vektor. Protože vektory qEi , qEj , i ¤ j , jsou ortogonální, a tudíž lineárně nezávislé, platí, že geometrická násobnost vlastního čísla je rovna algebraické násobnosti. Výše uvedené úvahy jsou shrnuty v následujícím důsledku. 

■ D˚usledek 10.14. _Diagonála matice_ D _z předchozí věty sestává z vlastních čísel matice_ A _(ta jsou reálná, protože věta říká, že_ D _je reálná matice) a sloupce matice_ Q _tvoří příslušné vlastní vektory (které jsou vzájemně ortogonální)._ 

Z věty 10.13 lze snadno vyvodit také následující vlastnost. 

- D˚usledek 10.15. a) _Kvadratická forma_ xAE xE<sup>T</sup> _se symetrickou maticí_ A 2 R<sup>n�n</sup> _je pozitivně definitní (resp. pozitivně semidefinitní), právě když všechna vlastní čísla matice_ A _jsou kladná (resp. nezáporná)._ 

- b) _Je-li kvadratická forma_ xAE xE<sup>T</sup> _se symetrickou maticí_ A 2 R<sup>n�n</sup> _pozitivně definitní (resp. pozitivně semidefinitní), pak_ det.A/ > 0 _(resp._ det.A/ � 0 _)._ 

_Důkaz._ a) Nechť yE 2 R<sup>n</sup> je libovolný nenulový vektor a položme xE<sup>T</sup> D Q Ey<sup>T</sup> , kde Q je ortogonální matice z věty 10.13. Pak vektor xE je také nenulový, protože Q je regulární. Máme tedy 



<!-- Start of picture text -->
n<br>xAE xE T D .Q Ey T / T A.Q Ey T / D y.QE T AQ/ Ey T D yDE  Ey T D X di yi 2;<br>i<br><!-- End of picture text -->

kde D D diag.d1; : : : ; dn/ je podle předchozího důsledku diagonální matice, jejíž prvky di jsou vlastní čísla matice A (využili jsme přitom asociativitu maticového násobení). Protože vektor yE je libovolný nenulový, pravá strana je kladná (resp. nezáporná), právě když všechna di jsou kladná (resp. nezáporná). 

b) Díky větvi a) víme, že matice A pozitivně definitní formy má vlastní čísla �i (i D 1; 2; : : : ; n) kladná. Máme tedy 

det.A/ D det.Q<sup>T</sup> DQ/ D det.Q<sup>T</sup> / det.D/ det.Q/ D det.D/ D �1�2 ��� �n > 0; 

přičemž využíváme, že det.Q/ D det.Q<sup>T</sup> / D ˙1 pro jakoukoli ortogonální matici Q a determinant součinu je roven součinu determinantů. Analogicky, matice pozitivně semidefinitní formy má všechna vlastní čísla nezáporná, a tedy det.A/ D �1�2 ��� �n � 0. 

_Důkaz Sylvestrova kritéria._ (i) „H)“ Nechť ExAxE<sup>T</sup> je pozitivně definitní kvadratická forma se symetrickou maticí A 2 R<sup>n�n</sup> . Označme symbolem Ak submatice matice A vystupující v definici 10.9, jejichž determinanty jsou čísla Mk. Nechť yEk D .y1; y2; : : : ; yk/ 2 R<sup>k</sup> , k � n, je nenulový vektor a položme xEk D .x1; x2; : : : ; xk; 0; : : : ; 0/ 2 R<sup>n</sup> . Pak pro každý index k z množiny f1; 2; : : : ; ng platí yEkAk Eyk<sup>TD</sup> xEkAxEk<sup>T> 0, tj. kvadratická formayEkAk Ey</sup> k<sup>Tje pozitivně definitní, a podle důsledku 10.15b) je det.Ak/ D</sup> Mk > 0. 

„(H“ Tuto implikaci dokážeme matematickou indukcí. Případ n D 1 zřejmě platí, neboť v takovém případě je A D a 2 R, a tedy předpoklad M1 D det.A/ D a > 0 implikuje, že xAx D ax<sup>2</sup> > 0 pro x ¤ 0, tj. forma xAx je pozitivně definitní. V indukčním kroku předpokládejme, že implikace platí pro n D j � 1 a ukažme, že pak platí i pro n D j (kde j > 1 je libovolně ale pevně zvolené přirozené číslo). Nechť tedy A 2 R<sup>j �j</sup> je symetrická matrice taková, že Mk > 0 pro každé k D 1; 2; : : : ; j a A<sup>0</sup> 2 R<sup>.j�1/�.j�1/</sup> je matice, která vznikne z matice A vynecháním posledního řádku a posledního sloupce. Pak podle indukčního předpokladu je pozitivně definitní kvadratická forma yAE<sup>0</sup> yE<sup>T</sup> . Pro spor předpokládejme, že kvadratická forma xAE xE<sup>T</sup> není pozitivně definitní. To znamená, že matice A musí mít vlastní číslo �1 � 0 (viz důsledek 10.15b)). Kdyby bylo nulové, pak by muselo být Mj D det.A/ D �1�2 ��� �j D 0, což je spor s Mj > 0. Musí tedy být �1 < 0. Pokud všechna ostatní vlastní čísla �2; �3; : : : ; �j jsou kladná, tak Mj D �1�2 ��� �j < 0, což je opět spor s předpokladem. Matice A tedy musí mít alespoň dvě vlastní čísla �1; �2 < 0. K této dvojici vlastních čísel existují dva ortogonální vektory u;E Ev 2 R<sup>j</sup> (viz důsledek 10.14). Uvažujme nyní lineární kombinaci wE D ˛uE C ˇvE a konstanty ˛; ˇ 2 R zvolme tak, aby wE byl nenulový 

10 Lokální a globální extrémy 

43 

a jeho poslední složka byla nulová (˛; ˇ nemohou být současně nulové, jinak by wE nebyl nulový). Protože AuE<sup>T</sup> D �1 Eu<sup>T</sup> a AvE<sup>T</sup> D �2vE<sup>T</sup> , platí 



<!-- Start of picture text -->
wAE w E T D .˛uE C ˇv/A.˛E uE C ˇv/E T D .˛uE C ˇv/.˛AE uE T C ˇAvE T /<br>D .˛uE C ˇv/.˛�E 1 Eu T C ˇ�2vE T / D ˛ 2 �1 EuuE T C ˛ˇ�2 EuvE T C ˛ˇ�1vEuE T C ˇ 2 �2vEvE T<br>D ˛ 2 �1 EuuE T C ˇ 2 �2vEvE T ;<br><!-- End of picture text -->

přičemž poslední rovnost plyne z ortogonality vektorů uE a vE. Skalární součiny uEuE<sup>T</sup> , vEvE<sup>T</sup> jsou kladné (oba vektory jsou nenulové) a �1; �2 < 0, máme tedy wAE Ew<sup>T</sup> < 0. Protože poslední složka vektoru wE je nulová, musí také být EzA<sup>0</sup> zE<sup>T</sup> < 0, kde Ez D .w1; w2; : : : ; wj �1/ 2 R<sup>j�1</sup> . To je ale spor s indukčním předpokladem, tj. s pozitivní definitností formy yAE<sup>0</sup> yE<sup>T</sup> . Matice A tedy musí mít všechna vlastní čísla kladná, což podle Důsledku 10.15 znamená, že kvadratická forma xAE xE<sup>T</sup> je pozitivně definitní. Princip matematické indukce dává platnost tvrzení pro každou formu se symetrickou maticí A 2 R<sup>n�n</sup> . 

(ii) Tato větev plyne z (i) uvážíme-li, že když je forma xAE xE<sup>T</sup> pozitivně definitní, pak forma �ExAxE<sup>T</sup> D x.E �A/xE<sup>T</sup> je negativně definitní (a naopak) a platí det.�Ak/ D .�1/<sup>k</sup> det.Ak/. 

(iii) Postup je obdobný jako v případě větve (i). „H)“ Nechť kvadratická forma xAE xE<sup>T</sup> se symetrickou maticí A 2 R<sup>n�n</sup> je pozitivně semidefinitní. Označme symbolem A<sup>`</sup> k<sup>submatice matice A, které vzniknou</sup> tak, že v matici A vynecháme n � k odpovídajících si řádků a sloupců. Vezměme libovolný nenulový vektor yEk 2 R<sup>k</sup> a sestrojme nový vektor xEk 2 R<sup>n</sup> tak, že yEk doplníme n � k nulami, které budou na pozicích odpovídajících vynechaným řádkům (sloupcům). Potom xEk je také nenulový a pro každé k D 1; 2; : : : ; n a každé ` D 1; 2; : : : �kn� platí yAE<sup>`</sup> k<sup>yETDxEkAxE</sup> k<sup>T�0, tj. formayAE`</sup> k<sup>yETje pozitivně semidefinitní. Podle</sup> důsledku 10.15b) zároveň platí Mk<sup>`D det.A`</sup> k<sup>/ �0.</sup> 

„(H“ Pro n D 1 tvrzení opět platí triviálně, neboť v případě A D a 2 R předpoklad M1<sup>1D</sup> det.A/ D a � 0 implikuje xAx D ax<sup>2</sup> � 0 pro libovolné x ¤ 0, tj. forma xAx je pozitivně semidefinitní. V indukčním kroku dokazujeme implikaci „j �1 ) j “. Nechť tedy A 2 R<sup>j �j</sup> je symetrická matice taková, že Mk<sup>`�0 pro každé kD 1; 2; : : : ; ja každé ` D 1; 2; : : : ;</sup> �kj �, a forma yAE i Ey<sup>T</sup> je pozitivně semidefinitní pro každou matici Ai 2 R<sup>.j�1/�.j�1/</sup> (i D 1; 2; : : : ; j ), která vznikne z matice A vynecháním i-tého řádku a i -tého sloupce (indukční předpoklad). Ukažme, že forma xAE xE<sup>T</sup> je pozitivně semidefinitní. Pro spor předpokládejme, že tomu tak není. Podle důsledku 10.15a) to znamená, že A má vlastní číslo �1 < 0. Pokud jsou všechna další vlastní čísla této matice kladná, pak bychom měli Mj<sup>1D det.A/ < 0, což je spor. Musí</sup> tedy existovat další vlastní číslo �2 � 0. Ke dvojici �1; �2 existuje dvojice ortogonálních vlastních vektorů u;E Ev 2 R<sup>j</sup> . Zvolme číslo ˇ 2 R tak, aby vektor wE D uE C ˇvE 2 R<sup>j</sup> měl alespoň jednu složku nulovou, nechť je to i -tá složka (i 2 f1; 2; : : : ; j g). Podobně jako ve větvi (i) máme wAE w E<sup>T</sup> D �1 EuuE<sup>T</sup> C ˇ<sup>2</sup> �2vEvE<sup>T</sup> . Protože �1 < 0 a �2 � 0, musí být wAE w E<sup>T</sup> < 0. Nechť nyní Ez 2 R<sup>j �1</sup> je vektor, který vznikne z vektoru wE vynecháním i-té (nulové) složky. Pak zAE i Ez<sup>T</sup> D wAE Ew < 0. To ale znamená, že forma s maticí Ai nemůže být pozitivně semidefinitní, což je spor s indukčním předpokladem. Matice A tedy musí mít všechna vlastní čísla nezáporná, tj. forma xAE xE<sup>T</sup> je pozitivně semidefinitní. Podle principu matematické indukce implikace „(H“ platí pro každou formu se symetrickou maticí A 2 R<sup>n�n</sup> . 

(iv) Tato větev opět plyne okamžitě z předchozí díky analogické vlastnosti jako ve větvi (ii) (forma �ExAxE<sup>T</sup> je negativně semidefinitní, právě když forma xAE xE<sup>T</sup> je pozitivně semidefinitní). 

Konečně, pokud minory Mk<sup>`nevyhovují ani jedné z větví (i)–(iv), tak je formaxAExETindefinitní. To</sup> je důsledkem faktu, že podmínky v jednotlivých větvích jsou formulovány jako ekvivalence. 

Poznámka 10.16. Důkaz větve (iii) naznačuje, proč k pozitivní semidefinitnosti formy nestačí mít nezáporné pouze základní hlavní minory (viz příklad 10.18c) níže). Kdybychom vektor wE zkonstruovali stejně jako ve větvi (i), tj. pomocí lineární kombinace wE D ˛uE C ˇvE, pak bychom museli požadovat ˛ ¤ 0, protože pouze vlastní číslo �1 je záporné (při nulovém ˛ by funkční hodnota wAE Ew<sup>T</sup> byla pouze nezáporná, a tudíž bychom v následujícím kroku nedostali spor). Tomu se tak skutečně děje, ve větvi (iii) klademe totiž ˛ D 1 v konstrukci vektoru wE . Problém ale je, že takto nemusíme být schopni pomocí druhé konstanty ˇ získat poslední složku nulovou (stačí, aby vektor uE měl poslední složku nenulovou, zatímco vektor vE ji měl nulovou). Přesněji řečeno, nulovou složku ve vektoru wE získat lineární kombinací uE C ˇvE vždy lze, ale nemusí se to podařit na poslední pozici. 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

44 

- D˚usledek 10.17. a) _Je-li alespoň jeden hlavní minor_ Mk<sup>`</sup><sup>_záporný pro_k</sup><sup>_sudé, pak_xAExET</sup><sup>_je indefinitní._</sup> 

- b) _Jsou-li všechny základní hlavní minory_ Mk _nenulové a nenastává ani jeden z případů_ (i) _,_ (ii) _předchozího tvrzení, pak_ xAE xE<sup>T</sup> _je indefinitní._ 

- c) _Je-li forma_ xAE xE<sup>T</sup> _pozitivně (resp. negativně) definitní, pak_ aii > 0 _(resp._ sgn.aii / D .�1/<sup>i</sup> / _pro každé_ i D 1; 2; : : : ; n _. Podobně, je-li_ xAE xE<sup>T</sup> _pozitivně (resp. negativně) semidefinitní, pak_ aii � 0 _(resp._ sgn.aii / D .�1/<sup>i</sup> _nebo_ aii D 0 _) pro každé_ i D 1; 2; : : : ; n _. Je-li tedy diagonální prvek_ aii _matice_ A _záporný pro_ i _sudé, tak forma_ xAE xE<sup>T</sup> _je indefinitní._ 

Pˇríklad 10.18. Rozhodněte o typu kvadratických forem: 

a) K.x; y; z/ D 3x<sup>2</sup> C 3y<sup>2</sup> C 6z<sup>2</sup> C 2xy C 4xz � 2yz; 

b) K.x; y; z/ D 16yz � 2z<sup>2</sup> ; c) K.x1; x2; x3; x4/ D x1<sup>2C x</sup> 2<sup>2C x</sup> 3<sup>2C x</sup> 4<sup>2C 2x1x2 C 2x1x3 C 4x1x4 C 2x2x3 C 2x2x4 C 2x3x4.</sup> 

_Řešení._ a) Kvadratická forma je reprezentována symetrickou maticí 



<!-- Start of picture text -->
A D 0 31 13 �21 1<br>2 �1 6<br>@ A :<br><!-- End of picture text -->

Protože D1 D 3, D2 D 8, D3 D 29, podle větve (i) Sylvestrova kritéria je kvadratická forma pozitivně definitní. 

b) V tomto případě kvadratické formě odpovídá matice 



<!-- Start of picture text -->
A D 0 00 00 08 1<br>0 8 �2<br>@ A ;<br><!-- End of picture text -->

přičemž M1<sup>1D0, M</sup> 1<sup>2D0, M</sup> 1<sup>3D�2, M 1</sup> 2<sup>D0, M</sup> 2<sup>2D0, M</sup> 2<sup>3D�16, M</sup> 3<sup>1D0. Podle Sylvestrova</sup> kritéria (resp. důsledku 10.17) je forma indefinitní. Lze rozhodnout i snadněji, například K.1; 1; 1/ D 14 > 0, ale K.1; 1; �1/ D �18 < 0, tj. forma mění znaménko, což znamená indefinitnost. 

c) Matice formy má nyní tvar 



<!-- Start of picture text -->
011 11 11 211<br>A D<br>1 1 1 1<br>2 1 1 1<br>BB@ CCA ;<br><!-- End of picture text -->

jejíž základní hlavní minory jsou M1 D 1, M2 D 0, M3 D 0, M4 D 0. Protože některé jsou nulové, nestačí to k určení definitnosti formy a je potřeba počítat ostatní hlavní minory. Máme M1<sup>1DM</sup> 1<sup>2D</sup> M1<sup>3DM</sup> 1<sup>4D1,M 1</sup> 2<sup>DM</sup> 2<sup>2DM</sup> 2<sup>3DM 4</sup> 2<sup>DM</sup> 2<sup>5D0,M</sup> 2<sup>6D�1. Nyní již pokračovat nemusíme,</sup> vidíme totiž, že jeden minor sudého řádu je nulový, a tedy podle důsledku 10.17 je kvadratická forma indefinitní. Toto opět můžeme vidět také vhodným dosazením za proměnné, např. K.1; 0; 0; 1/ > 0, zatímco K.1; 0; 0; �1/ < 0. 

Druhý totální diferenciál d<sup>2</sup> f .X/ je kvadratická forma reprezentovaná Hessovou<sup>8</sup> maticí druhých parciálních derivací 



<!-- Start of picture text -->
fx 00 1x1 fx 00 1x2 : : : fx 00 1xn<br>0fx 00 2x1 fx 00 2x2 : : : fx 00 2xn 1<br>Hf .X/ D<br>::: ::: ::: :::<br>BBB@fx 00 nx1 fx 00 nx2 : : : fx 00 nxn CCCA .X/;<br><!-- End of picture text -->

tj. platí d<sup>2</sup> f .X/ D .h1; h2; : : : ; hn/Hf .X/.h1; h2; : : : ; hn/<sup>T</sup> . 

■ Vˇeta 10.19. _Nechť_ f W R<sup>n</sup> ! R _je funkce,_ S _její stacionární bod a nechť Hessova matice_ Hf _je spojitá na nějakém okolí bodu_ S _. Je-li_ d<sup>2</sup> f .S/ 

8Ludwig Otto Hesse 1811–1874, Němec 

10 Lokální a globální extrémy 

45 

(i) _pozitivně definitní, pak_ f _má v bodě_ S _ostré lokální minimum,_ 

(ii) _negativně definitní, pak_ f _má v bodě_ S _ostré lokální maximum,_ 

(iii) _indefinitní, pak_ f _nemá v bodě_ S _lokální extrém._ 

_Důkaz._ Z předpokladu spojitosti Hessovy matice na nějakém okolí O.S/ bodu S plyne podle vět 8.3 a 8.6 spojitost parciálních derivací prvního řádu a funkce samotné na tomto okolí. Podle Taylorovy věty pak pro X 2 O.S/ máme 



<!-- Start of picture text -->
f .X/ D f .S/ C df .S I X � S/ C 1 2 d2f .S C #.X � S/I X � S/; # 2 .0; 1/:<br><!-- End of picture text -->

Protože S je stacionární bod, platí df .S/ D 0, a tedy 



<!-- Start of picture text -->
f .X/ � f .S/ D 1 2 d2f .S C #.X � S/I X � S/; # 2 .0; 1/: (�)<br><!-- End of picture text -->

(i) Je-li d<sup>2</sup> f .S/ pozitivně definitní (tj. hH<sup>E</sup> f .S/h<sup>ET</sup> > 0 pro libovolný nenulový vektor h<sup>E</sup> 2 R<sup>n</sup> ), pak (z důvodu spojitosti Hessovy matice Hf ) existuje okolí O1.S/ takové, že 



<!-- Start of picture text -->
hHE f .X/hE T > 0 pro každý bod X 2 O1.S/:<br><!-- End of picture text -->

Uvažujeme-li eukleidovskou metriku, tak do tohoto okolí náleží i bod S C #.X � S/, protože # 2 .0; 1/. Vlastnost platí pro libovolný nenulový vektor h<sup>E</sup> , můžeme jej tedy volit jako h<sup>E</sup> D X � S , X ¤ S . Platí tedy 



<!-- Start of picture text -->
d 2 f .S C #.X � S/I X � S/ D hH E f .S C #h/ E h ET > 0<br><!-- End of picture text -->

pro každý bod X 2 O1<sup>�.S/. To spolu s (�) znamená, že f .X/ �f .S/>0 pro každé X2O</sup> 1<sup>�.S/, tj.</sup> v bodě S nastává ostré lokální minimum. 

(ii) Důkaz se provede analogicky jako v první větvi. 

(iii) Nechť d<sup>2</sup> f .S/ je indefinitní, tj. existují (nenulové) vektory h;<sup>E</sup> k<sup>E</sup> 2 R<sup>n</sup> takové, že 



<!-- Start of picture text -->
a<br>hHE f .S/hE T > 0 kHE f .S/kE T < 0:<br><!-- End of picture text -->

Tyto dvě nerovnosti platí i v libovolném bodě X vhodného okolí O1.S/ � O.S/ z důvodu spojitosti Hessovy matice na O.S/. Nechť nyní O2.S/ je libovolné okolí bodu S a zvolme čísla th; tk > 0 tak, aby body X1 D S C thh<sup>E</sup> a X2 D S C tkk<sup>E</sup> náležely průniku O1.S/ \ O2.S/. Potom h<sup>E</sup> D .X1 � S/=th, kE D .X2 � S/=tk a podle (�) existují čísla #1; #2 2 .0; 1/ taková, že 



<!-- Start of picture text -->
f .X1/ � f .S/ D 1 d 2 f .S C #1.X1 � S/I X1 � S/ D hH E f .S C #1thh/ E h ET > 0;<br>t 2<br>h<br>f .X2/ � f .S/ D 1 d 2 f .S C #2.X1 � S/I X1 � S/ D kH E f .S C #2tkk/ E k ET < 0:<br>t 2<br>k<br><!-- End of picture text -->

To znamená, že f .X1/ > f .S/ a zároveň f .X2/ < f .S/, a tedy v bodě S nemůže nastat lokální extrém protože okolí O2.S/ bylo voleno libovolně. 

Poznámka 10.20. Je-li d<sup>2</sup> f .S/ pozitivně nebo negativně semidefinitní, nelze o extrému rozhodnout. 

Pˇríklad 10.21. Vyšetřete lokální extrémy funkce f .x; y; z/ D 2xy<sup>2</sup> � 4xy C x<sup>2</sup> C z<sup>2</sup> � 2z. 

_Řešení._ Položíme-li gradient funkce roven nulovému vektoru, dostaneme soustavu tří rovnic 



<!-- Start of picture text -->
2y 2 � 4y C 2x D 0; 4xy � 4x D 0; 2z � 2 D 0;<br><!-- End of picture text -->

ze které obdržíme tři stacionární body S1 D Œ1; 1; 1�, S2 D Œ0; 0; 1� a S3 D Œ0; 2; 1�. Hessova matice zadané funkce má tvar 



<!-- Start of picture text -->
Hf .x; y; z/ D 04y �2 4 4y4x � 4 001<br>0 0 2<br>@ A<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

46 

a po dosazení stacionárních bodů máme 



<!-- Start of picture text -->
Hf .S1/ D 020 04 001 Hf .S2/ D 0�24 �04 001 Hf .S3/ D 024 40 001<br>0 0 2 0 0 2 0 0 2<br>@ A ; @ A ; @ A :<br><!-- End of picture text -->

Pomocí Sylvestrova kritéria snadno určíme, že d<sup>2</sup> f .S1/ je pozitivně definitní kvadratická forma (D1 D 2 > 0, D2 D 8 > 0, D3 D 16 > 0), d<sup>2</sup> f .S2/ je indefinitní kvadratická forma (D1 D 2 > 0, D2 D �16 < 0, D3 D �32 < 0) a d<sup>2</sup> f .S3/ je také indefinitní (D1 D 2 > 0, D2 D �16 < 0, D3 D �32 < 0). Lokální extrém tedy nastává pouze ve stacionárním bodě S1 (a to ostré lokální minimum). 

Pˇríklad 10.22. Vyšetřete lokální extrémy funkce f .x; y/ D x<sup>2</sup> .1 C y<sup>2</sup> /. 

_Řešení._ Podmínka grad f D oE vede na soustavu 

2x.1 C y<sup>2</sup> / D 0; 2x<sup>2</sup> y D 0; 

která má nekonečně mnoho řešení S D Œ0; y�, y 2 R (stacionárním bodem je tedy každý bod ležící na ose y). Hessova matice má potom tvar 



<!-- Start of picture text -->
4xy 0<br>Hf .x; y/ D �2.14xy C y2/ 2x 2 � ; vyčísleno v bodech S: Hf .x; y/ D �2.1 C0  y2/ 0� :<br><!-- End of picture text -->

Protože M1<sup>1D2.1 C y2/>0,M</sup> 1<sup>2D0,M</sup> 2<sup>1D0,d 2f .S/jepozitivněsemidefinitníkvadratickou</sup> formou a podle poznámky výše nelze na základě věty 10.19 o extrému rozhodnout. Uvážíme-li však, že f .S/ D 0 a f .x; y/ > 0 8Œx; y� 2 R<sup>2</sup> mimo osu y, je zřejmé, že f má v každém bodě S lokální minimum, které však není ostré (graf funkce je na obrázku). 



Obrázek 10.1: Graf funkce f .x; y/ D x<sup>2</sup> .1 C y<sup>2</sup> /. Každý bod osy y je bodem (neostrého) lokálního minima 

Definice 10.23. Buď f W R<sup>n</sup> ! R funkce a M � D.f /. Řekneme, že f nabývá na množině M v bodě X0 2 M _globálního minima_ (resp. _maxima_ ), jestliže f .X0/ � f .X/ (resp. f .X0/ � f .X/) pro 8X 2 M . Jsou-li nerovnosti ostré pro každé X ¤ X0, mluvíme o _ostrých globálních minimech_ (resp. _maximech_ ) na M . (Ostrá) globální maxima a minima nazýváme souhrnně _(ostré) globální extrémy funkce_ f na množině M . 

Poznámka 10.24. Je-li bod globálního extrému X0 na množině M vnitřním bodem této množiny, pak je X0 bodem lokálního extrému. Funkce f tedy může mít globální extrém na množině M v bodě lokálního extrému nebo v hraničním bodě množiny M , pokud tento bod do množiny M patří. Např. funkce f .x; y/ D x<sup>2</sup> C y<sup>2</sup> má na uzavřeném jednotkovém kruhu x<sup>2</sup> C y<sup>2</sup> � 1 (ostré) globální minimum 0 v bodě Œ0; 0� a (neostré) globální maximum 1 v každém bodě hranice kruhu (tj. kružnice x<sup>2</sup> C y<sup>2</sup> D 1). Kdybychom uvažovali otevřený kruh, tak funkce má stále (ostré) globální minimum 0 v bodě Œ0; 0�, ale globální maximum nemá (ostré ani neostré). 

Praktický postup při výpočtu globálních extrémů na kompaktní množině (tj. ohraničené a uzavřené) bude ukázán později v kapitole o vázaných extrémech. 

11 Implicitní funkce, diferencovatelná zobrazení mezi prostory vyšší dimenze 

47 

#### Pˇríklady k procviˇcení 

Vyšetřete body lokálních extrémů níže uvedených funkcí (ve výsledcích X<sup>min</sup> , resp. X<sup>max</sup> , značí bod lokálního minima, resp. maxima) a S stacionární bod, ve kterém nenastává extrém): 

10.1. 



<!-- Start of picture text -->
f .x; y/ D x.x � 1/ C y.y � 1/ � xy C 2:<br><!-- End of picture text -->

10.2. f .x; y/ D x<sup>4</sup> C y<sup>4</sup> C 4.x<sup>3</sup> � y<sup>3</sup> / C 5.x<sup>2</sup> C y<sup>2</sup> / C 4.x � y/ � 2xy C 2: 

10.3. 



<!-- Start of picture text -->
f .x; y/ D xy C x 8 C y 8 :<br><!-- End of picture text -->

10.4. 



<!-- Start of picture text -->
f .x; y; z/ D x C y2 x; y; z > 0:<br>4x C z y 2 C z 2 ;<br><!-- End of picture text -->

10.5. 



<!-- Start of picture text -->
f .x; y/ D y p 1 C x C x p 1 C y:<br><!-- End of picture text -->

10.6. 



<!-- Start of picture text -->
f .x; y/ D x 4 � 3x 2 y C 3y � y 3 :<br><!-- End of picture text -->

10.7. 



<!-- Start of picture text -->
f .x; y; z/ D x2 x; y; z > 0:<br>yz C y xz 2 C xy z2 ;<br><!-- End of picture text -->

_Výsledky._ 10.1. X<sup>min</sup> D Œ1; 1�. 10.2. X1<sup>min</sup> D Œ�2; 0�, X2<sup>min</sup> D Œ0; 2�, S D Œ�1; 1�. 10.3. X<sup>min</sup> D Œ2; 2�. 10.4. X<sup>min</sup> D Œ1=2; 1; 1�. 10.5. X<sup>min</sup> D Œ�2=3; �2=3�. 10.6. X<sup>min</sup> D Œ0; �1�, X<sup>max</sup> D Œ0; 1�, S3;4 D Œ˙ ~~p~~ 3=2; 1=2�. 10.7. X<sup>min</sup> D fŒx; y; z� 2 R<sup>3</sup> W x D t; y D t; z D t; t > 0g. 

### 11 Implicitní funkce, diferencovatelná zobrazení mezi prostory vyšší dimenze 

Definice 11.1 — implicitní funkce. Nechť F W R<sup>2</sup> ! R je funkce a Œx0; y0� 2 R<sup>2</sup> je takový bod, že F.x0; y0/ D 0. Řekneme, že _funkce_ y D f .x/ _je v okolí bodu_ Œx0; y0� _zadána implicitně rovnicí_ F.x; y/ D 0, jestliže existuje ı > 0 takové že, pro x 2 .x0 � ı; x0 C ı/ je F.x; f .x// D 0 a graf funkce f prochází bodem Œx0; y0� (tj. y0 D f .x0/). 

Pˇríklad 11.2. a) Rovnice 3x � y C 2 D 0 představuje implicitní vyjádření jediné funkce y D 3x C 2; b) rovnice x<sup>2</sup> C y<sup>2</sup> D 1 představuje dvojici funkcí y D ˙ ~~p~~ 1 � x<sup>2</sup> ; c) rovnice xy �jxyj D 0 určuje nekonečně mnoho funkcí y D f .x/ s grafem ležícím v prvním nebo třetím kvadrantu. 

■ Vˇeta 11.3 — o existenci implicitní funkce. _Nechť_ F W R<sup>2</sup> ! R _je spojitá funkce na otevřeném čtverci_ 



<!-- Start of picture text -->
R D .x0 � a; x0 C a/ � .y0 � a; y0 C a/<br><!-- End of picture text -->

_pro nějaké_ a > 0 _(tj. na okolí_ Oa.Œx0; y0�/ _v metrice_ �1 _) a nechť_ F.x0; y0/ D 0 _. Dále předpokládejme, že_ F _má na tomto čtverci parciální derivaci_ Fy<sup>0</sup><sup>_, která je spojitá v bodě_Œx0; y0�</sup><sup>_a platí_F</sup> y<sup>0.x0; y0/ ¤ 0</sup><sup>_._</sup> _Pak existuje_ ı > 0 _takové, že na intervalu_ .x0 � ı; x0 C ı/ _je rovnicí_ F.x; y/ D 0 _implicitně definována právě jedna spojitá funkce_ y D f .x/ _procházející bodem_ Œx0; y0� _._ 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

48 

_Důkaz._ Na R<sup>2</sup> uvažujme metriku �1 a položme d D Fy<sup>0.x0; y0/. Podle předpokladu je d¤ 0. Protože</sup> Fy<sup>0je spojitá v bodě Œx0; y0�a existuje na R, k jdj=2 existuje " > 0 takové, že pro Œx; y�2 O".x0; y0/ D</sup> .x0 � "; x0 C "/ � .y0 � "; y0 C "/ je jFy<sup>0.x; y/ �dj < jdj=2, tj. j1 �d �1F</sup> y<sup>0.x0; y0/j < 1=2. Označme</sup> 

Q D fg 2 C.hx0 � "; x0 C "i/ W g.x0/ D y0; jg.x/ � y0j < " 8x 2 hx0 � "; x0 C "ig: 

Pro g 2 Q tedy platí g.x0/ D y0, F.x0; g.x0// D F.x0; y0/ D 0. Protože g i F jsou spojité, k " > 0 existuje ı1 > 0 takové, že pro každé x 2 hx0 � ı1; x0 C ı1i platí 



<!-- Start of picture text -->
� y0<br>ˇˇˇˇg.x/ � F .x; dg.x// ˇˇˇˇ < ":<br><!-- End of picture text -->

Položme ı D minf"; ı1g a P D Q \ C.hx0 � ı; x0 C ıi/. Množina P tedy obsahuje funkce z Q, jejichž definiční obor je zúžen na hx0 � ı; x0 C ıi. Definujme zobrazení T W P ! C.hx0 � ı; x0 C ıi/ předpisem 



<!-- Start of picture text -->
T .g/.x/ D g.x/ � F .x; g.x// : (�)<br>d<br><!-- End of picture text -->

Je-li funkce f pevným bodem zobrazení T , pak f .x/ D f .x/�d<sup>�1</sup> F.x; f .x// pro x 2 hx0 � ı; x0 C ıi, tj. F.x; f .x// D 0 pro x 2 hx0 � ı; x0 C ıi, tj. f je spojitá funkce, která je na .x0 � ı; x0 C ı/ implicitně zadána rovnicí F.x; y/ D 0. Existenci jediné funkce f této vlastnosti dokážeme pomocí Banachovy věty o pevném bodu. Na P uvažujme metriku stejnoměrné konvergence �C . Pak T .g/.x0/ D g.x0/ � d<sup>�1</sup> F.x0; g.x0// D y0 pro g 2 P a díky (�) také jT .g/.x/ � y0j < " pro x 2 hx0 � ı; x0 C ıi, tj. T .g/ 2 P . S využitím věty o střední hodnotě dostaneme 



<!-- Start of picture text -->
�C .T .g/; T .h// D x2hx0max�ı;x0Cıi jT .g/.x/ � T .h/.x/j<br>D max � h.x/ C F .x; h.x//<br>x2hx0�ı;x0Cıi ˇˇˇˇg.x/ � F .x; dg.x// d ˇˇˇˇ<br>D max Fy 0 .x; �/.g.x/ � h.x//<br>x2hx0�ı;x0Cıi ˇˇˇˇˇg.x/ � h.x/ � d ˇˇˇˇˇ<br>D max Fy 0 .x; �/<br>x2hx0�ı;x0Cıi jg.x/ � h.x/j ˇˇˇˇˇ1 � d ˇˇˇˇˇ ;<br><!-- End of picture text -->

kde bod � leží mezi hodnotami g.x/ a h.x/, g; h 2 P , tedy � 2 O".x0; y0/. Podle (�) tedy je 



<!-- Start of picture text -->
�C .T .g/; T .h// � 1 max<br>2 x2hx0�ı;x0Cıi jg.x/ � h.x/j D 2 1 �C .g; h/;<br><!-- End of picture text -->

což znamená, že T je kontrakce na P . 

Poznámka 11.4. a) Vedle spojité funkce může existovat i další nespojitá funkce, např. rovnice y.y �1/ D 0 určuje na okolí bodu Œ0; 0� spojitou funkci y.x/ D 0, ale kromě ní také např. nespojitou funkci 



<!-- Start of picture text -->
0 pro x � 0<br>y1.x/ D nebo funkci y2.x/ D �.x/:<br>(1 pro x > 0<br><!-- End of picture text -->

b) Podmínka Fy<sup>0.x0; y0/¤0jepostačujícíproexistenciimplicitnífunkce,nikolivnutnou,např.</sup> rovnice x � y<sup>3</sup> D 0 určuje v okolí bodu Œ0; 0� funkci y D<sup>~~p~~</sup> 3 x, ale přitom Fy<sup>0.0; 0/ D 0.</sup> 

■ Vˇeta 11.5 — o derivaci implicitní funkce. _Nechť jsou splněny předpoklady věty 11.3 a_ F _má na čtverci_ R _spojité parciální derivace. Pak má funkce_ y D f .x/ _, která je implicitně určena v okolí bodu_ Œx0; y0� _rovnicí_ F.x; y/ D 0 _, derivaci v bodě_ x0 _a platí_ 



<!-- Start of picture text -->
f 0 .x0/ D � F x  0 .x0; y0/<br>Fy 0 .x0; y0/ :<br><!-- End of picture text -->

11 Implicitní funkce, diferencovatelná zobrazení mezi prostory vyšší dimenze 

49 

_Důkaz._ Podle věty 11.3 existuje číslo ı > 0 takové, že na .x0 � ı1; x0 C ı1/ existuje jediná spojitá funkce f daná implicitně rovnici F.x; y/ D 0 a splňující y0 D f .x0/. Z důkazu věty 11.3 také plyne, že Fy<sup>0.x; f .x//¤0prokaždéx2.x0�ı; x0Cı/.Vezměmelibovolnédvarůznébody</sup> x; x1 2 .x0 � ı; x0 C ı/. Pak platí F.x; f .x// D 0 a F.x1; f .x1/ D 0. Označme y1 D f .x1/. Protože F je diferencovatelná v bodě Œx1; y1� (existuje okolí bodu Œx1; y1�, na kterém jsou dle předpokladu spojité obě parciální derivace), platí 



<!-- Start of picture text -->
F.x; f .x// � F.x1; y1/<br>„ ƒ‚ … „ ƒ‚ …<br>D0 D0<br>D dF.x1; y1I x � x1; f .x/ � y1/ C q .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � y1/;<br><!-- End of picture text -->

kde �.h; k/ ! 0 pro Œh; k� ! Œ0; 0�. Úpravou dostaneme 



<!-- Start of picture text -->
0 D dF.x1; y1I x � x1; f .x/ � y1/ C q .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � f .x1//<br>D dF.x1; y1I x � x1; f .x/ � y1/<br><!-- End of picture text -->



<!-- Start of picture text -->
p .x � x1/ 2 C .f .x/ � y1/ 2<br>C q .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � y1/<br>p .x � x1/ 2 C .f .x/ � y1/ 2<br>.x � x1/ 2<br>D dF.x1; y1I x � x1; f .x/ � y1/ C p .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � y1/<br>.f .x/ � y1/ 2<br>C p .x � x1/ 2 C .f .x/ � f .x1// 2 �.x � x1; f .x/ � y1/:<br><!-- End of picture text -->

Uvážíme-li, že dF.x1; y1I x � x1; f .x/ � y1/ D Fx<sup>0.x1; y1/.x �x1/ C F</sup> y<sup>0.x1; y1/.f .x/ �y1/, pak po</sup> vydělení rozdílem x � x1 dostaneme 



<!-- Start of picture text -->
0 D Fx 0 .x1; y1/ C F y  0 .x1; y1/ f .x/ � y1 C x � x1<br>x � x1 p .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � y1/<br>C f .x/ � y1 � f .x/ � y1<br>x � x1 p .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � y1/<br>f .x/ � y1<br>D Fx 0 .x1; y1/ C F y  0 .x1; y1/ f .x/ � y1 1 C<br>x � x1 p .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � y1/ !<br>x � x1<br>C p .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � y1/:<br><!-- End of picture text -->

Funkce f je spojitá v bodě x1 (tj. platí limx!x1 f .x/ D f .x1/ D y1), a tedy �.x � x1; f .x/ � y1/ ! 0 pro x ! x1. Oba členy obsahující odmocninu ve jmenovateli jsou v absolutní hodnotě ohraničené jedničkou, a proto také 



<!-- Start of picture text -->
x � x1<br>lim<br>x!x1<br>p .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � y1/ D 0;<br>f .x/ � y1<br>lim<br>x!x1<br>p .x � x1/ 2 C .f .x/ � y1/ 2 �.x � x1; f .x/ � y1/ D 0:<br><!-- End of picture text -->

Limitním přechodem pro x ! x1 tedy celkově dostáváme 



<!-- Start of picture text -->
f .x/ � f .x1/ x .x1; y1/<br>0 D Fx 0 .x1; y1/ C F y  0 .x1; y1/ x lim !x1 x � x1 ; neboli f 0 .x1/ D � F Fy  00 .x1; y1/ :<br><!-- End of picture text -->

Protože bod x1 byl v intervalu .x0 � ı; x0 C ı/ volen libovolně, můžeme za něj volit bod x0. Dokázali jsme tedy, že derivace f<sup>0</sup> .x0/ existuje a je dána vzorcem věty. 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

50 

Poznámka 11.6. a) Samotný vzorec pro výpočet derivace si není potřeba pamatovat, lze jej snadno formálně odvodit z pravidla pro derivování složené funkce: 



<!-- Start of picture text -->
x .x; f .x//<br>F.x; f .x// D 0 = 0 x ) F x  0 .x; f .x// � 1 C F y  0 .x; f .x//f 0.x/ D 0 ) f 0.x/ D � F 0<br>Fy 0 .x; f .x// :<br><!-- End of picture text -->

Dosadíme-li x D x0, tak s využitím y0 D f .x0/ dostaneme vzorec tvrzení. 

b) Z důkazu je zřejmé, že derivace existuje nejenom v bodě Œx0; y0�, ale na celém .x0 � ı; x0 C ı/ a je zde spojitá. 

Pˇríklad 11.7. Určete rovnici tečny a normály ke křivce dané rovnicí x<sup>3</sup> C y<sup>3</sup> � 2xy D 0 v bodě Œ1; 1�. 

_Řešení._ Funkce F.x; y/ D x<sup>3</sup> C y<sup>3</sup> � 2xy je má parciální derivace Fx<sup>0.x; y/ D 3x2 �2y, F</sup> y<sup>0.x; y/ D</sup> 3y<sup>2</sup> � 2x, které jsou spojité na libovolném (čtvercovém) okolí bodu Œ1; 1� (sama funkce F tedy musí být také spojitá v každém bodě uvažovaného okolí, protože je zde diferencovatelná). Protože navíc Fy<sup>0.1; 1/D1¤0,jsousplněnyvšechnypředpokladyvěty11.3,atedyvokolíboduŒ1; 1�existuje</sup> implicitní funkce y D f .x/, která má v bodě x0 D 1 derivaci, přičemž 



<!-- Start of picture text -->
f 0 .1/ D � 3 � 12 � 2 � 1<br>3 � 1 2 � 2 � 1 D �1:<br><!-- End of picture text -->

Rovnice tečny funkce f v bodě x0 je dána vzorcem y D y0 C f<sup>0</sup> .x0/.x � x0/, viz Matematická analýza I. Po dosazení tedy dostáváme y D 1 � .x � 1/, tj. hledaná tečna má rovnici x C y � 2 D 0. Normála je potom kolmá na tečnu, snadno napíšeme její parametrické vyjádření x D 1 C t, y D 1 C t, t 2 R. Eliminací parametru t pak dostaneme rovnici normály x � y D 0. 

Poznámka 11.8. a) Z příkladu je zřejmé, že rovnice tečny v bodě Œx0; y0� ke grafu funkce y D f .x/ určené implicitně rovnicí F.x; y/ D 0 má tvar Fx<sup>0.x0; y0/.x �x0/ C F</sup> y<sup>0.x0; y0/.y �y0/ D 0.</sup> 

b) Jsou-li splněny předpoklady věty 11.3 a F má navíc na R spojité druhé parciální derivace, pak funkce y D f .x/, která je v okolí bodu Œx0; y0� dána implicitně rovnicí F.x; y/ D 0 má v bodě x0 druhou derivaci a platí 



<!-- Start of picture text -->
y 00 .x0/<br>Fxx 00 .x0; y0/.F y  0 .x0; y0//2 � 2F x  00 y .x0; y0/F x  0 .x0; y0/F y  0 .x0; y0/ C F yy  00 .x0; y0/.F x  0 .x0; y0//2<br>D � .Fy 0 .x0; y0// 3 :<br><!-- End of picture text -->

Jak je to ve vyšší dimenzi? 

Definice 11.9 — implicitní funkce dvou promˇenných. Nechť F W R<sup>3</sup> ! R je funkce, Œx0; y0; z0� 2 R<sup>3</sup> je takový bod, že F.x0; y0; z0/ D 0. Řekneme, že _funkce_ z D f .x; y/ _je v okolí bodu_ Œx0; y0; z0� _zadána implicitně rovnicí_ F.x; y; z/ D 0, jestliže existuje ı > 0 takové že pro Œx; y� 2 .x0 � ı; x0 C ı/ � .y0 � ı; y0 C ı/ je F.x; y; f .x; y// D 0 a graf funkce f prochází bodem Œx0; y0; z0�. 

■ Vˇeta 11.10 — o implicitní funkci dvou promˇenných a jejích parciálních derivacích. _Nechť_ F W R<sup>3</sup> ! R _je funkce spojitá na krychli_ K D .x0 � a; x0 C a/ � .y0 � a; y0 C a/ � .z0 � a; z0 C a/ _pro nějaké_ a > 0 _,_ F.x0; y0; z0/ D 0 _a má zde derivaci_ Fz<sup>0</sup><sup>_,kterájespojitávbodě_Œx0; y0; z0�</sup><sup>_,_</sup> _přičemž_ Fz<sup>0.x0; y0; z0/¤0</sup><sup>_. Pak existuje číslo_ı>0</sup><sup>_a jediná spojitá funkce_zDf .x; y/</sup><sup>_, která je na_</sup> .x0 � ı; x0 C ı/ � .y0 � ı; y0 C ı/ _dána implicitně rovnicí_ F.x; y; z/ D 0 _. Jsou-li navíc na krychli_ K _spojité parciální derivace_ Fx<sup>0</sup><sup>_,_F</sup> y<sup>0</sup><sup>_a_F</sup> z<sup>0</sup><sup>_, pak funkce_zD f .x; y/</sup><sup>_má parciální derivace v bodě_Œx0; y0�</sup> _a platí_ 



<!-- Start of picture text -->
x .x0; y0; z0/ Fy 0 .x0; y0; z0/<br>fx 0 .x0; y0/ D � F 0 fy 0.x0; y0/ D �<br>Fz 0 .x0; y0; z0/ ; Fz 0 .x0; y0; z0/ :<br><!-- End of picture text -->

Poznámka 11.11. Z předchozí definice a věty je již zřejmé, jak by vypadalo rozšíření na případ implicitní funkce tří a více proměnných. 

11 Implicitní funkce, diferencovatelná zobrazení mezi prostory vyšší dimenze 

51 



<!-- Start of picture text -->
Definice 11.12 — m -funkce. Nechť f1; f2; : : : ; fm jsou funkce n proměnných takové, že D.f1/ \<br>D.f2/ \ ���\ D.fm/ ¤ ;. Pak zobrazení  F W R n ! R m dané předpisem<br>F<br>Œx1; x2; : : : ; xn� 7�! Œf1.x1; x2 : : : ; xn/; f2.x1; x2 : : : ; xn/; : : : ; fm.x1; x2 : : : ; xn/�<br><!-- End of picture text -->

nazveme m _-funkcí_ n _proměnných_ . Funkce f1; f2; : : : ; fm nazýváme _složky F_ , množina 



<!-- Start of picture text -->
m<br>D. F / WD \ D.fi /<br>i D1<br><!-- End of picture text -->

se nazývá _definiční obor_ m-funkce _F_ . 

Poznámka 11.13. a) Interpretujeme-li obraz bodu X 2 R<sup>n</sup> jako vektor v R<sup>m</sup> , pak m-funkci nazýváme také _vektorovou funkcí_ a je-li m D n, tak _vektorovým polem_ . 

b) _Spojitostí_ m-funkce v bodě X0 2 D. _F_ / � R<sup>n</sup> rozumíme spojitost každé složky fi , i D 1; 2; : : : ; m, v bodě X0. To je v souladu z definicí spojitosti zobrazení mezi metrickými prostory, pokud m-funkci _F_ chápeme jako zobrazení množiny D. _F_ / do R<sup>m</sup> (není podstatné jakou z metrik �1; �2, �1 na D. _F_ / a R<sup>m</sup> použijeme), což skutečně vede na spojitost jednotlivých složek (viz analogická argumentace jako v prvním bodě příkladu 3.10). 

Definice 11.14 — diferencovatelnosti **m** -funkce. Řekneme, že m-funkce _F_ W R<sup>n</sup> ! R<sup>m</sup> je diferencovatelná v bodě X0 2 R<sup>n</sup> , jestliže každá z funkcí f1; f2; : : : ; fm je diferencovatelná v tomto bodě. Zobrazení d _F_ .X0/ W R<sup>n</sup> ! R<sup>m</sup> dané předpisem 



<!-- Start of picture text -->
Œh1; h2; : : : ; hn� 7�! Œdf1.X0/; df2.X0/; : : : ; dfm.X0/�<br><!-- End of picture text -->

se nazývá _totální diferenciál_ m _-funkce F v bodě_ X0 a m-funkce _F_ se nazývá _diferencovatelná na_ množině M � D. _F_ /, je-li diferencovatelná v každém bodě z M . 

Poznámka 11.15. Totální diferenciál d _F_ .X0/ je lineární zobrazení z R<sup>n</sup> do R<sup>m</sup> určené maticí 



<!-- Start of picture text -->
@f1 @f1 @f1<br>@x1 @x2 : : : @xn<br>0 1<br>@f2 @f2 @f2<br>F 0 .X0/ D @x1 @x2 : : : @xn .X0/;<br>::: ::: ::: :::<br>@fm @fm @fm<br>: : :<br>BBBBBB@ @x1 @x2 @xn CCCCCCA<br><!-- End of picture text -->

tj. platí 



<!-- Start of picture text -->
0 ddff12.X.X00// 1 0hh121<br>::: :::<br>BBB@dfm.X0/CCCA D  F  0.X0/ BBB@hnCCCA :<br><!-- End of picture text -->

Matice _F_<sup>0</sup> .X0/ se nazývá _Jacobiova_<sup>9</sup> _matice_ m _-funkce F v bodě_ X0. Je-li n D m, pak se determinant Jacobiovy matice m-funkce _F_ v bodě X0 nazývá _Jacobián_ , budeme značit J _F_ .X0/ nebo stručně J.X0/. 

■ Vˇeta 11.16 — o Jacobiovˇe matici složeného zobrazení. _Nechť G_ W R<sup>n</sup> ! R<sup>m</sup> _je_ m _-funkce diferencovatelná v bodě_ X0 2 R<sup>n</sup> _a F_ W R<sup>m</sup> ! R<sup>p</sup> _je_ p _-funkce diferencovatelná v bodě_ Y0 D _G_ .X0/ 2 R<sup>m</sup> _. Pak složené zobrazení H_ D _F_ ı _G_ W R<sup>n</sup> ! R<sup>p</sup> _je_ p _-funkce diferencovatelná v bodě_ X0 _a pro její Jacobiovu matici platí_ 



<!-- Start of picture text -->
H 0 .X0/ D  F 0 .Y0/ G 0 .X0/ :<br>„ ƒ‚ … „ ƒ‚ … „ ƒ‚ …<br>p�n p�m m�n<br><!-- End of picture text -->

9Carl Gustav Jacob Jacobi 1804–1851, Němec 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

52 

_Důkaz._ Podle definice p-funkce _H_ máme 



<!-- Start of picture text -->
hi .x1; x2; : : : ; xn/ D fi .g1.x1; x2; : : : ; xn/; g2.x1; x2; : : : ; xn/; : : : ; gm.x1; x2; : : : ; xn//<br><!-- End of picture text -->

a podle věty 9.1 platí 



<!-- Start of picture text -->
@hi<br>.x1; x2; : : : ; xn/<br>@xj<br>p @fi<br>D<br>X �g1.x1; x2; : : : ; xn/; g2.x1; x2; : : : ; xn/; : : : ; gm.x1; x2; : : : ; xn/� @gk .x1; x2; : : : ; xn/<br>kD1 @gk @xj<br><!-- End of picture text -->



<!-- Start of picture text -->
pro i D 1; 2; : : : ; p, j D 1; 2; : : : ; n.<br><!-- End of picture text -->

Zabývejme se nyní otázkou, za jakých podmínek existuje k dané n-funkci inverzní n-funkce. V případě n D 1 (tj. funkce jedné proměnné) byla situace poměrně jednoduchá, existence inverzní funkce k funkci f na intervalu I je zaručena striktní monotonií f , a ta je zase zaručena, je-li f<sup>0</sup> na I nenulová. Pokud máme zaručenu nenulovost derivace pouze v jednom bodě x0, tak tvrzení bude stále platit lokálně (na okolí tohoto bodu), ale potřebujeme k tomu spojitost derivace v bodě x0. Intuitivně, pokud _F_ .X0/ D Y0, tak podle Taylorovy věty na okolí bodu X0 platí 



<!-- Start of picture text -->
F .X/ � Y0 C d F .X0I X � X0/:<br><!-- End of picture text -->

Lineární zobrazení na pravé straně přibližné rovnosti je prosté, právě když je Jacobiova matice _F_<sup>0</sup> .X0/ regulární. Lze se domnívat, že prostá bude na daném okolí i samotná n-funkce _F_ . Následující věta říká, že tato domněnka je oprávněná. 

■ Vˇeta 11.17 — o lokální inverzi. _Nechť F_ W R<sup>n</sup> ! R<sup>n</sup> _je spojitě diferencovatelná_ n _-funkce na nějaké otevřené množině_ U � R<sup>n</sup> _obsahující bod_ X0 _a F_<sup>0</sup> .X0/ _je regulární (tj._ det. _F_<sup>0</sup> .X0// ¤ 0 _). Pak existují otevřené množiny_ V; W � R<sup>n</sup> _takové, že_ X0 2 V � U _,_ W D _F_ .V / _a F je na_ V _prostá. Existuje tedy inverzní_ n _-funkce F_<sup>�1</sup> W W ! V _. Tato inverze je navíc na_ W _spojitě diferencovatelná a v libovolném bodě_ Y D _F_ .X/ 2 W _pro její Jacobiovu matici platí_ 



<!-- Start of picture text -->
1<br>. F �1 / 0 .Y / D . F 0 .X// �1 ; a tedy J F  �1 .Y / D<br>J F  .X/ :<br><!-- End of picture text -->

K důkazu tvrzení budeme potřebovat několika poznatků z lineární algebry formulovaných v následujícím lemmatu. Je-li xE D .x1; x2; : : : ; xn/<sup>T</sup> 2 R<sup>n</sup> vektor, symbolem jExj označíme jeho eukleidovskou velikost, tj. 



<!-- Start of picture text -->
jExj D q x1 2 C x 2 2 C ���C x2n;<br><!-- End of picture text -->

a je-li A D .aij /<sup>n</sup> i;j D1<sup>2Rn�nčtvercová matice, symbolem kAkFoznačíme Frobeniovu normu této</sup> matice, tj. 



<!-- Start of picture text -->
v u n n<br>kAkF D uX X aij 2 :<br>tiD1 j D1<br><!-- End of picture text -->

■ Lemma 11.18. a) _Nechť_ A 2 R<sup>n�n</sup> _je čtvercová matice. Pak_ 



<!-- Start of picture text -->
jAxEj �kAkF jExj 8Ex 2 R n :<br><!-- End of picture text -->

b) _Pro libovolné dvě čtvercové matice_ A; B 2 R<sup>n�n</sup> _platí_ 



<!-- Start of picture text -->
kABkF �kAkF kBkF :<br><!-- End of picture text -->

- c) _Nechť_ A; B 2 R<sup>n�n</sup> _jsou čtvercové matice, přičemž_ A _je regulární (tj._ det.A/ ¤ 0 _a_ A _má inverzi). Jestliže_ 



<!-- Start of picture text -->
1<br>kA � BkF � ;<br>kA �1 kF<br><!-- End of picture text -->

_pak_ B _je také regulární._ 

11 Implicitní funkce, diferencovatelná zobrazení mezi prostory vyšší dimenze 

53 

_Důkaz._ a) Nerovnost je téměř okamžitým důsledkem Cauchyho–Schwarzovy nerovnosti. Skutečně, pro libovolný vektor xE 2 R<sup>n</sup> platí 



<!-- Start of picture text -->
n n n n n n<br>jAxEj 2 D X � X aij xj �2 � X�X n aij 2 X xj 2 � D �X n X aij 2 � X xj 2 D kAk F 2 jExj2;<br>iD1 j D1 i D1 j D1 j D1 i D1 j D1 j D1<br><!-- End of picture text -->

a tedy jAxEj �kAkF jExj. 

b) Platí AB D �PnkD1<sup>aikbkj</sup> �ni;j D1<sup>,atedy,opětsvyužitímCauchyho–Schwarzovynerovnosti,</sup> máme 



<!-- Start of picture text -->
n n n n n<br>kABk 2 F D X X� X n aikbkj �2 � X X� X n aik 2 �� X akj 2 �<br>i D1 j D1 kD1 i D1 j D1 kD1 kD1<br>D jv poslední sumě přeznačme k 7! `j<br>n n n n n n n<br>D X X� X n aik 2 �� X a`j 2 � D X X X X aik 2 b `j 2<br>iD1 j D1 kD1 `D1 iD1 j D1 kD1 `D1<br>n n<br>D �X n X aik 2 �� X n X b`j 2 � D kAk 2 F kBk2 F :<br>iD1 j D1 kD1 `D1<br><!-- End of picture text -->

Po odmocnění tedy dostáváme požadovanou nerovnost. 

c) Podle předpokladu je A regulární, a tedy existuje inverzní matice A<sup>�1</sup> (což znamená, že A<sup>�1</sup> je nenulová, a tudíž kA<sup>�1</sup> kF ¤ 0). Rovnost A<sup>�1</sup> .A � B/xE D xE � A<sup>�1</sup> B Ex si přepišme na tvar 



<!-- Start of picture text -->
xE D A �1 .A � B/xE C A �1 B Ex:<br><!-- End of picture text -->

Odtud 



<!-- Start of picture text -->
jExj D jA �1 .A � B/xE C A �1 B Exj �jA �1 .A � B/xEj C jA �1 B Exj<br>�kA �1 kF kA � BkF jExj C kA �1 kF jB Exj;<br><!-- End of picture text -->

kde jsme využili trojúhelníkovou nerovnost jEu C Evj �jEujCjEvj a vlastností a), b) lemmatu. Předpokládejme nyní xE ¤ oE (a tedy jExj ¤ 0). Aplikujeme-li na člen kA � BkF předpoklad kA � BkF < 1=kA<sup>�1</sup> kF , dostáváme 

jExj < jExjCkA<sup>�1</sup> kF jB Exj; tj. 0 < kA<sup>�1</sup> kF jB Exj; tj. 0 < jB Exj; tj. jB Exj ¤ 0; tj. B Ex ¤ o:E 

Poslední podmínka B Ex ¤ 0 pro každé xE ¤ oE zaručuje, že lineární zobrazení xE 7! B Ex je prosté (kdyby existovaly xE ¤ yE takové, že B Ex D B Ey, pak bychom dostali oE D B Ex � B Ey D B.xE �Ey/ ) xE D yE, což je spor), a tedy existuje inverzní zobrazení reprezentované maticí B<sup>�1</sup> . Jinak řečeno, B je regulární. 

Poznámka 11.19. Frobeniova norma může být použita na měření vzdálenosti dvou matic A; B 2 R<sup>n�n</sup> . Přesněji, není těžké ukázat, že zobrazení � definované �.A; B/ D kA � BkF je metrikou na množině všech čtvercových matic řádu n. Uvažujeme-li nyní maticovou funkci _F_ (jakožto zobrazení z R<sup>n</sup> do R<sup>n�n</sup> ) definovanou na nějaké množině M � R<sup>n</sup> , tak spojitost této funkce v bodě X0 2 M znamená, že ke každému " > 0 existuje ı > 0 takové, že pro každé X 2 Oı .X0/ \ D. _F_ / platí k _F_ .X/ � _F_ .X0/kF < ". (Tato definice je v souladu s definicí spojitosti zobrazení mezi metrickými prostory.) 

_Důkaz věty 11.17._ Položme A D _F_<sup>0</sup> .X0/. Protože _F_<sup>0</sup> je spojitá v bodě X0, který je vnitřním bodem množiny U , pro " D 1=.2kA<sup>�1</sup> kF / existuje okolí V D Oı .X0/ (tj. otevřená koule se středem v bodě X0 a poloměrem ı, přičemž není podstatné jakou z metrik �1, �2, �1 uvažujeme) takové, že V � U a pro každé X 2 V platí 



<!-- Start of picture text -->
1<br>kA � F 0 .X/kF < ; (␆)<br>2kA �1 kF<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

54 

a navíc, díky vlastnosti c) lemmatu 11.18, Jacobiova matice _F_<sup>0</sup> .X/ je regulární pro každé X 2 V . Interpretujme nyní bod X D Œx1; : : : ; xn� 2 R<sup>n</sup> jako sloupcový vektor .x1; : : : ; xn/<sup>T</sup> a _F_ jakou sloupcovou vektorovou funkci .f1; : : : ; fn/<sup>T</sup> . Definujme zobrazení _T_ Y W V ! R<sup>n</sup> předpisem 



<!-- Start of picture text -->
T Y .X/ D X � A �1 .Y � F .X//;<br><!-- End of picture text -->

kde Y 2 R<sup>n</sup> je parametr. Protože A<sup>�1</sup> je regulární, rovnost _T_ Y .X/ D X (tj. X je pevným bodem zobrazení _T_ Y ) nastane, právě když Y D _F_ .X/. Ukažme, že _T_ Y je na uvažovaném okolí kontraktivní. 

Nechť X1; X2 2 V jsou libovolně zvolené dva body. Rozdíl _T_ Y .X2/ � _T_ Y .X1/ je možné napsat ve tvaru 



<!-- Start of picture text -->
d<br>T Y .X2/ � T Y .X1/ D � 01 dt T Y .X1 C t.X2 � X1// dt D � 01 T Y 0 .X1 C t.X2 � X1//.X2 � X1/ dt<br>D � � 01 T Y 0 .X1 C t.X2 � X1// dt �.X2 � X1/ D  T Y 0 .X�/ � � 01 dt �.X2 � X1/;<br>„ ƒ‚ …<br>D1<br><!-- End of picture text -->

kde X� D X1 C t�.X2 � X1/, t� 2 .0; 1/. Ve druhé rovnosti jsme přitom využili řetězové pravidlo pro derivování složené funkce a ve třetí rovnosti integrální větu o střední hodnotě. Všimněme si, že výraz X1 C t.X2 � X1/, t 2 h0; 1i, představuje úsečku spojující body X1; X2. Zřejmě, všechny body této úsečky leží v kouli V (a tedy i X� 2 V ). Dále 



<!-- Start of picture text -->
j T Y .X2/ � T Y .X1/j D j T 0 .X�/.X2 � X1/j �k T 0 .X�/kF jX2 � X1j;<br><!-- End of picture text -->

kde nerovnost plyne z lematu 11.18a). Protože 



<!-- Start of picture text -->
T Y 0 .X/ D I � A�1 F  0.X/ D A�1.A � F  0.X//<br><!-- End of picture text -->

(I je jednotková matice), máme s využitím lemmatu 11.18b) 



<!-- Start of picture text -->
k T Y 0 .X/kF D kA�1.A � F  0.X//kF �kA�1kF kA � F  0.X/kF :<br><!-- End of picture text -->

Odhadneme-li člen na pravé straně pomocí (␆), dostáváme k _T_ Y<sup>0.X/kF<</sup><sup><u>1</u></sup> 2<sup>, a tedy (vzhledem k tomu, že</sup> body X1; X2 2 V byly voleny libovolně) 



<!-- Start of picture text -->
j T Y .X2/ � T Y .X1/j � 1 8X1; X2 2 V;<br>2 jX2 � X1j<br><!-- End of picture text -->

což znamená, že _T_ Y je na V kontraktivní. Zatím není možné aplikovat Banachovu větu o pevném bodě, protože nevíme, zda obraz množiny V je podmnožinou této množiny (intuitivně, toto bude záviset na parametru Y 2 R<sup>n</sup> ). Nyní pouze víme, že pevný bod, pokud existuje, je nejvýše jeden, protože _T_ Y je kontrakce (viz bod d) důkazu Banachovy věty). Jinak řečeno, pro Y 2 R<sup>n</sup> existuje nejvýše jedno X 2 V takové, že _F_ .X/ D Y , tedy _F_ je na V prosté. Označme W D _F_ .V / a ukažme, že W je otevřená. 

Vezměme Y<sup>�</sup> 2 W libovolně. Potřebujeme ukázat, že Y<sup>�</sup> je vnitřní bod množiny W , tj. že existuje okolí (otevřená koule) bodu Y<sup>�</sup> , které je podmnožinou W . Protože W je oborem hodnot zobrazení _F_ na množině V a _F_ je prosté, existuje jediné X<sup>�</sup> 2 V takové, že _F_ .X<sup>�</sup> / D Y<sup>�</sup> . Nechť r > 0 je dostatečně malý poloměr takový, aby uzavřená koule Br ŒX<sup>�</sup> � (nyní uvažujme eukleidovskou metriku) byla podmnožinou V (takový poloměr jistě existuje, protože V je otevřená). Nechť Y 2 R<sup>n</sup> je takový bod, že 



<!-- Start of picture text -->
r<br>jY � Y � j < :<br>2kA �1 kF<br><!-- End of picture text -->

Jestliže nyní X<sup>��</sup> 2 Br ŒX<sup>�</sup> �, pak 



<!-- Start of picture text -->
j T Y .X �� / � X � j �j T Y .X �� / � T Y .X � /j C j T Y .X � / � X � j � 1<br>2 jX �� � X �j C jA�1.Y � Y �/j<br>r<br>� 2 r C kA�1kF jY � Y �j < 2 r C kA�1kF 2kA �1 kF D r:<br><!-- End of picture text -->

11 Implicitní funkce, diferencovatelná zobrazení mezi prostory vyšší dimenze 

55 

Ukázali jsme tedy, že pro body Y dostatečně blízké bodu Y<sup>�</sup> , _T_ Y zobrazuje uzavřenou kouli Br ŒX<sup>�</sup> � do otevřené koule Br .X<sup>�</sup> / � Br ŒX<sup>�</sup> �. Protože uzavřená množina v R<sup>n</sup> s eukleidovskou metrikou tvoří úplný prostor a _T_ Y je kontraktivní, toto zobrazení má jediný pevný bod X 2 Br ŒX<sup>�</sup> �, tj. X D _T_ Y .X/, tj. _F_ .X/ D Y . Navíc, 



<!-- Start of picture text -->
F .Br ŒX � �/ D Br=.2kA�1/kF /.Y � / � F .V / D W;<br><!-- End of picture text -->

a tedy W je otevřená množina. 

Protože _F_ je prostá n-funkce na V , existuje inverzní n-funkce _F_<sup>�1</sup> W W ! V . Ukažme nejprve, že _F_<sup>�1</sup> je v každém bodě Y 2 W diferencovatelná (a tedy má na W Jacobiovu matici). Nechť tedy Y 2 W a K 2 R<sup>n</sup> je takové, že také Y C K 2 W . Protože _F_ je bijekce množiny V na množinu W , existuje jediné X 2 V takové, že _F_ .X/ D Y , a existuje jediné nenulové H 2 R<sup>n</sup> takové, že _F_ .X C H/ D Y C K. Jinak řečeno, _F_<sup>�1</sup> .Y / D X a _F_<sup>�1</sup> .Y C K/ D X C H . Platí 



<!-- Start of picture text -->
T Y .X C H/ � T Y .X/ D H C A �1 . F .X/ � F .X C H// D H � A �1 K:<br><!-- End of picture text -->

Protože _T_ Y je na V kontraktivní s Lipschitzovou konstantou 1=2, dostaneme snadno odhad velikosti vektoru na pravé straně jako 



<!-- Start of picture text -->
jH � A �1 Kj D j T Y .X C H/ � T Y .X/j � 2 1 jX C H � Xj D jH 2 j :<br><!-- End of picture text -->

Využijeme-li bezprostředního důsledku trojúhelníkové nerovnosti<sup>10ˇˇ</sup> jEuj �jEvjˇˇ �jEu �Evj 8Eu; Ev 2 Rn, tak 



<!-- Start of picture text -->
jH j �jA �1 Kj �jH � A �1 Kj � jH j ) jH j � 2jA �1 Kj � 2kA �1 kF jKj:<br>2<br><!-- End of picture text -->

Z posledního vyjádření plyne 



<!-- Start of picture text -->
jH j<br>jKj � 2kA�1kF : (␆␆)<br><!-- End of picture text -->

Protože X 2 V , Jacobiova matice _F_<sup>0</sup> .X/ je regulární, a tedy existuje inverzní matice B D . _F_<sup>0</sup> .X//<sup>�1</sup> . Intuitivně, tato matice bude Jacobiovou maticí n-funkce _F_<sup>�1</sup> v bodě Y . Ukažme, že tomu tak skutečně je. Diferencovatelnost n-funkce _F_<sup>�1</sup> v bodě Y s maticí B totálního diferenciálu znamená, že 



<!-- Start of picture text -->
j F �1 .Y C K/ � F �1 .Y / � BKj<br>! 0 pro jKj ! 0:<br>jKj<br><!-- End of picture text -->

Platí 



<!-- Start of picture text -->
j F �1 .Y C K/ � F �1 .Y / � BKj D jH � BKj D jBK � H j D jB. F .X C H / � F .X// � H j<br>jKj jKj jKj jKj<br>D jB. F .X C H / � F .X/ � B �1H /j D jB. F .X C H / � F .X/ � F  0.X/H /j<br>jKj jKj<br>jH j j F .X C H / � F .X/ � F 0 .X/H /j<br>�kBkF<br>jKj jH j<br>j F .X C H / � F .X/ � F 0 .X/H /j<br>� 2kBkF kA �1 kF ;<br>jH j<br><!-- End of picture text -->

kde jsme využili první vlastnosti lemmatu 11.18 a odhadu (␆␆). Když jKj ! 0, tak zároveň jH j ! 0 (to plyne ihned z nerovnosti jH j � 2kA<sup>�1</sup> kF jKj). Podle předpokladu je _F_ na V spojitě diferencovatelná (Jacobiova matice _F_<sup>0</sup> .X/ je maticí totálního diferenciálu v bodě X 2 V ), pravá strana konverguje k nule pro jH j ! 0. V důsledku toho 



<!-- Start of picture text -->
j F �1 .Y C K/ � F �1 .Y / � BKj<br>lim D 0;<br>jKj!0 jKj<br><!-- End of picture text -->

> 10Platí totiž jEuj D jEu �Ev C Evj �jEu �Evj C jEvj, a tedy jEuj �jEvj �jEu �Evj. Zároveň však jEvj D jEv �Eu C uEj �jEv �Euj C jEuj D jEu �Evj C jEuj, a tedy jEvj �jEuj �jEu �Evj. Protože absolutní hodnota má vlastnost .a < b ^ �a < b/ ) jaj < b, zkombinováním obou výsledných nerovností máme ˇˇjEuj �jEvjˇˇ �jEu �Evj. 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

56 

neboli _F_<sup>�1</sup> je diferencovatelná v bodě Y 2 W , přičemž maticí totálního diferenciálu d _F_<sup>�1</sup> .Y / je matice B D . _F_<sup>0</sup> .X//<sup>�1</sup> D . _F_<sup>�1</sup> /<sup>0</sup> .Y /. 

Zbývá ukázat, že Jacobiova matice . _F_<sup>�1</sup> /<sup>0</sup> je na W spojitá, tj. že _F_<sup>�1</sup> je spojitě diferencovatelná n-funkce (viz věta 8.6). Předně si uvědomme, že když je maticová funkce spojitá a regulární v každém bodě nějaké množiny, tak inverzní matice je opět spojitá v každém bodě této množiny. To plyne z toho, že inverzní matici lze psát ve tvaru 



<!-- Start of picture text -->
1<br>M �1 D det.M/ adj.M/;<br><!-- End of picture text -->

kde adj.M/ značí adjungovanou matici (transponovanou matici algebraických doplňků). Determinant det.M/ je spojitou funkcí, protože se jedná o konečný počet operací násobení a sčítání (resp. odečítání) složek matice (které jsou spojité). Zároveň je v každém bodě uvažované množiny det.M/ ¤ 0. Ze stejného důvodu jsou spojité složky matice adj.M/. Spojitost . _F_<sup>�1</sup> /<sup>0</sup> na W nyní plyne z vyjádření 



<!-- Start of picture text -->
. F �1 / 0 .Y / D � F 0 . F �1 .Y //��1;<br><!-- End of picture text -->

protože _F_<sup>�1</sup> je na W diferencovatelná, a tudíž spojitá, a složení dvou spojitých n-funkcí je spojitá n-funkce. 

Poznámka 11.20. a) Jsou známy i důkazové techniky, které se obejdou bez Banachovy věty o pevném bodu. 

b) Kdybychom od začátku věděli, že _F_ má na okolí bodu X0 inverzi, která je diferencovatelná, tak vzorec pro Jacobiovu matici plyne z věty 11.16 aplikované na identické zobrazení _F_<sup>�1</sup> ı _F_ .x1; x2; : : : ; xn/ D Œx1; x2; : : : ; xn� (Jacobiovou maticí identity je jednotková matice I ). Tedy . _F_<sup>�1</sup> /<sup>0</sup> . _F_ .x1<sup>0; x</sup> 2<sup>0; : : : ; x</sup> n<sup>0// �</sup> _F_<sup>0</sup> .x1<sup>0; x</sup> 2<sup>0; : : : ; x</sup> n<sup>0/ D I, což je jinak napsaný vzorec věty.</sup> c) Věta vlastně říká, za jakých okolností má soustava rovnic _F_ .X/ D Y jednoznačné řešení X v závislosti na Y , musíme se ovšem pohybovat „blízko“ bodů X0 a Y0 (pro které platí _F_ .X0/ D Y0). 

Uvažujme nyní soustavu rovnic 



<!-- Start of picture text -->
g1.x1; x2; : : : ; xn; y1; y2; : : : ; ym/ D 0;<br>g2.x1; x2; : : : ; xn; y1; y2; : : : ; ym/ D 0;<br>(␄)<br>:::<br><!-- End of picture text -->



<!-- Start of picture text -->
gm.x1; x2; : : : ; xn; y1; y2; : : : ; ym/ D 0;<br><!-- End of picture text -->

m-funkci 



<!-- Start of picture text -->
y1 D f1.x1; x2; : : : ; xn/;<br>y2 D f2.x1; x2; : : : ; xn/;<br>(␄␄)<br>:::<br><!-- End of picture text -->



<!-- Start of picture text -->
ym D fm.x1; x2; : : : ; xn/;<br><!-- End of picture text -->

bod ŒX0; Y0� D Œx1<sup>0; x</sup> 2<sup>0; : : : ; x</sup> n<sup>0; y</sup> 1<sup>0; y</sup> 2<sup>0; : : : ; y</sup> m<sup>0�2RnCm, který vyhovuje soustavě (␄) a nechť ı>0.</sup> Řekneme, že m-funkce (␄␄) je dána na okolí Oı .X0/ implicitně soustavou (␄), jestliže pro každé X 2 Oı .X0/ platí 



<!-- Start of picture text -->
g1.x1; x2; : : : ; xn; f1.x1; x2; : : : ; xn/; f2.x1; x2; : : : ; xn/; : : : ; fm.x1; x2; : : : ; xn// D 0;<br>g2.x1; x2; : : : ; xn; f1.x1; x2; : : : ; xn/; f2.x1; x2; : : : ; xn/; : : : ; fm.x1; x2; : : : ; xn// D 0;<br>:::<br><!-- End of picture text -->



<!-- Start of picture text -->
gm.x1; x2; : : : ; xn; f1.x1; x2; : : : ; xn/; f2.x1; x2; : : : ; xn/; : : : ; fm.x1; x2; : : : ; xn// D 0:<br><!-- End of picture text -->

11 Implicitní funkce, diferencovatelná zobrazení mezi prostory vyšší dimenze 

57 

■ Vˇeta 11.21 — o existenci implicitní **m** -funkce a její Jacobiovˇe matici. _Nechť G_ D Œg1; g2; : : : ; gm� W R<sup>nCm</sup> ! R<sup>m</sup> _je spojitá_ m _-funkce v okolí_ Oa.ŒX0; Y0�/ _pro nějaké_ a > 0 _(okolí bereme opět v metrice_ �1 _), přičemž bod_ ŒX0; Y0� _vyhovuje soustavě G_ .X; Y / D O D Œ0; 0; : : : ; 0� _(tj. soustavě_ (␄) _), a nechť všechny prvky matice_ 



<!-- Start of picture text -->
@g1 @g1 @g1<br>@y1 @y2 : : : @ym<br>0 1<br>@g2 @g2 @g2<br>G Y 0 D @y1 @y2 : : : @ym<br>::: ::: ::: :::<br>@gm @gm @gm<br>: : :<br>BBBBBB@ @y1 @y2 @ym CCCCCCA<br><!-- End of picture text -->

_existují v_ Oa.ŒX0; Y0�/ _, jsou spojité v bodě_ ŒX0; Y0� _a platí_ det. _G_ Y<sup>0.X0; Y0//¤0</sup><sup>_.Pakexistujeokolí_</sup> Oı .X0/ � R<sup>n</sup> _, na kterém je soustavou G_ .X; Y / D O _implicitně dána jediná spojitá_ m _-funkce_ 



<!-- Start of picture text -->
Y D  F .X/ D Œf1.X/; f2.X/; : : : ; fm.X/�<br><!-- End of picture text -->

_(tj._ m _-funkce ve tvaru_ (␄␄) _). Jsou-li navíc spojité všechny prvky matice_ 



<!-- Start of picture text -->
@g1 @g1 @g1 @g1<br>@x1 @x2 : : : @xm : : : @xn<br>0 1<br>@g2 @g2 @g2 @g2<br>G X 0 D @x1 @x2 : : : @xm : : : @xn<br>::: ::: ::: ::: ::: :::<br>@gm @gm @gm @gm<br>: : : : : :<br>BBBBBB@ @x1 @x2 @xm @xn CCCCCCA<br><!-- End of picture text -->

_a všechny prvky matice G_ Y<sup>0</sup><sup>_v_Oa.ŒX0; Y0�/</sup><sup>_, pak Fje diferencovatelná v_X0</sup><sup>_a pro její Jacobiovu matici_</sup> _platí_ 



<!-- Start of picture text -->
F 0 .X0/ D �. G Y 0 .X0; Y0//�1 G X  0 .X0; Y0/:<br><!-- End of picture text -->

_Idea důkazu._ Označíme-li d D det. _G_ y<sup>0.X0; Y0//abudeme-lismaticemi</sup><sup>_G_</sup> y<sup>0a</sup><sup>_G_</sup> x<sup>0manipulovatstejně</sup> jako s derivacemi Fy<sup>0a F</sup> x<sup>0v důkazu věty 11.3, tak zjistíme, že tento důkaz lze přepsat i pro maticový</sup> případ. 

Poznámka 11.22. První část věty vlastně říká, za jakých podmínek lze ze soustavy (␄) vyjádřit m-tici (␄␄) (pokud to jde, tak to ještě neznamená, že je to početně jednoduché). 

Pˇríklad 11.23. Najděte bod, v jehož okolí vyjadřuje soustava x<sup>2</sup> C y<sup>2</sup> C u<sup>2</sup> C v<sup>2</sup> D 2, xu C yv C e<sup>uv</sup> D 0 implicitně 2-funkci u D u.x; y/, v D v.x; y/ a určete její Jacobiovu matici v tomto bodě. 

_Řešení._ Dosazením ověříme, že soustavě vyhovuje např. bod Œx0; y0; u0; v0� D Œ�1; 0; 1; 0�. Dále máme 



<!-- Start of picture text -->
2y 2u 2v<br>G Œx;y� 0 D �2xu v � ; G Œu;v� 0 D �x C v e uv y C u e uv � ;<br>det. G Œu;v� 0 / D 2uy C 2u2 euv �2xv � 2v2 euv :<br><!-- End of picture text -->

Odtud 



<!-- Start of picture text -->
1 �2v<br>. G Œu;v� 0 /�1 D 2uy C 2u 2 e uv �2xv � 2v 2 e uv ��yx C � uv e euv uv 2u � ;<br>�1 2y 2 C 2yu e uv �2v 2<br>F 0 D 2uy C 2u 2 e uv �2xv � 2v 2 e uv ��2xy2x 2  C� 2xu2xv e euv uv  �C2uv2u 2 �2xy � 2yv e uv C2uv� ;<br><!-- End of picture text -->

a tedy 



<!-- Start of picture text -->
0 0<br>F 0 .�1; 0/ D �1 D :<br>2 ��02 0� �01 0�<br><!-- End of picture text -->

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

58 

#### Pˇríklady k procviˇcení 

11.1. Ověřte, že daná rovnice zadává v okolí bodu A implicitně jedinou spojitou funkci y D f .x/. Vypočtěte její derivaci a napište rovnici tečny a normály ke grafu funkce f v bodě A: 



<!-- Start of picture text -->
x sin y C e x cos y C cos x D 1; A D Œ0; �=2�:<br><!-- End of picture text -->

11.2. Najděte body, v nichž pro následující rovnice nejsou splněny předpoklady věty o existenci implicitní funkce z D f .x; y/: 



<!-- Start of picture text -->
x 2<br>a/ z 2 � 2px D 0; p > 0; b/ a; b; c > 0:<br>a 2 C y b 22 � z c 22 D 1;<br><!-- End of picture text -->

11.3. Uvažujte funkci y D f .x/, která je implicitně určena rovnicí 



<!-- Start of picture text -->
x<br>y C y x C y D 3 a bodem A D Œ1; 1�:<br><!-- End of picture text -->

Napište Taylorův polynom druhého stupně této funkce v bodě x0 D 1. 

11.4. Na soustavu dvou rovnic x<sup>2</sup> C y<sup>2</sup> C z<sup>2</sup> � 9 D 0, x<sup>2</sup> C y<sup>2</sup> � z<sup>2</sup> D 0 lze geometricky nahlížet jako na křivku v prostoru, která vznikne jako průnik ploch (ty jsou určeny právě zadanými rovnicemi). Rozhodněte, zda lze tuto křivku v okolí bodu X0 D Œ ~~p~~ 3=2; ~~p~~ 3; 3= ~~p~~ 2� parametrizovat a) pomocí parametru y, b) pomocí parametru z (jinak řečeno, zda lze ze soustavy vyjádřit 2-funkci proměnné y, resp. proměnné z). Je-li některá varianta možná, určete tečný vektor křivky v bodě X0. 

11.5. Nalezněte druhé derivace funkcí x D '1.z/, y D '2.z/, které jsou dány implicitně soustavu rovnic 



<!-- Start of picture text -->
x 3 C y 3 C z 3 D 1;<br>x 2 C y 2 C z 2 D 3<br><!-- End of picture text -->

v okolí bodu Œ�1; 1; 1�. Vypočtěte jejich hodnoty v bodě z D 1. 

_Výsledky._ 11.1. t W x � y C �=2 D 0, n W x C y � �=2 D 0. 11.2. a) Body osy y, b) fŒx; y; z� 2 R<sup>3</sup> W x<sup>2</sup> =a<sup>2</sup> C y<sup>2</sup> =b<sup>2</sup> D 1; z D 0g. 11.3. T2.x/ D 1 � .x � 1/<sup>2</sup> . 11.4. a) Lze to, t<sup>E</sup> D .�2; 1; 0/, b) větu o existenci implicitní m-funkce nelze použít, ale pokud si uvědomíme, že křivka je kružnicí rovnoběžnou se souřadnou rovinou xy ve výšce z D 3= ~~p~~ 2, lehko zjistíme, že případ b) nelze provést. 11.5. '1<sup>00.1/ D �1,</sup> '2<sup>00.1/ D �3.</sup> 

### 12 Vázané extrémy 

Definice 12.1 — lokálního extrému vzhledem k množinˇe. Nechť f W R<sup>n</sup> ! R je funkce a M � D.f / je nějaká neprázdná množina. Řekneme, že funkce f má v bodě X0 2 M _lokální minimum_ (resp. _maximum_ ) _vzhledem k množině_ M , jestliže existuje okolí O.X0/ takové, že pro X 2 M \O.X0/ platí f .X0/ � f .X/ (resp. f .X0/ � f .X/). Jsou-li nerovnosti pro X ¤ X0 ostré, mluvíme o _ostrých lokálních extrémech vzhledem k_ M . 

V této kapitole budeme uvažovat případ, kdy množina M je zadána soustavou 



<!-- Start of picture text -->
g1.x1; x2; : : : ; xn/ D 0;<br>g2.x1; x2; : : : ; xn/ D 0;<br>(4)<br>:::<br>gm.x1; x2; : : : ; xn/ D 0; kde 1 � m < n:<br><!-- End of picture text -->

V tomto případě se místo termínu lokální extrém vzhledem k M používá termínu _lokální extrém vázaný podmínkami_ .4/ nebo stručně _vázaný lokální extrém_ . 

12 Vázané extrémy 

59 

■ Vˇeta 12.2 — metoda Lagrangeových multiplikátor˚u, nutná podmínka pro existenci vázaného lokálního extrému. _Nechť funkce_ f; g1; : : : ; gm W R<sup>n</sup> ! R _(_ 1 � m < n _) mají spojité parciální derivace v otevřené množině_ U � R<sup>n</sup> _a nechť v každém bodě množiny_ U _má Jacobiova matice G_<sup>0</sup> m _-funkce G_ D Œg1; g2; : : : ; gm� _hodnost_ m _. Dále, nechť_ M � U _je množina všech bodů_ X D Œx1; x2; : : : ; xn� _, které vyhovují rovnicím_ .4/ _. Má-li_ f _v bodě_ X0 2 M _vázaný lokální extrém, pak existují reálná čísla_ �1; �2; : : : ; �m _(Lagrangeovy multiplikátory) taková, že jsou splněny rovnosti_ 



<!-- Start of picture text -->
@f m @gk<br>.X0/ C X �k .X0/ D 0; j D 1; 2; : : : ; n: (~)<br>@xj kD1 @xj<br><!-- End of picture text -->

_Důkaz._ Větu lze dokázat vícero způsoby, jeden z nich využívá větu o lokální inverzi (viz věta 11.17). Zde si pro jednoduchost ukážeme důkaz pro n D 2 a m D 1 (tj. uvažujeme funkci f D f .x; y/ dvou proměnných s jednou vazebnou podmínkou g.x; y/ D 0). 

Nechť jsou tedy splněny předpoklady věty a f má v bodě Œx0; y0� vázaný lokální extrém. Pak g.x0; y0/ D 0. Protože hodnost h.gx<sup>0; g</sup> y<sup>0/ D 1 (matice je zde typu 1 �2, tj. řádkový vektor) na nějaké</sup> množině U obsahující bod Œx0; y0�, nemůže být zároveň gx<sup>0.x0; y0/ D 0 a g</sup> y<sup>0.x0; y0/ D 0. Nechť např.</sup> gy<sup>0.x0; y0/ ¤ 0. Pak jsou splněny předpoklady vět o existenci implicitní funkce a o její derivaci, tj. existuje</sup> funkce y D '.x/ taková, že y0 D '.x0/ a 



<!-- Start of picture text -->
' 0 .x0/ D � g x 0 .x0; y0/<br>gy 0 .x0; y0/ :<br><!-- End of picture text -->

Úlohu o vázaném extrému převedeme na na úlohu o (volném) lokálním extrému funkce h.x/ D f .x; '.x//. Podle věty o derivování složené funkce platí 



<!-- Start of picture text -->
x .x;y0/<br>h 0 .x0/ D fx 0 .x0; '.x0// � 1 C f y 0.x0; '.x0// '0.x0/ D f x 0 .x0; y0/ C f y 0.x0; y0/ �g0<br>gy 0 .x0; y0/ D 0:<br><!-- End of picture text -->

Pro Œx; y� 2 U splňující g.x; y/ D 0 je dg D gx<sup>0h C g</sup> y<sup>0kD 0, a tedy i g</sup> x<sup>0.x0; y0/h C g</sup> y<sup>0.x0; y0/kD 0.</sup> Odtud pro h ¤ 0 �<sup><u>g</u></sup> <u>x</u><sup>0</sup><sup><u>.x0; y0/</u></sup> h<sup>:</sup> gy<sup>0</sup> .x0; y0/<sup>Dk</sup> 

Po dosazení této rovnosti do vyjádření pro h<sup>0</sup> .x0/ dostaneme vynásobením h rovnost 



<!-- Start of picture text -->
fx 0 .x0; y0/h C f y 0.x0; y0/k D 0<br><!-- End of picture text -->

K této rovnici nyní přičtěme výše uvedenou rovnost gx<sup>0.x0; y0/h C g</sup> y<sup>0.x0; y0/kD0vynásobenou</sup> parametrem � 2 R. Tím dostáváme novou rovnost ve tvaru 



<!-- Start of picture text -->
�fx 0 .x0; y0/ C �g x 0 .x0; y0/ � h C �fy 0.x0; y0/ C �g y 0 .x0; y0/ � k D 0:<br><!-- End of picture text -->

Zvolme � tak, aby fy<sup>0.x0; y0/C�g</sup> y<sup>0.x0; y0/ D 0 (to jistě lze, neboť jsme předpokládali, že g</sup> y<sup>0.x0; y0/ ¤ 0).</sup> Pak ale také musí být fx<sup>0.x0; y0/ C �g</sup> x<sup>0.x0; y0/ D 0, protože h je libovolné. Jinak řečeno, existuje �2 R</sup> takové, že rf .x0; y0/ C �rg.x0; y0/ D .0; 0/, což jsme chtěli ukázat. 

Definice 12.3 — stacionárního bodu funkce na M . Bod X0 2 M , pro který existují Lagrangeovy multiplikátory �1; : : : ; �m tak, že platí .~/, se nazývá _stacionární bod funkce_ f _na_ M . 

Poznámka 12.4. Věta 12.2 vlastně dává návod, jak stacionární body nalézt. Sestrojí se Lagrangeova funkce 



<!-- Start of picture text -->
m<br>L.x1; x2; : : : ; xn; �1; �2; : : : ; �m/ D f .x1; x2; : : : ; xn/ C X �kgk.x1; x2; : : : ; xn/:<br>kD1<br><!-- End of picture text -->

Položíme-li její gradient roven nulovému vektoru, dostaneme právě vztahy .~/. 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

60 

■ Vˇeta 12.5 — postaˇcující podmínky pro existenci vázaného lokálního extrému. _Nechť_ S _je stacionární bod funkce_ f _na_ M _,_ �S D Œ�<sup>S</sup> 1<sup>; �S</sup> 2<sup>; : : : ; �</sup> m<sup>S�</sup><sup>_jsou Lagrangeovy multiplikátory příslušné bodu_S</sup><sup>_,_</sup> _funkce_ f; g1; g2; : : : ; gm _mají spojité druhé parciální derivace v bodě_ S _a nějakém jeho okolí a Jacobiova matice G_<sup>0</sup> .S/ _má hodnost_ m _. Je-li_ d<sup>2</sup> L.S; �S / 

(i) _pozitivně definitní, pak v_ S _je ostré vázané lokální minimum._ 

- (ii) _negativně definitní, pak v_ S _je ostré vázané lokální maximum._ 

_Důkaz._ Předpoklady věty jsou takové, že pozitivní definitnost d<sup>2</sup> L.S; �S / zaručuje existenci (volného) lokálního minima Lagrangeovy funkce L v bodě S při pevném � D �S , tj. existuje okolí O.S/, na kterém platí 



<!-- Start of picture text -->
L.S; �S / < L.X; �S /;<br><!-- End of picture text -->

tj. 



<!-- Start of picture text -->
m m m<br>f .S/ C X � S k gk.S/ < f .X/ C X � S k gk.X/ H) f .S/ < f .X/ C X � S k gk.X/:<br>kD1 kD1 kD1<br><!-- End of picture text -->

Uvedená nerovnost platí i pro body X z množiny M , na které je gk.X/ D 0, k D 1; 2; : : : ; m a tedy pro tyto body platí f .S/ < f .X/. To však znamená, že funkce má v S ostré lokální minimum vázané podmínkami .4/. Analogicky by se ukázalo pro maximum. 

Poznámka 12.6. a) Protože diferenciál součtu je součet diferenciálů, platí d<sup>2</sup> L D d<sup>2</sup> f C<sup>Pm</sup> kD1<sup>�kd2gk.</sup> Stejně tak pro Hessovu matici diferenciálu d<sup>2</sup> L platí HL D Hf C<sup>P</sup> k<sup>m</sup> D1<sup>�kHg</sup> k<sup>.</sup> 

b) Pozor, je-li d<sup>2</sup> L.S; �S / indefinitní, tak to (na rozdíl od volných lokálních extrémů) neznamená, že v S není vázaný lokální extrém. Pro existenci vázaných lokálních extrémů stačí, když d<sup>2</sup> L.S; �S / je kladná (resp. záporná) pro všechny nenulové vektory h<sup>E</sup> D .h1; h2; : : : ; hn/ kolmé k vektorům rgk.S/, k D 1; 2; : : : ; m). Je-li tedy d<sup>2</sup> L.S; �S / indefinitní, lze dále postupovat takto: Ze soustavy 



<!-- Start of picture text -->
dg1.S/ D 0;<br>dg2.S/ D 0;<br>:::<br><!-- End of picture text -->



<!-- Start of picture text -->
dgm.S/ D 0;<br><!-- End of picture text -->

tj. ze soustavy 



<!-- Start of picture text -->
0hh121 0001<br>G 0 .S/<br>::: :::<br>BBB@hnCCCA D BBB@0CCCA ;<br><!-- End of picture text -->

lze jednoznačně vyjádřit m přírůstků hi (protože _G_<sup>0</sup> .S/ má hodnost m) jako lineární formy zbývajících přírůstků (lineární forma n-proměnných je funkce typu a1x1 C a2x2 C ���C anxn, kde ai 2 R, i D 1; 2; : : : ; n). Dosazením takto vyjádřených přírůstků do d<sup>2</sup> L.S; �S / dostaneme novou kvadratickou formu n � m proměnných, označme ji např. ˚. Potom platí: Je-li ˚ 

a) pozitivně definitní, pak v S je ostré vázané lokální minimum, 

- b) negativně definitní, pak v S je ostré vázané lokální maximum, 

- c) indefinitní, pak v S nenastává vázaný lokální extrém. 

Pˇríklad 12.7. Vyšetřete vázané extrémy funkce f .x; y/ D xy vzhledem k množině M D fŒx; y� 2 R<sup>2</sup> W x C y D 1g. 

_Řešení._ 1. způsob: Vazebnou podmínku pišme ve tvaru x C y � 1 D 0 (máme tedy g.x; y/ D x C y � 1). Lagrangeova funkce má tvar L.x; y; �/ D xy C �.x C y � 1/. Položíme-li parciální derivace podle všech proměnných rovny nule, dostaneme soustavu: 

L<sup>0</sup> x<sup>D y C �D 0;</sup> 

12 Vázané extrémy 

61 



<!-- Start of picture text -->
Ly 0 D x C � D 0;<br>L 0 � D x C y � 1 D 0;<br><!-- End of picture text -->

jejímž jediným řešením je x D<sup><u>1</u></sup> 2<sup>, yD</sup><sup><u>1</u></sup> 2<sup>a �D �</sup><sup><u>1</u></sup> 2<sup>(z první rovnice se vyjádří y, z druhé x a dosadí se</sup> do třetí). Máme tedy jeden stacionární bod S D � <u>12</u><sup>;</sup><sup><u>1</u></sup> 2 � a k němu příslušný multiplikátor �S D � 2<sup><u>1</u>.</sup> Dále, fxx<sup>00D 0, f</sup> xy<sup>00D 1, f</sup> yy<sup>00D 0, g</sup> xx<sup>00D g</sup> xy<sup>00D g</sup> yy<sup>00D 0, což dává Hessovu matici</sup> 



<!-- Start of picture text -->
HL.S/ D 1 � 1 0 D 1 :<br>�10 0� 2 �00 0� �10 0�<br><!-- End of picture text -->

Podle Sylvestrova kritéria je d<sup>2</sup> L.S/ indefinitní kvadratická forma, což podle poznámky nad příkladem znamená, že zatím nelze rozhodnout. Vyjádřeme tedy z rovnice dg.S/ D h C k D 0 např. proměnnou k, tj. k D �h. Dosadíme-li toto vyjádření do d<sup>2</sup> L.S/, dostáváme novou formu ˚.h/ D �2h<sup>2</sup> (s přihlédnutím k HL.S/ je d<sup>2</sup> L.S/ D 2hk). Platí ˚.h/ < 0 pro každé h ¤ 0, tj. forma ˚ je negativně definitní a v S je ostré vázané lokální maximum, viz obrázek 12.1. 

2. způsob: Příklad lze vyřešit podstatně jednodušeji převodem na lokální extrém funkce jedné proměnné. Z vazebné podmínky vyjádříme jednu z proměnných, např. y D 1 � x a zavedeme novou funkci ' W R ! R vztahem '.x/ D f .x; 1 � x/ (jedná se o stejný obrat, který jsme používali již u vyšetřování limit funkce dvou proměnných nad svazkem přímek). Platí '.x/ D x.1 � x/ D x � x<sup>2</sup> a z rovnice '<sup>0</sup> .x/ D 1 � 2x D 0 dostaneme jediný stacionární bod xs D<sup><u>1</u></sup> 2<sup>. Zřejmě je '00.xs/ D �2 < 0, a proto má funkce 'v bodě xs</sup> ostré lokální maximum. To znamená, že funkce f má v bodě Œxs; ys� D � <u>12</u><sup>;</sup> 2<sup><u>1</u></sup> � (druhou složku dostaneme z vazebné podmínky, tj. ys D 1 � x1 D 2<sup><u>1</u>) ostré vázané maximum.</sup> 



Obrázek 12.1: Ostré vázané lokální maximum funkce f .x; y/ nad přímkou x C y D 1 nastává v bodě � 21<sup>;</sup><sup><u>1</u></sup> 2 � 

Poznámka 12.8. Druhý způsob v předchozím příkladě skutečně vede výrazně rychleji k cíli, je ale potřeba si uvědomit, že jej lze použít pouze v případě, kdy můžeme snadno vyjádřit z vazebných podmínek m-tici proměnných v závislosti na zbývajících. To nemusí být vůbec jednoduché, metoda se tedy uplatňuje spíše v případě funkce dvou proměnných s jednou vazebnou podmínkou. 

Pˇríklad 12.9. Nalezněte globální extrémy funkce f .x; y/ D 3x<sup>2</sup> � y<sup>2</sup> na množině M D fŒx; y� 2 R<sup>2</sup> W x<sup>2</sup> C y<sup>2</sup> � 4g. 

_Řešení._ Předně si uvědomme, že M je kompaktní množina v R<sup>2</sup> (tj. ohraničená a uzavřená), a protože f je na M spojitá, podle věty 5.5 (která je jinou formulací Weierstrassových vět) musí globální maximum i minimum na M existovat. Podle poznámky 10.24 pak globální extrém nastane buď v bodě lokálního extrému, nebo na hranici (v případě kompaktní množiny M � R<sup>n</sup> hranice do této množiny patří). Stačí 

Kapitola 2. Diferenciální poˇcet funkce více promˇenných 

62 

tedy vyšetřit stacionární ležící uvnitř M (jinde lokální extrém nastat nemůže, protože f má na M obě parciální derivace) a stacionární body na hranici @M (zde se jedná o problém vázaných extrémů funkce f vzhledem k hraniční množině). Není přitom ani potřeba zjišťovat, zda lokální (vázaný lokální) extrém ve stacionárním bodě nastává, stačí si poznamenat funkční hodnotu funkce f v takovém bodě a nakonec se podívat, ve kterém bodě je funkční hodnota největší, resp. nejmenší. 

Ze soustavy fx<sup>0D 6xD 0, f</sup> y<sup>0D �2yD 0 dostáváme stacionární bod Œ0; 0�(ten leží uvnitř zadané</sup> množiny), přičemž f .0; 0/ D 0. Podívejme se dále na situaci na hranici. Kružnici x<sup>2</sup> C y<sup>2</sup> D 4 lze vyjádřit parametricky jako x D 2 cos t, y D 2 sin t, t 2 h0; 2�i. Úlohu o vázaném extrému převedeme na úlohu o volném lokálním extrému funkce '.t/ D f .2 cos t; 2 sin t/ D 12 cos<sup>2</sup> t � 4 sin<sup>2</sup> t. Máme '<sup>0</sup> .t/ D �24 cos t sin t � 8 sin t cos t D �32 sin t cos t D �16 sin 2t. Stacionární body tedy obdržíme z rovnice �16 sin 2t D 0, neboli sin 2t D 0. Řešením uvnitř intervalu h0; 2�i jsou body t1 D<sup><u>�</u></sup> 2<sup>, t2D �,</sup> t3 D<sup><u>3�</u></sup> 2<sup>. Tyto hodnoty parametru todpovídají postupně bodům S1D Œ0; 2�, S2D Œ�2; 0�, S3D Œ0; �2�</sup> a krajní body intervalu h0; 2�i pak odpovídají bodu S4 D Œ2; 0�. Odpovídající funkční hodnoty jsou f .0; 2/ D f .0; �2/ D �9, f .2; 0/ D f .�2; 0/ D 12. Na základě úvahy na začátku příkladu tedy lze usoudit, že globální maximum nastává nad osou x v bodech Œ�2; 0� a Œ2; 0� (jeho hodnota je 12) a globální minimum nad osou y v bodech Œ0; �2� a Œ0; 2� (jeho hodnota je �9). Tyto extrémy nejsou ostré. Graf funkce nad kruhem M je na obrázku 12.2. 



Obrázek 12.2: Graf funkce f .x; y/ D 3x<sup>2</sup> � y<sup>2</sup> nad uzavřeným kruhem x<sup>2</sup> C y<sup>2</sup> � 4. Globální maxima jsou ve dvou bodech nad osou x a globální minima ve dvou bodech nad osou y 

#### Pˇríklady k procviˇcení 

12.1. Nalezněte vázané lokální extrémy funkce f .x; y/ D x<sup>2</sup> C2y<sup>2</sup> za podmínky x<sup>2</sup> �2x C2y<sup>2</sup> C4y D 0. 

12.2. Nalezněte největší a nejmenší vzdálenost (v metrice �2) počátku od množiny bodů dané rovnicí 5x<sup>2</sup> � 6xy C 5y<sup>2</sup> � 8 D 0. 

12.3. Určete lokální a globální extrémy funkce f .x; y; z/ D x<sup>2</sup> C y<sup>2</sup> � z<sup>2</sup> na množině M bodů vyhovujících rovnici x<sup>2</sup> C y<sup>2</sup> C z<sup>2</sup> D 1. 

12.4. Určete největší a nejmenší hodnotu funkce f .x; y/ D x � 2y � 3 na trojúhelníku 

M D fŒx; y� 2 R<sup>2</sup> W x � 0; y � 0; x C y � 1g: 

12.5. Mezi všemi pravoúhlými trojúhelníky, mající obsah S, najděte ten, který má nejmenší obvod. 

12.6. Určete tři reálná čísla x; y; z tak, aby jejich součin byl maximální, víte-li, že jejich součet je 12. 

_Výsledky._ 12.1. Ostré vázané lokální minimum v Œ0; 0�, f .0; 0/ D 0, ostré vázané lokální maximum v Œ2; �2�, f .2; �2/ D 12. 12.2. Nejmenší vzdálenost 1 nastane 1 v bodech �˙ ~~p~~ 2=2; � ~~p~~ 2=2� a největší vzdálenost 2 nastane v bodech �˙ ~~p~~ 2; ˙ ~~p~~ 2�. 12.3. globální minimum v Œ0; 0; ˙1�, f .0; 0; ˙1/ D �1, 

12 Vázané extrémy 

63 

globální maximum na kružnici x<sup>2</sup> C y<sup>2</sup> D 1 v rovině z D 0 (funkční hodnota v těchto bodech je 1). 12.4. maxŒx;y�2M f .x; y/ D �2, minŒx;y�2M f .x; y/ D �5. 12.5. Rovnoramenný trojúhelník. 12.6. x D y D z D 4. 

## Kapitola 3 

# Integrální poˇcet funkce více promˇenných 

### 13 Dvojný integrál 

Motivace: Riemannův integrál byl zaveden tak, aby pro kladnou spojitou funkci na ha; bi odpovídal obsahu obrazce ohraničeného grafem funkce, osou x a přímkami x D a, x D b. Dvojný integrál zavedeme analogicky, tj. tak, aby v případě kladné spojité funkce na dvourozměrném intervalu ha; bi �hc; d i odpovídal objemu tělesa ohraničeného grafem funkce a rovinami z D 0; x D a; x D b; y D c a y D d . Vycházíme z funkce ohraničené na dvojrozměrném uzavřeném intervalu I D ha; bi �hc; d i (tj. na uzavřeném obdélníku), kde a; b; c; d 2 R, a < b, c < d . 

Nechť Dx W a D x0 < x1 < ��� < xn D b je dělení intervalu ha; bi a Dy W c D y0 < y1 < ��� < ym D d je dělení intervalu hc; d i. Pak definujeme dělení D D .Dx; Dy / obdélníku I jakožto systém uzavřených obdélníků Iij D hxi �1; xi i �hyj �1; yj i (kde i D 1; 2; : : : ; n, j D 1; 2; : : : ; m) a jejich obsah označme 



<!-- Start of picture text -->
�.Iij / D .xi � xi �1/ � .yj � yj �1/:<br><!-- End of picture text -->

Symbolem _D_ .I/ označíme množinu všech dělení D obdélníku I . Nyní pro každé D 2 _D_ .I/ položme mij WD infff .x; y/ W Œx; y� 2 Iij g a Mij WD supff .x; y/ W Œx; y� 2 Iij g a definujme dolní a horní součet příslušný funkci f a dělení D jako 



<!-- Start of picture text -->
n m n m<br>s.D; f / WD X X mij �.Iij / a S.D; f / WD X X Mij �.Iij /;<br>i D1 j D1 iD1 j D1<br><!-- End of picture text -->

a dolní a horní integrál funkce f na intervalu I jako 

f .x; y/ dxdy WD supfs.D; f / W D 2 _D_ .I/g a f .x; y/ dxdy WD inffS.D; f / W D 2 _D_ .I/g: <u>� I �</u> I 

Definice 13.1 — dvojného Riemannova integrálu na obdélníku. Řekneme, že _funkce_ f _je na intervalu_ I _(riemannovsky) integrovatelná_ , platí-li 



<!-- Start of picture text -->
f .x; y/ dxdy D f .x; y/ dxdy:<br>� I � I<br><!-- End of picture text -->

Tuto společnou hodnotu nazveme _dvojným (Riemannovým) integrálem funkce_ f _na intervalu_ I . 

Poznámka 13.2. a) V souladu s výkladem Riemannova integrálu funkce jedné proměnné, výše uvedený přístup je Darbouxův (originální Riemannova definice pracuje opět s integrálními součty příslušnými k funkci f , dělení D a výběrem reprezentantů � ). 

> b) Protože je dvojný integrál zaveden analogicky jako u funkce jedné proměnné, lze očekávat, že i základní vlastnosti zůstanou zachovány. Zejména platí: jsou-li f; g integrovatelné na obdélníku I , pak 1. cf je integrovatelná na I a platí � I<sup>cf .x; y/ dxdyD c</sup> � I<sup>f .x; y/ dxdy,</sup> 

Kapitola 3. Integrální poˇcet funkce více promˇenných 

66 

2. jf j je integrovatelná na I a platí ˇˇ � I<sup>f .x; y/ dxdy</sup> ˇˇ � � I<sup>jf .x; y/j dxdy,</sup> 3. f Cg je integrovatelná na I a platí � I<sup>Œf .x; y/Cg.x; y/�dxdyD</sup> � f .x; y/ dxdyC � I<sup>g.x; y/ dxdy,</sup> 4. je-li I D I1[I2, kde I1; I2 jsou obdélníky s I1<sup>ı\I</sup> 2<sup>ıD ;, pak</sup> � I<sup>f .x; y/ dxdyD</sup> � I1<sup>f .x; y/ dxdyC</sup> � I2<sup>f .x; y/ dxdy.</sup> 

Pˇríklad 13.3. Přímo z definice lze spočítat, že a) � I<sup>1 dxdyD �.I/ D .b�a/.d �c/, b)</sup> � I<sup>f .x; y/ dxdy,</sup> kde f .x; y/ D �.x/, neexistuje, neboť 



<!-- Start of picture text -->
f .x; y/ dxdy D 0 a f .x; y/ dxdy D 1:<br>� I � I<br><!-- End of picture text -->

■ Vˇeta 13.4 — postaˇcující podmínka pro existenci integrálu na obdélníku. _Je-li funkce_ f W R<sup>2</sup> ! R _spojitá na uzavřeném obdélníku_ I _, pak je na_ I _integrovatelná._ 

_Důkaz._ Uzavřený obdélník I je kompaktní množinou v R<sup>2</sup> , a protože f je podle předpokladu spojitá funkce na I , tak podle věty 5.5 je f .I/ kompaktní množina v R, tj. uzavřený interval v R. Funkce f je tedy na I ohraničená, a tudíž má horní a dolní integrál. Je potřeba ukázat, že se rovnají. 

Podle Heineho–Cantorovy věty (viz věta 5.9) je spojitá funkce na uzavřeném obdélníku stejnoměrně spojitá. To znamená, že vezmeme-li " > 0 libovolné, pak k "=�.I <u>/ existuje ı</u> > 0 takové, že pro libovolné body Œx1; y2�, Œx2; y2� z obdélníku I splňující ~~p~~ .x1 � x2/<sup>2</sup> C .y1 � y2/<sup>2</sup> < ı, platí jf .x1; y1/ � f .x2; y2/j < "=�.I/. 

Buď nyní D D .Dx; Dy / D fIij W i D 1; : : : ; n; j D 1; : : : ; mg nějaké dělení, jehož norma je menší než ı, tj. délka uhlopříčky libovolného obdélníku Iij v dělení je menší než ı. Protože také všechny Iij jsou kompaktní a f je na nich spojitá, nabývá na každém Iij svého (globálního) minima a maxima, tj. existují body Œ�ij<sup>�; ��</sup> ij<sup>�2 Iija Œ�</sup> ij<sup>��; ���</sup> ij<sup>�2 Iijtakové, že</sup> 



<!-- Start of picture text -->
uij WD f .�ij � ; �� ij / � f .x; y/ 8Œx; y� 2 Iij ;<br>Uij WD f .�ij ��; ��� ij / � f .x; y/ 8Œx; y� 2 Iij :<br><!-- End of picture text -->

Zároveň platí 



<!-- Start of picture text -->
"<br>0 � Uij � uij < �.I/ ; protože q .�ij � � � ij ��/2 C .�� ij � ��� ij /2 < ı:<br><!-- End of picture text -->

Odtud máme 



<!-- Start of picture text -->
n m n m n m<br>S.D; f / � s.D; f / D X X Uij �.Iij / � X X uij �.Iij / D X X.Uij � uij /�.Iij /<br>i D1 j D1 iD1 j D1 i D1 j D1<br>n m n m<br>" " "<br>< X X �.I/ �.Iij / D �.I/ X X �.Iij / D �.I/ �.I/ D ":<br>iD1 j D1 iD1 j D1<br><!-- End of picture text -->

Ukázali jsme, že rozdíl horního a dolního součtu lze při vhodném dělení D udělat libovolně malý (menší než "), což je nutnou a postačující podmínkou pro integrovatelnost funkce na obdélníku I (jedná se o analogii věty 20.17 z Matematické analýzy I). Tím je důkaz hotov. 

Praktický výpočet dvojného integrálu nám umožňuje následující tvrzení. 

■ Vˇeta 13.5 — Fubiniova<sup>1</sup> na obdélníku. _Buď_ f W R<sup>2</sup> ! R _funkce integrovatelná na uzavřeném dvojrozměrném intervalu_ I D ha; bi�hc; d i _. Je-li pro každé_ x 2 ha; bi _funkce_ y 7! f .x; y/ _integrovatelná na_ hc; d i _, pak je na_ ha; bi _integrovatelná funkce_ g.x/ D � cd<sup>f .x; y/ dy</sup><sup>_a platí_</sup> 



<!-- Start of picture text -->
f .x; y/ dxdy D f .x; y/ dy dx:<br>� I � ab� � cd �<br><!-- End of picture text -->

1Guido Fubini 1879–1943, Ital 

13 Dvojný integrál 

67 

_Je-li naopak pro každé_ y 2 hc; d i _na_ ha; bi _integrovatelná funkce_ x 7! f .x; y/ _, pak je na_ hc; d i _integrovatelná funkce_ h.y/ D � ab<sup>f .x; y/ dx</sup><sup>_a platí_</sup> 



<!-- Start of picture text -->
f .x; y/ dxdy D f .x; y/ dx dy:<br>� I � cd � � ab �<br><!-- End of picture text -->

_Důkaz._ Pro libovolné dělení D D .Dx; Dy / obdélníku I máme 



<!-- Start of picture text -->
mij � f .x; y/ � Mij 8Œx; y� 2 Iij ; i D 1; 2; : : : ; n; j D 1; 2; : : : ; m<br><!-- End of picture text -->

(mij a Mij mají stejný význam jako v úvodu této kapitoly). Protože dle předpokladu je y 7! f .x; y/ integrovatelná na hc; d i, je integrovatelná i na hyi �1; yi i (monotonie vzhledem k integračnímu oboru, viz věta 21.17 v Matematické analýze I), a tedy musí platit 



<!-- Start of picture text -->
mij .yj � yj �1/ � f .x; y/ dy � Mij .yj � yj �1/ 8x 2 hxi�1; xi i ; 8i 2 f1; 2; : : : ; ng<br>� yjy�j 1<br><!-- End of picture text -->

(viz věta 21.5 v Matematické analýze I). Sečtením přes j D 1; 2; : : : ; m dostaneme 



<!-- Start of picture text -->
m m m<br>X mij .yj � yj �1/ � X f .x; y/ dy � X Mij .yj � yj �1/;<br>j D1 j D1 � yjy�j 1 j D1<br><!-- End of picture text -->

tj. 



<!-- Start of picture text -->
m m<br>X mij .yj � yj �1/ � f .x; y/ dy � X Mij .yj � yj �1/ 8x 2 hxi �1; xi i ; 8i 2 f1; 2; : : : ; ng:<br>j D1 � cd j D1<br><!-- End of picture text -->



<!-- Start of picture text -->
(␆)<br><!-- End of picture text -->

kde na prostřední člen jsme aplikovali větu 21.15 z Matematické analýzy I (aditivitu vzhledem k integračnímu oboru). Označme 



<!-- Start of picture text -->
g.x/ WD f .x; y/ dy<br>� cd<br><!-- End of picture text -->

a ukažme, že tato funkce je integrovatelná na ha; bi, tj. že <u>� ab</u><sup>g.x/ dxD</sup> � ab<sup>g.x/ dx. Předně si všimněme,</sup> že g je ohraničená na ha; bi. To plyne ihned z faktu, že f je integrovatelná na I , tj. musí zde být ohraničená, tj. platí 



<!-- Start of picture text -->
inf dy � f .x; y/ dy � sup f .x; y/ dy 8x 2 ha; bi<br>„Œx;y�2I f .x; y/ ƒ‚ � cd … � „cd ƒ‚ … Œx;y�„ 2I ƒ‚ � cd …<br>konst : g.x/ KONST :<br><!-- End of picture text -->

Z ohraničenosti g pak plyne, že výše uvedený spodní a horní integrál na ha; bi existují. Z nerovností (␆) dále plyne, že 



<!-- Start of picture text -->
n n<br>� ab g.x/ dx D iXD1 � xxi �i 1 g.x/ dx � iXD1 � xxi �i 1 �jX D m 1 Mij .yj � yj �1/�dx<br>n m n m<br>D X X Mij .yj � yj �1/ dx D X X Mij .xi � xi �1/.yj � yj �1/<br>i D1 j D1 � xxi�i 1 i D1 j D1<br>n m<br>D<br>X X Mij �.Iij / D S.D; f /<br>iD1 j D1<br><!-- End of picture text -->

(první rovnost plyne opět z věty 21.15 v Matematické analýze I). Analogicky bychom ukázali, že 



<!-- Start of picture text -->
s.D; f / � g.x/ dx:<br>� ab<br><!-- End of picture text -->

Kapitola 3. Integrální poˇcet funkce více promˇenných 

68 

Protože poslední dvě nerovnosti platí pro libovolné dělení D 2 _D_ .I/, dostáváme odtud (spolu s vlastností suprema a infima) 



<!-- Start of picture text -->
f .x; y/ dxdy � g.x/ dx � g.x/ dx � f .x; y/ dxdy:<br>� I � ab � ab � I<br><!-- End of picture text -->

Protože podle předpokladu je f integrovatelná, v posledním vztahu nastanou rovnosti, a tedy g je integrovatelná na ha; bi přičemž 



<!-- Start of picture text -->
f .x; y/ dxdy D g.x/ dx:<br>� I � ab<br><!-- End of picture text -->

Pro funkci h by se ukázalo analogicky. 

Poznámka 13.6. a) Za předpokladů věty tedy nezáleží na pořadí integrace, v případě spojité funkce na I jsou tyto předpoklady splněny automaticky. Může se však stát, že pořadí není rovnocenné z hlediska obtížnosti integrace, viz následující příklad. 

b) Je-li f .x; y/ D g.x/h.y/, kde g; h jsou spojité, pak lze psát 



<!-- Start of picture text -->
f .x; y/ dxdy D g.x/ dx h.y/ dy:<br>� I � ab � cd<br><!-- End of picture text -->

Pˇríklad 13.7. Vypočítejte � I<sup>xy dxdy, kde ID h0; 1i �h1; 2i.</sup> 

_Řešení._ Integrovaná funkce je na I spojitá, a tedy podle Fubiniovy věty integrovatelná, přičemž 



<!-- Start of picture text -->
x 2 � x<br>x y dxdy D x y dy dx D dx D dx:<br>� I � 01� � 12 � � 01 � lnxy x �21 � 01 ln x<br><!-- End of picture text -->

Problém nyní je, že poslední integrál neumíme vyčíslit, neboť nelze určit primitivní k funkci integrované. Zkusme tedy opačný postup, kdy nejprve budeme integrovat vzhledem k y: 



<!-- Start of picture text -->
x yC1 1 � 0<br>x y dxdy D x y dx dy D dy D<br>� I � 12� � 01 � � 12 " y C 1 #10 � 12 y C 1 dy<br>D<br>�ln.y C 1/�21 D ln 3 � ln 2 D ln 3 2 :<br><!-- End of picture text -->

Definice 13.8 — normální množiny. Nechť '1; '2 jsou spojité funkce na ha; bi takové, že '1.x/ < '2.x/ pro 8x 2 .a; b/. Množinu 



<!-- Start of picture text -->
M1 WD fŒx; y� 2 R 2 W a � x � b; '1.x/ � y � '2.x/g<br><!-- End of picture text -->

nazveme _normální množinou vzhledem k ose_ x. 

Podobně, jsou-li 1; 2 spojité funkce na hc; d i takové, že 1.y/ < 2.y/ pro 8y 2 .c; d/, pak množinu 



<!-- Start of picture text -->
M2 WD fŒx; y� 2 R 2 W c � y � d; 1.y/ � x � 2.y/g<br><!-- End of picture text -->

nazveme _normální množinou vzhledem k ose_ y. 

Množinu M nazveme _normální_ , je-li normální k alespoň jedné z os x; y. 

Definice 13.9 — dvojného integrálu na normální množinˇe. Nechť M je normální množina, např. vzhledem k ose x, a f W R<sup>2</sup> ! R je funkce definovaná a omezená na M . Zvolme c; d 2 R tak, že c � minf'1.x/ W x 2 ha; big, d � maxf'2.x/ W x 2 ha; big. Rozšiřme definiční obor funkce f na obdélník I D ha; bi �hc; d i tak, že položíme f .x; y/ D 0 pro 8Œx; y� 2 I n M . Řekneme, že funkce f 

13 Dvojný integrál 

69 

je _(riemannovsky) integrovatelná_ na M , jestliže je integrovatelná na I . V tomto případě klademe 



<!-- Start of picture text -->
f .x; y/ dxdy D f .x; y/ dxdy:<br>� M � I<br><!-- End of picture text -->

Poznámka 13.10. a) Uvedená definice zřejmě nezávisí na volbě konstant c; d (změnou těchto čísel se pouze zmenší nebo zvětší obdélník přes který integrujeme, ale pouze tam, kde je f nulová). Lze tedy vždy volit c D minf'1.x/ W x 2 ha; big, d D maxf'2.x/ W x 2 ha; big. 

> ■ Vˇeta 13.11 — postaˇcující podmínka pro existenci integrálu na normální množinˇe. _Nechť_ f W R<sup>2</sup> ! R _je spojitá funkce na normální množině_ M _. Pak je na_ M _integrovatelná._ 

_Idea důkazu._ Základní myšlenka je stejná jako ve větě 13.4 (využíváme vlastnosti, kdy funkce spojitá na kompaktní množině je zároveň stejnoměrně spojitá), důkaz je pouze o něco technicky náročnější. 

■ Vˇeta 13.12 — Fubiniova na normální množinˇe vzhledem k ose **x** . _Nechť_ M _je normální množina vzhledem k ose_ x _a nechť funkce_ f W R<sup>2</sup> ! R _je integrovatelná na_ M _. Je-li pro každé_ x 2 ha; bi _integrovatelná funkce_ y 7! f .x; y/ _na_ h'1.x/; '2.x/i _, pak platí_ 



<!-- Start of picture text -->
f .x; y/ dxdy D f .x; y/ dy dx:<br>� M � ab� � ''12.x/.x/ �<br><!-- End of picture text -->

_Důkaz._ Nechť c; d jsou takové, že c � minf'.x/ W x 2 ha; big, d � maxf .x/ W x 2 ha; big a I D ha; bi �hc; d i. Podle definice a Fubiniovy věty na obdélníku máme 



<!-- Start of picture text -->
f .x; y/ dxdy D f .x; y/ dxdy D f .x; y/ dy dx:<br>� M � I � ab� � cd �<br>Pro libovolné x 2 ha; bi je však hc; d i D hc; '1.x/i [ h'1.x/; '2.x/i [ h'2.x/; d i a tedy<br>f .x; y/ dy D f .x; y/ dy C f .x; y/ dy C f .x; y/ dy D f .x; y/ dy;<br>� cd � c'1.x/ � ''12.x/.x/ � 'd2.x/ � ''12.x/.x/<br><!-- End of picture text -->

protože pro y 2 hc; '1.x// i pro y 2 .'2.x/; d i je f .x; y/ D 0. Dosazením vyjde tvrzení. 

Poznámka 13.13. Pro normální množinu vzhledem k ose y by se vzorec modifikoval 



<!-- Start of picture text -->
f .x; y/ dxdy D f .x; y/ dx dy:<br>� M � cd � � 12.y/.y/ �<br>x 2<br>Pˇríklad 13.14. Vypočtěte<br>� M y 2 dxdy, kde M je vymezena křivkami y D 4x, x D 2, y D x 1 .<br><!-- End of picture text -->

_Řešení._ Množina M je normální množinou vzhledem k oběma osám, její vyjádření vzhledem k ose x je <u>12</u><sup>�x�2,</sup> x<sup><u>1</u>�y�4x. Integrand je spojitou funkcí na M, je zde tedy integrovatelný a podle Fubiniovy</sup> věty pak platí 



<!-- Start of picture text -->
x 2 x 2 �x 2<br>dx D dx<br>� M y 2 dxdy D � 1=22 � � 1=x4x y 2 dy � � 1=22 " y #4x1=x<br>D � x dx D � x2 D � 1<br>� 1=22 � 4 C x3� " 8 C x 4 4 #21=2 2 C 4 C 32 1 � 64 1 D 225 64 :<br><!-- End of picture text -->

Pˇríklad 13.15. Určete hodnotu integrálu xy dxdy, M je trojúhelník o vrcholech Œ0; 0�; Œ1; 1�; Œ2; 0�. � M 

Kapitola 3. Integrální poˇcet funkce více promˇenných 

70 

_Řešení._ Množina M je opět normální množinou vzhledem k oběma osám, nyní je ale výhodnější ji vyjádřit vzhledem k ose y, což vede na nerovnosti 0 � y � 1, y � x � 2 � y. Podle Fubiniovy věty tedy platí 



<!-- Start of picture text -->
� M xy dxdy D � 01� � y2�y xy dx�dy D 2 1 � 01 hx 2 yiy2�y dy D 1 2 � 01�.2 � y/ 2 y � y 3� dy<br>D .2y � 2y 2 / dy D y 2 � 2y3 D 1 � 2<br>� 01 3 3 D 1 3 :<br>" #10<br><!-- End of picture text -->

Poznámka 13.16. Definici dvojného integrálu je dále možné rozšířit na případ tzv. regulární množiny, což je množina, kterou lze rozložit na konečný počet normálních množin, tj. platí M D<sup>Sm</sup> i D1<sup>Mi,</sup> Mi<sup>ı\M</sup> j<sup>ı</sup> D ;, 8i; j , i ¤ j , kde Mi jsou normální. Příkladem regulární množiny je množina fŒx; y� 2 R<sup>2</sup> W 1 � x<sup>2</sup> C y<sup>2</sup> � 4g. Potom klademe 



<!-- Start of picture text -->
m<br>f .x; y/ dxdy WD X f .x; y/ dxdy:<br>� M i D1 � Mi<br><!-- End of picture text -->

#### Pˇríklady k procviˇcení 

13.1. Vypočítejte následující integrály: 



<!-- Start of picture text -->
x<br>a) M D h0; 1i �h1; 2i I<br>� M y dxdy;<br>b) 1 � x2 C y2 dxdy; M D h0; 1i 2 :<br>� M 2<br>!<br><!-- End of picture text -->

13.2. Vypočítejte následující integrály přes normální množiny: 



<!-- Start of picture text -->
a) x 2 dxdy; M je vymezena přímkami y D x; y D x � 1; y D 0; y D 2I<br>� M<br>y<br>b) M je vymezena křivkami y 2 D 2x; y D x:<br>� M x 2 C y 2 dxdy;<br><!-- End of picture text -->

_Výsledky._ 13.1. a)<sup><u>1</u></sup> 2<sup>ln 2; b)2=3. 13.2. a)16=3; b) ln 2.</sup> 

### 14 Alternativní pˇrístup k definování dvojného integrálu 

Nejprve se vybuduje teorie míry na vhodných podmnožinách množiny R<sup>2</sup> . Pojem míry zobecňuje pojem obsahu rovinného obrazce. Označíme-li �.A/ míru množiny A � R<sup>2</sup> , pak � lze chápat jako zobrazení z množiny podmnožin R<sup>2</sup> do R<sup>C</sup> 0<sup>. Míra by měla splňovat následující přirozené podmínky:</sup> 

- (i) Je-li A � B, pak �.A/ � �.B/ (z této vlastnosti také ihned plyne, že totožné množiny mají stejnou míru). 

(ii) Je-li A \ B D ;, pak �.A [ B/ D �.A/ C �.B/. 

Obecnou míru v prostoru R<sup>2</sup> (resp. v R<sup>n</sup> ) jako první zkonstruoval Camille Jordan (1838–1922, Francouz). Nechť n 2 N0, j; k 2 Z. _Čtverec řádu_ n definujeme jako množinu 



<!-- Start of picture text -->
Qj;k n WD �Œx; y� 2 R 2 W 2 jn � x � j 2 Cn 1 ; 2 kn � y � k C 2 n 1 � :<br><!-- End of picture text -->

Není-li podstatné umístění čtverce, píšeme stručně Q<sup>n</sup> . Množinu všech čtverců řádu n nazveme _síť řádu_ n a síť řádu 0 nazveme _základní síť_ . Reálné číslo 



<!-- Start of picture text -->
�.Qj;k n / WD � 21 n �2 D 4 1n<br><!-- End of picture text -->

14 Alternativní pˇrístup k definování dvojného integrálu 

71 

nazveme _mírou čtverce řádu_ n. Dále klademe �.;/ D 0. Konečné sjednocení čtverců řádu n nazveme _elementární množinou řádu_ n. Je-li M D<sup>S</sup> j;k2 _I_<sup>Q</sup> j;k<sup>n(</sup><sup>_I_značí nějakou množinu indexů j; k) elementární</sup> množina řádu n, pak klademe 



<!-- Start of picture text -->
�.M/ WD � 0 Qj;k n 1 X � �Qj;k n � :<br>@j;k [ 2 I A D j;k2 I<br><!-- End of picture text -->

Nechť A � R<sup>2</sup> je libovolná ohraničená množina. _Jádro řádu_ n _množiny_ A definujeme jako největší (vzhledem k množinové inkluzi) elementární množinu, která je obsažena ve vnitřku A, budeme značit Vn.A/. Platí tedy 



<!-- Start of picture text -->
Vn.A/ D [˚Qj;k n W Q j;k n � Aı� :<br>j;k<br><!-- End of picture text -->

_Obal řádu_ n _množiny_ A (budeme značit Wn.A/) definujeme jako nejmenší (vzhledem k množinové inkluzi) elementární množinu řádu n, jejíž vnitřek obsahuje uzávěr množiny A, tj. 



<!-- Start of picture text -->
Wn.A/ D [fQj;k n W A \ Qj;k n ¤ ;g;<br>j;k<br><!-- End of picture text -->

viz obrázek 14.1. Neexistuje-li čtverec řádu n, který by byl částí A<sup>ı</sup> , klademe Vn.A/ D ;. Je-li A D ;, klademe Wn.A/ D ;. 



<!-- Start of picture text -->
y<br>Wn ( A )<br>A<br>Vn ( A )<br>x<br><!-- End of picture text -->

Obrázek 14.1: Jádro řádu n (tmavší šedá) a obal řádu n (světlejší šedá) množiny A (čtverce jádra jsou zároveň čtverci obalu) 

Vlastnosti: 



<!-- Start of picture text -->
(i) Vn � A � Wn,<br><!-- End of picture text -->

(ii) �.Wn.@A// D �.Wn.A// � �.Vn.A//, 

(iii) �.Vn.A// � �.VnC1.A//, �.Wn.A// � �.WnC1.A// pro 8n 2 N0, (iv) posloupnosti měr f�.Vn.A//g<sup>1</sup> nD0<sup>a f�.Wn.A//g1</sup> nD0<sup>mají vlastní limitu.</sup> Poslední vlastnost nás opravňuje k následující definici. 

Definice 14.1 — vnˇejší a vnitˇrní Jordanovy míry. Nechť A � R<sup>2</sup> je ohraničená množina. Číslo 



<!-- Start of picture text -->
��.A/ WD nlim!1 �.Vn.A//<br> A a číslo a číslo<br>� � .A/ WD nlim!1 �.Wn.A//<br><!-- End of picture text -->

se nazývá _vnitřní Jordanova míra množiny_ A a číslo a číslo 

se nazývá _vnější Jordanova míra množiny_ A. Jestliže ��.A/ D �<sup>�</sup> .A/, pak řekneme, že _množina_ A _je (jordanovsky) měřitelná_ a číslo �.A/ D ��.A/ D �<sup>�</sup> .A/ se nazývá _(Jordanova) míra množiny_ A. 

Kapitola 3. Integrální poˇcet funkce více promˇenných 

72 

Poznamenejme, že vždy platí 0 � ��.A/ � �<sup>�</sup> .A/. 

Pˇríklad 14.2. Zjistěte, zda je měřitelná množina A D fŒx; y� 2 Q<sup>2</sup> W 0 � x � 1; 0 � y � 1g. 

_Řešení._ Platí A<sup>ı</sup> D ; a tedy také Vn.A/ D ; pro libovolné n. To znamená, že ��.A/ D 0. Dále A D h0; 1i �h0; 1i D Q0;0<sup>0a tedy</sup> 



<!-- Start of picture text -->
�.W0.A// D 1 C 8 � 1 D 1 C 2 � 4<br>2 0 ;<br>�.W1.A// D 1 C 12 � 4 1 D 1 C 3 2  �24 ;<br>�.W2.A// D 1 C 20 � 16 1 D 1 C 5 2  �44 ;<br>:::<br><!-- End of picture text -->



<!-- Start of picture text -->
1<br>�.Wn.A// D 1 C .4 � 2 n C 4/ � D 1 C .2n C 1/4 D 1 C 4 :<br>� 21 n �2 2 2n � 21 n C 2 2n �<br><!-- End of picture text -->

Tedy �<sup>�</sup> .A/ D nlim!1�1 C 4� 21<sup><u>n</u>C</sup> 2<sup>2n</sup> <u>1</u> �� D 1. Protože 0 D ��.A/ < �<sup>�</sup> .A/ D 1, není A jordanovsky měřitelná. 

Vlastnosti: 

1. Je-li �<sup>�</sup> .A/ D 0, pak A je měřitelná a platí �.A/ D 0. 

2. Jsou-li A; B � R<sup>2</sup> ohraničené množiny, pak platí: 

   - (i) je-li A � B, pak ��.A/ � ��.B/, �<sup>�</sup> .A/ � �<sup>�</sup> .B/, 

   - (ii) �<sup>�</sup> .A [ B/ � �<sup>�</sup> .A/ C �<sup>�</sup> .B/, 

   - (iii) je-li A \ B D ;, pak ��.A/ C ��.B/ � ��.A [ B/. 

3. Jsou-li A; B � R<sup>2</sup> měřitelné množiny, pak platí: 

   - (i) Je-li A � B, pak �.A/ � �.B/, 

   - (ii) Je-li A \ B D ;, pak �.A/ C �.B/ D �.A [ B/. 

   - Jordanova míra tedy splňuje motivační vlastnosti z úvodu odstavce. 

4. Každá konečná množina A � R<sup>2</sup> je měřitelná a platí �.A/ D 0. Dále mají míru nula křivky tvořené grafy spojitých funkcí y D '.x/ nebo x D .y/ na uzavřených intervalech nebo obecněji (definice uvedeme později) tzv. jednoduché hladké (rovinné) křivky jako je např. kružnice nebo její část či tzv. jednoduché po částech hladké (rovinné) křivky jako je křivka složená z hranice @I obdélníka I , která má čtyři hladké části, jimiž jsou strany obdélníka. Obecně můžeme uvažovat i množiny tvořené konečně mnoha křivkami v R<sup>2</sup> (tj. rovinnými) všech zmíněných typů. 

5. Ohraničená množina A � R<sup>2</sup> je měřitelná () �.@A/ D 0. Vzhledem k předchozímu bodu jsou měřitelné všechny normální množiny (protože hranice má míru nula, vnitřek takové množiny má stejnou míru jako celá množina). Speciálně, obdélník I D ha; bi �hc; d i je měřitelná množina a má míru �.I/ D .b � a/.d � c/. 

6. Jsou-li množiny A; B měřitelné, pak také množiny A \ B, A [ B, A n B jsou měřitelné. Odtud plyne, že regulární množiny jsou měřitelné. 

Nyní můžeme přistoupit k (alternativní) definici Riemannova integrálu na měřitelné množině. Množinu 



<!-- Start of picture text -->
C n D Cj;k n WD �Œx; y� 2 R 2 W 2 jn � x < j 2 Cn 1 ; 2 kn � y < k C 2 n 1 � ; n 2 N0; j; k 2 Z<br><!-- End of picture text -->

nazveme čtvercovou množinou řádu n (od čtverce řádu n se liší tím, že není uzavřená). Čtvercové množiny pokrývají celý prostor R<sup>2</sup> a jsou po dvou disjunktní, tj. každý bod Œx; y� 2 R<sup>2</sup> je prvkem právě jedné z nich. Každá čtvercová množina řádu n je měřitelná a její míra je �.C<sup>n</sup> / D 41<sup><u>n</u></sup> 

Buď M � R<sup>2</sup> měřitelná množina a buďte C1<sup>n; C</sup> 2<sup>n; : : : ; C n</sup> m<sup>všechny čtvercové množiny řádu n takové,</sup> že P1<sup>nWDC</sup> 1<sup>n\ M¤;; : : : ; P n</sup> m<sup>WDC</sup> m<sup>n\ M¤;. Systém množin</sup><sup>_P_nWDfP</sup> 1<sup>n; : : : ; P n</sup> m<sup>g nazveme</sup> 

14 Alternativní pˇrístup k definování dvojného integrálu 

73 

_pokrytím řádu_ n _množiny_ M . Každá z množin Pi<sup>nje měřitelná, protože je průnikem dvou měřitelných</sup> množin. Míra množiny M je pak rovna 



<!-- Start of picture text -->
m<br>�.M/ D X �.Pi n/:<br>i D1<br><!-- End of picture text -->

Dále, nechť f je funkce ohraničená na M . Pro pokrytí _P_ n množiny M položme 

hi WD infff .x; y/ W Œx; y� 2 Pi<sup>ng;</sup> Hi WD supff .x; y/ W Œx; y� 2 Pi<sup>ng:</sup> 

Pak čísla 



<!-- Start of picture text -->
m m<br>sn.M; f / WD X hi �.Pi n/ a Sn.M; f / WD X Hi �.Pi n/<br>i D1 i D1<br><!-- End of picture text -->

nazveme _dolní a horní součet řádu_ n _příslušný množině_ M _a funkci_ f . Lze ukázat, že posloupnost fsn.M; f /g<sup>1</sup> nD1<sup>je neklesající a posloupnost fSn.M; f /g1</sup> nD1<sup>je nerostoucí, přičemž obě jsou ohraničené.</sup> To nás (spolu s větou o monotónních posloupnostech) opravňuje k následující definici. 

Definice 14.3 — dvojného (Riemannova) integrálu na mˇeˇritelné množinˇe. Nechť M � R<sup>2</sup> je měřitelná množina a f W R<sup>2</sup> ! R je ohraničená funkce na M . Definujme _dolní a horní integrál z funkce_ f _přes množinu_ M jako 



<!-- Start of picture text -->
� M f .x; y/ dxdy WD nlim!1 sn.M; f / a � M f .x; y/ dxdy WD nlim!1 Sn.M; f /:<br>Je-li<br>f .x; y/ dxdy D f .x; y/ dxdy;<br>� M � M<br><!-- End of picture text -->

řekneme, že _funkce_ f _je na množině_ M _(riemannovsky) integrovatelná_ a tuto společnou hodnotu nazveme _dvojným (Riemannovým) integrálem z funkce_ f _přes množinu_ M . 

Poznámka 14.4. Je-li M uzavřený obdélník, resp. normální množina, pak definice 14.3 je ekvivalentní definici 13.1, resp. definici 13.9, tj. je-li funkce integrovatelná podle jedné definice, je integrovatelná i podle druhé a naopak, přičemž hodnoty integrálů jsou stejné. 

Vlastnosti: 

1. Jsou-li f; g integrovatelné na měřitelné množině M a ˛; ˇ 2 R, pak ˛f C ˇg je integrovatelná na M a platí 



<!-- Start of picture text -->
�˛f .x; y/ C ˇg.x; y/� dxdy D ˛ f .x; y/ dxdy C ˇ g.x; y/ dxdy:<br>� M � M � M<br><!-- End of picture text -->

2. Jsou-li f; g integrovatelné na měřitelné množině M a f .x; y/ � g.x; y/ 8Œx; y� 2 M , pak 



<!-- Start of picture text -->
f .x; y/ dxdy � g.x; y/ dxdy:<br>� M � M<br><!-- End of picture text -->

3. Je-li f integrovatelná na měřitelné množině M , pak je i jf j integrovatelná na M a platí 



<!-- Start of picture text -->
f .x; y/ dxdy jf .x; y/j dxdy:<br>ˇˇˇˇ � M ˇˇˇˇ � � M<br><!-- End of picture text -->

4. Jsou-li f; g integrovatelné na měřitelné množině M takové, že ˛ � f .x; y/ � ˇ, 0 � g.x; y/ 8Œx; y� 2 M , pak existuje konstanta � (˛ � � � ˇ) taková, že 



<!-- Start of picture text -->
f .x; y/g.x; y/ dxdy D � g.x; y/ dxdy (integrální věta o střední hodnotě).<br>� M � M<br><!-- End of picture text -->

Kapitola 3. Integrální poˇcet funkce více promˇenných 

74 

5. Je-li f integrovatelná na měřitelné množině M , pak je integrovatelná na každé měřitelné podmnožině A � M . 

6. Jsou-li M1; M2 dvě disjunktní měřitelné množiny, na kterých je f integrovatelná, pak je integrovatelná také na M1 [ M2 a platí 



<!-- Start of picture text -->
f .x; y/ dxdy D f .x; y/ dxdy C f .x; y/ dxdy:<br>� M1[M2 � M1 � M2<br><!-- End of picture text -->

7. Je-li f ohraničená na množině M míry nula, pak je f na M integrovatelná a platí 



<!-- Start of picture text -->
f .x; y/ dxdy D 0:<br>� M<br><!-- End of picture text -->

8. Jsou-li M1; M2 měřitelné množiny takové, že jejich průnik je měřitelný a platí �.M1 \ M2/ D 0 a je-li f integrovatelná na M1 i M2, pak je integrovatelná také na M1 [ M2 a platí 

9. Platí 



<!-- Start of picture text -->
f .x; y/ dxdy D f .x; y/ dxdy C f .x; y/ dxdy:<br>� M1[M2 � M1 � M2<br>dxdy D �.M/ pro libovolnou měřitelnou množinu M:<br>� M<br><!-- End of picture text -->

Definice 14.5 — vlastnosti „skoro všude“. Řekneme, že funkce f W R<sup>2</sup> ! R definovaná na nějaké množině A má _skoro všude vlastnost V_ , jestliže existuje podmnožina B � A taková, že �.B/ D 0 a f má vlastnost _V_ ve všech bodech množiny A n B. 

■ Vˇeta 14.6. _Je-li funkce_ f W R<sup>2</sup> ! R _integrovatelná na měřitelné množině_ M _a funkce_ g W R<sup>2</sup> ! R _je ohraničená na_ M _, přičemž skoro všude na_ M _platí_ f D g _. Pak funkce_ g _je integrovatelná na_ M _a platí_ 



<!-- Start of picture text -->
g.x; y/ dxdy D f .x; y/ dxdy:<br>� M � M<br><!-- End of picture text -->

Poznámka 14.7. Jinými slovy, změníme-li u integrovatelné funkce hodnoty na množině míry nula, tak hodnota integrálu se nezmění. Vzhledem k této vlastnosti pak taková funkce na množině míry nula nemusí být vůbec definována. 

■ Vˇeta 14.8 — postaˇcující podmínka pro integrovatelnost na mˇeˇritelné množinˇe. _Je-li funkce_ f W R<sup>2</sup> ! R _ohraničená na měřitelné množině_ M _a skoro všude na_ M _spojitá, pak je_ f _na_ M _integrovatelná._ 

#### Pˇríklady k procviˇcení 

14.1. Pomocí definice určete Jordanovu míru množiny A D fŒx; y� 2 R<sup>2</sup> W 0 � x � 1; y D xg (tj. úsečky spojující počátek s bodem Œ1; 1�). 

_Výsledky._ 14.1. 0. 

### 15 Trojný integrál 

V případě trojného integrálu je možné postupovat analogicky jako v předchozích dvou kapitolách. 1. Začali bychom s definicí trojného integrálu ohraničené funkce f W R<sup>3</sup> ! R na uzavřeném kvádru 

I D ha1; b1i �ha2; b2i �ha3; b3i : 

Ten „rozřežeme“ na systém menších kvádrů Iijk, na každém kvádru vezmeme infimum a supremum funkce f a definujeme dolní a horní součet příslušný funkci f a dělení D. Supremum dolních součtů a infimum horních součtů přes všechna možná dělení kvádru bychom nazvali _dolním_ a _horním integrálem na kvádru_ I ; pokud tyto dvě hodnoty jsou stejné, tak řekneme, že f _je (riemannovsky) integrovatelná na kvádru_ I a společnou hodnotu nazveme _trojným (Riemannovým) integrálem funkce_ u _na kvádru_ I . 

15 Trojný integrál 

75 

2. Nejjednodušší postačující podmínkou pro integrovatelnost funkce na I je její spojitost na I . 

3. Fubiniova věta potom říká, že je-li f integrovatelná na I a pro všechna Œx; y� 2 Ixy D ha1; b1i � ha2; b2i je integrovatelná funkce z 7! f .x; y; z/ na ha3; b3i, pak platí 



<!-- Start of picture text -->
f .x; y; z/ dxdydz D f .x; y; z/ dz dxdy;<br>� I � Ixy � � ab33 �<br><!-- End of picture text -->

analogicky pro integrovatelnost funkcí y 7! f .x; y; z/ a z 7! f .x; y; z/. Speciálně, je-li f spojitá na I , pak platí 



<!-- Start of picture text -->
f .x; y; z/ dxdydz D f .x; y; z/ dz dy dx<br>� I � ab11 � � ab22 � � ab33 � �<br>D f .x; y; z/ dy dz dx D ���D f .x; y; z/ dx dy dz:<br>� ab11 � � ab33 � � ab22 � � � ab33 � � ab22 � � ab11 � �<br> f .x; y; z/ D f1.x/f2.y/f3.z/, pak lze psát D f1.x/f2.y/f3.z/, pak lze psát f1.x/f2.y/f3.z/, pak lze psát1.x/f2.y/f3.z/, pak lze psát.x/f2.y/f3.z/, pak lze psát2.y/f3.z/, pak lze psát.y/f3.z/, pak lze psát3.z/, pak lze psát.z/, pak lze psát, pak lze psát<br>f .x; y; z/ dxdydz D f1.x/ dx � f2.y/ dy � f3.z/ dz:<br>� I � ab11 � ab22 � ab33<br><!-- End of picture text -->

Je-li navíc f .x; y; z/ D f1.x/f2.y/f3.z/, pak lze psát D f1.x/f2.y/f3.z/, pak lze psát f1.x/f2.y/f3.z/, pak lze psát1.x/f2.y/f3.z/, pak lze psát.x/f2.y/f3.z/, pak lze psát2.y/f3.z/, pak lze psát.y/f3.z/, pak lze psát3.z/, pak lze psát.z/, pak lze psát, pak lze psát 

4. Dále bychom rozšířili pojem trojného integrálu na normální množiny. Buď Mxy normální množina v R<sup>2</sup> a 1, 2 spojité funkce na Mxy takové, že 1.x; y/ < 2.x; y/ 8Œx; y� 2 Mxy<sup>ı.</sup><sup>_Normální množinou_</sup> _vzhledem k rovině_ xy nazveme množinu M WD fŒx; y; z� 2 R<sup>3</sup> W Œx; y� 2 Mxy a 1.x; y/ � z � 2.x; y/g. Analogicky bychom definovali normální množinu vzhledem k rovinám xz a yz. Množinu 

M � R<sup>3</sup> nazveme _normální_ , je-li normální k alespoň jedné ze souřadných rovin xy, xz, yz. Trojný integrál na normální množině pak definujeme tak, že tuto normální množinu „vnoříme“ do nějakého uzavřeného kvádru I a funkci f na I mimo množinu M dodefinujeme nulou. Řekneme potom, že funkce f je integrovatelná na normální množině M , je-li dodefinovaná funkce integrovatelná na I . 

5. Buď M normální např. vzhledem k souřadné rovině xy. Potom se vzorec z Fubiniovy věty modifikuje 



<!-- Start of picture text -->
f .x; y; z/ dxdydz D f .x; y; z/ dz dxdy:<br>� M � Mxy � � 12.x;y/.x;y/ �<br><!-- End of picture text -->

Pojem trojného integrálu by dále bylo možno rozšířit na případ konečného sjednocení normálních množin (s disjunktními průniky). 

6. Konečně, alternativní přístup k definování trojného integrálu je možné založit na pojmu Jordanovy míry v R<sup>3</sup> . V příslušných definicích by nyní namísto čtverců vystupovaly krychle. Zjednodušeně lze říci, že v případě „rozumných“ těles Jordanova míra odpovídá objemu tělesa, přičemž hranice tělesa má nulovou míru. 

7. Zejména platí analogie věty 14.8 – je-li f ohraničená na měřitelné množině M � R<sup>3</sup> a spojitá skoro všude na M , pak je zde integrovatelná. 

Pˇríklad 15.1. Určete hodnotu integrálu .x C 2y � 3z/ dxdydz, kde M D h1; 3i �h�1; 1i �h0; 2i. � M 

_Řešení._ Funkce je spojitá na daném kvádru M a tedy integrovatelná. Podle Fubiniovy věty pak platí 



<!-- Start of picture text -->
.x C 2y � 3z/ dxdydz D .x C 2y � 3z/ dz dy dx<br>� M � 13� � �11� � 02 � �<br>D xz C 2yz � 3 dy dx D .2x C 4y � 6/ dy dx<br>� 13� � �11 � 2 z2 �20 � � 13� � �11 �<br>D<br>2xy C 2y 2 � 6y .2x C 2 � 6 C 2x � 2 � 6/ dx D .4x � 12/ dx<br>� 13h i1�1 dx D � 13 � 13<br>D h2x 2 � 12xi31 D �8:<br><!-- End of picture text -->

Kapitola 3. Integrální poˇcet funkce více promˇenných 

76 

Pˇríklad 15.2. Určete hodnotu integrálu y cos.x Cz/ dxdydz, kde M je množina vymezená plochami � M y D<sup>~~p~~</sup> x, y D 0, z D 0, x C z D �=2. 

_Řešení._ Funkce f .x; y; z/ D y cos.x C z/ je spojitá v celém prostoru R<sup>3</sup> , a tedy i na zadané množině M , což znamená, že je zde integrovatelná. Vyjádřeme M jako normální množinu vzhledem k rovině xy, tj. 



<!-- Start of picture text -->
0 � x � � (body);<br>2<br>0 � y � p x; (křivky);<br>0 � z � � 2 � x (plochy):<br><!-- End of picture text -->

Podle Fubiniovy věty pak máme 



<!-- Start of picture text -->
x<br>y cos.x C z/ dxdydz D y cos.x C z/ dz dy dx<br>� M � 0�=2� � 0 p � � 0�=2�x � �<br>x x<br>D � 0�=2� � 0 p y�sin.x C z/��=20 �xdy� dy� dx D � 0�=2� � 0 p y�sin � 2 � sin x � dy� dx<br>y 2 x<br>D sin � dx D 1 x.1 � sin x/ dx<br>� 0�=2 2 � 2 � sin x 2 � 0�=2<br>" � # p 0<br>D ˇˇˇˇ uu 0  DD x 1 vv 0 DD x 1 C � cossin x x ˇˇˇˇ D 21 �x 2 C x cos x��=20 � 1 2 � 0�=2.x C cos x/ dx<br>D � 2 x 2 D � 2 � 2 D � 2 D:  0; 11685:<br>8 � 2 1 2 C sin x 8 � 2 1 8 C 1 16 � 2 1<br>" #�=20 !<br><!-- End of picture text -->

#### Pˇríklady k procviˇcení 

15.1. Vypočtěte následující trojné integrály: 



<!-- Start of picture text -->
1<br>a) M D fŒx; y; z� 2 R 3 W x � 0; y � 0; x C y � 1; x C y C z � 1g;<br>� M x C y C 1 dxdydz;<br>b) xyz dxdydz; M je osmina koule o poloměru 1 se středem v počátku ležící v I. oktantu:<br>� M<br><!-- End of picture text -->

_Výsledky._ 15.1. a) 2<sup><u>3</u>�2 ln 2, b)1=48.</sup> 

### 16 Substituce (transformace) ve dvojném a trojném integrálu 

Připomeňme nejprve, jak vypadá věta o substituci v případě funkce jedné proměnné: Je-li f spojitá funkce na ha; bi a ' je rostoucí (a tedy prostá) funkce na h˛; ˇi, která zde má spojitou derivaci, přičemž '.˛/ D a, '.ˇ/ D b, pak 



<!-- Start of picture text -->
f .x/ dx D f .'.t//' 0 .t/ dt:<br>� ab � ˛ˇ<br> h˛; ˇi, přičemž nyní '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikuje˛; ˇi, přičemž nyní '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikujei, přičemž nyní '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikuje, přičemž nyní '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikuje '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikuje D b, '.ˇ/ D a, pak se vzorec modifikuje b, '.ˇ/ D a, pak se vzorec modifikuje, '.ˇ/ D a, pak se vzorec modifikuje '.ˇ/ D a, pak se vzorec modifikuje D a, pak se vzorec modifikuje a, pak se vzorec modifikuje, pak se vzorec modifikuje<br>f .x/ dx D f .'.t//' 0 .t/ dt D � f .'.t//' 0 .t/ dt:<br>� ab � ˇ˛ � ˛ˇ<br><!-- End of picture text -->

Je-li naopak ' klesající na h˛; ˇi, přičemž nyní '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikuje˛; ˇi, přičemž nyní '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikujei, přičemž nyní '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikuje, přičemž nyní '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikuje '.˛/ D b, '.ˇ/ D a, pak se vzorec modifikuje D b, '.ˇ/ D a, pak se vzorec modifikuje b, '.ˇ/ D a, pak se vzorec modifikuje, '.ˇ/ D a, pak se vzorec modifikuje '.ˇ/ D a, pak se vzorec modifikuje D a, pak se vzorec modifikuje a, pak se vzorec modifikuje, pak se vzorec modifikuje 

Zaměníme-li předpoklad ryzí monotonie funkce ' předpokladem '<sup>0</sup> .t/ ¤ 0 pro každé t 2 h˛; ˇi (to nám zaručí, že ' je zde rostoucí, nebo je klesající), pak lze oba vzorce psát v jednom jako 



<!-- Start of picture text -->
f .x/ dx D f .'.t//j' 0 .t/j dt: (�)<br>� ab � ˛ˇ<br><!-- End of picture text -->

16 Substituce (transformace) ve dvojném a trojném integrálu 

77 

Diferencovatelnost funkce f v bodě Œx0; y0� vyžadovala, aby f byla definována na nějakém okolí tohoto bodu, tj. pojem má smysl pro vnitřní body nějaké množiny (neboli pro body otevřené množiny). Následující definice upřesňuje, jak chápat (spojitou) diferencovatelnost funkce na množinách, které nejsou nutně otevřené. 

Definice 16.1 — spojitˇe diferencovatelné 2-funkce na množinˇe. Nechť _F_ W R<sup>2</sup> ! R<sup>2</sup> je 2-funkce definovaná na množině M � R<sup>2</sup> . Řekneme, že _F je spojitě diferencovatelná na_ M , jestliže existuje otevřená množina ˝ � R<sup>2</sup> taková, že M � ˝ a 2-funkci _F_ lze rozšířit na ˝ takovým způsobem, že Jacobiova matice _F_<sup>0</sup> existuje a je spojitá v každém bodě množiny ˝. 

Věty o substituci budou dále využívat pojem regulární 2-funkce. 

Definice 16.2 — regulární 2-funkce. Nechť _F_ W R<sup>2</sup> ! R<sup>2</sup> je 2-funkce, která je spojitě diferencovatelná na otevřené množině M . Řekneme, že _F_ je _regulární na_ M , jestliže J _F_ ¤ 0 v každém bodě množiny M . 

■ Vˇeta 16.3 — o substituci ve dvojném integrálu. _Nechť_ M<sup>�</sup> � R<sup>2</sup> _je uzavřená měřitelná množina,_ ˝ � R<sup>2</sup> _je otevřená množina a nechť_ M<sup>�</sup> � ˝ _. Nechť dále F_ .u; v/ D Œg.u; v/; h.u; v/� _je prostá a regulární 2-funkce na_ ˝ _a_ f W R<sup>2</sup> ! R _je spojitá na_ M D _F_ .M<sup>�</sup> / _. Pak platí_ 



<!-- Start of picture text -->
f .x; y/ dxdy D f . F .u; v// jJ F  .u; v/j dudv:<br>� M � M � „ ƒ‚ …<br>f .g.u;v/;h.u;v//<br><!-- End of picture text -->

Poznámka 16.4. a) Vzorec věty formálně odpovídá vzorci (�). 

b) Ve větě vystupuje předpoklad, že 2-funkce _F_ je prostá a regulární na otevřené oblasti ˝. Potom, je-li M omezená množina taková, že M � ˝, tak platí, že M je měřitelná, právě když _F_ .M/ je měřitelná. 

c) Vysvětleme si význam jakobiánu na pravé straně rovnosti. Zvolme f .x; y/ D 1 a předpokládejme pro jednoduchost, že jakobián J _F_ ¤ 0 je konstantní. Potom podle předchozí věty je 



<!-- Start of picture text -->
dxdy D jJ F  j tj. �.M/ D jJ F  j�.M � /:<br>� M � M � dudv;<br><!-- End of picture text -->

Jako příklad uvažujme čtverec M<sup>�</sup> D h0; 1i<sup>2</sup> a lineární 2-funkci _F_ .u; v/ D Œau C bv; cu C dv�, kde a; b; c; d 2 R. Protože J _F_ .u; v/ D ad � bc, je třeba požadovat ad � bc ¤ 0. Dosazením do výše uvedeného vzorce tedy máme �.M/ D jad � bcj, kde M D _F_ .M<sup>�</sup> / je rovnoběžník s vrcholy Œ0; 0�, Œa; c�, Œb; d� a Œa C b; c C d�. To odpovídá známému faktu z analytické geometrie, kdy obsah rovnoběžníku určeného vektory .a; c/ a .b; d/ je roven absolutní hodnotě determinantu 



<!-- Start of picture text -->
b<br>det c d :<br>�a �<br><!-- End of picture text -->

Pokud jakobián J _F_ není konstantní, pak na základě integrální věty o střední hodnotě lze psát �.M/ D jJ _F_ .u0; v0/j�.M<sup>�</sup> /, kde Œu0; v0� 2 M<sup>�</sup> . V jakobiánu je tedy „schován“ poměr obsahů množin M<sup>�</sup> a M . 

Pˇríklad 16.5. Určete míru (obsah) množiny M , která je vymezena křivkami xy D a, xy D b (0 < a < b), y<sup>2</sup> D cx, y<sup>2</sup> D dx (0 < c < d ). 

_Řešení._ Označíme-li xy D u,<sup><u>y</u></sup> x<sup>2</sup> D v, pak M<sup>�</sup> je vymezena nerovnostmi a � u � b, c � v � d a 2-funkce x D u<sup>2=3</sup> v<sup>�1=3</sup> , y D u<sup>1=3</sup> v<sup>1=3</sup> je prostá uvnitř I. kvadrantu (každému bodu Œu0; v0� odpovídá jediný bod Œx0; y0�, který leží na hyperbole xy D u0 a parabole y<sup>2</sup> =x D v0). Platí 



<!-- Start of picture text -->
J.u; v/ D det 231 u�1=3v�1=3 �1 1 3 u2=3v�4=3 D 1 ve vnitřku I. kvadrantu:<br>3v ¤ 0<br>3 u�2=3v1=3 3 u1=3v�2=3 !<br><!-- End of picture text -->

Protože Jacobiova matice je spojitá ve vnitřku I. oktantu, naše 2-funkce je regulární a podle věty 16.3 platí 



<!-- Start of picture text -->
dxdy D 1 du D 1<br>� M � M � jJ.u; v/jdudv D � ab� � cd 3v dv � 3 .b � a/ ln d c :<br><!-- End of picture text -->

Kapitola 3. Integrální poˇcet funkce více promˇenných 

78 

Poznámka 16.6. Požadavek věty 16.3, aby bylo možné 2-funkci _F_ prostě rozšířit na otevřenou nadmnožinu integračního oboru M<sup>�</sup> při zachování regularity, je často nesplnitelný (i v případě poměrně jednoduchých transformací). Tento požadavek lze oslabit, byť za cenu komplikovanější formulace tvrzení. Zhruba řečeno, substituční vzorec zůstane v platnosti, pokud předpoklady věty 16.3 nejsou splněny na množinách míry nula, viz následující tvrzení. 

> ■ Vˇeta 16.7 — o substituci ve dvojném integrálu za slabších pˇredpoklad˚u. _Nechť_ ˝<sup>�</sup> � R<sup>2</sup> _je otevřená množina,_ M<sup>�</sup> � R<sup>2</sup> _je měřitelná množina a platí_ ˝<sup>�</sup> � M<sup>�</sup> _,_ �.M<sup>�</sup> n ˝<sup>�</sup> / D 0 _. Dále, nechť 2-funkce F_ W R<sup>2</sup> ! R<sup>2</sup> _daná jako F_ .u; v/ D Œg.u; v/; h.u; v/� _je spojitě diferencovatelná na_ M<sup>�</sup> _, přičemž je prostá a regulární v_ ˝<sup>�</sup> _. Označme_ ˝ D _F_ .˝<sup>�</sup> / _,_ M D _F_ .M<sup>�</sup> / _a předpokládejme, že_ M _je měřitelná s_ �.M n ˝/ D 0 _. Nechť_ f W R<sup>2</sup> ! R _je funkce ohraničená na_ M _, spojitá na_ ˝ _a nechť funkce_ .f ı _F_ /jJ _F_ j _je ohraničená na_ M<sup>�</sup> _. Pak platí_ 



<!-- Start of picture text -->
f .x; y/ dxdy D f . F .u; v// jJ F  .u; v/j dudv:<br>� M � M � „ ƒ‚ …<br>f .g.u;v/;h.u;v//<br><!-- End of picture text -->

Poznámka 16.8. Důkazy vět 16.3 a 16.7 jsou dosti náročné (využívá se zde některých speciálních vlastností regulárních zobrazení). 

Bˇežnˇe používané transformace 

1. Posunutí (translace): x D u C a, y D v C b, kde a; b 2 R, 



<!-- Start of picture text -->
0<br>J.u; v/ D det D 1:<br>0 1<br>�1 �<br><!-- End of picture text -->

2. Dilatace (změna měřítka): x D au, y D bv, kde a; b 2 R, a ¤ 0, b ¤ 0, 



<!-- Start of picture text -->
0<br>J.u; v/ D det D ab:<br>0 b<br>�a �<br><!-- End of picture text -->

3. Transformace do polárních souřadnic: x D � cos ', y D � sin ', kde � � 0 a ' nabývá obvykle hodnot z intervalu h0; 2�i (resp. z h��; �i), může to ale být i z delšího intervalu. 



<!-- Start of picture text -->
�� sin '<br>J.�; '/ D det D �.cos 2 ' C sin 2 '/ D �:<br>�cossin ' ' � cos ' �<br><!-- End of picture text -->

4. Transformace do zobecněných polárních souřadnic: x D a� cos ', y D b� sin ', a; b 2 R<sup>C</sup> , 



<!-- Start of picture text -->
b� sin '<br>J.�; '/ D det D ab�.cos 2 ' C sin 2 '/ D ab�:<br>�aa cos sin ' ' b� cos '�<br>Pˇríklad 16.9. Určete hodnotu dvojného integrálu x 2 dxdy, kde M je množina vymezená nerovností<br>� M<br>x 2 C y 2 � 4.<br><!-- End of picture text -->

_Řešení._ Množina M je uzavřený kruh se středem v počátku o poloměru 2. Tomu odpovídá množina M<sup>�</sup> D h0; 2i �h0; 2�i, tj. uzavřený obdélník. V tomto případě nelze splnit předpoklady věty 16.3, protože 2-funkce _F_ .�; '/ D Œ� cos '; � sin '� není prostá na M<sup>�</sup> . To je způsobeno tím, že všechny body ležící na levé hraniční úsečce obdélníka se zobrazí na počátek Œ0; 0� a pro každé c 2 h0; 2i se body Œc; 0� a Œc; 2�� zobrazí na bod Œc; 0� 2 M . Prostá by byla, kdybychom uvažovali např. M<sup>�</sup> D .0; 2i �h0; 2�/, ale pak by M<sup>�</sup> nebyla uzavřená, což je též ve větě požadováno. 

Lze však použít větu 16.7. Za množinu ˝<sup>�</sup> vezmeme vnitřek obdélníka M<sup>�</sup> D h0; 2i �h0; 2�i. Množina M<sup>�</sup> n ˝<sup>�</sup> představuje hranici obdélníka M<sup>�</sup> a tedy �.M<sup>�</sup> n ˝<sup>�</sup> / D 0. Množina M n ˝ se skládá z kružnice x<sup>2</sup> C y<sup>2</sup> D 4 a úsečky spojující body Œ0; 0� a Œ2; 0�, což je množina míry nula. Zobrazení _F_ je na ˝<sup>�</sup> prostou a regulární 2-funkcí (J.�; '/ D � ¤ 0 pro 8Œ�; '� 2 ˝<sup>�</sup> ). Integrovaná funkce je spojitá na 

16 Substituce (transformace) ve dvojném a trojném integrálu 

79 

M (a tedy ohraničená na M a spojitá na ˝) a funkce �<sup>3</sup> cos<sup>2</sup> ' je spojitá na M<sup>�</sup> (a tedy ohraničená na M<sup>�</sup> ). Podle věty 16.7 tedy máme 



<!-- Start of picture text -->
� M x 2 dxdy D � 02 � 3 d� � � 02� cos 2 ' d' D �4 4 � h '2 i2�0 D 4�:<br>" #20<br><!-- End of picture text -->

Pˇríklad 16.10. Určete obsah množiny vymezené Bernoulliovou lemniskátou, což je křivka určená jako množina bodů Œx; y� 2 R<sup>2</sup> vyhovující rovnici .x<sup>2</sup> C y<sup>2</sup> /<sup>2</sup> D 2a<sup>2</sup> .x<sup>2</sup> � y<sup>2</sup> / (a > 0). 

_Řešení._ Pomocí substituce do polárních souřadnic x D � cos ', y D � sin ' přejde rovnice na tvar �<sup>2</sup> D 2a<sup>2</sup> cos 2'. Uvědomíme-li si, křivka musí být symetrická vzhledem k ose x i y (změna x 7! �x i y 7! �y rovnici nezmění), stačí uvažovat obrazec, jehož míru máme spočítat, např. jenom v I. kvadrantu. Výsledná míra pak bude čtyřnásobek této části. Prvnímu kvadrantu odpovídá úhel z intervalu ˝0;<sup><u>�</u></sup> 2 ˛. Protože levá strana rovnice �<sup>2</sup> D 2a<sup>2</sup> cos 2' je nezáporná, musí být nezáporná také pravá strana, což v uvažovaném intervalu nastane, je-li ' 2 ˝0;<sup><u>�</u></sup> 4 ˛. Čtvrtina množiny M � je tedy vymezena nerovnostmi 0 � ' �<sup><u>�</u></sup> 4<sup>, 0 ���a</sup><sup>~~p~~</sup> 2 cos 2' a platí 



<!-- Start of picture text -->
2 cos 2' 2 cos 2'<br>�.M/ D 4 � d� d' D 2 d'<br>� M � d�d' D 4 � 0�=4� � 0a p � � 0�=4 h� 2ia 0 p<br>D 4a 2 cos 2' d' D 2a 2 Œsin 2'� �=4 0 D 2a 2 :<br>� 0�=4<br><!-- End of picture text -->

V případě substituce ve trojném integrálu by za analogických předpokladů vět 16.3 a 16.7 příslušný vzorec vypadal 



<!-- Start of picture text -->
f .x; y; z/ dxdydz D<br>� M � M � f . F .u; v; w//jJ F  .u; v; w/j dudvdw:<br><!-- End of picture text -->

Vedle translace a dilatace jsou běžně používanými transformacemi transformace do cylindrických (válcových) souřadnic a do sférických souřadnic. 

1. Transformace do cylindrických souřadnic: x D � cos ', y D � sin ', z D z, kde � � 0 a ' nabývá obvykle hodnot z intervalu délky 2�, 



<!-- Start of picture text -->
J.�; '; z/ D det 0cossin ' ' ���cossin ' ' 001<br>0 0 1<br>@ A D �:<br><!-- End of picture text -->

2. Transformace do sférických souřadnic: I. zp. x D � cos ' cos #, y D � sin ' cos #, z D � sin #, kde � � 0, ' je obvykle z intervalu délky 2� a omezení na úhel # je �<sup><u>�</u></sup> 2<sup>�#�</sup><sup><u>�</u></sup> 2<sup>,</sup> 



<!-- Start of picture text -->
0cos ' cos # �� sin ' cos # �� cos ' sin #1<br>J.�; '; #/ D det sin ' cos # � cos ' cos # �� sin ' sin #<br>@ sin # 0 � cos # A D � 2 cos #:<br><!-- End of picture text -->

II. zp. x D � cos ' sin #, y D � sin ' sin #, z D � cos #, kde � � 0, ' je obvykle z intervalu délky 2� a omezení na úhel # je 0 � # � �. 



<!-- Start of picture text -->
0cos ' sin # �� sin ' sin # � cos ' cos #1<br>J.�; '; #/ D det sin ' sin # � cos ' sin # � sin ' cos #<br>@ cos # 0 � sin # A D � 2 sin #:<br><!-- End of picture text -->

Pˇríklad 16.11. Odvoďte známý vzorec pro objem kužele o poloměru podstavy r a výšce h. 

_Řešení._ Použijeme transformace do cylindrických souřadnic x D � cos ', y D � sin ', z D z. Kužel umístěme např. tak, že jeho podstava leží v rovině xy a má střed v počátku. Pak průmětem kužele do 

Kapitola 3. Integrální poˇcet funkce více promˇenných 

80 



<!-- Start of picture text -->
z<br>ρ<br>ϑ<br>z  =  x<br>x<br><!-- End of picture text -->

Obrázek 16.1: Řez tělesem rovinou xz (z obrázku je patrno, že průvodič � se skutečně mění s úhlem #) 

roviny xy je kruh o poloměru r, který je v polárních souřadnicích vyjádřen nerovnostmi 0 � ' � 2�, 0 � � � r. Samotná kuželová plocha má rovnici 



<!-- Start of picture text -->
z D h � h r q x 2 C y 2 ;<br><!-- End of picture text -->

a v cylindrických souřadnicích (toto vyjádření dostaneme po dosazení za x a y) z D h �<sup><u>h</u></sup> r<sup>�. Množina</sup> M<sup>�</sup> , přes kterou budeme integrovat, je tedy vyjádřena nerovnostmi 



<!-- Start of picture text -->
0 � ' � 2�; 0 � � � r; 0 � z � h � h r �<br><!-- End of picture text -->

a objem tělesa je dán integrálem 



<!-- Start of picture text -->
�.M/ D � M � � d'd�dz D � 02� � � 0r � � 0h�h�=r � dz� d�� d' D � 02� � � 0r Œ�z� h 0 �h�=r d�� d'<br>D 2� h� � h�2 d� D h� 2 � h�3 D 2� hr 2 � hr 2 D 1<br>� 0r r 2 3r 2 3 3 �r 2:<br>! " #r0 !<br><!-- End of picture text -->

Pˇríklad 16.12. Určete objem tělesa vymezeného nerovnostmi x<sup>2</sup> C y<sup>2</sup> C z<sup>2</sup> � 2z a kuželem x<sup>2</sup> C y<sup>2</sup> � z<sup>2</sup> . 

_Řešení._ Použijeme substituce do sférických souřadnic. Hraniční plochy tělesa se skládají z části kulové plochy x<sup>2</sup> C y<sup>2</sup> C z<sup>2</sup> D 2z o poloměru 1 se středem v bodě Œ0; 0; 1� (rovnice psána ve středovém tvaru totiž je x<sup>2</sup> C y<sup>2</sup> C .z � 1/<sup>2</sup> D 1) a částí kuželové plochy z<sup>2</sup> D x<sup>2</sup> C y<sup>2</sup> . Po dosazení výrazů x D � cos ' sin #, y D � sin ' sin #, z D � cos # má kulová plocha ve sférických souřadnicích vyjádření � D 2 cos #. Z geometrického náhledu (viz obrázek 16.1) vidíme, že množina M<sup>�</sup> , přes kterou integrujeme, je vymezena nerovnostmi 0 � ' � 2�, 0 � # �<sup><u>�</u></sup> 4<sup>, 0 ���2 cos #(platí x2 C y2 C z2D �2). Objem</sup> tělesa je pak dán integrálem 



<!-- Start of picture text -->
�.M/ D<br>� M � �2 sin # d'd#d�<br>D � 02� d' � 0�=4� � 02 cos # � 2 sin #� d�� d# D 2� 3 � 0�=4 h� 3 sin #i20 cos # d#<br>cos # D t<br>D 16� cos 3 # sin # d# D d# D �dt= sin # D 16� t 3 dt<br>3 � 0�=4 ˇˇˇˇˇˇ 0 ! 1; �=4 ! p 2=2 ˇˇˇˇˇˇ 3 � p 12=2<br>D 16� t 4 D 4� 1 � 1 D �:<br>3 " 4 #1 p 2=2 3 � 4 �<br><!-- End of picture text -->

Poznámka 16.13. Transformaci do cylindrických i sférických souřadnic lze zobecnit podobně jako v případě polárních souřadnic, tj. x D a� cos ', y D b� sin ', z D z, J.�; '; z/ D ab�, resp. x D a� cos ' cos #, y D b� sin ' cos #, z D c� sin #, J.�; '; #/ D abc �<sup>2</sup> cos #. 

17 Aplikace dvojného a trojného integrálu v mechanice 

81 

#### Pˇríklady k procviˇcení 

16.1. Určete hodnotu integrálu 



<!-- Start of picture text -->
� M q a 2 � x 2 � y 2 dxdy; M D fŒx; y� 2 R 2 W x 2 C y 2 � axg .a > 0/:<br>Výsledky. 16.1. a 3 3 �� � 4 3 �.<br><!-- End of picture text -->

17 Aplikace dvojného a trojného integrálu v mechanice Již víme, že integrál 



<!-- Start of picture text -->
dxdy<br>� M<br><!-- End of picture text -->

představuje rovinný obsah množiny M , integrál 



<!-- Start of picture text -->
dxdydz<br>� M<br><!-- End of picture text -->

představuje objem tělesa M a integrál 



<!-- Start of picture text -->
f .x; y/ dxdy;<br>� M<br><!-- End of picture text -->

kde f .x; y/ � 0, představuje objem tělesa pod plochu f .x; y/. Označme 



<!-- Start of picture text -->
dm D �.x; y/ dxdy; resp. dm D �.x; y; z/ dxdydz;<br><!-- End of picture text -->

kde funkce �.x; y/, resp. �.x; y; z/, je hustota v bodě Œx; y� 2 M � R<sup>2</sup> , resp. Œx; y; z� 2 M � R<sup>3</sup> (veličině dm se říká hmotnostní element). Pak (zejména v mechanice) jsou užitečné následující integrály: 1. hmotnost desky M , resp. tělesa M 



<!-- Start of picture text -->
m.M/ D dm; resp. m.M/ D dm;<br>� M � M<br><!-- End of picture text -->

2. statické momenty desky M vzhledem k osám x a y 



<!-- Start of picture text -->
Sx.M/ D y dm; Sy .M/ D x dm;<br>� M � M<br><!-- End of picture text -->

3. statické momenty tělesa M vzhledem k souřadným rovinám xy, xz a yz 



<!-- Start of picture text -->
Sxy .M/ D z dm; Sxz.M/ D y dm; Syz.M/ D x dm;<br>� M � M � M<br><!-- End of picture text -->

4. momenty setrvačnosti desky M vzhledem k osám x a y, a polární moment setrvačnosti 



<!-- Start of picture text -->
Ix.M/ D y 2 dm; Iy .M/ D x 2 dm; Ip.M/ D .x 2 C y 2 / dm;<br>� M � M � M<br>souřadnice těžiště desky M M<br>xT D Sy .M / yT D Sx.M /<br>m.M/ ; m.M/ ;<br>souřadnice těžiště tělesa M M<br>xT D Syz.M / yT D Sxz.M / zT D Sxy .M /<br>m.M/ ; m.M/ ; m.M/ ;<br><!-- End of picture text -->

5. souřadnice těžiště desky M M 

6. souřadnice těžiště tělesa M M 

7. momenty setrvačnosti tělesa M vzhledem k osám x, y a z 



<!-- Start of picture text -->
Ix.M/ D .y 2 C z 2 / dm; Iy .M/ D .x 2 C z 2 / dm; Iz.M/ D .x 2 C y 2 / dm;<br>� M � M � M<br><!-- End of picture text -->

Kapitola 3. Integrální poˇcet funkce více promˇenných 

82 

8. polární moment setrvačnosti tělesa M 



<!-- Start of picture text -->
.x 2 C y 2 C z 2 / dm;<br>� M<br><!-- End of picture text -->

9. plošné momenty setrvačnosti tělesa M vzhledem k souřadným rovinám xy, xz a yz 



<!-- Start of picture text -->
Ixy .M/ D z 2 dm; Ixz.M/ D y 2 dm; Iyz.M/ D x 2 dm;<br>� M � M � M<br><!-- End of picture text -->

10. deviační momenty tělesa M vzhledem k souřadným rovinám xy, xz a yz 



<!-- Start of picture text -->
Dxy .M/ D xy dm; Dxz.M/ D xz dm; Dyz.M/ D yz dm:<br>� M � M � M<br><!-- End of picture text -->

Momenty setrvačnosti lze uspořádat do tzv. _tenzoru setrvačnosti_ 



<!-- Start of picture text -->
I  D 0�DIxxy �DIyxy ��DDyzxz1<br>@�Dxz �Dyz Iz A :<br><!-- End of picture text -->

#### Pˇríklady k procviˇcení 

17.1. Určete míru (objem) tělesa vymezeného průnikem tří válcových ploch o poloměru r > 0, které mají vzájemně kolmé osy rotace protínající se v jednom bodě (toto těleso se nazývá Steinmetzovo). 

17.2. Určete souřadnice těžiště osminy koule o poloměru r ležící v I. oktantu. 

17.3. Vypočítejte míru (objem) tělesa vymezeného nerovnostmi ~~p~~ x<sup>2</sup> C y<sup>2</sup> � z, x<sup>2</sup> C y<sup>2</sup> C z<sup>2</sup> � 2z. 

17.4. Vypočítejte statický moment vzhledem k rovině xy tělesa o jednotkové hustotě, které je vymezeno nerovnostmi 0 � z � 4 � x<sup>2</sup> � y<sup>2</sup> . 

_Výsledky._ 17.1. 8.2 � ~~p~~ 2/r<sup>3</sup> . 17.2. xT D yT D zT D<sup>3r</sup> =8. 17.3. �. 17.4.<sup>32�</sup> =3. 

## Kapitola 4 

# Kˇrivkové a plošné integrály 

### 18 Kˇrivky v rovinˇe a prostoru 

Definice 18.1 — rovinné kˇrivky. Nechť _F_ D Œ'; � W R ! R<sup>2</sup> je 2-funkce spojitá na intervalu ha; bi. _Rovinnou křivkou_ nazveme množinu � WD f _F_ .t/ W t 2 ha; big � R<sup>2</sup> , přičemž 2-funkce _F_ D Œ'; � se nazývá _parametrizace křivky_ � . Body A WD Œ'.a/; .a/�, B WD Œ'.b/; .b/� nazýváme _koncové body křivky_ � . Křivka � se nazývá _uzavřená_ , je-li A D B. 

Poznámka 18.2. a) Všimněme si, že křivkou zde nenazýváme samotnou 2-funkci _F_ , ale její obraz v R<sup>2</sup> (takové množině se říká také _hodograf_ ). V tomto i dalších pojmech týkajících se křivek nepanuje v literatuře jednotnost, někdy se křivkou myslí zobrazení _F_ a množině � se říká (vedle již zmíněného pojmu hodograf) _geometrický obraz křivky_ . 

b) Na křivku lze nahlížet jako na pohyb hmotného bodu v rovině (řídícího se 2-funkcí _F_ ) v časovém intervalu ha; bi. 

c) Definice připouští i množiny � , které příliš neodpovídají intuitivní představě o křivce. Např. známá Peanova křivka vyplňuje čtverec v rovině, má tedy nenulovou Jordanovu míru. Níže proto požadavky na křivku postupně zpřísníme tak, abychom se v další kapitole (kde se budeme věnovat křivkovým integrálům) nedostali nikde do problémů. 

Definice 18.3 — kˇrivek se speciálními vlastnostmi. 1. Křivka � se nazývá _jednoduchá_ , je-li _F_ prostá na ha; bi. Geometricky to znamená, že křivka se nikde neprotíná (postačující podmínkou pro to, aby _F_ byla prostá, je ryzí monotonie alespoň jedné z funkcí ', na ha; bi). 

2. Křivka � se nazývá _jednoduchá uzavřená_ (neboli _jordanovská_ ), je-li uzavřená a _F_ je prostá na .a; b/. 

3. Křivka � se nazývá _třídy_ C<sup>1</sup> , jestliže její parametrizace _F_ má spojitou Jacobiovu matici na ha; bi (tj. funkce ' a mají spojité derivace na ha; bi). 

4. Křivka � se nazývá _jednoduchá hladká_ , je-li jednoduchá, je třídy C<sup>1</sup> a navíc .'<sup>0</sup> .t//<sup>2</sup> C .<sup>0</sup> .t//<sup>2</sup> > 0 8t 2 ha; bi (jinak řečeno, hodnoty '<sup>0</sup> .t/,<sup>0</sup> .t/ nejsou v žádném bodě intervalu současně nulové). 

5. Křivka � se nazývá _jednoduchá uzavřená hladká_ , je-li jednoduchá uzavřená, je třídy C<sup>1</sup> , platí .'<sup>0</sup> .t//<sup>2</sup> C .<sup>0</sup> .t//<sup>2</sup> > 0 8t 2 ha; bi, a navíc 'C<sup>0.a/ D '</sup> �<sup>0.b/,</sup> C<sup>0.a/ D</sup> �<sup>0.b/.</sup> 

6. Křivka � se nazývá _jednoduchá po částech hladká_ , je-li spojením konečně mnoha jednoduchých hladkých křivek, přičemž toto spojení je pouze skrz koncové body. Přesněji, existuje parametrizace _F_ , která je na intervalu ha; bi spojitá, a existuje dělení D intervalu ha; bi takové, že na každém dílčím intervalu hti �1; ti i představuje _F_ jednoduchou hladkou křivku. Zde již nebudeme rozlišovat, zda výsledná křivka je nebo není uzavřená. 

Poznámka 18.4. a) Každá jednoduchá (a jednoduchá uzavřená křivka) má nekonečně mnoho parametrizací, např. jednotková kružnice se středem v počátku má parametrizaci Œcos t; sin t�, t 2 h0; 2�i, nebo Œcos 2t; sin 2t�, t 2 h0; �i, nebo Œsin t; cos t�, t 2 h0; 2�i. 

Kapitola 4. Kˇrivkové a plošné integrály 

84 

b) Je-li f W R ! R funkce spojitá na ha; bi, pak její graf je křivka s parametrizací '.t/ D t, .t/ D f .t/, t 2 ha; bi. 

c) Je-li � křivka třídy C<sup>1</sup> a pro nějaké t0 2 ha; bi je _F_<sup>0</sup> .t0/ D Œ0; 0�, pak bod P D Œ'.t0/; .t0/� nazveme _singulárním bodem_ křivky, v opačném případě jej nazveme _regulárním bodem_ . Máme-li dvě různé parametrizace téže křivky, může se stát, že některý bod je regulární v jedné parametrizaci a singulární v druhé. Např úsečka spojující body Œ�1; �1� a Œ1; 1� má při parametrizaci Œt; t�, t 2 h�1; 1i všechny body regulární, ale při parametrizaci Œt<sup>3</sup> ; t<sup>3</sup> �, t 2 h�1; 1i je počátek singulárním bodem. Jednoduchá (resp. jednoduchá uzavřená) hladká křivka má tedy všechny body regulární. Není težké si rozmyslet, že _F_<sup>0</sup> .t/ představuje tečný vektor ke křivce � v bodě _F_ .t/ D Œ'.t/; .t/� (viz obrázek 18.1). Tento tečný vektor 



<!-- Start of picture text -->
F ′ ( t )<br>F ( t  + h )<br>F ( t )<br>F ( t  + h ) − F ( t )<br>h<br><!-- End of picture text -->

Obrázek 18.1: Jacobiova matice _F_<sup>0</sup> .t/ je v případě 2-funkce _F_ W R ! R<sup>2</sup> vektorem v rovině, který představuje tečný vektor ke křivce v bodě _F_ .t/ D Œ'.t/; .t/� 

lze také interpretovat jako vektor okamžité rychlosti, kterou má hmotný bod při pohybu po křivce v čase t . Když je vektor v každém čase t 2 ha; bi nenulový a mění se spojitě, nemůže hmotný bod najednou prudce změnit směr, nemůže zastavit a pak se vydat opačným směrem atp. Jeho pohyb je skutečně „hladký“. Příkladem křivky, kdy hmotný bod zastaví (v singulárním bodě) a vydá se jiným směrem, je např. část cykloidy o parametrizaci _F_ .t/ D Œa.t � sin t/; a.1 � cos t/�, t 2 h0; 4�i (a > 0), viz obrázek 18.2. Na tomto příkladu vidíme, že samotná spojitost Jacobiovy matice parametrizace _F_ hladkost, jak ji i intuitivně chápeme, nezaručí. 



<!-- Start of picture text -->
y<br>x<br>0 2 πa 4 πa<br><!-- End of picture text -->

Obrázek 18.2: Dva oblouky cykloidy při parametrizaci _F_ .t/ D Œ a.t � sin t/; a.1 � cos t/ �, 0 � t � 4� (a > 0 je parametr). Tato křivka má tři singulární body (počátek a body Œ2�a; 0�, Œ4�a; 0�) 

Pro případ křivkového integrálu II. druhu je navíc potřeba zavést pojem orientace křivky. Orientovat křivku znamená určit směr, ve kterém jsou body křivky procházeny (to lze dvěma způsoby). 

- Definice 18.5 — souhlasné a nesouhlasné orientace jednoduché (uzavˇrené) kˇrivky. 1. Buď � D fŒ'.t/; .t/� W t 2 ha; big jednoduchá křivka a zvolme na ní dva různé body P1 D Œ'.t1/; .t1/� a P2 D Œ'.t2/; .t2/�. Orientujme křivku tak, že se pohybujeme od bodu P1 směrem k bodu P2 (říkáme také, že bod P1 je před bodem P2, zapisujeme P1 � P2). Je-li t1 < t2, řekneme, že _křivka_ � _je orientována souhlasně s parametrizací_ Œ'; �. Je-li naopak t1 > t2, řekneme, že _křivka_ � _je orientována nesouhlasně s parametrizací_ Œ'; �. 

2. V případě jednoduché uzavřené křivky � ji orientujme pomocí tří bodů P1, P2 a P3 tak, že se po křivce pohybujeme z bodu P1 do P2 a z P2 do P3 (bodu Pi odpovídá parametr ti , i D 1; 2; 3). Je-li t1 < t2 < t3 nebo t3 < t1 < t2 nebo t2 < t3 < t1, pak řekneme, že _křivka_ � _je orientována souhlasně s parametrizací_ Œ'; � a je-li t1 > t2 > t3 nebo t2 > t3 > t1 nebo t3 > t1 > t2, pak řekneme, že 

19 Kˇrivkový integrál 

85 

_křivka_ � _je orientována nesouhlasně s parametrizací_ Œ'; �. 

Pˇríklad 18.6. Jednotková kružnice se středem v počátku orientovaná proti oběhu hodinových ručiček je orientována souhlasně vzhledem k parametrizaci _F_ .t/ D Œcos t; sin t�, ale nesouhlasně vzhledem k parametrizaci _G_ .t/ D Œsin t; cos t�. 

Prostorovou křivku bychom definovali jako množinu 

� D fŒ'.t/; .t/; �.t/� W t 2 ha; big � R<sup>3</sup> ; 

kde 3-funkce _F_ D Œ'; ; �� je spojitá na ha; bi. Ostatní pojmy jako jednoduchá nebo hladká křivka by se zavedly analogicky. Pozor, křivku v prostoru nelze zadat explicitně pomocí funkce! 

#### Pˇríklady k procviˇcení 

18.1. Ověřte, že existují parametrizace, vzhledem ke kterým je úsečka (spojující libovolné dva body v rovině) jednoduchá hladká křivka, a elipsa je jednoduchá uzavřená hladká křivka. 

18.2. Napište rovnice tečny ke křivce � o parametrizaci _F_ .t/ D Œt cos t; t sin t; t�, t 2 h0; 2�i, v bodě T D Œ0; 0; 0�. 

_Výsledky._ 18.2. x D t , y D 0, z D t , t 2 R. 

### 19 Kˇrivkový integrál 

Definice 19.1 — kˇrivkového integrálu I. druhu ze spojité funkce. Nechť � je jednoduchá (nebo jednoduchá uzavřená) hladká křivka s parametrizací _F_ D Œ'; � a f W R<sup>2</sup> ! R je spojitá funkce na nějaké otevřené množině obsahující křivku � . Potom definujeme křivkový integrál I. druhu jako 



<!-- Start of picture text -->
� � f .x; y/ ds WD � ab f .'.t/; .t// q .' 0 .t// 2 C .  0 .t// 2 dt (�)<br><!-- End of picture text -->

Ukažme, co nás vedlo ke vzorci v předchozí definici. Jako motivaci uvažujme úlohu určit obsah plochy 



<!-- Start of picture text -->
� D fŒx; y; z� 2 R 3 W Œx; y� 2 �; 0 � z � f .x; y/g:<br><!-- End of picture text -->

Proveďme nějaké dělení intervalu a D t0 < t1 < ��� < tn D b intervalu ha; bi. Tímto dělením je určeno také dělení A D P0 � P1 � P2 ����� Pn D B křivky � (Pk D Œ'.tk/; .tk/�, k D 0; 1; : : : ; n/. Potom je přirozené aproximovat hledaný obsah číslem 



<!-- Start of picture text -->
n<br>Sn WD X f .'.tk/; .tk// q .Œ'.tk/ � '.tk�1/� 2 C Œ .tk/ �  .tk�1/� 2 :<br>kD1<br><!-- End of picture text -->

Potřebujeme ukázat, že Sn konverguje k hodnotě na pravé straně (�) pro každou nulovou posloupnost dělení intervalu ha; bi (připomeňme, že se jedná o posloupnost dělení, ve které norma dělení maxk2f1;2;:::;ng jtk � tk�1j jde s rostoucím n k nule). Podle Lagrangeovy věty o střední hodnotě (viz věta 15.3 v Matematické analýze I) existují čísla �k, �k 2 .tk�1; tk/ taková, že '.tk/ � '.tk�1/ D '<sup>0</sup> .�k/.tk � tk�1/ a .tk/ � .tk�1/ D<sup>0</sup> .�k/.tk � tk�1/. Hodnotu Sn tedy můžeme přepsat 



<!-- Start of picture text -->
n<br>Sn D X f .'.tk/; .tk// q Œ' 0 .�k/� 2 C Œ  0 .�k/� 2 .tk � tk�1/:<br>kD1<br><!-- End of picture text -->

Kdyby pod odmocninou byly hodnoty derivací v bodě tk (namísto �k a �k), pak by Sn představoval přímo integrální součet (s výběrem reprezentantů � D ftk W k D 1; 2; : : : ; ng) a v limitě bychom ihned dostali 

Kapitola 4. Kˇrivkové a plošné integrály 

86 

požadovaný integrál (protože f je spojitá nad křivkou � a výraz ~~p~~ '<sup>02</sup> C<sup>02</sup> je také spojitá funkce díky předpokladu hladkosti � ). Jako poslední krok je tedy potřeba ukázat, že 



<!-- Start of picture text -->
n<br>nlim!1 Sn D n lim !1 X f .'.tk/; .tk// q Œ' 0 .tk/� 2 C Œ  0 .tk/� 2 .tk � tk�1/:<br>kD1<br><!-- End of picture text -->

Důkaz tohoto kroku využívá Heineho–Cantorovy věty (viz věta 12.20 v Matematické analýze I), která říká, že spojitá funkce na uzavřeném intervalu je zde také stejnoměrně spojitá. 

Poznámka 19.2. a) Předpoklad hladkosti křivky lze v definici křivkového integrálu oslabit, zejména lze připustit jednoduché C<sup>1</sup> křivky, které mají konečný počet singulárních bodů, případně lze porušit „jednoduchost“ křivky ve smyslu, že dovolíme konečný počet protnutí. 

b) Je-li křivka třídy C<sup>1</sup> , která je buď jednoduchá, nebo protíná sebe sama v maximálně konečném počtu izolovaných bodů, pak je tzv. _rektifikovatelná_ . To znamená, že délka lomené čáry při zjemňování dělení neroste nade všechny meze, a tedy křivka má konečnou délku (délka křivky je právě takto definována, tj. jako supremum délek lomených čar přes všechna možná dělení). Příkladem nerektifikovatelné křivky je křivka o parametrizaci _F_ D Œ'; �, kde 



<!-- Start of picture text -->
0 pro t D 0<br>'.t/ D t;  .t/ D t 2 h0; 1i ; 0 není spojitá v bodě 0:<br>(t sin 1 t pro t > 0:  ;<br><!-- End of picture text -->

Pro délku rektifikovatelné křivky � platí 



<!-- Start of picture text -->
`.�/ D � � ds D � ab q .' 0 .t// 2 C .  0 .t// 2 dt:<br><!-- End of picture text -->

Veličině ds D ~~p~~ .'<sup>0</sup> .t//<sup>2</sup> C .<sup>0</sup> .t//<sup>2</sup> dt se říká _diferenciál oblouku_ , přičemž výraz ~~p~~ .'<sup>0</sup> .t//<sup>2</sup> C .<sup>0</sup> .t//<sup>2</sup> představuje velikost tečného vektoru ke křivce (vektoru rychlosti hmotného bodu) v bodě _F_ .t/ D Œ'.t/; .t/�. 

c) Lze ukázat, že za předpokladů kladených na křivku a integrovanou funkci hodnota integrálu nezávisí na zvolené parametrizaci dané křivky. 

d) Křivkový integrál je možné definovat obecněji než v definici 19.1, kdy vycházíme z ohraničené funkce na oblasti obsahující křivku a zavedeme podobně jako u standardního Riemannova integrálu horní a dolní součty funkce nad křivkou, případně integrální součty. 

e) Křivkový integrál přes jednoduchou po částech hladkou křivku bychom definovali jako součet integrálů přes jednotlivé části. 

f) V případě uzavřené křivky se někdy znak integrálu píše jako 

Pˇríklad 19.3. Určete hodnotu integrálu 



<!-- Start of picture text -->
.x C y/ ds;<br>� �<br><!-- End of picture text -->

kde � je obvod trojúhelníka ABC , A D Œ0; 0�, B D Œ0; 2�, C D Œ1; 0�. 

_Řešení._ Jedná se o po částech hladkou křivku, pokud budeme strany trojúhelníka parametrizovat např. takto: stranu AB je nejjednodušší parametrizovat 2-funkcí _F_ 1.t/ D Œ0; t�, t 2 h0; 2i, stranu BC 2-funkcí _F_ 2.t/ D Œt; 2 � 2t�, t 2 h0; 1i a stranu AC 2-funkcí _F_ 3.t/ D Œt; 0�, t 2 h0; 1i. Protože _F_ 1<sup>0.t/ D Œ0; 1�,</sup> _F_ 2<sup>0.t/ D Œ1; �2�a</sup><sup>_F_0</sup> 3<sup>.t/ D Œ1; 0�, jednotlivé křivkové integrály jsou dány</sup> 



<!-- Start of picture text -->
t 2<br>.x C y/ ds D .0 C t/ p 0 2 C 1 2 dt D D 2;<br>� AB � 02 2<br>" #20<br>� BC .x C y/ ds D � 01.t C 2 � 2t/ q 1 2 C .�2/ 2 dt D p 5 2t � t 2 2 D 3 p 2 5 ;<br>" #10<br><!-- End of picture text -->

19 Kˇrivkový integrál 

87 



<!-- Start of picture text -->
.x C y/ ds D .t C 0/ p 1 2 C 0 2 dt D t 2 D 1<br>� AC � 01 2 2 :<br>" #10<br><!-- End of picture text -->

Celkově tedy 



<!-- Start of picture text -->
p 5<br>.x C y/ ds D .x C y/ ds C .x C y/ ds C .x C y/ ds D 2 C 3 C 1 �5 C 3 p 5�:<br>� � � AB � BC � AC 2 2 D 2 1<br>Pˇríklad 19.4. Určete hodnotu integrálu<br>arctg y<br>� � x ds;<br><!-- End of picture text -->

kde � je část Archimédovy spirály � D ' ležící v kruhu se středem v počátku o poloměru<sup>�</sup> =2. 

_Řešení._ Archimédova spirála začíná v počátku (pro ' D 0) a s rostoucím úhlem roste (lineárně) vzdálenost � bodu křivky od počátku. Bodu na kružnici o poloměru<sup>�</sup> =2 tedy dosáhne, je-li � D ' D<sup><u>�</u></sup> 2<sup>. Odvoďme</sup> nejprve, jak vypadá diferenciál oblouku ds, je-li křivka vyjádřena v polárních souřadnicích. Vzhledem k transformačním rovnicím mezi kartézskými a polárními souřadnicemi x D �.'/ cos ' a y D �.'/ sin ' platí 



<!-- Start of picture text -->
ds 2 D dx 2 C dy 2 D .� 0 .'/ cos ' � �.'/ sin '/ 2 d' 2 C .� 0 .'/ sin ' C �.'/ cos '/ 2 d' 2<br>D<br>�.� 0 .'// 2 cos 2 ' � 2� 0 .'/�.'/ cos ' sin ' C � 2 .'/ sin 2 '<br>C .� 0 .'// 2 sin 2 ' C 2� 0 .'/�.'/ cos ' sin ' C � 2 .'/ cos 2 '� d' 2 D �.� 0 .'// 2 C � 2 .'/� d' 2 :<br><!-- End of picture text -->

Odtud 



<!-- Start of picture text -->
ds D q .� 0 .'// 2 C � 2 .'/ d':<br><!-- End of picture text -->

Nyní již stačí dosadit do zadaného integrálu (nyní máme �<sup>0</sup> .'/ D 1), což vede na 



<!-- Start of picture text -->
� � arctg y x ds D � 0�=2 arctg ' '  cos  sin  ' ' q 1 2 C ' 2 d' D � 0�=2 ' q 1 C ' 2 d'<br>1 C ' 2 D t 2 ; d' D t dt='<br>D ˇˇˇˇ 0 ! 1; �=2 ! p 1 C � 2 =4 ˇˇˇˇ<br>1C� 2 =4 1C� 2 =4<br>D t 2 dt D 1 D 1 1 C � 2 � 1 :<br>� 1 p 3 ht 3i p 1 3 �� 4 �3=2 �<br><!-- End of picture text -->

Poznámka 19.5. V případě prostorové křivky � by se za analogických předpokladů vzorec definice 19.1 modifikoval na 



<!-- Start of picture text -->
� � f .x; y; z/ ds D � ab f .'.t/; .t/; �.t// q Œ' 0 .t/� 2 C Œ  0 .t/� 2 C Œ� 0 .t/� 2 dt:<br><!-- End of picture text -->

Pˇríklad 19.6. Určete hodnotu integrálu 



<!-- Start of picture text -->
� � q 2y 2 C z 2 ds; kde � D fŒx; y; z� 2 R 3 W x 2 C y 2 C z 2 D 4; x D y; x � 0; z � 0g:<br><!-- End of picture text -->

_Řešení._ Prostorová křivka � je průnikem kulové plochy (sféry) x<sup>2</sup> C y<sup>2</sup> C z<sup>2</sup> D 4 s rovinou y D x (procházející osou z), což je kružnice o poloměru 2. Omezení x � 0, z � 0 pak dává čtvrtkružnici (ležící ve III. oktantu). Tuto křivku lze snadno parametrizovat pomocí úhlů ', #, které vystupují v substituci do sférických souřadnic: 



<!-- Start of picture text -->
x D 2 cos 5� p 2 cos #; y D 2 sin 5� p 2 cos #; z D 2 sin #; 0 � # � �<br>4 cos # D � 4 cos # D � 2 :<br>Pro diferenciál oblouku ještě potřebujeme derivace parametrických rovnic:<br>x 0 D p 2 sin #; y 0 D p 2 sin #; z 0 D 2 cos #:<br><!-- End of picture text -->

Pro diferenciál oblouku ještě potřebujeme derivace parametrických rovnic: 

Kapitola 4. Kˇrivkové a plošné integrály 

88 

Podle výše uvedeného vzorce pak platí 



<!-- Start of picture text -->
� � q 2y 2 C z 2 ds D � 0�=2 q 4 cos 2 # C 4 sin 2 # q 2 sin 2 # C 2 sin 2 # C 4 cos 2 # d#<br>D 4 d# D 4Œ#� �=2 0 D 2�:<br>� 0�=2<br><!-- End of picture text -->

V případě křivkového integrálu druhého druhu přes rovinnou křivku budeme hodnoty 2-funkce dvou proměnných interpretovat jako vektory, budeme tedy hovořit o vektorovém poli a značit ho E f .x; y/ D .P.x; y/; Q.x; y//. 

Definice 19.7 — kˇrivkového integrálu II. druhu ze spojitého vektorového pole. Nechť � je orientovaná jednoduchá (nebo jednoduchá uzavřená) hladká křivka s parametrizací _F_ D Œ'; � a f<sup>E</sup> je vektorové pole spojité na nějaké otevřené množině obsahující křivku � . Pak definujeme křivkový integrál II. druhu 



<!-- Start of picture text -->
E<br>f .x; y/ � dsE D P.x; y/ dx C Q.x; y/ dy<br>� � � �<br>(��)<br>WD ˙ ŒP.'.t/; .t//' 0 .t/ C Q.'.t/; .t//  0 .t/� dt;<br>� ab<br><!-- End of picture text -->

kde znaménko „C“ bereme v případě souhlasné orientace křivky s parametrizací _F_ a znaménko „�“ v případě nesouhlasné. 

Motivace pro vzorec (��) je následující. Buď AB orientovaná úsečka s počátečním bodem A a koncovým bodem B. Uvažujeme-li konstantní silové pole f<sup>E</sup> , pak z fyziky je známo, že práce, kterou vykoná silové pole f<sup>E</sup> po úsečce AB, je dána skalárním součinem f<sup>E</sup> � .B � A/. Je-li tento skalární součin kladný, jedná se o vykonanou práci, je-li záporný, jedná se o spotřebovanou práci. Opačná orientace úsečky by znamenala práci s opačným znaménkem. 

E Jaká bude práce, kterou vykoná/spotřebuje silové pole f<sup>E</sup> D f .x; y/ po orientované křivce � ? Uvažujme opět nějaké dělení a D t0 < t1 < ��� < tn D b intervalu ha; bi (to opět určí dělení A D P0 � P1 ����� Pn D B křivky � ). Nahradíme-li orientované křivky �k WD fŒ'.t/; .t/� W t 2 htk�1; tkig (k D 1; 2; : : : ; n) orientovanými úsečkami Pk�1Pk a na každé z nich silové pole f<sup>E</sup> konstantním silovým polem s hodnotou f .'.t<sup>E</sup> k�1/; .tk�1//, pak získáme aproximaci vykonané práce 



<!-- Start of picture text -->
n<br>E<br>Wn WD X f .'.tk�1/; .tk�1// � .Pk � Pk�1/<br>kD1<br>n<br>E<br>D<br>X f .'.tk�1/; .tk�1// � .'.tk/ � '.tk�1/; .tk/ �  .tk�1//:<br>kD1<br><!-- End of picture text -->

Přepíšeme-li rozdíly '.tk/ � '.tk�1/ a .tk/ � .tk�1/ pomocí Lagrangeovy věty o střední hodnotě, dostaneme 



<!-- Start of picture text -->
n<br>E<br>Wn WD X f .'.tk�1/; .tk�1// � .' 0 .�k/;  0 .�k//.tk � tk�1/:<br>kD1<br><!-- End of picture text -->

Pomocí Heineho–Cantorovy věty lze opět ukázat, že 



<!-- Start of picture text -->
n<br>E<br>nlim!1 Wn D n lim !1 X f .'.tk�1/; .tk�1// � .' 0 .tk�1/;  0 .tk�1//.tk � tk�1/:<br>kD1<br><!-- End of picture text -->

Suma za znakem limity na pravé straně předchozího vztahu představuje integrální součet spojité funkce, takže v limitě (pro n ! 1) Wn dává pravou stranu vzorce (��) pro libovolnou nulovou posloupnost dělení intervalu ha; bi. 

19 Kˇrivkový integrál 

89 

Pˇríklad 19.8. Určete .xy; 0/ � dsE, kde � je část paraboly x D y<sup>2</sup> jdoucí z bodu Œ1; 1� do počátku Œ0; 0�. � � 

_Řešení._ Vzhledem k parametrizaci x D t<sup>2</sup> , y D t, 0 � t � 1 je křivka � orientována nesouhlasně. Dosazením do vzorce .��/ pak máme 



<!-- Start of picture text -->
.xy; 0/ � dsE D � .t 3 ; 0/ � .2t; 1/ dt D � 2t 4 dt D � 2t 5 D � 2<br>� � � 01 � 01 5 5 :<br>" #10<br><!-- End of picture text -->

Poznámka 19.9. Vztah mezi křivkovým integrálem I. a II. druhu je následující. Je-li � jednoduchá (resp. jednoduchá uzavřená) hladká křivka s parametrizací _F_ D Œ'; �, tak tečný vektor _F_<sup>0</sup> .t/ D .'<sup>0</sup> .t/;<sup>0</sup> .t// je nenulový v každém 8t 2 ha; bi. Potom vektor _F_ 1<sup>0.t/ D</sup><sup>_F_0.t/=j</sup><sup>_F_0.t/j je jednotkový (j�j je eukleidovská</sup> velikost vektoru). Uvažujeme-li spojité vektorové pole f<sup>E</sup> v nějaké oblasti obsahující křivku � , pak platí 



<!-- Start of picture text -->
fE � dsE D ˙ fE � F 1 0 ds<br>� � � �<br><!-- End of picture text -->

(„C“ v případě souhlasné orientace křivky � s parametrizací _F_ a „�“ v případě nesouhlasné). 

Následující tvrzení dává do souvislosti dvojný integrál přes množinu M s křivkovým integrálem II. druhu přes hranici množiny M . Řekneme, že _hranice_ @M _množiny_ M _je orientována kladně_ , jestliže množina při pohybu po @M zůstává po levé ruce. 

■ Vˇeta 19.10 — Greenova<sup>1</sup> pˇres normální množinu vzhledem k ose **x** . _Nechť_ M _je normální množina vzhledem k ose_ x _(tj._ M D fŒx; y� 2 R<sup>2</sup> W a � x � b; '.x/ � y � .x/g _a její hranice_ @M _je kladně orientovaná křivka, přičemž předpokládáme, že funkce_ '; _mají spojitou derivaci na_ ha; bi _. Nechť dále vektorové pole_ f<sup>E</sup> D .P; Q/ _je spojité na_ M _a má zde spojité parciální derivace_ Py<sup>0</sup><sup>_a_Q</sup> x<sup>0</sup><sup>_. Pak platí_</sup> 



<!-- Start of picture text -->
.Qx 0 � P y  0 / dxdy D .P; Q/ � ds:E<br>� M @M<br><!-- End of picture text -->

_Důkaz._ Protože M je normální vzhledem k ose x, její hranici @M lze složit ze čtyř částí �` W x D a; y 2 h'.a/; .a/i, �d W y D '.x/, x 2 ha; bi, �p W x D b; y 2 h'.b/; .b/i a �h W y D .x/, x 2 ha; bi. Části hranice �` a �p jsou zřejmě (vzhledem ke vhodné parametrizaci) jednoduché hladké křivky a díky předpokladu spojitosti derivací funkcí '; jsou i části hranice �d a �h jednoduché hladké křivky (např. vzhledem k parametrizaci Œt; '.t/�, resp. Œt; .t/�). Platnost tvrzení bude prokázána, pokud ukážeme, že 



<!-- Start of picture text -->
� Py 0 .x; y/ dxdy D P.x; y/ dx a Qx 0 .x; y/ dxdy D Q.x; y/ dy:<br>� M � @M � M � @M<br>P.x; y/ dx D P.x; y/ dx C P.x; y/ dx C P.x; y/ dx C P.x; y/ dx;<br>� @M � �` � �d � �p � �h<br>„ ƒ‚ … „ ƒ‚ …<br>D0; protože ' 0 .t/D0 D0; protože ' 0 .t/D0<br><!-- End of picture text -->

Platí 

tj. 



<!-- Start of picture text -->
P.x; y/ dx D P.x; y/ dx C P.x; y/ dx D P.x; '.x// dx � P.x; .x// dx<br>� @M � �d � �h � ab � ab<br>D<br>ŒP.x; '.x// � P.x; .x//� dx:<br>� ab<br>Na druhou stranu, podle Fubiniovy věty<br>� � M Py 0 .x; y/ dxdy D � � ab� � '.x/ .x/ Py 0 .x; y/ dy �dx D � � abŒP.x; y/�  .x/ '.x/ dx<br><!-- End of picture text -->

Na druhou stranu, podle Fubiniovy věty 

1George Green 1793–1841, Angličan 

Kapitola 4. Kˇrivkové a plošné integrály 

90 



<!-- Start of picture text -->
D<br>ŒP.x; '.x// � P.x; .x//�dx;<br>� ab<br><!-- End of picture text -->

tj. platí � � M<sup>P.x; y/ dxdyD</sup> � @M<sup>P.x; y/dx.</sup> Důkaz druhé rovnosti � M<sup>Q.x; y/ dxdyD</sup> � @M<sup>Q.x; y/ dx je trochu obtížnější, opírá se o následující</sup> vlastnost integrálu závislého na parametru: 

_Nechť_ f W R<sup>2</sup> ! R _je spojitá funkce na nějaké otevřené množině_ ˝ _obsahující normální množinu_ M D fŒx; y� 2 R<sup>2</sup> W a � x � b; '.x/ � y � .x/g _. Potom integrál_ F.x/ WD � '.x/ .x/<sup>f .x; y/ dy</sup><sup>_je_</sup> _spojitá funkce na_ ha; bi _. Má-li navíc_ f _spojitou parciální derivaci_ fx<sup>0</sup><sup>_na_˝</sup><sup>_a_'0;0</sup><sup>_jsou spojité na_ha; bi</sup><sup>_,_</sup> _pak_ F _má derivaci na_ ha; bi _a platí_ 



<!-- Start of picture text -->
F 0 .x/ D fx 0 .x; y/ dy C f .x; .x//  0.x/ � f .x; '.x//'0.x/: (4)<br>� '.x/ .x/<br><!-- End of picture text -->

Rovnost (4) využijeme při výpočtu � M<sup>Q</sup> x<sup>0.x; y/ dxdy. Fubiniova věta dává</sup> 



<!-- Start of picture text -->
Qx 0 .x; y/ dxdy D Qx 0 .x; y/ dy dx:<br>� M � ab� � '.x/ .x/ �<br><!-- End of picture text -->

Položíme-li f D Q v rovnosti (4), pak 



<!-- Start of picture text -->
Qx 0 .x; y/ dy D F 0.x/ � Q.x; .x//  0.x/ C Q.x; '.x//'0.x/<br>� '.x/ .x/<br><!-- End of picture text -->

a tedy 



<!-- Start of picture text -->
Qx 0 .x; y/ dxdy D ŒF.x/�b a � Q.x; .x//  0 .x/ dx C Q.x; '.x//' 0 .x/ dx<br>� M � ab � ab<br>D<br>f .b; y/ dy � f .a; y/ dy � Q.x; .x//  0 .x/ dx C Q.x; '.x//' 0 .x/ dx:<br>� '.b/ .b/ � '.a/ .a/ � ab � ab<br>Zároveň však platí<br>Q.x; y/ dy D Q.x; y/ dy C Q.x; y/ dy C Q.x; y/ dy C Q.x; y/ dy<br>� @M � �p � �` � �h � �d<br>D<br>f .b; y/ dy � f .a; y/ dy � Q.x; .x//  0 .x/ dx C Q.x; '.x//' 0 .x/ dx;<br>� '.b/ .b/ � '.a/ .a/ � ab � ab<br>tj. Q.x; y/ dxdy D Q.x; y/ dx.<br>� M � @M<br><!-- End of picture text -->

Poznámka 19.11. a) Analogicky by se tvrzení dokázalo pro normální množinu vzhledem k ose y. 

b) Tvrzení zůstane v platnosti, i když části hranice �d a �h budou po částech hladké křivky. 

c) Tvrzení dále bude platit i v případě, kdy M je regulární množina (připomeňme, že to je množina, kterou lze „rozřezat“ na konečný počet normálních množin). 

d) Platnost tvrzení lze rozšířit i na případ ještě komplikovanějších množin než jsou regulární množiny (např. typu „řez ementálem s nepříliš pěknými oky“). Zejména lze (za určitých dalších předpokladů) připustit hranice, které obsahují konečný počet singulárních bodů. 

e) Obsah (míru) ohraničené množiny M lze pomocí Greenovy věty počítat jako 



<!-- Start of picture text -->
�.M/ D 1 x dy � y dx:<br>2 � @M<br><!-- End of picture text -->

Pˇríklad 19.12. Určete obsah eliptické výseče mezi body A D Œ'.t1/; .t1/� a B D Œ'.t1/; .t2/�, kde Œ'.t/; .t/� D Œa cos t; b sin t�, a; b > 0, 0 � t1 < t2 �<sup>�</sup> =2. 

19 Kˇrivkový integrál 

91 

_Řešení._ Budeme integrovat přes hranici eliptické úseče, která se skládá ze tří hladkých částí: úsečky OA, oblouku elipsy AB<sup>¿</sup> a úsečky BO (O značí počátek). Aby platil vzorec nad příkladem, je potřeba hranici úseče orientovat kladně, tj. ve směru O ! A ! B ! O. Úsečku OA parametrizujme např. rovnicemi x D at cos t1, y D bt sin t1, t 2 h0; 1i, vůči této parametrizaci je orientace úsečky souhlasná. Příslušný křivkový integrál je potom vyjádřen 



<!-- Start of picture text -->
.�y; x/ � dsE D .�bt sin t1; at cos t1/ � .a cos t1; b sin t1/ dt D 0 dt D 0:<br>� OA � 01 � 01<br><!-- End of picture text -->

Oblouk AB<sup>¿</sup> je vůči parametrizaci x D a cos t , y D b sin t , t 2 ht1; t2i (viz zadání) orientován souhlasně, platí tedy 



<!-- Start of picture text -->
¿ .�y; x/ � dsE D .�b sin t; a cos t/ � .�a sin t; b cos t/ dt<br>� AB � t1t2<br>D ab .sin 2 t C cos 2 t/ dt D ab dt D ab.t2 � t1/:<br>� t1t2 � t1t2<br><!-- End of picture text -->

Integrál přes úsečku BO bude, podobně jako integrál přes úsečku OA, nulový. Celkově tedy 



<!-- Start of picture text -->
�.úseče/ D 1 .�y; x/ � dsE C 1 ¿ .�y; x/ � dsE C 1 .�y; x/ � dsE<br>2 � OA 2 � AB 2 � BO<br>D 0 C 2 1 ab.t2 � t1/ C 0 D 1 2 ab.t2 � t1/:<br><!-- End of picture text -->

Poznamenejme, že pro t1 D 0 a t2 D 2� dostáváme celou elipsu, vzorec tedy souhlasí se známým vzorcem pro obsah množiny ohraničené elipsou S D �ab (ten se redukuje na vzorec pro obsah kruhu, je-li a D b). 

Poznámka 19.13. To, že v předchozím příkladu byly integrály přes obě úsečky vycházející z počátku nulové, není náhoda. Plyne to z faktu, že práci přes úsečku spojující počátek s nějakým bodem roviny koná silové pole f .x; y/<sup>E</sup> D .�y; x/. V každém bodě Œx; y� úsečky je tento vektor kolmý k úsečce, což znamená, že žádnou práci nevykoná. Obecně tedy, při výpočtu obsahu pomocí Greenovy věty, integrály přes úsečky vycházející z počátku není potřeba počítat. 

#### Pˇríklady k procviˇcení 

19.1. Určete hodnotu křivkového intgerálu 



<!-- Start of picture text -->
p 1 C 4x 2 ds; � D fŒx; y� 2 R 2 W y D x 2 ; 0 � x � 3=2g:<br>� �<br><!-- End of picture text -->

19.2. Napište vzorce pro statický moment Sxy (vzhledem k rovině xy), prostorové křivky � o jednotkové délkové hustotě, která vznikne průnikem válcové plochy x<sup>2</sup> C y<sup>2</sup> D 4 a parabolického válce z D x<sup>2</sup> . 

19.3. Určete hodnotu křivkového integrálu 



<!-- Start of picture text -->
.y; x/ � ds;E<br>� �<br><!-- End of picture text -->

kde � je čtvrtina elipsy x<sup>2</sup> =4Cy<sup>2</sup> =9 D 1, ležící v I . kvadrantu orientovaná proti smyslu oběhu hodinových ručiček. 

19.4. Uvažujte v R<sup>3</sup> silové pole f<sup>E</sup> D �x<sup>E</sup> i � yj=2<sup>E</sup> � 2zk<sup>E</sup> . V tomto poli se bod o jednotkové hmotnosti vzdálený 2 m od osy z kolem ní otáčí konstantní úhlovou rychlostí �=2 rad � s<sup>�1</sup> a současně se pohybuje konstantní rychlostí 3/2 m � s<sup>�1</sup> v kladném směru osy z (pohyb je tedy realizován po šroubovici). Vypočtěte práci, kterou vykoná silové pole za dobu t D 4 s, je-li na počátku bod v poloze Œ2; 0; 0�. 

Kapitola 4. Kˇrivkové a plošné integrály 

92 

19.5. Pomocí Greenovy věty odvoďte, že pro dostatečně rozumné množiny M � R<sup>2</sup> platí následující vzorec pro výpočet obsahu (míry) této množiny: 



<!-- Start of picture text -->
�.M/ D 1 .�y; x/ � ds;E<br>2 � @M<br><!-- End of picture text -->

kde @M je kladně orientovaná hranice množiny M . 

19.6. Pomocí předchozího vzorce odvoďte vzorec pro obsah kruhu o poloměru r. 

_Výsledky._ 19.1. 6. 19.2. Sxy D 8 � 02� .cos<sup>2</sup> t/ ~~p~~ 1 C 4 sin<sup>2</sup> 2t dt. 19.3. 0. 19.4. �36 (práce se tedy spotřebovala). 19.6. �r<sup>2</sup> . 

### 20 Nezávislost kˇrivkového integrálu na integraˇcní cestˇe 

Definice 20.1 — nezávislosti kˇrivkového integrálu na integraˇcní cestˇe. Nechť ˝ je oblast (tj. souvislá a otevřená množina) v R<sup>2</sup> , f<sup>E</sup> D .P; Q/ W R<sup>2</sup> ! R<sup>2</sup> je spojité vektorové pole na ˝, A D ŒxA; yA� a B D ŒxB ; yB � jsou body v ˝ a � je jednoduchá po částech hladká křivka ležící v ˝ jdoucí z bodu A do bodu B. Pokud hodnota integrálu � � f<sup>E</sup> � dsE zůstává stejná pro každou křivku � , říkáme, že _integrál nezávisí na integrační cestě mezi body_ A; B a píšeme 



<!-- Start of picture text -->
fE � ds:E<br>� AB<br><!-- End of picture text -->

Jestliže uvedený integrál nezávisí na integrační cestě mezi libovolnými body A, B (zvolenými kdekoliv v oblasti ˝), říkáme, že _integrál nezávisí na integrační cestě v oblasti_ ˝. 

■ Vˇeta 20.2. _Nechť_ � �<sup>.P; Q/ �dsE</sup><sup>_nezávisí na integrační cestě v oblasti_˝</sup><sup>_. Potom výraz_</sup> 



<!-- Start of picture text -->
P.x; y/ dx C Q.x; y/ dy<br><!-- End of picture text -->

_(Pfaffova_<sup>2</sup> _forma) je totálním diferenciálem kmenové funkce (potenciálu)_ 



<!-- Start of picture text -->
˚.x; y/ D .P; Q/ � dsE<br>� ŒxŒx;y�A;yA�<br><!-- End of picture text -->

_(zápis chápeme tak, že integrujeme po libovolné po částech hladké křivce ležící v oblasti_ ˝ _spojující libovolný, ale pevně zvolený bod_ A D ŒxA; yA� _s „proměnlivým“ bodem_ B D Œx; y� _)._ 

_Důkaz._ Nechť integrál z f<sup>E</sup> D .P; Q/ nezávisí v ˝ na integrační cestě. Potřebujeme ukázat, že funkce ˚ vystupující ve větě je v ˝ diferencovatelná a platí d˚ D P dx C Qdy (tj. ˚x<sup>0DP , ˚</sup> y<sup>0DQ). Buď</sup> B D Œx; y� 2 ˝ nějaký bod. Protože ˝ je otevřená množina, existuje okolí bodu B takové, že je celé obsaženo v ˝. Vezměme v tomto okolí libovolný bod B1 D Œx1; y�, x1 < x (druhou souřadnici má tedy E bod B1 stejnou jako bod B). Protože hodnota integrálu � AB f � dsE je pro každou po částech hladkou křivku stejná, můžeme jednu konkrétní vybrat. Uvažujme křivku, která se skládá z libovolné jednoduché hladké křivky �1 jdoucí z bodu A do bodu B1 a úsečky �2 jdoucí z bodu B1 do bodu B o parametrizaci Œt; y�, x1 � t � x (vzhledem k této parametrizaci je úsečka �2 souhlasně orientovanou jednoduchou hladkou křivkou). Máme tedy 



<!-- Start of picture text -->
˚.x; y/ D .P; Q/ � dsE C .P; Q/ � dsE<br>� �1 � �2<br><!-- End of picture text -->

Hodnota prvního integrálu je nějaké reálné číslo, a tudíž parciální derivace tohoto člene podle x je nulová. Máme tedy 



<!-- Start of picture text -->
˚x 0 .x; y/ D @ .P; Q/ � dsE D @ P.t; y/ dt D P.x; y/;<br>@x � �2 @x � xx1<br><!-- End of picture text -->

2Johann Friedrich Pfaff 1765–1825, Němec 

20 Nezávislost kˇrivkového integrálu na integraˇcní cestˇe 

93 

kde v poslední rovnosti jsme využili větu 22.6 z Matematické analýzy I (resp. jejího důsledku 22.8), která říká, že integrál jako funkce horní meze ze spojité funkce má derivaci rovnu původní funkci. Analogicky bychom ukázali platnost Qy<sup>0DQ(zakřivku�2bychomnyníuvažovaliúsečkuvedoucídoboduB</sup> rovnoběžnou s osou y). Protože funkce P , Q jsou v ˝ spojité (to je v předpokladu definice nezávislosti integrálu na integrační cestě), je ˚ na ˝ (spojitě) diferencovatelná. Celkově tedy d˚ D P dx C Qdy. 

Poznámka 20.3. a) Vektorové polef<sup>E</sup> W R<sup>n</sup> ! R<sup>n</sup> spojité na nějaké oblasti ˝ � R<sup>n</sup> se nazývá _potenciálové v_ ˝, jestliže existuje funkce ˚ W R<sup>n</sup> ! R taková, že f<sup>E</sup> D grad ˚ v každém bodě oblasti ˝. Protože pro totální diferenciál diferencovatelné funkce F platí 



<!-- Start of picture text -->
dF D Fx 0 1 dx1 C F x  0 2 dx2 C ���C F x  0 n dxn D grad F � .dx1; dx2; : : : ; dxn/;<br><!-- End of picture text -->

lze předchozí větu formulovat takto: Pokud křivkový integrál II. druhu vektorového pole f<sup>E</sup> W R<sup>2</sup> ! R<sup>2</sup> nezávisí na integrační cestě v oblasti ˝, pak je toto pole potenciálové v ˝. 

b) Potenciál se v literatuře někdy uvažuje s opačným znaménkem, tj. je li ˚ kmenová funkce, pak funkce � D �˚ se nazývá potenciál. 

■ Vˇeta 20.4. _Nechť_ P _,_ Q _jsou spojité funkce v rovinné oblasti_ ˝ _a nechť Pfaffova forma_ P dx C Q dy _je v_ ˝ _totálním diferenciálem nějaké funkce_ ˚ _(tj. pole_ f<sup>E</sup> D .P; Q/ _je zde potenciálové). Potom integrál_ � � f<sup>E</sup> � dsE _nezávisí na integrační cestě v_ ˝ _a platí_ 



<!-- Start of picture text -->
fE � dsE D P dx C Q dy D ˚.B/ � ˚.A/:<br>� AB � AB<br><!-- End of picture text -->

_Důkaz._ Nechť je splněn předpoklad věty, tj. vektorové pole f<sup>E</sup> D .P; Q/ je potenciálové v ˝. Existuje tedy funkce ˚ W R<sup>2</sup> ! R taková, že .P; Q/ D grad ˚ v ˝. Nechť dále � � ˝ je libovolná jednoduchá po částech hladká křivka spojující body A; B 2 ˝, která je orientována souhlasně se svou parametrizací _F_ .t/ D Œ'.t/; .t/�, t 2 ha; bi. Potom 



<!-- Start of picture text -->
P.x; y/ dx C Q.x; y/ dy D .P.x; y/; Q.x; y// � dsE D grad ˚.x; y/ � dsE<br>� � � � � �<br>D �˚x 0 �'.t/; .t/�; ˚y 0 �'.t/; .t/�� � �' 0 .t/;  0 .t/� dt<br>� ab<br>D � ab�˚x 0 �'.t/; .t/�' 0 .t/ C ˚y 0 �'.t/; .t/� 0 .t/� dt D � ab�˚�'.t/; .t/� � 0 dt<br>D �˚�'.t/; .t/��ba D ˚ �'.b/; .b/� � ˚�'.a/; .a/� D ˚.B/ � ˚.A/;<br><!-- End of picture text -->

kde první rovnost v posledním řádku plyne z pravidla pro derivaci složené funkce a druhá plyne z Newtonovy–Leibnizovy formule. Protože křivka mezi body A a B byla libovolná, integrál nezávisí na integrační cestě (přesněji, důkaz jsme provedli pouze pro jednoduchou hladkou křivku, pro po částech hladkou křivku by se důkaz modifikoval snadno, viz první poznámka e) v kapitole 19). 

Poznámka 20.5. a) Předchozí dvě věty tedy říkají, že pro nezávislost integrálu na integrační cestě v oblasti ˝ je nutné a stačí, aby existovala funkce ˚ W ˝ ! R, pro kterou platí, že P dx C Q dy je v ˝ jejím totálním diferenciálem. 

b) Na větu lze nahlížet jako na zobecnění tvrzení o Newtonově–Leibnizově formuli. To ve své základní verzi říká, že pro spojitou funkci f na uzavřeném intervalu ha; bi, která zde má primitivní funkci F (tu lze chápat jako jednorozměrný potenciál), platí � ab<sup>f .x/ dxD F.b/ �F.a/.</sup> 

c) Věta umožňuje snazší výpočet práce potenciálového (konzervativního) silového pole, kdy je tato práce dána rozdílem potenciálních energií v koncovém a počátečním bodě křivky. V případě uzavřené křivky je 



<!-- Start of picture text -->
fE � dsE D ˚.B/ � ˚.A/ D ˚.A/ � ˚.A/ D 0;<br>�<br><!-- End of picture text -->

Kapitola 4. Kˇrivkové a plošné integrály 

94 

a tedy potenciálové silové pole žádnou práci nevykoná. Podmínka 



<!-- Start of picture text -->
fE � dsE D 0<br>�<br><!-- End of picture text -->

přes libovolnou uzavřenou po částech hladkou křivku � je zároveň postačující podmínkou pro nezávislost na integrační cestě (potenciálovost pole f<sup>E</sup> ). To plyne z jednoduché úvahy. Označme A společný počáteční a koncový uvažované křivky � a zvolme na křivce bod B. Tento bod rozdělí křivku na dvě části. Označme �1 část jdoucí z bodu A do bodu B a �2 část jdoucí z bodu B do bodu A. Pak platí 



<!-- Start of picture text -->
E E E E E<br>0 D f � dsE D f � dsE C f � dsE H) f � dsE D � f � ds:E<br>� � �1 � �2 � �1 � �2<br><!-- End of picture text -->

Pokud symbolem �2<sup>�nyní označíme opačně orientovanou křivku �2(ta nyní jde z bodu A do bodu B),</sup> tak vidíme, že 



<!-- Start of picture text -->
fE � dsE D fE � ds;E<br>� �1 � �2 �<br><!-- End of picture text -->

a protože � byla libovolná uzavřená po částech hladká křivka, plyne z poslední rovnosti nezávislost integrálu na integrační cestě (což je ekvivalentní s potenciálovostí integrovaného vektorového pole). 

Z praktického hlediska je podstatná následující věta, která dává postačující podmínku pro nezávislost na integrační cestě. Oblast ˝ se nazývá _jednoduše souvislá_ , jestliže každou uzavřenou křivku ležící v ˝ lze „stáhnout“ v bod, aniž bychom oblast opustili. Jednoduše souvislá oblast tedy nemá žádné „díry“. 

■ Vˇeta 20.6 — postaˇcující podmínka pro nezávislost integrálu na integraˇcní cestˇe. _Nechť_ ˝ _je jednoduše souvislá oblast v_ R<sup>2</sup> _,_ P; Q _jsou spojité spolu s parciálními derivacemi_ Py<sup>0</sup><sup>_,_Q</sup> x<sup>0</sup><sup>_na_˝</sup><sup>_a platí_</sup> 



<!-- Start of picture text -->
Py 0 .x; y/ D Q x 0 .x; y/ 8Œx; y� 2 ˝:<br><!-- End of picture text -->



<!-- Start of picture text -->
Potom P dx C Q dy nezávisí na integrační cestě v  ˝ .<br>� �<br><!-- End of picture text -->

_Důkaz._ Z poznámky 20.5c) již víme, že nezávislost integrálu na integrační cestě je ekvivalentní tomu, že integrál po libovolné po částech hladké uzavřené křivce ležící v oblasti ˝ je nulový. Dále, v duchu poznámky 19.11 lze dokázat, že Greenova věta platí, pokud budeme uvažovat kompaktní množinu v rovině, jejíž hranice je po částech hladká uzavřená křivka. Vezměme tedy v jednoduše souvislé oblasti ˝ libovolnou po částech hladkou uzavřenou křivku � a uzavřenou množinu M � ˝ takovou, že @M D � . Protože vektorové pole f<sup>E</sup> je spojité spolu s parciálními derivacemi Py<sup>0, Q</sup> x<sup>0na ˝, a tedy i na M, podle Greenovy</sup> věty platí 



<!-- Start of picture text -->
.Qx 0 � P y  0 / dxdy D fE � ds:E<br>� M �<br><!-- End of picture text -->

Dvojný integrál na levé straně je však nulový díky rovnosti Py<sup>0D Q</sup> x<sup>0, tedy je nulový také křivkový integrál</sup> na pravé straně, a protože po částech hladká uzavřená křivka � byla volena libovolně, integrál ve větě nezávisí na integrační cestě. 

Poznámka 20.7. a) Má-li pole f<sup>E</sup> D .P; Q/ uvedené parciální derivace spojité, podmínka Py<sup>0DQ</sup> x<sup>0</sup> v ˝ je zároveň nutnou podmínkou pro nezávislost integrálu na integrační cestě, resp. existenci potenciálu (i v případě oblasti, která není jednoduše souvislá). To plyne ihned ze Schwarzovy věty: Py<sup>0D .˚</sup> x<sup>0/</sup> y<sup>0D</sup> ˚xy<sup>00D ˚</sup> yx<sup>00D .˚</sup> y<sup>0/</sup> x<sup>0D Q</sup> x<sup>0.</sup> 

b) Předpoklad jednoduše souvislé oblasti obecně nelze vynechat. Pokud oblast není jednoduše souvislá, tak vektorové pole f<sup>E</sup> může, ale také nemusí mít potenciál. Např. pole 



<!-- Start of picture text -->
E x y<br>f .x; y/ D<br>p x 2 C y 2 ; p x 2 C y 2 !<br><!-- End of picture text -->

20 Nezávislost kˇrivkového integrálu na integraˇcní cestˇe 

95 

je spojité na ˝ D R<sup>2</sup> n fŒ0; 0�g a není těžké nalézt potenciál (lze i uhodnout) ˚.x; y/ D ~~p~~ x<sup>2</sup> C y<sup>2</sup> C C . Podle věty 20.4 tedy integrál � � f<sup>E</sup> � dsE nezávisí na integrační cestě. Uvažujme nyní např. vektorové pole 



<!-- Start of picture text -->
�y x<br>g.x; y/E  D ;<br>� x 2 C y 2 ; x 2 C y 2 �<br><!-- End of picture text -->

které je spojité opět na oblasti ˝ D R<sup>2</sup> n fŒ0; 0�g. Spočítejme integrál � �<sup>gE �dsE přes jednotkovou kružnici</sup> se středem v počátku: 



<!-- Start of picture text -->
gE � dsE D .� sin t.� sin t/ C cos t cos t/ dt D 1 dt D 2�;<br>� � � 02� � 02�<br><!-- End of picture text -->

což znamená, že integrál závisí na integrační cestě (podle věty 20.4 tedy gE nemůže mít v R<sup>2</sup> n Œ0; 0� potenciál). 

c) V případě integrálu vektorového pole f<sup>E</sup> D .P; Q; R/ přes prostorovou křivku � bychom nezávislost na integrační cestě definovali analogicky. Obsah vět 20.2, 20.4 a 20.6 zůstává v platnosti, přičemž podmínka z věty 20.6 se modifikuje na 



<!-- Start of picture text -->
rot f E WD det 0 @xE@i @yj@E @zk@E 1 � @R@y � @ @z Q ; @P @z � @R @x ; @ @x Q � @P @y � D o:E<br>B@ P Q R CA D<br><!-- End of picture text -->

To znamená, že postačující podmínkou pro nezávislost integrálu na integrační cestě v jednoduše souvislé prostorové oblasti ˝ jsou rovnosti Ry<sup>0D Q</sup> z<sup>0, P 0</sup> z<sup>D R</sup> x<sup>0, Q</sup> x<sup>0D P</sup> y<sup>0v ˝. Důkaz nyní využívá Stokesovu</sup> větu, viz kapitola 22. 

Pˇríklad 20.8. Rozhodněte, zda vektorové pole f<sup>E</sup> D .xy<sup>2</sup> � 2; x<sup>2</sup> y C 5y<sup>2</sup> / je potenciálové (konzervativní), pokud ano, nalezněte příslušný potenciál. 

_Řešení._ Platí Py<sup>0D2xyDQ</sup> x<sup>0v každém bodě roviny, a tedy vektorové pole</sup> f<sup>E</sup> je potenciálové v celé rovině R<sup>2</sup> (množina R<sup>2</sup> je jednoduše souvislou oblastí). Protože P D ˚x<sup>0, Q D ˚</sup> y<sup>0, musí naopak být</sup> 



<!-- Start of picture text -->
˚ D P dx nebo ˚ D Q dy:<br>� �<br>˚.x; y/ D .xy 2 � 2/ dx D 1<br>� 2 x2y2 � 2x C c.y/<br><!-- End of picture text -->

Uvažujeme-li např. první variantu, pak 

a zbývá určit funkci c. Tu získáme tak, že předchozí rovnost derivujeme podle opačné proměnné, než jsme integrovali (v našem případě podle y); získaná rovnost se pak musí rovnat složce Q. Máme tedy 



<!-- Start of picture text -->
˚y 0 .x; y/ D x2y C c0.y/ D x2y C 5y2: Odtud c 0 .y/ D 5y 2 H) c.y/ D 5 � y 2 dy D 5 3 y3 C C:<br>Celkově<br><!-- End of picture text -->



<!-- Start of picture text -->
˚.x; y/ D 2 1 x2y2 � 2x C 5 3 y3 C C:<br><!-- End of picture text -->

Tuto funkci by také bylo možné získat z křivkového integrálu zadaného vektorového pole po libovolné křivce spojující body ŒxA; yA� a Œx; y� (nejjednodušeji po úsečce). 

Poznámka 20.9. Kmenová funkce (potenciál) je, podobně jako primitivní funkce k funkci jedné proměnné, určena jednoznačně až na aditivní konstantu C 2 R. 



<!-- Start of picture text -->
Pˇríklad 20.10. Určete hodnotu integrálu .2xy; x 2 � z; 1 � y/ � dsE.<br>� Œ1;0;0�Œ2;�1;3�<br><!-- End of picture text -->

Kapitola 4. Kˇrivkové a plošné integrály 

96 

_Řešení._ Ověřme, že vektorové pole je skutečně potenciálové. Platí 



<!-- Start of picture text -->
Ry 0 D �1 D Q z 0 ; Pz 0 D 0 D R x 0 ; Qx 0 D 2x D P y  0 8Œx; y; z� 2 R 3 :<br><!-- End of picture text -->

To znamená, že rot f<sup>E</sup> D oE v R<sup>3</sup> , a tedy f<sup>E</sup> je v celém prostoru potenciálové. Potenciál můžeme vypočítat stejnou technikou jako v předchozím příkladě, tj. vyjdeme z faktu ˚x<sup>0D P , ˚</sup> y<sup>0D Q, ˚</sup> z<sup>0D R. Odtud</sup> např. 



<!-- Start of picture text -->
˚.x; y; z/ D R.x; y; z/ dz D .1 � y/ dz D z � yz C c.x; y/:<br>� �<br><!-- End of picture text -->

Funkci c určíme tak, že předchozí rovnost parciálně zderivujeme (postupně podle x a y) a využijeme, že ˚x<sup>0D P , ˚</sup> y<sup>0D Q. Máme tedy</sup> 



<!-- Start of picture text -->
˚x 0 .x; y; z/ D c x 0 .x; y/ D 2xy a ˚y 0 .x; y; z/ D �z C c y 0 .x; y/ D x2 � z;<br><!-- End of picture text -->

tj. 



<!-- Start of picture text -->
cx 0 .x; y/ D 2xy a cy 0 .x; y/ D x2:<br><!-- End of picture text -->

Integrací druhé rovnosti vzhledem k y pak máme c.x; y/ D x<sup>2</sup> y C k.x/. Zbývá určit funkci k. Derivujme poslední rovnost podle x, což vede na cx<sup>0.x; y/ D 2xyCk0.x/ a díky výše uvedené rovnosti c</sup> x<sup>0.x; y/ D 2xy</sup> platí cx<sup>0.x; y/D2xyC k0.x/D2xy,nebolik0.x/D0.Toznamená,žek.x/DC,kdeC2Rje</sup> libovolná konstanta. Kmenová funkce má tedy tvar 



<!-- Start of picture text -->
˚.x; y; z/ D z � yz C x 2 y C C<br><!-- End of picture text -->

a hodnota integrálu je 



<!-- Start of picture text -->
.2xy; x 2 � z; 1 � y/ � dsE D ˚.2; �1; 3/ � ˚.1; 0; 0/ D 2 C C � C D 2:<br>� Œ1;0;0�Œ2;�1;3�<br><!-- End of picture text -->

#### Pˇríklady k procviˇcení 

20.1. Rozhodněte, zda dané vektorové pole je potenciálové v oblasti ˝ a v kladném případě určete potenciál: 



<!-- Start of picture text -->
E y<br>a) f .x; y/ D ; ˝ D R C � R C ;<br>� .xx C C y/ 2y 2 ; .x C y/ 2 �<br>E 1 1 1 3 1 3<br>b) f .x; y/ D � ; ˝ D R C � R C � R C :<br>� x 2 y C x 2 z ; � xy 2 � y 2 z ; xz 2 � yz 2 �<br><!-- End of picture text -->

20.2. Rozhodněte, zda silové pole f<sup>E</sup> D .�y; x/ je konzervativní a určete práci, kterou vykoná po úsečce z bodu Œ0; 0� do bodu Œ3; 2�. 

20.3. Vypočtěte práci W , kterou vykoná tíhové pole f<sup>E</sup> D �mgk<sup>E</sup> z bodu A D ŒxA; yA; zA� do bodu B D ŒxB ; yB ; zB �. 

20.4. Určete cirkulaci vektorového pole f .x; y/<sup>E</sup> D x<sup>3E</sup> i � y<sup>3 E</sup> j (tj. integrál � f<sup>E</sup> � dsE) po uzavřené křivce � , která se skládá z části kružnice x D r cos t, y D r sin t, t 2 h0; �=2i a úseček spojujících konce části kružnice s počátkem. Takto křivka je orientována kladně. Úlohu řešte dvěma způsoby: a) spočítejte křivkový integrál, b) využijte poznatků o nezávislosti integrálu na integrační cestě. 

20.5. Vypočtěte integrál 



<!-- Start of picture text -->
.2x C 3y C sin z 2 ; 2x; 2xz cos z 2 / � ds:E<br>� Œ0;0;0�Œ1;0;0�<br><!-- End of picture text -->

_Výsledky._ 20.1. a) ˚.x; y/ D ln.x C y/ � xCy y<sup>C C, b) ˚.x; y; z/ D �</sup> xy<sup><u>1</u>�</sup> xz<sup><u>1</u>C</sup> yz<sup><u>3</u>C C. 20.2. Není</sup> a práce je nulová. 20.3. W D mg.zA � zB /. 20.4. 0. 20.5. Nelze (pole není potenciálové). 

21 Plochy v prostoru 

97 

### 21 Plochy v prostoru 

- Definice 21.1 — prostorové plochy a souvisejících pojm˚u. 1. Nechť Suv je kompaktní množina v R<sup>2</sup> taková, že existuje oblast ˝ � R<sup>2</sup> splňující ˝ � Suv (Suv tedy nemůže být bod nebo křivka) a nechť _F_ D Œ'; ; �� W R<sup>2</sup> ! R<sup>3</sup> je 3-funkce spojitá na Suv. _Plochou v_ R<sup>3</sup> _(prostorovou plochou)_ nazveme množinu 

   - S D fŒx; y; z� 2 R<sup>3</sup> W x D '.u; v/; y D .u; v/; z D �.u; v/; Œu; v� 2 Suvg 

a 3-funkci _F_ nazveme _parametrizací plochy_ S . 

2. Nechť množina Suv z předchozího bodu má po částech hladkou hranici @Suv, _F_ je prostá na Suv, Jacobiova matice _F_<sup>0</sup> je spojitá na Suv a tečné vektory 



<!-- Start of picture text -->
tEu.u; v/ D .'u 0 .u; v/;  u 0 .u; v/; �0 u .u; v//; tEv.u; v/ D .'v 0 .u; v/;  v 0 .u; v/; �0 v .u; v//<br><!-- End of picture text -->

jsou lineárně nezávislé v každém bodě Œu; v� 2 Suv. Pak plochu S nazveme _jednoduchou hladkou plochou_ . Obraz _F_ .@Suv/ křivky @Suv nazveme _okrajem plochy_ S a budeme značit @S (s vědomím, že jsme v kolizi se značením, neboť symbol @S jsme používali také pro hranici množiny, což je v našem případě opět S). Z uvedených předpokladů je zřejmé, že hladké plochy se nikde neprotínají, nemají žádné „ostré“ hrany ani vrcholy, a v každém bodě plochy lze sestrojit tečnou rovinu. 

3. Plochu S � R<sup>3</sup> nazveme _po částech hladkou plochou_ , existují-li jednoduché hladké plochy S1; S2; : : : ; Sn takové, že platí: 

   - (i) S D S1 [ S2 [ ���[ Sn; 

   - (ii) Si \ Sj � @Si \ @Sj pro každé i ¤ j , přičemž Si \ Sj je buď jednoduchá hladká křivka, nebo po částech hladká křivka (může být i uzavřená) – v tomto případě říkáme, že Si a Sj jsou _přilehlé plochy_ , nebo bod, nebo prázdná množina; 

   - (iii) Pro každá i ¤ j ¤ k je Si \ Sj \ Sk jednobodová nebo prázdná množina; 

   - (iv) Pro každé i D 2; 3; : : : ; n je plocha Si přilehlá k některé z ploch S1; S2; : : : ; Si �1. 

4. Křivku � nazveme _částí okraje_ po částech hladké plochy S (která se skládá z n jednoduchých hladkých ploch), jestliže existuje právě jedno i 2 f1; 2; : : : ; ng tak, že ; ¤ � \ @Si � @Si . _Okraj_ @S _po částech hladké plochy_ S pak definujeme jako sjednocení všech částí okraje této plochy. 

5. Po částech hladká plocha S se nazývá _uzavřená_ , jestliže @S D ;. Příkladem uzavřené plochy je kulová plocha, povrch kvádru, válce, kužele, atp. 

Poznámka 21.2. a) V dalším uvidíme, že důležitou roli bude hrát normálový vektor v bodech plochy. Protože t<sup>E</sup> u, t<sup>E</sup> v jsou tečné vektory, normálový vektor je dán vektorovým součinem t<sup>E</sup> u � t<sup>E</sup> v. V případě jednoduché hladké plochy lineární nezávislost vektorů t<sup>E</sup> u a t<sup>E</sup> v na celé množině Suv zaručuje, že vektorový součin je nenulový, a tedy normálový vektor v každém bodě hladké plochy existuje. Navíc se spojitě mění díky předpokladu spojitosti _F_<sup>0</sup> . 

b) Graf funkce dvou proměnných z D f .x; y/, kde Œx; y� 2 Sxy představuje plochu. Lze ji vždy parametrizovat nekonečně mnoha způsoby, např. x D u, y D v, z D f .u; v/, kde Œu; v� 2 Sxy . Analogicky pro graf funkcí y D g.x; z/ a x D h.y; z/. 

c) Jednoduché hladké plochy mají dvě „strany“. Nepatří mezi ně např. známý Möbiův list (August Ferdinand Möbius 1790–1868, Johann Benedikt Listing 1808–1882, Němci), který lze popsat parametricky x D cos t C p cos t=2 cos t, x D sin t C p cos t=2 sin t, z D p sin t=2, t 2 h0; 2�i, p 2 hpmin; pmaxi (takto popsaný list by měl jednotkovou délku). Druhým nejznámějším příkladem plochy, která nemá dvě strany, je Kleinova nádoba (Felix Christian Klein 1849–1925, Němec). Tu si lze zjednodušeně představit jako uzavřenou nádobu, která nemá vnitřek ani vnějšek. Podobných ploch je známo více, nazýváme je _jednostrannými plochami_ . 

d) Pro potřeby plošného integrálu II. druhu je třeba plochu orientovat. Plochu orientujeme tak, že vybereme směr vektoru normály. Jednostranné plochy nelze orientovat. 

Kapitola 4. Kˇrivkové a plošné integrály 

98 

#### Pˇríklady k procviˇcení 

21.1. Parametrizujte množinu S, je-li 



<!-- Start of picture text -->
a) S D fŒx; y; z� 2 R 3 W x 2 C y 2 C z 2 D 100; �8 � z � 6g;<br>b) S D fŒx; y; z� 2 R 3 W x 2 C y 2 C z 2 D 4; x 2 C y 2 � 2x; z � 0g:<br><!-- End of picture text -->

_Výsledky._ 21.1. a) x D ~~p~~ 100 � u<sup>2</sup> cos v, y D ~~p~~ 100 � u<sup>2</sup> sin v, z D u, Suv D h�8; 6i �h0; 2�i, b) x D u cos v, y D u sin v, z D ~~p~~ 4 � u<sup>2</sup> , Suv D fŒu; v� 2 R<sup>2</sup> W �� � v � �; 0 � u � 2 cos vg. 

### 22 Plošný integrál 

Definice 22.1 — plošného integrálu I. druhu pˇres hladkou plochu. Nechť S je jednoduchá hladká plocha s parametrizací _F_ D Œ'; ; �� W R<sup>2</sup> ! R<sup>3</sup> a f W R<sup>3</sup> ! R je spojitá funkce na nějaké prostorové oblasti obsahující plochu S. Potom definujeme _plošný integrál I. druhu_ vztahem 



<!-- Start of picture text -->
f .x; y; z/ dS WD f .'.u; v/; .u; v/; �.u; v// jt E u.u; v/ � t E v.u; v/j dudv: (�)<br>� S � Suv<br><!-- End of picture text -->

Poznámka 22.2. a) Za uvedených předpokladů je funkce f .'.u; v/; .u; v/; �.u; v//jt<sup>E</sup> u.u; v/ � t<sup>E</sup> v.u; v/j spojitá na Suv, tudíž je integrovatelná a definice má smysl. 

b) Jako motivace pro takto zavedený integrál poslouží úloha spočítat hmotnost plochy S, kde funkce f představuje plošnou hustotu. Pro jednoduchost předpokládejme, že Suv je obdélník. Uvedený vzorec se odvodí tak, že množina Suv se (stejně jako u zavedení dvojného integrálu) „rozřeže“ na malé obdélníky Iij D hui�1; ui i � ˝vj �1; vj ˛, i D 1; : : : ; n, j D 1; : : : ; m. Tyto obdélníky zároveň určují dělení plochy pomocí malých plošek Sij . Myšlenka je, že obsah každé plošky Sij nahradíme obsahem části tečné roviny (nad obdélníkem Iij ), například v bodě _F_ .ui �1; vj �1/. Lze ukázat, že obsah této části tečné roviny je roven jt<sup>E</sup> u.ui �1; vi�1/ � t<sup>E</sup> v.ui �1; vi �1/j.ui � ui�1/.vi � vi�1/. Aproximace hmotnosti plošky Sij je pak dána hodnotou f . _F_ .ui �1; vj �1//jt<sup>E</sup> u.ui �1; vi �1/ � t<sup>E</sup> v.ui�1; vi �1/j.ui � ui�1/.vi � vi�1/ a aproximace hmotnosti celé plochy S je 

n m X X f . _F_ .ui�1; vj �1//jt<sup>E</sup> u.ui�1; vi �1/ � t<sup>E</sup> v.ui �1; vi�1/j.ui � ui�1/.vi � vi �1/: i D1 j D1 

To ale není nic jiného než integrální součet, který v limitě (pro každou nulovou posloupnost dělení Suv, tj. posloupnost dělení, ve které délky uhlopříček největšího z obdélníků konverguje k nule) dává pravou stranu rovnosti (�). 

c) Stejně jako u křivkového integrálu lze ukázat, že hodnota integrálu nezávisí na zvolené parametrizaci. d) Integrál � S<sup>dSpředstavuje obsah plochy S.</sup> 

e) Je-li plocha S dána explicitně, např. jako z D f .x; y/, kde Œx; y� 2 Sxy , a jsou-li parciální derivace fx<sup>0, f</sup> y<sup>0spojité na Sxy, pak pro velikost normálového vektoru v bodě Œx; y�2 Sxyplatí</sup> 



<!-- Start of picture text -->
jEn.x; y/j D q 1 C .fx 0 .x; y// 2 C .fy 0 .x; y// 2 :<br><!-- End of picture text -->

f) Je-li S po částech hladká plocha skládající se z hladkých ploch Si , i D 1; : : : ; n, pak definujeme 



<!-- Start of picture text -->
n<br>f .x; y; z/ dS WD X f .x; y; z/ dS;<br>� S iD1 � Si<br><!-- End of picture text -->

kde Si jsou hladké. Lze ukázat, že hodnota nezávisí na konkrétním rozkladu na hladké plochy. 

Pˇríklad 22.3. Vypočítejte integrál � S<sup>.x2 C y2/ dS, kde Sje povrch kužele</sup> ~~p~~ x<sup>2</sup> C y<sup>2</sup> � z � 1. 

22 Plošný integrál 

99 

_Řešení._ Povrch se skládá z podstavy a pláště. Podstava má parametrické vyjádření x D � cos ', y D � sin ', z D 1, Œ'; �� 2 h0; 2�i �h0; 1i, a tedy tečné vektory jsou t<sup>E</sup> �.'; �/ D .cos '; sin '; 0/, t<sup>E</sup> ' .'; �/ D .�� sin '; � cos '; 0/. Jejich vektorový součin pak představuje normálový vektor 

n.'; �/E D .cos '; sin '; 0/ � .�� sin '; � cos '; 0/ D .0; 0; �/ H) jEn.'; �/j D � 

Integrál přes podstavu má tvar 



<!-- Start of picture text -->
� 4<br>Intpodst D � S'� � 2 d'd� D � 02� � � 01 � 2 � � d��d' D 2� " 4 #10 D � 2 :<br><!-- End of picture text -->

Plášť kužele pak lze parametricky vyjádřit jako x D � cos ', y D � sin ', z D �, Œ'; �� 2 h0; 2�i � h0; 1i. Odtud 

n.'; �/E D .cos '; sin '; 1/ � .�� sin '; � cos '; 0/ D .�� cos '; �� sin '; �/ H) jEn.'; �/j D ~~p~~ 2�: 

Plošný integrál přes plášť je pak dán dvojným integrálem 

Celkově 



<!-- Start of picture text -->
� 4 p 2�<br>Intplášť D p 2 � 3 d'd� D 2 p 2� D :<br>� S'� " 4 #10 2<br>.x 2 C y 2 / dS D Intpodst C Intplášť D � �1 C p 2�:<br>� S 2<br><!-- End of picture text -->

Definice 22.4 — plošného integrálu II. druhu pˇres hladkou plochu. Nechť S je orientovaná jednoduchá hladká plocha s parametrizací _F_ D Œ'; ; �� W R<sup>2</sup> ! R<sup>3</sup> a vektorové pole f<sup>E</sup> D .P; Q; R/ W R<sup>3</sup> ! R<sup>3</sup> je spojité v nějaké prostorové oblasti obsahující plochu S . Označme dS<sup>E</sup> D .dydz; dxdz; dxdy/ (orientovaný diferenciál plochy). Potom _plošný integrál II. druhu_ definujeme jako 



<!-- Start of picture text -->
E E<br>f .x; y; z/ � dS E WD ˙ f .'.u; v/; .u; v/; �.u; v// � .t E u.u; v/ � t E v.u; v// dudv; (��)<br>� S � Suv<br><!-- End of picture text -->

kde znaménko C uplatníme, je-li normálový vektor nE D t<sup>E</sup> u � t<sup>E</sup> v orientován souhlasně se zadanou orientací plochy (tj. má stejný stejný směr jako vektor definující orientaci plochy), a znaménko �, je-li tomu naopak. Uvědomme si přitom, že pokud normálový vektor spočítáme jako t<sup>E</sup> v � t<sup>E</sup> u, dostaneme opačnou orientaci (vektorové násobení je antikomutativní operace). 

Poznámka 22.5. a) Motivace pro takto zavedený integrál je následující. Buď � rovinná plocha, přes kterou protéká ve směru jejího jednotkového normálového vektoru nE1 nestlačitelná kapalina konstantní rychlostí (tj. nezávislou na poloze i čase) danou vektorem f<sup>E</sup> c. Potom (objemové) množství kapaliny, které proteče přes plochu � za jednotku času je dáno číslem f<sup>E</sup> c �En1�.�/, kde �.�/ je obsah plochy �. Jaký bude tok vektorového pole f<sup>E</sup> přes plochu S ? Uvažujeme-li opět pro jednoduchost množinu Suv jako obdélník, který rozdělíme na malé obdélníky Iij D hui �1; ui i � ˝vj �1; vj ˛, pak aproximace toku přes část plochy Sij (ta je dána obrazem _F_ .Iij /) bude dána tokem vektoru f .u<sup>E</sup> i�1; vj �1/ přes část tečné roviny (nad obdélníkem Ijk) v bodě _F_ .ui�1; vj �1/, tj. hodnotou 



<!-- Start of picture text -->
E<br>tEu.ui �1; vj �1/ �Etv.ui �1; vj �1/<br>f . F .ui�1; vj �1// � jt E u.ui �1; vj �1/ � t E v.ui �1; vj �1/j<br>jt E u.ui �1; vj �1/ � t E v.ui �1; vj �1/j<br>.ui � ui�1/.vj � vj �1/<br><!-- End of picture text -->

Df .<sup>E</sup> _F_ .ui�1; vj �1// � .t<sup>E</sup> u.ui�1; vj �1/ � t<sup>E</sup> v.ui�1; vj �1//.ui � ui �1/.vj � vj �1/: 

Aproximací celkového toku pak bude součet přes všechny obdélníky Iij , což ale není nic jiného než integrální součet, který v limitě (pro každou nulovou posloupnost dělení Suv) dává pravou stranu vzorce (��). 

Kapitola 4. Kˇrivkové a plošné integrály 

100 

b) Pokud plochu S lze vyjádřit explicitně zároveň jako x D f .y; z/, kde Œy; z� 2 Syz, resp. y D g.x; z/, kde Œx; z� 2 Sxz, resp. z D h.x; y/, kde Œx; y� 2 Sxy , pak lze integrál vyjádřit jako 



<!-- Start of picture text -->
P dydz C Q dxdz C R dxdy<br>� S<br>D ˙ P.f .y; z/; y; z/ dydz ˙ Q.x; g.x; z/; z/ dxdz ˙ R.x; y; h.x; z// dxdy;<br>� Syz � Sxz � Sxy<br><!-- End of picture text -->

kde „C“ bereme, pokud normálový vektor z orientace plochy svírá s kladným směrem osy x, resp. y, resp. z ostrý úhel a „�“ bereme, pokud svírá tupý úhel. Je-li průmětem plochy do nějaké ze souřadných roviny křivka, klademe příslušný integrál roven nule (to odpovídá situaci, kdy je normálový vektor kolmý na vektor souřadnicové osy, a tedy příslušná složka vektorového pole k celkovému toku nepřispívá). Poznamenejme ještě, že při daném značení pro normálový vektor plochy S platí nE D .1; �fy<sup>0; �f</sup> z<sup>0/, resp.</sup> nE D .�gx<sup>0; 1; �g</sup> z<sup>0/, resp.nE D .�h0</sup> x<sup>; �h</sup> y<sup>0; 1/.</sup> 

Pˇríklad 22.6. Určete tok kapaliny s rychlostním polem f<sup>E</sup> D .x; y; z/ přes válcovou plochu x<sup>2</sup> C y<sup>2</sup> D 1 mezi rovinami z D 0 a z D 1. Plocha je orientována tak, že normálový vektor směřuje od osy z „pryč“. 

_Řešení._ Zadanou část válcové plochy parametrizujme rovnicemi x D cos ', y D sin ', z D v, Œ'; v� 2 h0; 2�i �h0; 1i. Normálový vektor je dán vektorovým součinem tečných vektorů, tj. máme 



<!-- Start of picture text -->
n.'; v/E  D .� sin '; cos '; 0/ � .0; 0; 1/ D .cos '; sin '; 0/:<br><!-- End of picture text -->

Dosadíme-li např. bod ' D 0, vidíme, že n.0; v/E D .1; 0; 0/, tj. normálový vektor směřuje v kladném směru osy x, tj. od osy z „pryč“, což znamená, že orientace vektoru nE je se zadanou orientací plochy souhlasná. Tok kapaliny je pak dán integrálem 



<!-- Start of picture text -->
� S .x; y; z/ � dS E D � 02� � � 01.cos '; sin '; v/ � .cos '; sin '; 0/ dv�d'<br>D .cos 2 ' C sin 2 '/ dv d' D d' dv D 2�:<br>� 02� � � 01 � � 02� � 01<br><!-- End of picture text -->

Poznámka 22.7. Vztah mezi plošným integrálem I. a II. druhu je následující. Je-li S jednoduchá hladká plocha, potom její normálový vektor nE D t<sup>E</sup> u � t<sup>E</sup> v lze normalizovat vydělením jeho velikostí, tj. vektor 



<!-- Start of picture text -->
tEu �Etv<br>nE1 D<br>jt E u � t E vj<br><!-- End of picture text -->

je jednotkový a platí 



<!-- Start of picture text -->
fE � dS E D ˙ fE �En1 dS:<br>� S � S<br><!-- End of picture text -->

■ Vˇeta 22.8 — Gaussova–Ostrogradského<sup>3</sup> . _Nechť_ M _je normální množina v_ R<sup>3</sup> _taková, že její hranice_ @M _je po částech hladká uzavřená plocha orientovaná ve směru vnější normály a nechť vektorové pole_ fE D .P; Q; R/ _je spojité na_ M _a má zde spojité parciální derivace_ Px<sup>0; Q</sup> y<sup>0</sup><sup>_a_R</sup> z<sup>0</sup><sup>_. Potom platí_</sup> 



<!-- Start of picture text -->
div f .x; y; z/ E  dxdydz D f .x; y; z/E  � dS; E<br>� M " @M<br><!-- End of picture text -->



<!-- Start of picture text -->
kde  div f E WD Px 0 C Q y 0 C R z 0 .<br><!-- End of picture text -->

Poznámka 22.9. Platnost tvrzení lze rozšířit i na komplikovanější množiny než je normální, úplně libovolné množiny to ale být nemohou. 

3Michail Vasiljevič Ostrogradskij 1801–1862, kozák z území dnešní Ukrajiny 

22 Plošný integrál 

101 

Pˇríklad 22.10. Určete tok vektorového pole f<sup>E</sup> D .yz; xz; xy/ přes boční stěny čtyřstěnu s vrcholy Œ0; 0; 0�, Œ2; 0; 0�, Œ0; 1; 0� a Œ0; 0; 2�, které jsou orientovány tak, že normalový vektor směřuje z tělesa „ven“. Využijte faktu, že tok přes boční stěny je dán tokem přes celý povrch bez toku přes podstavu. 

_Řešení._ Platí divf<sup>E</sup> D .yz/<sup>0</sup> x<sup>C .xz/</sup> y<sup>0C .xy/</sup> z<sup>0D 0, a tedy trojný integrál přes zadaný čtyřstěn je nulový.</sup> Nyní stačí spočítat plošný integrál přes podstavu: 



<!-- Start of picture text -->
.yz; xz; xy/ � dS E D � xy dxdy;<br>� Spodst � Sxy<br><!-- End of picture text -->

kde Sxy je trojúhelník vymezený nerovnostmi 0 � x � 2, 0 � y � 1 �<sup><u>x</u></sup> 2<sup>. Máme tedy</sup> 



<!-- Start of picture text -->
� xy dxdy D � xy dy dx<br>� Sxy � 02� � 01�x=2 �<br>D � 1 2 � 02Œxy 2 � 1 0 �x=2 dx D � 2 1 � 02 x�1 � x C x 4 2 � dx<br>D � 1 .4x � 4x 2 C x 3 / dx D � 1 2x 2 � 4<br>8 � 02 8 � 3 x3 C 4 1 x4 �20<br>D � 1 8 �8 � 32 3 C 4 � D � 1 8 � 36 � 3 32 D � 1 6 :<br><!-- End of picture text -->

Tok přes boční stěny pak je 0 � ��<sup><u>1</u></sup> 6 � D<sup><u>1</u></sup> 6<sup>.</sup> 

Poznámka 22.11. Objem tělesa ˝ lze pomocí Gaussovy–Ostrogradského věty počítat jako 



<!-- Start of picture text -->
V.˝/ D 1 .x; y; z/ � dS: E<br>3 " @˝<br><!-- End of picture text -->

> ■ Vˇeta 22.12 — Stokesova<sup>4</sup> . _Nechť_ S _je jednoduchá hladká plocha, která je spolu se svým okrajem_ @S _orientována tak, že když položíme dlaň pravé ruky kolmo k ploše_ S _na její okraj_ @S _tak, aby prsty ukazovaly orientaci křivky, pak palec ukazuje směr normály plochy. Nechť dále_ f<sup>E</sup> _je vektorové pole, které má spojité parciální derivace na nějaké oblasti obsahující plochu_ S _. Potom platí_ 



<!-- Start of picture text -->
rot f .x; y; z/ E  � dS E D f .x; y; z/E  � ds:E<br>� S @S<br><!-- End of picture text -->

Poznámka 22.13. Tvrzení zůstane v platnosti i v případě po částech hladké plochy, která má neprázdný okraj. 

Pˇríklad 22.14. Pomocí Stokesovy věty (po horní polovině kulové plochy x<sup>2</sup> C y<sup>2</sup> C z<sup>2</sup> D r<sup>2</sup> ) vypočtěte integrál 



<!-- Start of picture text -->
.x 2 y 3 ; 1; z/ � ds;E<br>� �<br><!-- End of picture text -->

kde � je kružnice x<sup>2</sup> C y<sup>2</sup> D r<sup>2</sup> (r > 0), z D 0, orientována tak, že v rovině .x; y/ „obíháme“ proti smyslu pohybu hodinových ručiček. 

_Řešení._ Pro rotaci zadaného vektorového pole platí 



<!-- Start of picture text -->
rot f E D .0; 0; �3x 2 y 2 /:<br><!-- End of picture text -->

Podle Stokesovy věty tedy máme 



<!-- Start of picture text -->
Int D .0; 0; �3x 2 y 2 / � dS; E<br>� S<br><!-- End of picture text -->

4George Gabriel Stokes 1819–1903, Ir 

Kapitola 4. Kˇrivkové a plošné integrály 

102 

kde S je horní polovina kulové plochy x<sup>2</sup> Cy<sup>2</sup> Cz<sup>2</sup> D r<sup>2</sup> orientovaná tak, že vektor normály svírá s kladným směrem osy z ostrý úhel. Parametrické vyjádření této plochy je x D r cos ' cos #, y D r sin ' cos #, z D r sin #, ' 2 h0; 2�i, # 2 h0; �=2i. Tečné vektory jsou dány 



<!-- Start of picture text -->
tE' D .�r sin ' cos #; r cos ' cos #; 0/; tE# D .�r cos ' sin #; �r sin ' sin #; r cos #/:<br><!-- End of picture text -->

Dále 



<!-- Start of picture text -->
nE D t E ' � t E # D .r 2 cos ' cos 2 #; r 2 sin ' cos 2 #; r 2 cos # sin #/;<br><!-- End of picture text -->

a tedy 



<!-- Start of picture text -->
Int D � . .0; 0; 3r 4 cos 2 ' sin 2 ' cos 4 #/<br>� 02� � 0�=2<br>�.r 2 cos ' cos 2 #; r 2 sin ' cos 2 #; r 2 cos # sin #/ d#/ d'<br>cos # D t<br>D �3r 6 cos 2 ' sin 2 ' d' cos 5 # sin # d# D d# D � sin dt  #<br>� 02� � 0�=2 ˇˇˇˇˇˇ 0 ! 1; �=2 ! 0 ˇˇˇˇˇˇ<br>D � 4 3 r 6 � 02� sin 2 2' � 01 t 5 dt D � 3 8 r 6 � 02� .1 � cos 4'/ d' t6 6<br>" #10<br>D � 3 8 � 1 6 r 6� '�2�0 D � 1 8 �r 6 :<br><!-- End of picture text -->

Nˇekolik operátorových identit 

Platí: 



<!-- Start of picture text -->
1. div f E D r � f E  ,<br>2. rot f E D r � f E  ,<br>3. rot rf D oE,<br>4. div rot f E D 0,<br>5. div rf D fxx 00 C f yy 00 C f zz 00 DW �f (symbol � se nazývá Laplaceův5 operátor).<br><!-- End of picture text -->

Poznámka 22.15. Stokesovu větu lze interpretovat také takto: je-li nějaké vektorové pole f<sup>E</sup> rotací jiného vektorového pole, pak plošný integrál � S f<sup>E</sup> � dS<sup>E</sup> závisí pouze na okraji plochy @S , nikoliv na jejím vnitřku. V takovém případě je podle bodu 4 předchozích identit div f<sup>E</sup> D 0 a říkáme, že _pole_ f<sup>E</sup> _je nezřídlové (solenoidální)_ . 

#### Pˇríklady k procviˇcení 

22.1. Určete plošný integrál 



<!-- Start of picture text -->
� S .1 C x1 C y/ 2 dS;<br><!-- End of picture text -->

kde S je povrch čtyřstěnu s vrcholy Œ1; 0; 0�, Œ0; 1; 0�, Œ0; 0; 1� a Œ0; 0; 0�. 

22.2. Spočítejte plošný integrál 



<!-- Start of picture text -->
.x; y; xyz/ � dS; E kde S D fŒx; y; z� 2 R 3 W z D xy; x 2 C y 2 � 5g<br>� S<br><!-- End of picture text -->

orientovaná tak, že normálový vektor svírá s kladným směrem osy z ostrý úhel. 

5Pierre Simon de Laplace 1749–1827, Francouz 

22 Plošný integrál 

103 

22.3. Pomocí Gaussovy–Ostrogradského věty spočítejte plošný integrál 

.x � y C z; y � z C x; z � y C x/ � dS;<sup>E</sup> kde S D fŒx; y; z� 2 R<sup>3</sup> W jxj C jyj C jzj D 3g � S 

orientovaná tak, že normálový vektor směřuje k počátku. 

22.4. Pomocí Stokesovy věty spočítejte integrál 



<!-- Start of picture text -->
� � .x; y; z/ � ds;E kde � D n Œx; y; z� 2 R 3 W x 2 C y 2 D 4; x 2 C z 3 D 1 o<br><!-- End of picture text -->

a orientace je dána pořadím bodů křivky Œ2; 0; 0�, Œ0; 2; 3� a Œ�2; 0; 6�. 

_Výsledky._ 22.1. . ~~p~~ 3 � 1/ ln 2 � ~~p~~ 3=2 C 3=2. 22.2. 125�=24. 22.3. �108. 22.4. 10�. 

# Literatura 

- [1] Bouchala, J., Vlach, O., _Křivkový a plošný integrál_ , Matematika pro inženýry 21. století (reg. č. CZ.1.07/2.2.00/07.0332), VŠB-TU Ostrava a ZČU v Plzni, 2011. 

- [2] Došlá, Z., Došlý, O., _Metrické prostory: teorie a příklady_ , 3. vyd., Masarykova univerzita, Brno, 2006. 

- [3] Jirásek, F., Čipera, S., Vacek, M., _Sbírka řešených příkladů z matematiky II_ , SNTL, Praha, 1989. 

- [4] Došlý, O., Kuben, J., _Křivkový integrál_ , text PřF MUNI, 2005. 

- [5] Hasil, P., Zemánek, P., _Sbírka řešených příkladů z matematické analýzy I_ , 3. vyd., text PřF MUNI a LDF MENDELU, Brno, 2012. 

- [6] Kalas, J., Kuben, J., _Integrální počet funkcí více proměnných_ , MUNI, Brno, 2009. 

- [7] Pospíšil, Z., Půža, B., _Základy matematické analýzy v reálném oboru_ , text PřF MUNI, 2004. 

- [8] Škrášek, J., Tichý, Z., _Základy aplikované matematiky I_ , SNTL, Praha, 1983. 

- [9] Škrášek, J., Tichý, Z., _Základy aplikované matematiky II_ , SNTL, Praha, 1986. 

- [10] Veselý, J., _Základy matematické analýzy II_ , MatfyzPress, 2009. 

