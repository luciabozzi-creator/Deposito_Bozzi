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

#cursor.execute("DELETE FROM Film")
#conn.commit()

# Salvataggio delle modifiche
conn.commit()

# Aggiunta di film iniziali

film_iniziali = [("Titanic", "James Cameron", "Drammatico", 195, "USA"),
    ("Avatar", "James Cameron", "Fantascienza", 162, "USA"),
    ("La vita è bella", "Roberto Benigni", "Drammatico", 116, "Italia"),
    ("Il gladiatore", "Ridley Scott", "Azione", 155, "USA")]

#cursor.executemany("""INSERT INTO Film (nome, regista, genere, durata, nazionalita) VALUES (?, ?, ?, ?, ?)""", film_iniziali)

conn.commit()

# Lista dei generi disponibili

generi = ["Azione","Commedia","Drammatico","Horror","Fantascienza"]


# Menù

def menu():

    print("\n--- CATALOGO FILM ---")
    print("1. Aggiungi un film")
    print("2. Rimuovi un film")
    print("3. Modifica un film:")
    print("   3.1 Modifica nome")
    print("   3.2 Modifica regista")
    print("   3.3 Modifica genere")
    print("   3.4 Modifica durata")
    print("   3.5 Modifica nazionalità")
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
    
# Visualizzazione di tutti i film
    print("\n--- FILM PRIMA DELLA MODIFICA ---")
    visualizza_film()

# Elimina il film in base al nome esatto
    print()
    nome_film_delete = input("Inserisci il nome del film da eliminare: ")

    cursor.execute("DELETE FROM Film WHERE nome = ?", (nome_film_delete,))

    conn.commit()

    print("Operazione di eliminazione completata!")

# Visualizzazione di tutti i film
    print("\n--- FILM DOPO LA MODIFICA ---")
    visualizza_film()

# Funzione 3 - Modifica film che si sviluppa in sotto-menu per ciascuna variabile

# Funzione 3.1 - Modifica nome del film

def modifica_nome():

    print("\n--- FILM PRIMA DELLA MODIFICA ---")
    visualizza_film()

# Inserimento del nome del film da modificare
    print()
    nome_film = input("Inserisci il nome del film da modificare: ")

# Inserimento del nuovo nome
    print()
    nuovo_nome = input("Inserisci il nuovo nome del film: ")

# Modifica del nome nel database
    cursor.execute("UPDATE Film SET nome = ? WHERE nome = ?", (nuovo_nome, nome_film))

# Salvataggio delle modifiche
    conn.commit()
    print("Nome del film modificato correttamente!")
        
    print()
    print("\n--- FILM DOPO LA MODIFICA ---")
    visualizza_film()
    
# Funzione 3.2 - Modifica regista

def modifica_regista():

    print("\n--- FILM PRIMA DELLA MODIFICA ---")
    visualizza_film()

# Inserimento del nome del film da modificare
    print()
    nome_film = input("Inserisci il nome del film da modificare: ")

# Inserimento del nuovo regista
    nuovo_regista = input("Inserisci il nuovo regista: ")

# Modifica del regista nel database
    cursor.execute("UPDATE Film SET regista = ? WHERE nome = ?", (nuovo_regista, nome_film))

# Salvataggio delle modifiche
    conn.commit()
    print("Regista modificato correttamente!")
    print()
    
    
    print("\n--- FILM DOPO LA MODIFICA ---")
    visualizza_film()
    
# Funzione 3.3 - Modifica genere

def modifica_genere():
    
    print("\n--- FILM PRIMA DELLA MODIFICA ---")
    visualizza_film()

# Inserimento del nome del film da modificare
    print()
    nome_film = input("Inserisci il nome del film da modificare: ")

# Visualizzazione dei generi disponibili
    print()
    print("Generi disponibili:")

    for genere in generi:
        print("-", genere)

# Inserimento del nuovo genere
    print()
    nuovo_genere = input("Inserisci il nuovo genere: ")

# Controllo del genere
    while nuovo_genere not in generi:
        print("Il genere non è presente: Errore")
        nuovo_genere = input("Inserisci un genere valido: ")

