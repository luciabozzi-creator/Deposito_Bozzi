# Scrivi un programma in Python che calcola il prezzo di una pizza in base alla dimensione scelta e al tipo di pagamento.
# Il menu prevede tre dimensioni di pizza:
# 	* Piccola: 5 euro
# 	* Media: 8 euro
# 	* Grande: 12 euro
# Ci sono però queste regole e sconti speciali:
# 	* Ingrediente Extra: Se l'utente aggiunge la doppia mozzarella, si aggiungono 2 euro al prezzo della pizza (valido per qualsiasi dimensione).
#	* Sconto Studenti: Se l'utente è uno studente, ha diritto a uno sconto del 10% sul totale della pizza (compreso l'eventuale extra).
#	* Supplemento Consegna: Se la pizza viene consegnata a domicilio, si aggiungono 3 euro fissi alla fine.
#	Nota bene: lo sconto studenti si applica solo sulla pizza, non sul costo della consegna!

# Cosa deve fare il programma:
# 	1. Definire le variabili di partenza (es. dimensione = 'media, doppia mozzarella = True, studente = True, domicilio = False).
#	2. Usare if-elif-else per impostare il prezzo di partenza in base alla dimensione.
#	3. Gestire l'aggiunta della doppia mozzarella.
#	4. Applicare lo sconto se l'utente è studente (puoi calcolare lo sconto facendo: prezzo = prezzo * 0.9).
#	5. Aggiungere il costo di consegna se richiesto.
#	6. Stampare il prezzo finale.

import locale
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

Dimensioni = input("Vuoi una pizza piccola (5 euro), media (8 euro) o grande (12 euro)? ")
Dimensioni = Dimensioni.upper()
print("Dimensioni:",Dimensioni)

if Dimensioni == "PICCOLA":
    Prezzo = 5.00
elif Dimensioni == "MEDIA":
    Prezzo = 8.00
elif Dimensioni == "GRANDE":
    Prezzo = 12.00   
else:
    print("Errore input dimensione pizza")
    Dimensioni = input("Vuoi una pizza piccola (5 euro), media (8 euro) o grande (12 euro)? ")
    Dimensioni = Dimensioni.upper()
    
if Dimensioni == "PICCOLA":
    Prezzo = 5.00
elif Dimensioni == "MEDIA":
    Prezzo = 8.00
elif Dimensioni == "GRANDE":
    Prezzo = 12.00   

Mozzarella = input("Vuoi la doppia mozzarella per due euro in più? SI/NO ")
Mozzarella = Mozzarella.upper()
print("Mozzarella:",Mozzarella)

Studente = input("Sei uno studente? (Sconto 10%) SI/NO ")
Studente = Studente.upper()
print("Studente:",Studente)

Consegna = input("Vuoi la consegna a domicilio con un costo di 3 euro? SI/NO ")
Consegna = Consegna.upper()
print("Consegna:",Consegna)


if Mozzarella == "SI":
    Prezzo +=2.00
elif Mozzarella == "NO":
    pass
else:
    print("Errore input scelta mozzarella")
  

if Studente == "SI":
    Prezzo *= (100-10)/100
elif Studente == "NO":
    pass
else:
    print("Errore input stato studente")


if Consegna == "SI":
    Prezzo += 3.00
elif Consegna == "NO":
    pass
else:
    print("Errore input scelta consegna")


print("Prezzo finale pizza:", locale.currency(Prezzo, grouping=True))

