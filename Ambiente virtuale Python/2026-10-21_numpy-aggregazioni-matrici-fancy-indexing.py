# Esercizi NumPy assegnati il 21 ottobre 2026.
# Nome e collocazione seguono la convenzione dei file NumPy della lezione.

import numpy as np


# ESERCIZIO 1: SOMMA E MEDIA DI ELEMENTI
# Consegna:
# Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
# Calcolare e stampare la somma di tutti gli elementi dell'array.
# Calcolare e stampare la media di tutti gli elementi dell'array.

print("ESERCIZIO 1: SOMMA E MEDIA DI ELEMENTI")

# randint esclude il limite superiore: 101 permette di includere anche 100.
array1 = np.random.randint(1, 101, size=15)
print("Array casuale:", array1)

somma1 = np.sum(array1)
media1 = np.mean(array1)
print("Somma degli elementi:", somma1)
print("Media degli elementi:", media1)


# ESERCIZIO 2: MANIPOLAZIONE DI ARRAY MULTIDIMENSIONALI
# Consegna:
# Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
# Estrarre e stampare la seconda colonna della matrice.
# Estrarre e stampare la terza riga della matrice.
# Calcolare e stampare la somma degli elementi della diagonale principale.

print("\nESERCIZIO 2: MANIPOLAZIONE DI ARRAY MULTIDIMENSIONALI")

# arange esclude il limite superiore: 26 permette di arrivare fino a 25.
matrice2 = np.arange(1, 26).reshape(5, 5)
print("Matrice 5x5:\n", matrice2)

# Gli indici partono da 0: la seconda colonna ha indice 1.
seconda_colonna = matrice2[:, 1]
print("Seconda colonna:", seconda_colonna)

# La terza riga ha indice 2.
terza_riga = matrice2[2, :]
print("Terza riga:", terza_riga)

# Selezioniamo le posizioni (0,0), (1,1), ..., (4,4) con gli indici delle righe e colonne.
indici_diagonale = [0, 1, 2, 3, 4]
diagonale_principale = matrice2[indici_diagonale, indici_diagonale]
somma_diagonale = np.sum(diagonale_principale)
print("Diagonale principale:", diagonale_principale)
print("Somma della diagonale principale:", somma_diagonale)


# ESERCIZIO 3: OPERAZIONI CON FANCY INDEXING
# Consegna:
# Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
# Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici
# (0, 1), (1, 3), (2, 2) e (3, 0).
# Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari
# dell'array (considerando la numerazione delle righe che parte da 0).
# Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo
# 10 al loro valore.

print("\nESERCIZIO 3: OPERAZIONI CON FANCY INDEXING")

# Anche qui randint esclude il limite superiore: 51 permette di includere 50.
matrice3 = np.random.randint(10, 51, size=(4, 4))
print("Matrice casuale iniziale:\n", matrice3)

# Gli indici di riga e colonna corrispondono a coppie:
# (0, 1), (1, 3), (2, 2) e (3, 0).
riga_indici = [0, 1, 2, 3]
colonna_indici = [1, 3, 2, 0]
elementi_selezionati = matrice3[riga_indici, colonna_indici]
print("Elementi agli indici richiesti:", elementi_selezionati)

# Con numerazione da zero, le righe dispari hanno indici 1 e 3.
righe_dispari = matrice3[[1, 3], :]
print("Righe con indici dispari (1 e 3):\n", righe_dispari)

# Aggiunge 10 proprio alle quattro celle selezionate in precedenza.
matrice3[riga_indici, colonna_indici] += 10
print("Matrice dopo aver aggiunto 10 agli elementi selezionati:\n", matrice3)
