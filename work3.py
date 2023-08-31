import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

beekeepers = pd.read_csv('./vcelari.csv', sep=';')

beekeepers_sorted = beekeepers.sort_values(by='Počet včelstev')
# Rozdělení dat na sloupce
beekeepers_years_counts = beekeepers_sorted['Počet včelařů'].values.reshape(-1, 1)
beehives_years_counts = beekeepers_sorted['Počet včelstev'].values

# Inicializace a trénink modelu lineární regrese
model = LinearRegression()
model.fit(beekeepers, beehives_years_counts)

# Predikce hodnot
y_pred = model.predict(beekeepers_years_counts)

# Vykreslení grafu
plt.scatter(beekeepers_years_counts, beehives_years_counts, color='blue', label='Data')
plt.plot(beekeepers_years_counts, y_pred, color='red', linewidth=2, label='Lineární regrese')
plt.xlabel('Počet včelařů')
plt.ylabel('Počet včelstev')
plt.legend()
plt.title('Lineární regrese')
plt.show()