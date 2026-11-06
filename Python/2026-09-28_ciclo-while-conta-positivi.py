# Esercizio Statement while(2)

# conta = 0
# while (True):
#    a = int(input("Digita un numero e premi ENTER (0 per terminare): "))
#    if (a > 0):
#        print("Hai digitato un numero positivo : viene contato")
#    elif (a < 0):
#        print("Hai digitato un numero negativo : NON viene contato")
#        continue
#    else:
#        print("Hai digitato 0 ed il programma termina.")
#        break
#    conta = conta + 1
    
# print("Hai digitato %d numeri positivi." % conta)

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


# Fissare il PIN di sblocco PIN_Corretto = .... e contatore tentativi

# Prendere in input un numero (stringa) e memorizzarlo in PIN

# Vedere quanto è lunga la string PIN e confrontarla con la lunghezza di PIN_Corretto

# Se è OK vado avanti, altrimenti dico all'utente che ha sbagliato

# Caso errato: ripropongo l'input

# Caso giusto: controllo il PIN carattere per carattere

# Caso errato: esco e dico all'utente che ha sbagliato max 3 volte

# Caso giusto: vado avanti

# Telefono sbloccato

PIN_Corretto = '12345678'
Lun_Corretto = 8

Tentativi = 1

while Tentativi <= 3:

    PIN_Digitato = input("Digita il pin per sbloccare il telefono di 8 cifre: ")
    Lun_PIN_Digitato = len(PIN_Digitato)
    print("Lunghezza PIN inserito:", Lun_PIN_Digitato)

    # Check lunghezza

    if Lun_PIN_Digitato == Lun_Corretto:
        print("Lunghezza PIN Corretta")

        # Inizio verifica cifra per cifra

        i = 0
        PIN_Valido = True

        while i < Lun_Corretto:

            if PIN_Corretto[i] == PIN_Digitato[i]:
                i += 1

            else:
                print("PIN errato al carattere:", i)
                PIN_Valido = False
                break

        # Esco dal controllo delle otto cifre

        if PIN_Valido == True:
            print("Telefono sbloccato!")
            break

        else:
            print("PIN errato. Riprova.")
            Tentativi += 1

    else:
        print("Lunghezza PIN errata. Riprova.")
        Tentativi += 1

else:
    print("PIN errato per tre volte, il telefono ora è bloccato!")

       

    
