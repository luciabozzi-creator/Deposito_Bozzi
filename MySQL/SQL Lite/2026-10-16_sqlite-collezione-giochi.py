"""Es1 - Collezione di giochi.

ESERCIZIO
Nel database collezione.db gestisci una tabella giochi (id, titolo, anno)
con tre funzioni: crea_tabella(), aggiungi_gioco(titolo, anno) ed
elenco_giochi(), che restituisce le righe invece di stamparle. Nel programma
principale aggiungi tre giochi e stampa l'elenco.

Obiettivo didattico: separare le funzioni che lavorano sul database dalla
funzione che visualizza i risultati.
"""

import sqlite3


NOME_DB = "collezione.db"


def connetti():
    # Apro una connessione al database SQLite del progetto.
    conn = sqlite3.connect(NOME_DB)

    # Con sqlite3.Row posso leggere una riga usando il nome della colonna,
    # per esempio gioco["titolo"], invece di usare solo gli indici numerici.
    conn.row_factory = sqlite3.Row
    return conn


def crea_tabella():
    # Apro la connessione solo per il tempo necessario alla creazione.
    conn = connetti()
    # Il contesto conn esegue il commit se l'istruzione termina bene.
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS giochi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titolo TEXT NOT NULL,
                anno INTEGER NOT NULL
            )
            """
        )
    # Chiudo esplicitamente la connessione dopo la creazione.
    conn.close()


def aggiungi_gioco(titolo, anno):
    # Apro una connessione per l'inserimento del nuovo gioco.
    conn = connetti()
    # Uso i placeholder ? per passare i valori separatamente dalla query.
    with conn:
        conn.execute("INSERT INTO giochi (titolo, anno) VALUES (?, ?)", (titolo, anno))
    # La connessione non serve più dopo l'inserimento.
    conn.close()


def elenco_giochi():
    # Apro la connessione per eseguire la SELECT.
    conn = connetti()
    # Restituisco le righe ordinate per titolo; non le stampo qui.
    giochi = conn.execute("SELECT id, titolo, anno FROM giochi ORDER BY titolo").fetchall()
    # Chiudo la connessione dopo aver recuperato i risultati.
    conn.close()
    return giochi


def stampa_giochi(giochi):
    # Gestisco anche il caso in cui la tabella non contenga giochi.
    if not giochi:
        print("Nessun gioco presente.")
        return

    # La funzione di stampa riceve i dati già recuperati dal database.
    for gioco in giochi:
        print(f'{gioco["id"]}: {gioco["titolo"]} ({gioco["anno"]})')


# Creo la tabella prima di inserire i giochi.
crea_tabella()

# Inserisco i tre giochi richiesti dall'esercizio.
# La funzione usa la query SQL INSERT INTO definita sopra.
aggiungi_gioco("GIOCO 1", 1985)
aggiungi_gioco("GIOCO 2", 1984)
aggiungi_gioco("GIOCO 3", 1986)

# Recupero l'elenco e lo passo alla funzione dedicata alla stampa.
stampa_giochi(elenco_giochi())

