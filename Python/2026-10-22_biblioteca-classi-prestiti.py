# Esercizio: Gestione Prestiti Biblioteca - con le classi.

"""
a) create la classe Biblioteca (che contiene oggetti di tipo Libro):
    a.1 - inserisci Libro
    a.2 - verifica Libro
    a.3 - elimina Libro
    a.4 - mostra Libri in Biblioteca
b) create la classe Libro (Titolo, autore, isbn)
    b.1 - modificare un titolo
    b.2 - modificare un autore
    b.3 - numero copie Libro
    b.4 - mostra isbn
c) create la classe Utente (numero tessera/CF, nome)
    c.1 - inserisci utente
    c.2 - elimina utente
    c.3 - mostra numero tessera/CF
    Ereditarietà e durata massima del prestito:
        Utente generico: 15 giorni
        Studente: 30 giorni
        Docente: 90 giorni
        Pensionato: 45 giorni
d) gestione dei prestiti (max 3 libri per utente)
    d.1 - verificare quanti libri ha preso in prestito l'utente
    d.2 - verificare quante copie sono disponibili
    d.3 - effettuare il prestito (associare il libro all'utente e scalare il numero
          di copie disponibili)
    d.4 - restituire il prestito (svincolare il libro dall'utente e scalare il numero
          di copie disponibili)
    d.5 - mostrare quali libri ha in prestito l'utente
    d.6 - gestire i solleciti
"""


# Biblioteca contiene i libri e svolge i punti a.1-a.4.
class Biblioteca:
    def __init__(self):
        # ISBN/codice libro -> oggetto Libro
        self.libri = {}
        # Tessera/codice utente -> oggetto Utente
        self.utenti = {}

    # a.1 - Chiede i dati e inserisce un libro nel dizionario.
    def inserisci_libro(self):
        isbn = input("Nuovo codice libro (es. 4): ")
        titolo = input("Titolo: ")
        autore = input("Autore: ")
        copie = int(input("Numero copie: "))

        if isbn in self.libri:
            print("Codice già presente.")
        else:
            self.libri[isbn] = Libro(isbn, titolo, autore, copie)
            print("Libro inserito.")

    # a.2 - Cerca un libro tramite codice e ne mostra i dati.
    def verifica_libro(self):
        isbn = input("Codice libro (1, 2 o 3): ")
        if isbn not in self.libri:
            print("Libro non trovato.")
        else:
            self.libri[isbn].mostra_dati()

    # a.3 - Elimina un libro se non ha prestiti attivi.
    def elimina_libro(self, prestiti):
        isbn = input("Codice libro da eliminare (1, 2 o 3): ")
        if isbn not in self.libri:
            print("Libro non trovato.")
        elif isbn in prestiti:
            print("Prima bisogna registrare la restituzione dei prestiti.")
        else:
            del self.libri[isbn]
            print("Libro eliminato.")

    # a.4 - Mostra tutti i libri presenti in biblioteca.
    def mostra_libri(self):
        if not self.libri:
            print("Non ci sono libri.")
            return

        for libro in self.libri.values():
            libro.mostra_dati()


# Libro contiene i dati e svolge i punti b.1-b.4.
class Libro:
    # Crea un libro con codice, titolo, autore e copie.
    def __init__(self, isbn, titolo, autore, numero_copie):
        self.isbn = isbn
        self.titolo = titolo
        self.autore = autore
        self.numero_copie = numero_copie
        self.copie_disponibili = numero_copie

    # b.1 - Modifica il titolo di questo libro.
    def modifica_titolo(self):
        self.titolo = input("Nuovo titolo: ")
        print("Titolo modificato.")

    # b.2 - Modifica l'autore di questo libro.
    def modifica_autore(self):
        self.autore = input("Nuovo autore: ")
        print("Autore modificato.")

    # b.3 - Mostra il numero totale di copie del libro.
    def mostra_numero_copie(self):
        print("Numero totale di copie:", self.numero_copie)

    # b.4 - Mostra il codice/ISBN di questo libro.
    def mostra_isbn(self):
        print(self.isbn)

    # Supporto ad a.2 e a.4: mostra i dati del libro.
    def mostra_dati(self):
        print(self.isbn, self.titolo, self.autore,
              "Copie totali:", self.numero_copie,
              "Copie disponibili:", self.copie_disponibili)


# Utente contiene i dati e svolge i punti c.1-c.3.
class Utente:
    # Crea un utente con tessera/codice e nome.
    def __init__(self, tessera, nome):
        self.tessera = tessera
        self.nome = nome

    # c.1 - Inserisce questo utente nel dizionario.
    def inserisci_utente(self, utenti):
        if self.tessera in utenti:
            print("Codice utente già presente.")
        else:
            utenti[self.tessera] = self
            print("Utente inserito.")

    # c.2 - Elimina questo utente se non ha prestiti attivi.
    def elimina_utente(self, utenti, prestiti):
        for prestiti_libro in prestiti.values():
            if self.tessera in prestiti_libro:
                print("Prima bisogna registrare la restituzione dei prestiti.")
                return

        del utenti[self.tessera]
        print("Utente eliminato.")

    # c.3 - Mostra il numero tessera/CF di questo utente.
    def mostra_tessera(self):
        print(self.tessera)

    # Utente generico: durata massima del prestito di 15 giorni.
    def giorni_massimi_prestito(self):
        return 15


