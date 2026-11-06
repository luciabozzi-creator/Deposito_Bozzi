"""
Esercizio: Gestione Prestiti Biblioteca.

Creare un programma che consente la gestione dei libri di una biblioteca
(titolo del libro, autore, utente che chiede il prestito, documento identità,
numero giorni, numero libri in prestito, email utente).

Il programma deve avere già una serie di libri da poter prestare.

Operazioni:
1. Chiedere un libro in prestito
2. Verificare se un libro è presente o in prestito
3. Inserire un nuovo libro
4. Inviare un sollecito
5. Stampare i libri in prestito di un utente
6. Restituire un libro

"""

# Creo il dizionario con alcuni libri già presenti in biblioteca

libri = {
    "L001": {"titolo": "1984", "autore": "George Orwell"},
    "L002": {"titolo": "Il nome della rosa", "autore": "Umberto Eco"},
    "L003": {"titolo": "Orgoglio e pregiudizio", "autore": "Jane Austen"},
    "L004": {"titolo": "Il Signore degli Anelli", "autore": "J.R.R. Tolkien"},
    "L005": {"titolo": "Harry Potter", "autore": "J.K. Rowling"},
    "L006": {"titolo": "Il piccolo principe", "autore": "Antoine de Saint-Exupéry"}}

# Creo un dizionario vuoto che conterrà i prestiti

prestiti = {}

# Creo la variabile che simula il trascorrere dei giorni

giorno = 0

# Funzione 1 - Chiedere un libro in prestito

def chiedi_prestito():

# Chiedo i dati dell'utente e del libro

    codice_libro = input("Inserisci il codice del libro: ")
    documento = input("Inserisci il documento di identità: ")
    nome = input("Inserisci nome e cognome dell'utente: ")
    email = input("Inserisci l'email dell'utente: ")
    numero_giorni = int(input("Inserisci il numero di giorni del prestito: "))

# Conto quanti libri ha già in prestito questo utente

    numero_libri = 0

    for codice in prestiti:

        if prestiti[codice]["documento"] == documento:
            numero_libri = numero_libri + 1

# Controllo che l'utente non abbia già tre libri

    if numero_libri >= 3:
        print("Prestito non consentito: l'utente ha già tre libri in prestito")

# Controllo che il libro esista in biblioteca

    elif codice_libro not in libri:
        print("Libro non presente in biblioteca")

# Controllo che il libro non sia già in prestito

    elif codice_libro in prestiti:
        print("Libro già in prestito")

# Se tutti i controlli sono superati registro il prestito

    else:
        prestiti[codice_libro] = {
            "utente": nome,
            "documento": documento,
            "email": email,
            "numero_giorni": numero_giorni,
            "giorno_prestito": giorno}

        print("Prestito effettuato correttamente")

# Funzione 2 - Verificare se un libro è presente o in prestito

def verifica_libro():

    codice_libro = input("Inserisci il codice del libro da cercare: ")

# Controllo se il libro è presente nella biblioteca

    if codice_libro in libri:

        print("Libro presente in biblioteca")
        print("Titolo:", libri[codice_libro]["titolo"])
        print("Autore:", libri[codice_libro]["autore"])

# Controllo se il libro è attualmente in prestito

        if codice_libro in prestiti:
            print("Il libro è attualmente in prestito")
        else:
            print("Il libro è disponibile")

    else:
        print("Libro non presente in biblioteca")


# Funzione 3 - Inserire un nuovo libro

def inserisci_libro():

    codice_libro = input("Inserisci il codice del nuovo libro: ")
    titolo = input("Inserisci il titolo: ")
    autore = input("Inserisci l'autore: ")

# Inserisco il nuovo libro nel dizionario

    libri[codice_libro] = {
        "titolo": titolo,
        "autore": autore}

    print("Nuovo libro inserito correttamente")


# Funzione 4 - Inviare un sollecito

def invia_sollecito():

    trovato = False

# Controllo tutti i libri attualmente in prestito

    for codice_libro in prestiti:

# Calcolo quanti giorni sono trascorsi dal giorno del prestito

        giorni_trascorsi = giorno - prestiti[codice_libro]["giorno_prestito"]

# Controllo se sono stati superati i giorni concessi

        if giorni_trascorsi > prestiti[codice_libro]["numero_giorni"]:

            print("SOLLECITO")
            print("Utente:", prestiti[codice_libro]["utente"])
            print("Email:", prestiti[codice_libro]["email"])
            print("Libro:", libri[codice_libro]["titolo"])
            print("Giorni trascorsi:", giorni_trascorsi)

            trovato = True

    if trovato == False:
        print("Non ci sono prestiti scaduti")


# Funzione 5 - Stampare i libri in prestito di un utente

def stampa_prestiti_utente():

    documento = input("Inserisci il documento di identità dell'utente: ")
    trovato = False
    numero_libri = 0

# Cerco tutti i prestiti associati al documento

    for codice_libro in prestiti:

        if prestiti[codice_libro]["documento"] == documento:
            print("Titolo:", libri[codice_libro]["titolo"])
            print("Autore:", libri[codice_libro]["autore"])

            numero_libri = numero_libri + 1
            trovato = True

# Stampo il numero totale di libri in prestito dell'utente

    if trovato == True:
        print("Numero libri in prestito:", numero_libri)

    else:
        print("Nessun libro in prestito per questo utente")


# Funzione 6 - Restituire un libro

def restituisci_libro():

    codice_libro = input("Inserisci il codice del libro da restituire: ")

# Controllo se il libro risulta in prestito

    if codice_libro in prestiti:

        del prestiti[codice_libro]
        print("Libro restituito correttamente")

    else:

        print("Il libro non risulta in prestito")

# Menu principale

def menu():

# Utilizzo la variabile globale giorno

    global giorno

    scelta = ""

    while scelta != "0":

# Ogni nuovo ciclo rappresenta il passaggio di un giorno

        giorno = giorno + 1

        print()
        print("Giorno:", giorno)
        print("1. Chiedi un libro in prestito")
        print("2. Verifica se un libro è presente o in prestito")
        print("3. Inserisci un nuovo libro")
        print("4. Invia un sollecito")
        print("5. Stampa i libri in prestito di un utente")
        print("6. Restituisci un libro")
        print("0. Esci")

        scelta = input("Digita la tua scelta: ")

        if scelta == "1": chiedi_prestito()

        elif scelta == "2": verifica_libro()

        elif scelta == "3": inserisci_libro()

        elif scelta == "4": invia_sollecito()

        elif scelta == "5":  stampa_prestiti_utente()

        elif scelta == "6": restituisci_libro()

        elif scelta == "0": print("Programma terminato")

        else:
            print("Scelta non valida")

# Lancio il programma

menu()