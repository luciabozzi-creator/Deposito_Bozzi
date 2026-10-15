import sqlite3

conn = sqlite3.connect("calcio.db")
cur = conn.cursor()

cur.execute("PRAGMA foreign_keys = ON")

cur.execute("DROP TABLE IF EXISTS giocatori")
cur.execute("DROP TABLE IF EXISTS squadre")

cur.execute(
    """
    CREATE TABLE squadre (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        citta TEXT
    )
    """)

cur.execute(
    """
    CREATE TABLE giocatori (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ruolo TEXT,
        squadra_id INTEGER,
        FOREIGN KEY (squadra_id) REFERENCES squadre(id)
    )
    """)

cur.executemany("INSERT INTO squadre (nome, citta) VALUES (?, ?)", [("Aquile", "Torino"), ("Leoni", "Napoli")])
cur.executemany(
    "INSERT INTO giocatori (nome, ruolo, squadra_id) VALUES (?, ?, ?)",
    [("Marco", "portiere", 1), ("Elia", "attaccante", 1), ("Paolo", "difensore", 2)]
)
conn.commit()

cur.execute("""
    SELECT giocatori.nome, squadre.nome
    FROM giocatori
    JOIN squadre ON giocatori.squadra_id = squadre.id
""")

for giocatore, squadra in cur.fetchall():
    print(f"giocatore {giocatore} gioca per {squadra}")

try:
    cur.execute("INSERT INTO giocatori (nome, ruolo, squadra_id) VALUES(?,?,?)", ("Fantasma", "Attaccante", 99))
    conn.commit()
except sqlite3.IntegrityError as err:
    print("Errore inserimento ForeignKey non esistente: \n", err)

try:
    cur.execute("DELETE FROM squadre WHERE id = ?", (2,))
    conn.commit()
except sqlite3.IntegrityError as err:
    print("Errore eliminazione id collegato a foreignkey: \n", err)

cur.execute("""
    SELECT giocatori.nome, squadre.nome
    FROM giocatori
    JOIN squadre ON giocatori.squadra_id = squadre.id
""")

for giocatore, squadra in cur.fetchall():
    print(f"giocatore {giocatore} gioca per {squadra}")

conn.close()