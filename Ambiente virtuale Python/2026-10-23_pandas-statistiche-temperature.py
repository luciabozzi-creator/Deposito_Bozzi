"""
Esercizio Avanzato: Calcolo di Statistiche di Base
Testo dell'esercizio:
Hai a disposizione un dataset, che devi autogenerare, contenuto in un DataFrame pandas con una singola colonna temperature che rappresenta la temperatura giornaliera in una città per un mese. 
Scrivi un programma Python che calcoli e stampi le seguenti statistiche:
La temperatura massima
La temperatura minima
La temperatura media
La mediana delle temperature
Grafico scatter plot

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Genera 30 temperature casuali tra 10 e 30 °C, arrotondate a due decimali.
temperature_giornaliere = np.round(np.random.uniform(10, 30, size=30), 2)

# Crea il DataFrame con la colonna temperature.
df = pd.DataFrame({"temperature": temperature_giornaliere})

# Calcola le statistiche e le salva in variabili.
temperature = df["temperature"]
temperatura_massima = temperature.max()
temperatura_minima = temperature.min()
temperatura_media = round(temperature.mean(), 2)
mediana_temperature = round(temperature.median(), 2)

# Stampa i risultati.
print("Massima:", temperatura_massima, "°C")
print("Minima:", temperatura_minima, "°C")
print("Media:", temperatura_media, "°C")
print("Mediana:", mediana_temperature, "°C")

plt.figure()
plt.plot(temperature, "o")
plt.title("Temperature giornaliere")
plt.xlabel("Giorno del mese")
plt.ylabel("Temperatura (°C)")
plt.show()
