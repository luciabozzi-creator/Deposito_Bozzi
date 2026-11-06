"""Esercizio 1: analisi esplorativa dei dati con Pandas.

Esercizio 1: Analisi Esplorativa dei Dati
Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati usando pandas.

Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su un gruppo di persone: Nome, Età, Città e Salario. 

Caricare i dati in un DataFrame autogenerandoli casualmente .

Visualizzare le prime e le ultime cinque righe del DataFrame.

Visualizzare il tipo di dati di ciascuna colonna.

Calcolare statistiche descrittive di base per le colonne numeriche (media, mediana, deviazione standard).

Identificare e rimuovere eventuali duplicati.

Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna.

Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18 anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).

Salvare il DataFrame pulito in un nuovo file CSV.

"""

import numpy as np
import pandas as pd


# Generiamo 20 valori casuali per ogni colonna con np.random.choice,

data = {
    "Nome": np.random.choice(["Nome1", "Nome2", "Nome3"], 20),
    "Età": np.random.choice([18, 19, 65, 70, np.nan], 20),
    "Città": np.random.choice(["Citta1", "Citta2", "Citta3"], 20),
    "Salario": np.random.choice([25000, 35000, 50000, np.nan], 20),}

df = pd.DataFrame(data)

# 1. Visualizzare il DataFrame creato.
print("DataFrame originale:")
print(df)

# 2. Visualizzare le prime e le ultime cinque righe.
print("\nPrime cinque righe:")
print(df.head())
print("\nUltime cinque righe:")
print(df.tail())

# 3. Visualizzare il tipo di dato di ogni colonna.
print("\nTipi di dato:")
print(df.dtypes)

# 4. Calcolare media, mediana e deviazione standard per le colonne numeriche.
print("\nStatistiche dell'età:")
print("Media:", df["Età"].mean())
print("Mediana:", df["Età"].median())
print("Deviazione standard:", df["Età"].std())

print("\nStatistiche del salario:")
print("Media:", df["Salario"].mean())
print("Mediana:", df["Salario"].median())
print("Deviazione standard:", df["Salario"].std())

# 5. Rimuovere le righe duplicate.
df = df.drop_duplicates()

# 6. Sostituire i valori mancanti numerici con la mediana della colonna.
mediana_eta = df["Età"].median()
mediana_salario = df["Salario"].median()

df["Età"] = df["Età"].fillna(mediana_eta)
df["Salario"] = df["Salario"].fillna(mediana_salario)

# 7. Creare la categoria d'età usando condizioni Python.
categorie_eta = []

for eta in df["Età"]:
    if eta <= 18:
        categorie_eta.append("Giovane")
    elif eta <= 65:
        categorie_eta.append("Adulto")
    else:
        categorie_eta.append("Senior")

df["Categoria Età"] = categorie_eta

print("\nDataFrame dopo la pulizia:")
print(df)

# 8. Salvare il DataFrame rielaborato in un nuovo file CSV.
df.to_csv("Esercizio_Pandas.csv")
print("\nFile CSV salvato.")
