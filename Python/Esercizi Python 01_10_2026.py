"""
Esercizio: Analisi temperature (Liste + Tuple + Entrambi i cicli)

Scenario: Hai una lista che contiene le temperature registrate in una settimana. Vuoi analizzarle.

- 	Crea una lista di numeri decimali:
    temperature = [14.5, 18.2, 12.0, 19.5, 15.0]

- 	Usa un ciclo for per calcolare la somma di tutte le temperature e trovare la media.

- 	Salva il valore minimo e massimo consentito in una tupla fissa di controllo:
    limiti = (13.0, 19.0)
    (dove 13.0 è il minimo e 19.0 è il massimo).

- 	Usa un ciclo while associato a un indice per scorrere nuovamente la lista e verificare quali temperature sono "fuori norma" (minori del minimo o maggiori del massimo della tupla), stampando un avviso con le f-string.

Temperature = [14.5, 18.2, 12.0, 19.5, 15.0]

"""
# La lista di 5 temperature
Temperature = [14.5, 18.2, 12.0, 19.5, 15.0]

# Ciclo for per fare la media delle temperature sommandole
somma = 0.0

for temperatura in Temperature:
    somma += temperatura

media = somma / 5

print("La temperatura media è: ", media)

# Tupla fissa con limite minimo e massimo
limite = (13.0, 19.0)

# Uso un ciclo while associato a un indice per scorrere nuovamente la lista per capire le fuori norma
indice = 0

while indice < 5:
    if limite[0] <= Temperature[indice] <= limite[1]:
        print(f"La Temperatura {Temperature[indice]} è nella norma")
    else:
        print(f"La Temperatura {Temperature[indice]} è fuori norma")
 
    indice += 1