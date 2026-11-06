"""Scatter plot Matplotlib di 50 coppie di valori casuali."""

import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
