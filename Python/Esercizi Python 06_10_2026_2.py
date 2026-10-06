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
        
# Creo un dizionario contenente i contatti 

rubrica = {}

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

# Controllo se il cellulare esiste come chiave nella rubrica

    if cellulare in rubrica:

        rubrica[cellulare]["nome"] = input("Modifica il nome in: ")
        rubrica[cellulare]["cognome"] = input("Modifica il cognome in: ")
        rubrica[cellulare]["azienda"] = input("Modifica l'azienda in: ")
        rubrica[cellulare]["localita"] = input("Modifica la località in: ")
        rubrica[cellulare]["telefono_fisso"] = input("Modifica il telefono fisso in: ")
        rubrica[cellulare]["email"] = input("Modifica la email in: ")

        print("Contatto modificato correttamente")
        menu()

    else:
        print("Contatto non trovato")
        menu()


# Cancellazione di un contatto (opzione 2)

def cancella_contatto():

    cellulare = input("Inserisci il cellulare del contatto da cancellare: ")

# Controllo se il cellulare esiste come chiave nella rubrica

    if cellulare in rubrica:

        del rubrica[cellulare]

        print("Contatto cancellato correttamente")
        menu()

    else:
        print("Contatto non trovato")
        menu()

# Lancio il programma
menu()
