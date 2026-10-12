import sqlite3

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

with connection:
    cur.execute("UPDATE dipendenti SET stipendio = ? WHERE nome = ?", (1600, "Anna"))
    print("Righe modificate (UPDATE): ", cur.rowcount)

    cur.execute("DELETE FROM dipendenti WHERE nome = ? OR nome = ?", ("Pippo","Fabio"))
    print("Righe modificate (DELETE): ", cur.rowcount)


cur.execute("SELECT * FROM dipendenti")
ris = cur.fetchall()

for id, nome, reparto, stipendio in ris:
    print(f"{id} - {nome} - {reparto} - {stipendio}")

connection.close()