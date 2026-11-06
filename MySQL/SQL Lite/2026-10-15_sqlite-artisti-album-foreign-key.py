"""
Esercizio: nel database musica.db crea le tabelle

- artisti (id, nome) e album (id, titolo, anno, artista_id collegato ad artisti).
- Inserisci 2 artisti e 4 album,
- poi stampa per ogni album una riga nel formato "titolo (anno) - artista", usando un JOIN.

Usa “PRAGMA foreign_key = ON” e
effettua un INSERT INTO con foreignkey non esistente gestendo l’errore con try-except. 

Gestite anche un caso di DELETE di un artista collegato ad un album,
sempre gestendo con try-except.

"""

import sqlite3

# Connessione al database
conn = sqlite3.connect("musica.db")
cur = conn.cursor()

# Attivazione delle chiavi esterne
cur.execute("PRAGMA foreign_keys = ON")

# Creo la tabella artisti
cur.execute("""
    CREATE TABLE IF NOT EXISTS artisti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL)
""")

# Creo la tabella album
cur.execute("""
    CREATE TABLE IF NOT EXISTS album (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titolo TEXT NOT NULL,
        anno INTEGER,
        artista_id INTEGER,
        FOREIGN KEY (artista_id) REFERENCES artisti(id))
""")

# Inserisco prima gli artisti
cur.execute("INSERT INTO artisti (nome) VALUES (?)", ("Artista 1",))
cur.execute("INSERT INTO artisti (nome) VALUES (?)", ("Artista 2",))

# Inserisco poi gli album perchè hanno la foreign key
cur.execute("INSERT INTO album (titolo, anno, artista_id) VALUES (?, ?, ?)", ("Album 1", 2026, 1))

cur.execute("INSERT INTO album (titolo, anno, artista_id) VALUES (?, ?, ?)", ("Album 2", 2025, 1))

cur.execute("INSERT INTO album (titolo, anno, artista_id) VALUES (?, ?, ?)", ("Album 3", 2024, 2))

cur.execute("INSERT INTO album (titolo, anno, artista_id) VALUES (?, ?, ?)", ("Album 4", 2023, 2))

conn.commit()

# JOIN tra album e artisti
cur.execute("""
    SELECT album.titolo, album.anno, artisti.nome
    FROM album
    JOIN artisti ON album.artista_id = artisti.id
""")

for album in cur.fetchall():
    print(album)

# Provo a inserire un album con artista inesistente numero 3
try:
    cur.execute("INSERT INTO album (titolo, anno, artista_id) VALUES (?, ?, ?)", ("Album senza Artista", 2026, 3))
    conn.commit()

except sqlite3.IntegrityError as err:
    print()
    print("Errore aggiunta album senza artista:", err)
    conn.rollback()

# Provo a eliminare un artista che ha degli album
try:
    cur.execute("DELETE FROM artisti WHERE id = ?", (1,))
    conn.commit()

except sqlite3.IntegrityError as err:
    print()
    print("Errore cancella Artista con Album:", err)
    conn.rollback()

# Chiusura connessione
conn.close()
