# La lista di 5 temperature
Temperature = [14.5, 18.2, 12.0, 19.5, 15.0]


# Ciclo for per fare la media delle temperature sommandole
somma = 0.0

for temperatura in Temperature:
    somma += temperatura

media = somma / 5

print(f"La temperatura media della settimana è: {media}°C\n")


# Titolo del controllo
print("--- CONTROLLO ANOMALIE ---")


# Tupla fissa con limite minimo e massimo
limiti = (13.0, 19.0)

# Uso un ciclo while associato a un indice
# per scorrere nuovamente la lista
indice = 0

while indice < 5:

    # Temperatura sotto il limite minimo
    if Temperature[indice] < limiti[0]:
        print(f"Attenzione! Giorno {indice + 1}: {Temperature[indice]}°C è FUORI dagli standard ({limiti[0]}°C - {limiti[1]}°C)")

    # Temperatura sopra il limite massimo
    elif Temperature[indice] > limiti[1]:
        print(f"Attenzione! Giorno {indice + 1}: {Temperature[indice]}°C è FUORI dagli standard ({limiti[0]}°C - {limiti[1]}°C)")

    # Temperatura compresa tra minimo e massimo
    else:
        print(f"Giorno {indice + 1}: {Temperature[indice]}°C è nella norma.")

    # Passo alla temperatura successiva
    indice += 1