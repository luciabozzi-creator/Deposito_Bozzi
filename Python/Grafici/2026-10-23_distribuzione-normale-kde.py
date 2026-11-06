"""Istogramma e KDE di un campione casuale dalla normale standard.

Esempio didattico: i valori sono generati dal programma e non sono dati reali.
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Imposta lo stile Seaborn con griglia scura.
sns.set_theme(style="darkgrid")

# Genera 100 valori casuali: media 0 e deviazione standard 1 per impostazione predefinita.
data = np.random.normal(size=100)

# Disegna l'istogramma e sovrappone una stima smussata della densità (KDE).
sns.histplot(data, kde=True)
plt.title("Distribuzione dei dati")
plt.show()
