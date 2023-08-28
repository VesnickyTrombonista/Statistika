# Včelaření

###### Josef Bálek, II. ročník
###### PSt1 - LS 2022/2023

#### Úvod
Na svoji statistickou práci jsem si vybral sobě blízké téma a tím je včelaření. Hned na začátku musím zmínit, že se mi nepovedlo dohledat velký dataset, který by byl vhodný pro účely statistiky, a proto i výsledky, kterých jsem dosáhl, jsou spíše informativního charakteru, než že by odpovídaly skutečnosti.

#### Data
Data jsem čerpal z výroční zprávy ministerstva zemědělství za rok 2021: https://eagri.cz/public/web/file/705171/Vcely_2021_WEB.pdf

Použité tabulky jsou uvedeny na stranách 14 -> vcelari.csv a 19 -> produkce.csv (číslováno dle stránek pdf).

#### Kód
Veškerý spustitelný kód je v souborech work1 a work2 (python files).
V kódu je vždy uvedena cesta k datům, zpracování dat, převedení do grafů a následně provedený t-test na danou hypotézu. Používám α = 0.05.

### Je počet včelstev vysoký?
Ze zkušenosti vím, že hodně starších včelařů má hodně včelstev, ale pro mě jako začátečníka jsou to jen jednotky. Za hranici bych považoval 10 včelstev, neboť to je počet, o kterém často slyším lidi mluvit a psát.
Problém je trochu s datasetem, ten je relativně malý a nejsou volně dostupná data o jednotlivcích, takže braný průměr může dost zkreslovat naše měření
Zkoumaná hypotéza je, jestli se ročně průměr pohybuje na deseti včelstvech na včelaře.

`p1_value = st.ttest_1samp(beekeepers_beehives_per_year, 10, alternative="greater").pvalue`

`print(p1_value)`

`# 0.01832389861421368 < 0.05 `

Jak vidíme, tak nulovou hypotézu můžeme zamítnout a prohlásit, že v průměru mají včelaři po více než deseti včelstvech.

### Je produkce včelstva nízká?

Ze zkušenosti vím, že hodně starších včelařů má hodně včelstev, ale pro mě jako začátečníka jsou to jen jednotky. Za hranici bych považoval 13 kg, protože se mi to zdá jako přiměřená produkce medu. 

Problém je trochu s datasetem, ten je relativně malý a nejsou volně dostupná data o jednotlivcích, takže braný průměr může dost zkreslovat naše měření.

Zkoumaná hypotéza je, že ročně se průměr pohybuje na 13 kilogramech na včelstvo.

`p1_value = st.ttest_1samp(average_honey_yield, 13, alternative="less").pvalue`

`print(p1_value)`

` # 0.7823446151002443 > 0.05`

Jak vidíme, tak nulovou hypotézu nemůžeme zamítnout a podle výsledku můžeme předpokládat, že v průměru se roční výnos na včelstvo pohybujkolem 13 kg, dle těchto dat

Pozn. toto je ovšem zavádějící informace, protožrůzné literatury udávají výnos 15-28 kg na včelstvo. Problém bude v typu včelstev, které byly nahlášeny, protože z oddělků se většinou mnoho medu nevytočí a zároveň se mohlo stát, že se někomu vyrojily včely, takže pak také tolik nevytočil. Proto informace, že se vytočí kolem 20 kg na běžné včelstvo, je přijatelná.