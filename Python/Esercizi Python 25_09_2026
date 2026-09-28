# Scrivere un programma in Python che calcola il prezzo del
# biglietto di un cinema in base all'età dell'utente e al
# giorno della settimana.

# Il prezzo base del biglietto è di 10 euro, ma ci sono queste
# regole per gli sconti:
# 1) Se l'utente ha meno di 5 anni, il biglietto è sempre gratis (0 euro).
# 2) Se l'utente ha tra i 5 e i 12 anni (compresi), paga una tariffa ridotta di 6 euro.
# 3) Se l'utente ha più di 65 anni (compresi), paga una tariffa ridotta di 7 euro
# 4) Per tutti gli altri, il prezzo è quello base (10 euro)
# 5) Regola speciale: Se oggi è mercoledì si applica uno sconto extra di 2 euro sul prezzo finale calcolato (tranne per chi entra gratis)

Eta = int(input("Salve, benvenuto, ora calcoliamo il prezzo del tuo biglietto, quanti anni hai? "))
Giorno = input("Indica in quale giorno della settimana vuoi andare al cinema? lunedì, martedi...? ")
 
# Ora converto il giorno in maiuscolo cosi posso gestirlo meglio

Giorno_Upper = str(Giorno.upper())

print("Giorno della settimana:",Giorno_Upper), print("Età indicata:",Eta)

if	(Eta < 5):
    Costo_Parziale = 0
    Costo_Finale = 0
        
elif (5 <= Eta <= 12): 
    Costo_Parziale = 6
    Costo_Finale = 6
            
elif (Eta >= 65):
    Costo_Parziale = 7
    Costo_Finale = 7
        
else:
    Costo_Parziale = 10
    Costo_Finale = 10
    
           
if (Giorno_Upper == "MERCOLEDI" and Eta >= 5):
    Costo_Finale = Costo_Parziale - 2 
    

print ("Il costo del biglietto è: ", Costo_Finale) 


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

Dimensioni = input("Vuoi una pizza piccola (5 euro), media (8 euro) o grande (12 euro)? ")
Dimensioni = Dimensioni.upper()
print("Dimensioni:",Dimensioni)

Mozzarella = input("Vuoi la doppia mozzarella per due euro in più? SI/NO ")
Mozzarella = Mozzarella.upper()
print("Mozzarella:",Mozzarella)

Studente = input("Sei uno studente? (Sconto 10%) SI/NO ")
Studente = Studente.upper()
print("Studente:",Studente)

Consegna = input("Vuoi la consegna a domicilio con un costo di 3 euro? SI/NO ")
Consegna = Consegna.upper()
print("Consegna:",Consegna)



if Dimensioni == "PICCOLA":
    Prezzo = 5
elif Dimensioni == "MEDIA":
    Prezzo = 8
elif Dimensioni == "GRANDE":
    Prezzo = 12

if Mozzarella == "SI":
    Prezzo +=2

if Studente == "SI":
    Prezzo *= 0.90

if Consegna == "SI":
    Prezzo += 3


print("Prezzo finale pizza: ", Prezzo)
