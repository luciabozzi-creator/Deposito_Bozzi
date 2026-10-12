"""
Esercizio: la playlist musicale

- Crea un database playlist.db con una tabella canzoni con le colonne id (autoincrementale), titolo e artista.
- Inserisci 4 canzoni in un colpo solo, partendo da una lista di tuple.
- Cancella una canzone a tua scelta indicandone il titolo, usando il segnaposto ?.
- Stampa le canzoni rimaste nel formato Titolo - Artista, una per riga.

"""

# 1. Importo la libreria sqlite3
import sqlite3

# 2. Creo e accedo al database playlist.db sulla Scrivania
conn = sqlite3.connect("/PATH/playlist.db")

# 3. Creo il cursore
cur = conn.cursor()

# 4. Creo la tabella canzoni
cur.execute("""
    CREATE TABLE IF NOT EXISTS canzoni (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo VARCHAR(30) NOT NULL,
    artista VARCHAR(30) NOT NULL)
""")

# 5. Salvo le modifiche
conn.commit()

# 6. Creo una lista di tuple con 4 canzoni
Lista_canzoni = [
     ("Canzone 1", "Artista 1"),
     ("Canzone 2", "Artista 2"),
     ("Canzone 3", "Artista 3"),
     ("Canzone 4", "Artista 4")]

# 7. Inserisco le 4 canzoni nella tabella
cur.executemany("INSERT INTO canzoni (titolo, artista) VALUES (?, ?)", Lista_canzoni)

# 8. Salvo le modifiche
conn.commit()

# 9. Visualizzo le canzoni inserite
print()
print("--- CANZONI INSERITE ---")
print()

cur.execute("SELECT * FROM canzoni")
Tabella_canzoni = cur.fetchall()

for id, titolo, artista in Tabella_canzoni:
    print(id, titolo, "-", artista)


# 10. Cancello una canzone indicando il titolo
print()
Titolo_canzone_delete = input("Digita il titolo della canzone che vuoi eliminare? ")

cur.execute("DELETE FROM canzoni WHERE titolo = ?",(Titolo_canzone_delete,))

# 11. Salvo le modifiche
conn.commit()

# 12. Visualizzo le canzoni rimaste
print()
print("--- CANZONI RIMASTE ---")
print()

cur.execute("SELECT * FROM canzoni")
Tabella_canzoni = cur.fetchall()

for id, titolo, artista in Tabella_canzoni:
    print(id, titolo, "-", artista)


# 13. Stampo la playlist nel formato richiesto dalla consegna
print()
print("--- PLAYLIST MUSICALE ---")
print()

cur.execute("SELECT titolo, artista FROM canzoni")
Tabella_canzoni = cur.fetchall()

for titolo, artista in Tabella_canzoni:
    print(titolo, "-", artista)


# 14. Chiudo la connessione
conn.close()