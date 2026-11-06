"""Serie storica e trend dei visitatori in un unico DataFrame."""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

# PASSO 1: creo un DataFrame con una riga per ciascuno dei 730 giorni.
date = pd.date_range("2026-01-01", "2027-12-31", freq="D")
df = pd.DataFrame(index=date)
df.index.name = "data"
df["periodo"] = "Previsione"
df.loc["2026-01-01":"2026-09-30", "periodo"] = "Storico"

# PASSO 2: imposto una media che cresce da 2000 a 2500.
# La deviazione standard resta sempre 500.
df["media_attesa"] = np.linspace(2000, 2500, len(df))
df["deviazione_standard"] = 500
print("PASSO 1-2 - Periodo, numero di righe e parametri")
print("Righe nel DataFrame:", len(df))
print("Media attesa iniziale:", df["media_attesa"].iloc[0])
print("Media attesa finale:", df["media_attesa"].iloc[-1])
print("Deviazione standard fissa:", df["deviazione_standard"].iloc[0])

# PASSO 3: genero lo storico di esempio fino a settembre 2026.
# Sono valori simulati: sostituiscili con quelli reali quando li avrai.
maschera_storico = df["periodo"] == "Storico"
visitatori_storici = np.random.normal(
    loc=df.loc[maschera_storico, "media_attesa"],
    scale=500,
    size=maschera_storico.sum(),
)
df["visitatori"] = np.nan
df.loc[maschera_storico, "visitatori"] = np.maximum(
    0, np.round(visitatori_storici)
).astype(int)

# PASSO 4: genero i valori previsti da ottobre 2026 in poi.
maschera_previsione = df["periodo"] == "Previsione"
trend_previsto = np.random.normal(
    loc=df.loc[maschera_previsione, "media_attesa"],
    scale=500,
    size=maschera_previsione.sum(),
)
df["trend"] = np.nan
df.loc[maschera_previsione, "trend"] = np.maximum(
    0, np.round(trend_previsto)
).astype(int)

# PASSO 5: metto i valori storici e previsti nella stessa colonna completa.
df["visitatori_complessivi"] = df["visitatori"].fillna(df["trend"])
print("\nPASSO 3-5 - Esempio di righe prima e dopo l'inizio della previsione")
print(df.loc["2026-09-28":"2026-10-03"])

# PASSO 6: calcolo la media mobile sugli ultimi 7 giorni.
df["media_mobile"] = df["visitatori_complessivi"].rolling(7).mean()
print("\nPASSO 6 - Visitatori e media mobile nei primi 10 giorni")
print(df[["visitatori_complessivi", "media_mobile"]].head(10).round(2))

# PASSO 7: calcolo la media e la deviazione standard osservate per mese.
# La deviazione standard mensile osservata può oscillare; il parametro usato
# per generare i dati rimane invece 500 per tutte le date.
statistiche_mensili = df["visitatori_complessivi"].groupby(
    df.index.to_period("M")
).agg(media_osservata="mean", deviazione_standard_osservata="std")
statistiche_mensili.index = statistiche_mensili.index.to_timestamp(how="end").normalize()
statistiche_mensili.index.name = "ultimo_giorno_del_mese"
print("\nPASSO 7 - Statistiche osservate per mese, datate a fine mese")
print(statistiche_mensili.round(2))

# PASSO 8: reshape dispone i 730 valori in 2 righe da 365 giorni.
visitatori_per_anno = df["visitatori_complessivi"].to_numpy().reshape(2, 365)
print("\nPASSO 8 - Forma dopo reshape (anni, giorni):", visitatori_per_anno.shape)

# Creo i valori mensili attesi e la deviazione standard fissa per il grafico.
media_attesa_mensile = df["media_attesa"].groupby(df.index.to_period("M")).mean()
deviazione_standard_mensile = df["deviazione_standard"].groupby(
    df.index.to_period("M")
).first()
date_fine_mese = media_attesa_mensile.index.to_timestamp(how="end").normalize()

# Tutti i pannelli sono contenuti nella stessa finestra.
fig, assi = plt.subplots(3, 1, figsize=(13, 15), constrained_layout=True)

# Grafico 1: storico, previsione e media mobile.
sns.lineplot(
    x=df.index,
    y=df["visitatori"],
    color="steelblue",
    label="Storico simulato (gen-set 2026)",
    ax=assi[0],
)
sns.lineplot(
    x=df.index,
    y=df["media_mobile"],
    color="navy",
    label="Media mobile a 7 giorni",
    ax=assi[0],
)
sns.lineplot(
    x=df.index,
    y=df["trend"],
    color="darkorange",
    label="Previsione (ott 2026-dic 2027)",
    ax=assi[0],
)
assi[0].axvline(pd.Timestamp("2026-10-01"), color="gray", linestyle="--")
assi[0].set_title("Visitatori del parco: storico e previsione")
assi[0].set_xlabel("Data")
assi[0].set_ylabel("Visitatori al giorno")
assi[0].legend()

# Grafico 2: media attesa lineare e deviazione standard fissa di 500.
asse_sigma = assi[1].twinx()
sns.lineplot(
    x=date_fine_mese,
    y=media_attesa_mensile.to_numpy(),
    color="steelblue",
    label="Media attesa",
    ax=assi[1],
)
sns.lineplot(
    x=date_fine_mese,
    y=deviazione_standard_mensile.to_numpy(),
    color="seagreen",
    label="Deviazione standard impostata (500)",
    ax=asse_sigma,
)
assi[1].set_title("Media attesa e deviazione standard a fine mese")
assi[1].set_xlabel("Data (ultimo giorno del mese)")
assi[1].set_ylabel("Media attesa visitatori", color="steelblue")
asse_sigma.set_ylabel("Deviazione standard", color="seagreen")
linee_media, etichette_media = assi[1].get_legend_handles_labels()
linee_sigma, etichette_sigma = asse_sigma.get_legend_handles_labels()
assi[1].legend(linee_media + linee_sigma, etichette_media + etichette_sigma)

# Grafico 3: confronto tra i due anni usando reshape.
giorno_anno = range(1, 366)
sns.lineplot(
    x=giorno_anno,
    y=visitatori_per_anno[0],
    label="2026 (storico + previsione)",
    ax=assi[2],
)
sns.lineplot(
    x=giorno_anno,
    y=visitatori_per_anno[1],
    label="2027 (previsione)",
    ax=assi[2],
)
assi[2].set_title("Confronto dei visitatori per giorno dell'anno")
assi[2].set_xlabel("Giorno dell'anno")
assi[2].set_ylabel("Visitatori al giorno")
assi[2].legend()

plt.show()
