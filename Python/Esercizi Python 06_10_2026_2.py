"""
Esercizio: Rubrica telefonica.

Creare una rubrica telefonica che consente di inserire i dati di contatti (nome, conome,
azienda, località sede azienda, telefono cellulare, telefono fisso, indirizzo email).

La struttura dati deve essere un dizionario. L'inserimento dei contatti avviene
tramite inpunt da tastiera.

L'agenza deve avere delle funzioni definite dal programmatore che consentano:
1. La modifica dei dati
2. La cancellazione di un contatto
3. L'inserimento di un contatto
4. La cancellazione di tutti i contatti
5. La ricerca di un contatto
6. La stampa dei contatti tramite filtro (es. azienda oppure prefisso telefonico)

"""

# Creo il dizionario contenente alcuni contatti iniziali
# Il numero di cellulare viene utilizzato come chiave

rubrica = {
    "3331234567": {"nome": "Mario", "cognome": "Rossi", "azienda": "Spotify", "localita": "Milano", "cellulare": "3331234567", "telefono_fisso": "021234567", "email": "mario.rossi@email.it"},
    "3472345678": {"nome": "Anna", "cognome": "Bianchi", "azienda": "Adobe", "localita": "Roma", "cellulare": "3472345678", "telefono_fisso": "061234567", "email": "anna.bianchi@email.it"},
    "3333456789": {"nome": "Luca", "cognome": "Verdi", "azienda": "Spotify", "localita": "Torino", "cellulare": "3333456789", "telefono_fisso": "011234567", "email": "luca.verdi@email.it"},
    "3204567890": {"nome": "Sara", "cognome": "Neri", "azienda": "Nintendo", "localita": "Milano", "cellulare": "3204567890", "telefono_fisso": "029876543", "email": "sara.neri@email.it"},
    "3475678901": {"nome": "Paolo", "cognome": "Conti", "azienda": "Adobe", "localita": "Napoli", "cellulare": "3475678901", "telefono_fisso": "081234567", "email": "paolo.conti@email.it"},
    "3206789012": {"nome": "Giulia", "cognome": "Moretti", "azienda": "LEGO", "localita": "Bologna", "cellulare": "3206789012", "telefono_fisso": "051234567", "email": "giulia.moretti@email.it"},
    "3337890123": {"nome": "Andrea", "cognome": "Romano", "azienda": "Ferrari", "localita": "Modena", "cellulare": "3337890123", "telefono_fisso": "059234567", "email": "andrea.romano@email.it"}}     

# Inserimento di un nuovo contatto con una funzione (funzione 3)

def inserisci_contatto():

# Chiedo all'utente i dati del nuovo contatto

    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    azienda = input("Inserisci l'azienda: ")
    localita = input("Inserisci la località dell'azienda: ")
    cellulare = input("Inserisci il cellulare: ")
    telefono_fisso = input("Inserisci il telefono fisso: ")
    email = input("Inserisci l'email: ")

# Inserisco il nuovo contatto nella rubrica
# Il numero di cellulare viene utilizzato come chiave

    rubrica[cellulare] = {
        "nome": nome,
        "cognome": cognome,
        "azienda": azienda,
        "localita": localita,
        "cellulare": cellulare,
        "telefono_fisso": telefono_fisso,
        "email": email}

    print("Nuovo contatto inserito")
    menu()
    
# Modifica dei dati di un contatto (scelta uno)

def modifica_contatto():

    cellulare = input("Inserisci il cellulare del contatto da modificare: ")

    if cellulare in rubrica:

        rubrica[cellulare]["nome"] = input("Modifica il nome in: ")
        rubrica[cellulare]["cognome"] = input("Modifica il cognome in: ")
        rubrica[cellulare]["azienda"] = input("Modifica l'azienda in: ")
        rubrica[cellulare]["localita"] = input("Modifica la località in: ")
        rubrica[cellulare]["telefono_fisso"] = input("Modifica il telefono fisso in: ")
        rubrica[cellulare]["email"] = input("Modifica la email in: ")

        print("Contatto modificato correttamente")

    else:
        print("Contatto non trovato")
    

# Cancellazione di un contatto (opzione 2)

def cancella_contatto():

    cellulare = input("Inserisci il cellulare del contatto da cancellare: ")

# Controllo se il cellulare esiste come chiave nella rubrica

    if cellulare in rubrica:

        del rubrica[cellulare]

        print("Contatto cancellato correttamente")
       
    else:
        print("Contatto non trovato")
      

# Cancellazione di tutti i contatti (opzione 4)

def cancella_tutti_contatti():

# Cancello tutti i contatti presenti nella rubrica

    rubrica.clear()
    print("Tutti i contatti sono stati cancellati")
      
# Ricerca di un contatto (opzione 5)

def ricerca_contatto():

# Chiedo il cellulare del contatto da cercare

    cellulare = input("Inserisci il numero di cellulare del contatto da cercare: ")

    if cellulare in rubrica:

        print("Contatto trovato:")
        print(rubrica[cellulare])
       
    else:
        print("Contatto non trovato")
             
# Stampa dei contatti (opzione 6)

def stampa_contatti():

# Chiedo all'utente cosa vuole stampare

    print("1. Stampa tutti i contatti")
    print("2. Filtra per azienda")
    print("3. Filtra per prefisso telefonico")

    scelta_filtro = input("Scegli cosa vuoi fare: ")

# Stampa tutti i contatti

    if scelta_filtro == "1":

        for cellulare in rubrica:
            print(rubrica[cellulare])

# Filtro per azienda

    elif scelta_filtro == "2":

        azienda = input("Inserisci l'azienda: ")
        trovato = False

        for cellulare in rubrica:

            if rubrica[cellulare]["azienda"] == azienda:
                print(rubrica[cellulare])
                trovato = True

        if trovato == False:
            print("Nessun contatto trovato")

# Filtro per prefisso telefonico

    elif scelta_filtro == "3":

        prefisso = input("Inserisci il prefisso telefonico: ")
        trovato = False

        for cellulare in rubrica:

            if cellulare[:len(prefisso)] == prefisso:
                print(rubrica[cellulare])
                trovato = True

        if trovato == False:
            print("Nessun contatto trovato")

    else:
        print("Scelta non valida")
        
# Menu principale

def menu():

    scelta = ""

    while scelta != "0":

        print("Benvenuto nella rubrica, seleziona dal menù cosa vuoi fare scrivendo il relativo numero:")
        print("1. Modifica i dati di un contatto")
        print("2. Cancella un contatto")
        print("3. Inserisci un nuovo contatto")
        print("4. Cancella tutti i contatti")
        print("5. Cerca un contatto")
        print("6. Stampa i contatti")
        print("0. Esci")

        scelta = input("Digita la tua scelta: ")

        if scelta == "1": modifica_contatto()
        elif scelta == "2": cancella_contatto()
        elif scelta == "3": inserisci_contatto()
        elif scelta == "4": cancella_tutti_contatti()
        elif scelta == "5": ricerca_contatto()
        elif scelta == "6": stampa_contatti()
        elif scelta == "0": print("Programma terminato")
        else:
            print("Scelta non valida")

menu()

