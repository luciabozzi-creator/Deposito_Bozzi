"""
Catalogo Film
Creare un programma Python, che utilizzi la libreria sqlite3, per la gestione di un catalogo di film.
Un film è formato da (Nome, Regista, Genere, Durata (in minuti), Nazionalità)
Il genere deve appartenere ad una lista di generi, hardcoded in Python.
Funzionalità:
-Creazione di un menù dove l'utente può:
-Creare ed aggiungere un film al catalogo.
-Rimuovere un film.
-Modificare i parametri di un film.
-Cercare film in base alla nazionalità.
-Uscire dal programma
"""

import sqlite3
conn = sqlite3.connect("catalogo_film.db")

# Creazione del cursore
cursor = conn.cursor()

# Creazione tabella film

cursor.execute("""
CREATE TABLE IF NOT EXISTS Film (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    regista TEXT,
    genere TEXT,
    durata INTEGER,
    nazionalita TEXT)
""")

# Svuotamento della tabella per test
# cursor.execute("DELETE FROM Film")
# conn.commit()

# Salvataggio delle modifiche
conn.commit()

# Aggiunta di film iniziali

film_iniziali = [("Titanic", "James Cameron", "Drammatico", 195, "USA"),
    ("Avatar", "James Cameron", "Fantascienza", 162, "USA"),
    ("La vita è bella", "Roberto Benigni", "Drammatico", 116, "Italia"),
    ("Il gladiatore", "Ridley Scott", "Azione", 155, "USA")]

# cursor.executemany("""INSERT INTO Film (nome, regista, genere, durata, nazionalita) VALUES (?, ?, ?, ?, ?)""", film_iniziali)

conn.commit()
# Lista dei generi disponibili

generi = ["Azione","Commedia","Drammatico","Horror","Fantascienza"]


# Menù

def menu():

    print("\n--- CATALOGO FILM ---")
    print("1. Aggiungi un film")
    print("2. Rimuovi un film")
    print("3. Modifica un film")
    print("4. Cerca film per nazionalità")
    print("5. Visualizza tutti i film")
    print("0. Esci")


# Funzione - Aggiungi un film

def aggiungi_film():

    try:

# Inserimento del nome del film
        nome = input("Inserisci il nome del film: ")

# Inserimento del regista
        regista = input("Inserisci il regista: ")

# Visualizzazione dei generi disponibili
        print("Generi disponibili:")

        for genere_disponibile in generi:
            print("-", genere_disponibile)

# Inserimento del genere
        genere = input("\nInserisci il genere: ")

# Controllo che il genere sia presente nella lista
        while genere not in generi:

            print("Il genere non è presente: Errore")
            genere = input("Inserisci un genere valido: ")

# Inserimento della durata
        durata = int(input("Inserisci la durata del film in minuti: "))

# Inserimento della nazionalità
        nazionalita = input("Inserisci la nazionalità: ")

# Inserimento dei dati nella tabella Film
        cursor.execute("""INSERT INTO Film (nome, regista, genere, durata, nazionalita) VALUES (?, ?, ?, ?, ?)""", (nome, regista, genere, durata, nazionalita))

# Salvataggio delle modifiche nel database
        conn.commit()
        print()
        print("Film aggiunto correttamente!")

# Gestione dell'errore relativo alla durata
    except ValueError:

        print("La durata deve essere un numero intero: Errore")

# Gestione degli errori del database
    except sqlite3.Error as errore:

        conn.rollback()
        print("Errore nel database:", errore)


# Funzione 2 - Rimuovi film

def rimuovi_film():
    pass


# Funzione 3 - Modifica film

def modifica_film():
    pass


# Funzione 4 - Cerca film per nazionalita
def cerca_film():
    pass


# Funzione 5 - Visualizza tutti i film

def visualizza_film():

    cursor.execute("SELECT nome, regista, genere, durata, nazionalita FROM Film")

    film = cursor.fetchall()

    for nome, regista, genere, durata, nazionalita in film:
        print(nome, "-", regista, "-", genere, "-", durata, "minuti -", nazionalita)


# Menu while

while True:

    menu()
    
    print()
    scelta = input("Seleziona una delle opzioni: ")

    if scelta == "1": aggiungi_film()
     
    elif scelta == "2": rimuovi_film()
    
    elif scelta == "3": modifica_film()

    elif scelta == "4": cerca_film()

    elif scelta == "5": visualizza_film()


    elif scelta == "0":
        print("Programma terminato!")
        break

    else:
        print("Opzione non valida. Scegli un numero nel menu")


# Chiusura connessione

conn.close()