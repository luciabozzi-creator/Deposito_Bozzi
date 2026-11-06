"""

Descrizione: Crea un array utilizzando linspace, cambia la sua forma con reshape, genera un array casuale e calcola la somma degli elementi.
Esercizio:
1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
2. Cambia la forma dell'array a una matrice 3x4.
3. Genera una matrice 3x4 di numeri casuali tra 0 e 1.
4. Calcola e stampa la somma degli elementi di entrambe le matrici.

"""

import numpy as np

np.set_printoptions(linewidth=350)


# 1. Crea un array di 12 numeri equidistanti tra 0 e 1 con np.linspace.
array_linspace = np.linspace(0, 1, 12)

# 2. Cambia la forma dell'array in una matrice di 3 righe e 4 colonne.
matrice_linspace = array_linspace.reshape(3, 4)

# 3. Genera una matrice 3x4 con numeri casuali tra 0 incluso e 1 escluso.
matrice_casuale = np.random.rand(3, 4)

# 4. Calcola e stampa la somma degli elementi di entrambe le matrici.
somma_linspace = np.sum(matrice_linspace)
somma_casuale = np.sum(matrice_casuale)

print("Array creato con linspace:")
print()
print(array_linspace)

print()
print("Matrice linspace trasformata con reshape in 3x4:")
print()
print(matrice_linspace)


print()
print("Matrice casuale:")
print()
print(matrice_casuale)

print()
print("Somma della matrice casuale:", somma_casuale)

print()
print("Somma della matrice linspace:", somma_linspace)

