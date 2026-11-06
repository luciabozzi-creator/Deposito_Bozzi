"""Esempio introduttivo di grafico a barre con Matplotlib."""

import matplotlib.pyplot as plt


categories = ["A", "B", "C", "D", "E"]
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)
plt.title("Grafico a Barre")
plt.xlabel("Categorie")
plt.ylabel("Valori")
plt.show()
