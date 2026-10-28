import pandas as pd


# Importa i dati dal file Excel nel DataFrame.
df = pd.read_excel("vendite.xlsx")

# Calcola il totale di ogni ordine: quantità per prezzo unitario.
df["Totale"] = df["Quantità"] * df["Prezzo_Unitario"]

# Riordina le colonne per mettere Totale prima di Città.
df = df[["ID_Ordine", "Prodotto", "Quantità", "Prezzo_Unitario", "Totale", "Città"]]

# Mostra i dati importati nella Shell di Thonny.
print(df)

# Aggiorna il file Excel con la nuova colonna.
df.to_excel("vendite.xlsx", sheet_name="Vendite", index=False)


# Filtra il DataFrame e restituisce solo le righe della città scelta.
def filtra_vendite_per_citta(df, citta):
    return df[df["Città"] == citta]


citta = input("Inserisci la città per la quale vuoi sapere il totale delle vendite: ")
df_citta = filtra_vendite_per_citta(df, citta)

print(f"\nVendite per {citta}:")
print(df_citta)
print(f"Totale vendite a {citta}: {df_citta['Totale'].sum()}")
