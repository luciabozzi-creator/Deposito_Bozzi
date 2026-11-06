"""
Es1: ndarray, dtype, shape, arange￼


Crea un array NumPy utilizzando arange e
verifica il tipo di dato (dtype) e la forma
(shape) dell'array.


Esercizio:
1.Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
2.Verifica il tipo di dato dell'array e stampa il risultato.
3.Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
4.Stampa la forma dell'array.


"""

import numpy as np


# Crea un array con i numeri interi da 10 a 49.
arr_A = np.arange(10, 50, dtype='int32')

# Verifica e stampa il tipo di dato e il contenuto dell'array.
print()
print(arr_A.dtype)
print()
print(arr_A)
print()

# Converti il tipo di dato dell'array in float64.
arr_B = arr_A.astype(np.float64)

# Verifica nuovamente il tipo di dato e stampa la forma dell'array.
print("-----------------------------------------------------------------------------")
print()
print(arr_B.dtype)
print()
print(arr_B)
print()
print(arr_B.shape)

