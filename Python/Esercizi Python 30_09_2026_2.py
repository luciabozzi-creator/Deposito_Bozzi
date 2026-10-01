"""
Esercizio: Il ciclo for

frutti = ["mela","pera","pesca","uva"]

for elemento in frutti:
    print(f"Mi piace la {elemento}")
    
for i in range(2, 5):
    print(f"Tentativo numero {i}")
    

Esercizio: La spesa del giorno (Liste + Ciclo while)

Scenario: Devi creare un programma per gestire una lista della spesa.

• Crea una lista vuota chiamata lista_spesa.
• Usa un ciclo while per chiedere all'utente cosa vuole comprare (usando .strip()).
• Se l'utente scrive "fine", il ciclo si interrompe.
• Altrimenti, aggiungi l'elemento alla lista usando il metodo .append().
• Stampate prima il numero di elemento della lista completa
• Alla fine, stampa la lista completa usando una f-string.

"""
lista_spesa = [] # Creo una lista vuota

while (True): # Inizio il ciclo
  
    Prodotto = input(f"Prodotto numero {len(lista_spesa) + 1}: ").strip() # Chiedo cosa vuole comprare e tolgo eventuali spazi

    if Prodotto.upper() == "FINE": # Se scrive "fine", termino il ciclo
        break
    
    lista_spesa.append(Prodotto) # Altrimenti aggiungo l'elemento alla lista

print(f"Numero prodotti: {len(lista_spesa)}") # Stampo il numero di elementi

print(f"Lista della spesa: {lista_spesa}") # Stampo la lista completa