"""
Esercizio: ndarray, dtype, shape e arange.

Creare un array NumPy con i numeri interi da 10 a 49,
verificare il tipo di dato, convertirlo in float64
e stampare la forma dell'array.
"""

import numpy as np

# Creo un array con i numeri da 10 a 49.
# Il valore finale 50 non è incluso.
arr = np.arange(10, 50)

# Verifico e stampo il tipo di dato iniziale.
print(arr.dtype)

# Stampo l'array.
print(arr)

# Cambio il tipo di dato in float64.
arr = arr.astype(np.float64)

# Verifico e stampo il nuovo tipo di dato.
print(arr.dtype)

# Stampo la forma dell'array.
print(arr.shape)
