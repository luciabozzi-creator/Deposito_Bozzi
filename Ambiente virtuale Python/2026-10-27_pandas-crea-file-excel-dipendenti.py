import pandas as pd


dati = {
    "Nome": ["Alice", "Bob", "Charlie", "Diana"],
    "Età": [25, 30, 35, 28],
    "Città": ["Milano", "Roma", "Napoli", "Torino"],
    "Stipendio (€)": [2500, 3100, 2900, 2700],
}

dF = pd.DataFrame(dati)

nome = "impiegati.xlsx"

dF.to_excel(nome, index=False)

print(f"File Excel {nome} creato con successo!!!")