# Studente è una sottoclasse di Utente.
class Studente(Utente):
    # Durata massima del prestito per uno studente: 30 giorni.
    def giorni_massimi_prestito(self):
        return 30


# Docente è una sottoclasse di Utente.
class Docente(Utente):
    # Durata massima del prestito per un docente: 90 giorni.
    def giorni_massimi_prestito(self):
        return 90


# Pensionato è una sottoclasse di Utente.
class Pensionato(Utente):
    # Durata massima del prestito per un pensionato: 45 giorni.
    def giorni_massimi_prestito(self):
        return 45


# Prestito gestisce il dizionario e svolge tutti i punti d.1-d.6.
class Prestito:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        # ISBN/codice libro -> {tessera/codice utente -> dati del prestito}
        self.prestiti = {}

    # d.1 - Conta quante copie ha in prestito l'utente scelto.
    def conta_libri_utente(self):
        tessera = input("Codice utente (1, 2 o 3): ")
        if tessera not in self.biblioteca.utenti:
            print("Utente non trovato.")
            return

        totale = 0
        for prestiti_libro in self.prestiti.values():
            if tessera in prestiti_libro:
                totale += prestiti_libro[tessera]["copie"]
        print("Libri in prestito:", totale)

    # d.2 - Mostra le copie disponibili del libro scelto.
    def verifica_copie_disponibili(self):
        isbn = input("Codice libro (1, 2 o 3): ")
        if isbn not in self.biblioteca.libri:
            print("Libro non trovato.")
        else:
            copie = self.biblioteca.libri[isbn].copie_disponibili
            print("Copie disponibili:", copie)

    # d.3 - Registra il prestito e scala le copie disponibili.
    def registra_prestito(self):
        isbn = input("Codice libro (1, 2 o 3): ")
        tessera = input("Codice utente (1, 2 o 3): ")
        giorni = int(input("Giorni del prestito: "))
        copie = int(input("Numero copie: "))

        if isbn not in self.biblioteca.libri:
            print("Libro non trovato.")
            return
        if tessera not in self.biblioteca.utenti:
            print("Utente non trovato.")
            return
        if copie <= 0:
            print("Il numero di copie deve essere maggiore di zero.")
            return

        libro = self.biblioteca.libri[isbn]
        if copie > libro.copie_disponibili:
            print("Non ci sono abbastanza copie disponibili.")
            return

        copie_gia_prestito = 0
        for prestiti_libro in self.prestiti.values():
            if tessera in prestiti_libro:
                copie_gia_prestito += prestiti_libro[tessera]["copie"]

        if copie_gia_prestito + copie > 3:
            print("Un utente può avere al massimo 3 libri in prestito.")
            return

        if isbn in self.prestiti:
            if tessera in self.prestiti[isbn]:
                print("Questo prestito è già registrato.")
                return
        else:
            self.prestiti[isbn] = {}

        self.prestiti[isbn][tessera] = {"giorni": giorni, "copie": copie}
        libro.copie_disponibili -= copie
        print("Prestito registrato.")

    # d.4 - Registra la restituzione e ripristina le copie disponibili.
    def restituisci_prestito(self):
        isbn = input("Codice libro (1, 2 o 3): ")
        tessera = input("Codice utente (1, 2 o 3): ")
        if isbn not in self.prestiti or tessera not in self.prestiti[isbn]:
            print("Prestito non trovato.")
            return

        copie = self.prestiti[isbn][tessera]["copie"]
        self.biblioteca.libri[isbn].copie_disponibili += copie
        del self.prestiti[isbn][tessera]

        if not self.prestiti[isbn]:
            del self.prestiti[isbn]
        print("Restituzione registrata.")

    # d.5 - Mostra quali libri ha in prestito l'utente scelto.
    def mostra_prestiti_utente(self):
        tessera = input("Codice utente (1, 2 o 3): ")
        if tessera not in self.biblioteca.utenti:
            print("Utente non trovato.")
            return

        trovato = False
        for isbn, prestiti_libro in self.prestiti.items():
            if tessera in prestiti_libro:
                dati_prestito = prestiti_libro[tessera]
                libro = self.biblioteca.libri[isbn]
                print(libro.titolo, "- Copie:", dati_prestito["copie"],
                      "- Giorni:", dati_prestito["giorni"])
                trovato = True

        if not trovato:
            print("Questo utente non ha prestiti attivi.")

    # d.6 - Mostra i prestiti oltre il numero di giorni indicato.
    def mostra_solleciti(self):
        giorni_limite = int(input("Mostra i prestiti oltre quanti giorni? "))
        trovato = False
        for isbn, prestiti_libro in self.prestiti.items():
            for tessera, dati_prestito in prestiti_libro.items():
                if dati_prestito["giorni"] > giorni_limite:
                    utente = self.biblioteca.utenti[tessera]
                    libro = self.biblioteca.libri[isbn]
                    print("Sollecito:", utente.nome, "-", libro.titolo)
                    trovato = True

        if not trovato:
            print("Nessun sollecito da mostrare.")


