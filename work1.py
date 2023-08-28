import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st

beekeepers = pd.read_csv('./vcelari.csv', sep=';')

beekeepers_sorted = beekeepers.sort_values(by='Počet včelstev')
# Rozdělení dat na sloupce
years = beekeepers_sorted['Rok']
beekeepers_years_counts = beekeepers_sorted['Počet včelařů']
beehives_years_counts = beekeepers_sorted['Počet včelstev']
# Vytvoření dvou grafů vedle sebe
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
# Graf pro Vývoj počtu včelařů
ax1.bar(years, beekeepers_years_counts, color='b')
ax1.set_xlabel('Rok')
ax1.set_ylabel('Počet včelařů')
ax1.set_title('Vývoj počtu včelařů')
# Graf pro Vývoj počtu včelstev
ax2.bar(years, beehives_years_counts, color='r')
ax2.set_xlabel('Rok')
ax2.set_ylabel('Počet včelstev')
ax2.set_title('Vývoj počtu včelstev')
plt.tight_layout()
# plt.show()

# Výpočet poměru počtu včelstev na jednoho včelaře
ratio = beehives_years_counts.astype(int) / beekeepers_years_counts.astype(int)

# Vytvoření grafu pro poměr
plt.figure(figsize=(10, 6))
plt.bar(years, ratio, color='g')
plt.xlabel('Rok')
plt.ylabel('Poměr počtu včelstev na jednoho včelaře')
plt.title('Vývoj poměru počtu včelstev na jednoho včelaře')
plt.xticks(rotation=45)  # Otočení názvů let pro lepší čitelnost
plt.tight_layout()
plt.show()

# zde se můžeme podívat na histogram udávající, kolik včelstev si v průměru udržuje jednotlivý včelař každý rok
plt.hist(ratio)
plt.show()

# Ze zkušenosti vím, že hodně starších včelařů má hodně včelstev, ale pro mě jako začátečníka jsou to jen jednotky
# Budu používat α = 0.05
# Nechť je hypotéza: Je počet včelstev vysoký?
# a za hranici bych považoval 10 včelstev, neboť to je počet, o kterém často slyším lidi mluvit a psát
# Problém je trochu s datasetem, ten je relativně malý a nejsou volně dostupná data o jednotlivcích, takže 
# braný průměr může dost zkreslovat naše měření
# Takže hypotéza je, že ročně se průměr pohybuje na deseti včelstev na včelaře

p1_value = st.ttest_1samp(ratio, 10, alternative="greater").pvalue

print(p1_value) # 0.01832389861421368 < 0.05
# Jak vidíme, tak nulovou hypotézu můžeme zamítnout a prohlásit, že v průměru mají
# včelaři po více než deseti včelstvech