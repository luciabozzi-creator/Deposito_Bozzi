"""Esercizio Slicing e Fancy Indexing - NumPy"""

import numpy as np


# 1. Crea un array 1D di 20 numeri interi casuali compresi tra 10 e 50.
array = np.random.randint(10, 50, size=20)
array_originale = array.copy()
print("1. Array creato:", array)

# 2. Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
primi_10 = array[:10]
print("2. Primi 10 elementi:", primi_10)

# 3. Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
ultimi_5 = array[-5:]
print("3. Ultimi 5 elementi:", ultimi_5)

# 4. Estrae gli elementi dall'indice 5 all'indice 15 escluso.
da_5_a_15 = array[5:15]
print("4. Elementi dagli indici 5 a 14:", da_5_a_15)

# 5. Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
ogni_terzo = array[2::3]
print("5. Ogni terzo elemento:", ogni_terzo)

# 6. Modifica gli elementi dall'indice 5 all'indice 10 escluso assegnando 99.
array[5:10] = 99
print("6. Array dopo la modifica degli indici 5-9:", array)

# 7. Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.
print("7. Array originale:", array_originale)
print("   Primi 10:", primi_10)
print("   Ultimi 5:", ultimi_5)
print("   Indici 5-14:", da_5_a_15)
print("   Ogni terzo elemento:", ogni_terzo)
