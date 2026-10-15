import sqlite3

conn = sqlite3.connect("calcio.db")
conn.row_factory = sqlite3.Row

cur = conn.cursor()

cur.execute(
    """
    SELECT g.nome AS giocatore, g.ruolo, s.nome AS squadra
    FROM giocatori g
    JOIN squadre s ON g.squadra_id = id
    WHERE s.citta = ?
    """, ("Torino",))

for riga in cur.fetchall():
    print(f"{riga["giocatore"] - {riga["ruolo"]} - {riga["squadra"]}}")

conn.close()