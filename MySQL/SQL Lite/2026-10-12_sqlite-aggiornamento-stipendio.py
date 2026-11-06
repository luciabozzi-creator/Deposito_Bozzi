import sqlite3

def aggiorna_stipendio(id_dip, nuovo_stip):
    connection = sqlite3.connect("azienda.db")
    cur = connection.cursor()

    try:
        if nuovo_stip < 0:
            raise ValueError("lo stipendio non può essere negativo")

        cur.execute("UPDATE dipendenti SET stipendio = ? WHERE id = ?", (nuovo_stip, id_dip))
        if cur.rowcount == 0:
            print("Nessun dipendente con id ", id_dip)
        else:
            connection.commit()
            print("Stipendio aggiornato")
    except ValueError as err:
        print("Dato non valido: ", err)
    except sqlite3.Error as err:
        connection.rollback()
        print("Errore del database: ", err)
    finally:
        connection.close()

connection = sqlite3.connect("azienda.db")
cur = connection.cursor()

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
connection.close()