# Dati di esempio: i codici sono semplici e già caricati.
biblioteca = Biblioteca()
biblioteca.libri = {
    "1": Libro("1", "Libro 1", "Autore 1", 2),
    "2": Libro("2", "Libro 2", "Autore 2", 3),
    "3": Libro("3", "Libro 3", "Autore 3", 1),
}
biblioteca.utenti = {
    "1": Utente("1", "Persona 1"),
    "2": Utente("2", "Persona 2"),
    "3": Utente("3", "Persona 3"),
}
prestito = Prestito(biblioteca)
prestito.prestiti = {
    "1": {
        "1": {"giorni": 7, "copie": 1},
    },
}
# La copia già prestata non è più disponibile.
biblioteca.libri["1"].copie_disponibili -= 1


# Il menu richiama direttamente il metodo relativo al punto scelto.
def menu():
    print("\\n--- MENU ---")
    print("1. a.1 - Inserisci un libro")
    print("2. a.2 - Cerca/verifica un libro")
    print("3. a.3 - Elimina un libro")
    print("4. a.4 - Mostra tutti i libri")
    print("5. b.1 - Modifica il titolo")
    print("6. b.2 - Modifica l'autore")
    print("7. b.3 - Mostra il numero totale di copie")
    print("8. b.4 - Mostra l'ISBN")
    print("9. c.1 - Inserisci un utente")
    print("10. c.2 - Elimina un utente")
    print("11. c.3 - Mostra il numero tessera/CF")
    print("12. d.1 - Conta i libri in prestito all'utente")
    print("13. d.2 - Verifica le copie disponibili")
    print("14. d.3 - Registra un prestito")
    print("15. d.4 - Registra una restituzione")
    print("16. d.5 - Mostra i prestiti di un utente")
    print("17. d.6 - Mostra i solleciti")
    print("0. Esci")


# Il ciclo continua finché l'utente non sceglie 0.
scelta = ""
while scelta != "0":
    menu()
    scelta = input("Scegli un punto: ")

    if scelta == "1":
        biblioteca.inserisci_libro()
    elif scelta == "2":
        biblioteca.verifica_libro()
    elif scelta == "3":
        biblioteca.elimina_libro(prestito.prestiti)
    elif scelta == "4":
        biblioteca.mostra_libri()
    elif scelta == "5":
        isbn = input("Codice libro (1, 2 o 3): ")
        if isbn in biblioteca.libri:
            biblioteca.libri[isbn].modifica_titolo()
        else:
            print("Libro non trovato.")
    elif scelta == "6":
        isbn = input("Codice libro (1, 2 o 3): ")
        if isbn in biblioteca.libri:
            biblioteca.libri[isbn].modifica_autore()
        else:
            print("Libro non trovato.")
    elif scelta == "7":
        isbn = input("Codice libro (1, 2 o 3): ")
        if isbn in biblioteca.libri:
            biblioteca.libri[isbn].mostra_numero_copie()
        else:
            print("Libro non trovato.")
    elif scelta == "8":
        isbn = input("Codice libro (1, 2 o 3): ")
        if isbn in biblioteca.libri:
            biblioteca.libri[isbn].mostra_isbn()
        else:
            print("Libro non trovato.")
    elif scelta == "9":
        tessera = input("Nuovo codice utente (es. 4): ")
        nome = input("Nome: ")
        utente = Utente(tessera, nome)
        utente.inserisci_utente(biblioteca.utenti)
    elif scelta == "10":
        tessera = input("Codice utente (1, 2 o 3): ")
        if tessera not in biblioteca.utenti:
            print("Utente non trovato.")
        else:
            biblioteca.utenti[tessera].elimina_utente(
                biblioteca.utenti, prestito.prestiti)
    elif scelta == "11":
        tessera = input("Codice utente (1, 2 o 3): ")
        if tessera in biblioteca.utenti:
            biblioteca.utenti[tessera].mostra_tessera()
        else:
            print("Utente non trovato.")
    elif scelta == "12":
        prestito.conta_libri_utente()
    elif scelta == "13":
        prestito.verifica_copie_disponibili()
    elif scelta == "14":
        prestito.registra_prestito()
    elif scelta == "15":
        prestito.restituisci_prestito()
    elif scelta == "16":
        prestito.mostra_prestiti_utente()
    elif scelta == "17":
        prestito.mostra_solleciti()
    elif scelta == "0":
        print("Programma terminato.")
    else:
        print("Scelta non valida.")
