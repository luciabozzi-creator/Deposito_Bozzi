"""Es2 - Ricettario con menu e ricerca per ingrediente.

ESERCIZIO
Nel database ricettario.db crea una tabella ricette (id, nome, ingredienti)
e un menu con quattro voci: aggiungi ricetta, mostra tutte le ricette, cerca
per ingrediente usando LIKE ed esci.

Il programma deve rifiutare un nome o un elenco di ingredienti vuoto,
chiedendo nuovamente i dati.

Obiettivo didattico: separare le funzioni del database, la stampa e il menu.
"""

import sqlite3


NOME_DB = "ricettario.db"


def connetti():
    # Apro una connessione al database SQLite del ricettario.
    conn = sqlite3.connect(NOME_DB)

    # Permetto di leggere le righe usando i nomi delle colonne.
    conn.row_factory = sqlite3.Row
    return conn


def crea_tabella():
    # Apro la connessione per creare la tabella se non esiste.
    conn = connetti()

    # Il contesto conn salva la modifica con il commit automatico.
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS ricette (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                ingredienti TEXT NOT NULL
            )
            """
        )

    # Chiudo esplicitamente la connessione.
    conn.close()


def aggiungi_ricetta(nome, ingredienti):
    # Elimino gli spazi all'inizio e alla fine dei dati inseriti.
    nome = nome.strip()
    ingredienti = ingredienti.strip()

    # Rifiuto i dati vuoti prima di eseguire la query INSERT INTO.
    if not nome or not ingredienti:
        print("Nome e ingredienti non possono essere vuoti.")
        return False

    # Apro la connessione per inserire la nuova ricetta.
    conn = connetti()

    # Passo i valori con i placeholder ? invece di concatenarli nella query.
    with conn:
        conn.execute("INSERT INTO ricette (nome, ingredienti) VALUES (?, ?)", (nome, ingredienti))

    # Chiudo la connessione dopo l'inserimento.
    conn.close()
    return True


def elenco_ricette():
    # Apro la connessione per leggere tutte le ricette.
    conn = connetti()

    # Restituisco le righe ordinate per nome senza stamparle qui.
    ricette = conn.execute("SELECT id, nome, ingredienti FROM ricette ORDER BY nome").fetchall()

    # Chiudo la connessione dopo aver recuperato i dati.
    conn.close()
    return ricette


def cerca_per_ingrediente(testo):
    # Elimino gli spazi dall'ingrediente cercato.
    testo = testo.strip()

    # Anche la ricerca richiede un valore non vuoto.
    if not testo:
        print("L'ingrediente non può essere vuoto.")
        return []

    # Apro la connessione per eseguire la ricerca.
    conn = connetti()

    # Uso LIKE e inserisco i caratteri jolly % nel parametro della query.
    ricette = conn.execute("SELECT id, nome, ingredienti FROM ricette WHERE ingredienti LIKE ? ORDER BY nome", (f"%{testo}%",)).fetchall()

    # Chiudo la connessione dopo la SELECT.
    conn.close()
    return ricette


def stampa_ricette(ricette):
    # Gestisco il caso in cui la ricerca non restituisca risultati.
    if not ricette:
        print("Nessuna ricetta trovata.")
        return

    # La funzione di stampa riceve i dati già letti dal database.
    for ricetta in ricette:
        print(f'{ricetta["id"]}: {ricetta["nome"]} — {ricetta["ingredienti"]}')


def menu():
    # Il menu resta attivo fino alla scelta 0.
    while True:
        print("\n1. Aggiungi ricetta")
        print("2. Mostra tutte le ricette")
        print("3. Cerca per ingrediente")
        print("0. Esci")
        scelta = input("Scelta: ").strip()

        # Scelta 1: raccolgo i dati e provo a inserire una ricetta.
        if scelta == "1":
            nome = input("Nome della ricetta: ")
            ingredienti = input("Ingredienti: ")
            aggiungi_ricetta(nome, ingredienti)

        # Scelta 2: recupero e stampo tutte le ricette.
        elif scelta == "2":
            stampa_ricette(elenco_ricette())

        # Scelta 3: cerco le ricette che contengono l'ingrediente indicato.
        elif scelta == "3":
            ingrediente = input("Ingrediente da cercare: ")
            stampa_ricette(cerca_per_ingrediente(ingrediente))

        # Scelta 0: esco dal ciclo while True.
        elif scelta == "0":
            print("Programma terminato.")
            break

        # Qualsiasi altro valore non corrisponde alle opzioni del menu.
        else:
            print("Scelta non valida.")


# Creo la tabella prima di avviare il menu.
crea_tabella()

# Avvio il menu interattivo.
menu()
