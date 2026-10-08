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
    "L001": {"titolo": "Titolo1", "autore": "Autore1"},
    "L002": {"titolo": "Titolo2", "autore": "Autore2"},
    "L003": {"titolo": "Titolo3", "autore": "Autore3"},
    "L004": {"titolo": "Titolo4", "autore": "Autore4"},
    "L005": {"titolo": "Titolo5", "autore": "Autore5"},
    "L006": {"titolo": "Titolo6", "autore": "Autore6"}}

# Creo un dizionario vuoto che conterrà i prestiti

prestiti = {
    "L001": {
        "utente": "Utente1",
        "documento": "AB123456",
        "email": "mario@email.it",
        "numero_giorni": 7,
        "giorno_prestito": 2},

    "L002": {
        "utente": "Utente2",
        "documento": "CD789012",
        "email": "anna@email.it",
        "numero_giorni": 5,
        "giorno_prestito": 6},

    "L003": {
        "utente": "Utente1",
        "documento": "AB123456",
        "email": "mario@email.it",
        "numero_giorni": 10,
        "giorno_prestito": 9}
}

# Creo la variabile giorno per capire che giorno è al momento del lancio del programma

giorno = int(input("Che giorno è oggi partendo da 1?: "))

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
        

# Funzione 7 - Visualizzare lo stato di tutti i libri

def stato_libri():

    print("STATO DEI LIBRI DELLA BIBLIOTECA")
    print("Giorno attuale:", giorno)

    for codice in libri:

        print()
        print("Codice:", codice)
        print("Titolo:", libri[codice]["titolo"])
        print("Autore:", libri[codice]["autore"])

        if codice in prestiti:

            print("Stato: IN PRESTITO")
            print("Utente:", prestiti[codice]["utente"])

            giorno_prestito = prestiti[codice]["giorno_prestito"]
            numero_giorni = prestiti[codice]["numero_giorni"]

            giorno_scadenza = giorno_prestito + numero_giorni

            print("Giorno del prestito:", giorno_prestito)
            print("Durata del prestito:", numero_giorni, "giorni")
            print("Giorno di scadenza:", giorno_scadenza)

            if giorno > giorno_scadenza:
                print("ATTENZIONE: PRESTITO SCADUTO!")

        else:
            print("Stato: DISPONIBILE")

# Menu principale

def menu():

# Utilizzo la variabile globale giorno

    global giorno

    scelta = ""

    while scelta != "0":

        print()
        print("Giorno:", giorno)
        print("1. Chiedi un libro in prestito")
        print("2. Verifica se un libro è presente o in prestito")
        print("3. Inserisci un nuovo libro")
        print("4. Invia un sollecito")
        print("5. Stampa i libri in prestito di un utente")
        print("6. Restituisci un libro")
        print("7. Visualizza lo stato di tutti i libri")
        print("8. Cambia il numero del giorno")
        print("0. Esci")

        scelta = input("Digita la tua scelta: ")

        if scelta == "1": chiedi_prestito()
        elif scelta == "2": verifica_libro()
        elif scelta == "3": inserisci_libro()
        elif scelta == "4": invia_sollecito()
        elif scelta == "5": stampa_prestiti_utente()
        elif scelta == "6": restituisci_libro()
        elif scelta == "7": stato_libri()
        elif scelta == "8": giorno = int(input("Inserisci il nuovo giorno attuale: "))
        elif scelta == "0": print("Programma terminato")
        else:
            print("Scelta non valida")

# Lancio il programma

menu()