# Modifica del genere nel database
    cursor.execute("UPDATE Film SET genere = ? WHERE nome = ?", (nuovo_genere, nome_film))

# Salvataggio delle modifiche
    conn.commit()
    print("Genere modificato correttamente!")
    
    print("\n--- FILM DOPO LA MODIFICA ---")
    visualizza_film() 

# Funzione 3.4 - Modifica durata

def modifica_durata():
    
    print("\n--- FILM PRIMA DELLA MODIFICA ---")
    visualizza_film()

    try:
# Inserimento del nome del film da modificare
        nome_film = input("Inserisci il nome del film da modificare: ")

# Inserimento della nuova durata
        nuova_durata = int(input("Inserisci la nuova durata in minuti: "))

# Modifica della durata nel database
        cursor.execute("UPDATE Film SET durata = ? WHERE nome = ?", (nuova_durata, nome_film))

# Salvataggio delle modifiche
        conn.commit()
        print("Durata modificata correttamente!")

    except ValueError:
        print("La durata deve essere un numero intero: Errore")
        
    print("\n--- FILM DOPO LA MODIFICA ---")
    visualizza_film()
        
# Funzione 3.5 - Modifica nazionalità

def modifica_nazionalita():
    
    print("\n--- FILM PRIMA DELLA MODIFICA ---")
    visualizza_film()

# Inserimento del nome del film da modificare
    nome_film = input("Inserisci il nome del film da modificare: ")

# Inserimento della nuova nazionalità
    nuova_nazionalita = input("Inserisci la nuova nazionalità: ")

# Modifica della nazionalità nel database
    cursor.execute("UPDATE Film SET nazionalita = ? WHERE nome = ?", (nuova_nazionalita, nome_film))

# Salvataggio delle modifiche
    conn.commit()
    print("Nazionalità modificata correttamente!")
    
    print("\n--- FILM DOPO LA MODIFICA ---")
    visualizza_film()
    

# Funzione 4 - Cerca film per nazionalità

def cerca_film():
    
# Ricerca delle nazionalità presenti nel database creando una tupla
    cursor.execute("SELECT DISTINCT nazionalita FROM Film")

    nazionalita_disponibili = cursor.fetchall()

# Visualizzazione delle nazionalità disponibili
    print()
    print("Nazionalità disponibili:")

    for nazionalita in nazionalita_disponibili:
        print("-", nazionalita[0])

# Inserimento della nazionalità da cercare
    print()
    nazionalita_input = input("Inserisci una nazionalità: ")

# Ricerca dei film per nazionalità
    cursor.execute("SELECT nome, regista, genere, durata, nazionalita FROM Film WHERE nazionalita = ?", (nazionalita_input,))

    ricerca_film_nazionalita = cursor.fetchall()

# Visualizzazione dei film trovati
    for nome, regista, genere, durata, nazionalita in ricerca_film_nazionalita:
        print()
        print(nome, "-", regista, "-", genere, "-", durata, "minuti -", nazionalita)
        
        
# Funzione 5 - Visualizza tutti i film

def visualizza_film():

    cursor.execute("SELECT nome, regista, genere, durata, nazionalita FROM Film")

    film = cursor.fetchall()

    for nome, regista, genere, durata, nazionalita in film:
        print()
        print(nome, "-", regista, "-", genere, "-", durata, "minuti -", nazionalita)


# Menu while

while True:

    menu()
    
    print()
    scelta = input("Seleziona una delle opzioni: ")

    if scelta == "1": aggiungi_film()
     
    elif scelta == "2": rimuovi_film()
    
    elif scelta == "3.1": modifica_nome()
    
    elif scelta == "3.2": modifica_regista()
    
    elif scelta == "3.3": modifica_genere()
    
    elif scelta == "3.4": modifica_durata()
    
    elif scelta == "3.5": modifica_nazionalita()  

    elif scelta == "4": cerca_film()

    elif scelta == "5": visualizza_film()


    elif scelta == "0":
        print("Programma terminato!")
        break

    else:
        print("Opzione non valida. Scegli un numero nel menu")


# Chiusura connessione

conn.close()