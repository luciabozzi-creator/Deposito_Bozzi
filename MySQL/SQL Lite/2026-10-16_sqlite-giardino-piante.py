import sqlite3

nome_db = "giardino.db"

def connetti():
    conn = sqlite3.connect(nome_db)
    conn.row_factory = sqlite3.Row  # righe leggibili per nome di colonna
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def crea_tabella():
    conn = connetti()
    with conn:  # commit automatico
        conn.execute("""
            CREATE TABLE IF NOT EXISTS piante (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                luogo TEXT
            )
        """)
    conn.close()

def aggiungi_pianta(nome, luogo):
    conn = connetti()
    with conn:
        conn.execute("INSERT INTO piante (nome, luogo) VALUES (?, ?)", (nome, luogo))
    conn.close()

def elenco_piante():
    conn = connetti()
    righe = conn.execute("SELECT id, nome, luogo FROM piante ORDER BY nome").fetchall()
    conn.close()
    return righe  # la funzione restituisce i dati, non li stampa

def stampa_elenco_piante(el_p):
    for p in el_p:
        print(p["id"], p["nome"], "-", p["luogo"])

# prova rapida (se rilanci il file, il basilico viene aggiunto di nuovo)
crea_tabella()
aggiungi_pianta("Basilico", "balcone")
stampa_elenco_piante(elenco_piante())
aggiungi_pianta("Rosmarino", "balcone")
stampa_elenco_piante(elenco_piante())

