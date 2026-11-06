import sqlite3

connection = sqlite3.connect("azienda.db")
cur = connection.cursor()

def sposta_stipendio(id_dante, id_ricevente, importo):
    # connection = sqlite3.connect("azienda.db")
    # cur = connection.cursor()

    try:
        with connection:
            cur.execute("UPDATE dipendenti SET stipendio = stipendio - ? WHERE id = ?", (importo, id_dante))
            cur.execute("UPDATE dipendenti SET stipendio = stipendio + ? WHERE id = ?", (importo, id_ricevente))
            if cur.rowcount == 0:
                raise ValueError("Seconso dipendente non trovato")
        print("Spostamento completato")
    except ValueError as err:
        print("Operazione annullata: ", err)
    except sqlite3.Error as err:
        print("Errore del database: ", err)

def stipendio(id_dip):
    cur.execute("SELECT stipendio FROM dipendenti WHERE id = ?", (id_dip,))
    return cur.fetchone()[0]
    
cur.execute("DROP TABLE IF EXISTS dipendenti")
cur.execute(
    """
    CREATE TABLE dipendenti(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    reparto TEXT,
    stipendio INTEGER)
    """)

list_dipendenti = [("Anna", "Vendite", 1500), ("Luca", "Vendite", 1400), ("Sara", "Magazzino", 1600)]
cur.executemany("INSERT INTO dipendenti (nome, reparto, stipendio) VALUES (?,?,?)", list_dipendenti)

connection.commit()

print(f"Prima: Anna, {stipendio(1)} - Sara {stipendio(3)}" )
sposta_stipendio(1, 4, 100)
print(f"Dopo: Anna, {stipendio(1)} - Sara {stipendio(3)}" )

connection.close()