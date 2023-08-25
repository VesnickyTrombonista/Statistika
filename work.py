import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

production = pd.read_csv('./produkce.csv', sep=';')
beekeepers = pd.read_csv('./vcelari.csv', sep=';')


beekeepers_sorted = beekeepers.sort_values(by='Počet včelstev')

# Rozdělení dat na sloupce
years = beekeepers_sorted['Rok']
beekeepers_count = beekeepers_sorted['Počet včelařů']
beehives_count = beekeepers_sorted['Počet včelstev']

# Vytvoření dvou grafů vedle sebe
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Graf pro Počet včelařů
ax1.bar(years, beekeepers_count, color='b')
ax1.set_xlabel('Rok')
ax1.set_ylabel('Počet včelařů')
ax1.set_title('Počet včelařů')

# Graf pro Počet včelstev
ax2.bar(years, beehives_count, color='r')
ax2.set_xlabel('Rok')
ax2.set_ylabel('Počet včelstev')
ax2.set_title('Počet včelstev')

plt.tight_layout()
plt.show()

# Výpočet poměru počtu včelstev na jednoho včelaře
ratio = beehives_count.astype(int) / beekeepers_count.astype(int)

# Vytvoření grafu pro poměr
plt.figure(figsize=(10, 6))
plt.bar(years, ratio, color='g')
plt.xlabel('Rok')
plt.ylabel('Poměr počtu včelstev na jednoho včelaře')
plt.title('Poměr počtu včelstev na jednoho včelaře')
plt.xticks(rotation=45)  # Otočení názvů let pro lepší čitelnost
plt.tight_layout()
plt.show()
