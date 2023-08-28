import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st

production = pd.read_csv('./produkce.csv', sep=';')

# Seřazení dat dle velikosti průměrného výnosu medu
production_avg_sorted = production.sort_values(by='Průměrný výnos medu (kg/včelstvo)')
production_total_sorted = production.sort_values(by='Celkový výnos medu (tuny)')

# Rozdělení dat na sloupce
years_for_avg = production_avg_sorted['Rok']
average_honey_yield = production_avg_sorted['Průměrný výnos medu (kg/včelstvo)']
years_for_total = production_total_sorted['Rok']
total_honey_yield = production_total_sorted['Celkový výnos medu (tuny)']

# Vytvoření dvou grafů vedle sebe
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Graf pro Průměrný výnos medu
ax1.bar(years_for_avg, average_honey_yield, color='b')
ax1.set_xlabel('Rok')
ax1.set_ylabel('Průměrný výnos')
ax1.set_title('Průměrný výnos medu v kg na včelstvo')

# Graf pro Celkový výnos medu
ax2.bar(years_for_total, total_honey_yield, color='r')
ax2.set_xlabel('Rok')
ax2.set_ylabel('Celkový výnos')
ax2.set_title('Celkový výnos medu v tunách')

plt.tight_layout()
plt.show()

# Pojďme se tedy podívat, kolik bylo za jednotlivé roky včelstev na danou produkci
production_beehives_sorted = production.sort_values(by='Počet včelstev')

years = production_beehives_sorted['Rok']
beehives_counts = production_beehives_sorted['Počet včelstev']

# Vytvoření dvou grafů vedle sebe
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Graf pro Průměrný výnos medu
ax1.bar(years_for_avg, average_honey_yield, color='b')
ax1.set_xlabel('Rok')
ax1.set_ylabel('Průměrný výnos')
ax1.set_title('Průměrný výnos medu v kg na včelstvo')

# Graf pro Vývoj počtu včelstev
ax2.bar(years, beehives_counts, color='r')
ax2.set_xlabel('Rok')
ax2.set_ylabel('Počet včelstev')
ax2.set_title('Vývoj počtu včelstev')

plt.tight_layout()
plt.show()

# Vytvoření grafu pro poměr
plt.figure(figsize=(10, 6))
plt.bar(years, average_honey_yield, color='g')
plt.xlabel('Rok')
plt.ylabel('Průměrný výnos medu (kg/včelstvo)')
plt.title('Vývoj produkce medu v kg na včelstvo')
plt.xticks(rotation=45)  # Otočení názvů let pro lepší čitelnost
plt.tight_layout()
plt.show()

# Zde se můžeme podívat na histogram udávající, kolik včelstev si v průměru udržuje jednotlivý včelař každý rok
plt.hist(average_honey_yield)
plt.show()

# Ze zkušenosti vím, že hodně starších včelařů má hodně včelstev, ale pro mě jako začátečníka jsou to jen jednotky
# Budu používat α = 0.05
# Je produkce včelstva nízká?
# Za hranici bych považoval 13 kg, protože se mi to zdá jako přiměřená produkce medu
# Problém je trochu s datasetem, ten je relativně malý a nejsou volně dostupná data o jednotlivcích, takže 
# braný průměr může dost zkreslovat naše měření.
# Takže hypotéza je, že ročně se průměr pohybuje na 13 kilogramech na včelstvo.

p1_value = st.ttest_1samp(average_honey_yield, 13, alternative="less").pvalue

print(p1_value) # 0.7823446151002443 > 0.05

# Jak vidíme, tak nulovou hypotézu nemůžeme zamítnout a podle výsledku můžeme předpokládat,
# že se v průměru roční výnos na včelstvo pohybuje kolem 13 kg (dle těchto dat).

# Pozn. toto je ovšem zavádějící informace, protože různé literatury udávají výnos 15-28 kg na včelstvo
# Problém bude v typu včelstev, které byly nahlášeny, protože z oddělků se většinou mnoho medu nevytočí
# a zároveň se mohlo stát, že se někomu vyrojily včely, takže pak také tolik nevytočil tolik, proto 
# reálná informace, že se vytočí kolem 20 kg na běžné včelstvo je přijatelná.