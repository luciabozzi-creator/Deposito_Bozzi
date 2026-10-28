import pandas as pd


dati = [
    {"ID_Ordine": 101, "Prodotto": "Laptop", "Quantità": 2, "Prezzo_Unitario": 800, "Città": "Milano"},
    {"ID_Ordine": 102, "Prodotto": "Smartphone", "Quantità": 1, "Prezzo_Unitario": 400, "Città": "Roma"},
    {"ID_Ordine": 103, "Prodotto": "Monitor", "Quantità": 5, "Prezzo_Unitario": 250, "Città": "Milano"},
    {"ID_Ordine": 104, "Prodotto": "Mouse", "Quantità": 10, "Prezzo_Unitario": 25, "Città": "Torino"},
    {"ID_Ordine": 105, "Prodotto": "Tastiera", "Quantità": 3, "Prezzo_Unitario": 45, "Città": "Roma"},
]

# Crea il DataFrame e lo salva in un foglio Excel.
df = pd.DataFrame(dati)
df.to_excel("vendite.xlsx", sheet_name="Vendite", index=False)
print("File Excel creato: vendite.xlsx")

# Rilegge il foglio Excel e mostra i dati nella Shell di Thonny.
df_importato = pd.read_excel("vendite.xlsx", sheet_name="Vendite")
print("\nDati letti dal file Excel:")
print(df_importato.to_string(index=False))
