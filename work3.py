import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Načtení CSV souboru do pandas DataFrame
data = pd.read_csv("./vcelari.csv", delimiter=";")

# Vybrání sloupců pro analýzu
beekeepers = data["Počet včelařů"].values.reshape(-1, 1)
beehives = data["Počet včelstev"].values

# Inicializace a fitování lineární regrese
regressor = LinearRegression()
regressor.fit(beekeepers, beehives)

# Výpis koeficientů regrese
print("Koeficient: ", regressor.coef_)
print("Intercept: ", regressor.intercept_)

# Vytvoření regresní přímky
regression_line = regressor.predict(beekeepers)

# Vykreslení dat a regresní přímky
plt.scatter(beekeepers, beehives, color="blue", label="Data")
plt.plot(beekeepers, regression_line, color="red", label="Lineární regrese")
plt.xlabel("Počet včelařů")
plt.ylabel("Počet včelstev")
plt.title("Lineární regrese mezi počtem včelařů a počtem včelstev")
plt.legend()
plt.tight_layout()
plt.show()