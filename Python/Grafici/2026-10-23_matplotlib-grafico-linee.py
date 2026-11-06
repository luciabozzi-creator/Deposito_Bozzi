"""Esempio introduttivo di grafico a linee con Matplotlib."""

import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)
plt.title("Grafico a linee")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
