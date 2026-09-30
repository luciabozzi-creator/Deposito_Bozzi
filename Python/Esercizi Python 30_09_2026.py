# Esercizio: Il controllo del PIN (Sicurezza)

# Consegna:
# Crea un programma che simuli lo sblocco di un telefono.
# Imposta un PIN corretto all'interno di una variabile (es. 12345).
# Chiedi all'utente di inserire il PIN usando input().

# Nello svolgimento della traccia, verificare la lunghezza del PIN.
# Generare un codice di errore e chiedere di nuovo il PIN per un massimo di 3 volte.
# Se è sbagliato per tre volte, stampa "PIN errato. Telefono Bloccato."
# Il controllo del PIN deve essere fatto cifra per cifra.
# Utilizzare gli operatori booleani per effettuare il controllo.

# Se il PIN è corretto, stampa "Telefono sbloccato!" e interrompi il programma.
# Se è sbagliato, stampa "PIN errato. Riprova." e chiedilo di nuovo.



PIN_Corretto = "12345678" 					# 1 Fissare il PIN di sblocco e il contatore tentativi
Tentativi = 0

while Tentativi < 3: 
    
    PIN = input("Digita il PIN: ")			# 2 Prendere in input il PIN        

    if len(PIN) == len(PIN_Corretto): 		# 3 Controllare la lunghezza del PIN

        PIN_Valido = True 					# 4 Caso giusto nella lunghezza del pin: vado avanti e imposto i per il controllo dei caratteri
        i = 0

        while i < len(PIN_Corretto): 		# 6 Controllo il PIN carattere per carattere con la i
            if PIN[i] == PIN_Corretto[i]:
                i += 1
                
            else: 							# 7 Caso errato: esco dal controllo carattere per carattere
                PIN_Valido = False
                break

        if PIN_Valido == True: 				# 8. Caso giusto: i caratteri sono tutti uguali

            print("Telefono sbloccato!")	# 9. Telefono sbloccato esco dal while
            break

        else:
            print("PIN errato. Riprova.")	# 10. Caso errato: Pin errato nel controllo carattere
            Tentativi += 1

    else:  
        print("PIN errato, Numero caratteri diverso. Riprova.")  # 11. Caso errato nella lunghezza caratteri e richiedo pin 
        Tentativi += 1

if Tentativi == 3:							# 11. Caso errato nei check caratteri e richiedo pin
    print("PIN errato per tre volte. Telefono bloccato!")