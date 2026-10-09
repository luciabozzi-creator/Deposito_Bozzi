"""

Obiettivo: crea un database rubrica.db con una tabella contatti (id, nome,
telefono). Inserisci 3 contatti a tua scelta, salva le modifiche e stampa a video
tutti i contatti presenti nella tabella.

"""

# 1. creo e accedo al database rubrica.db
import sqlite3
conn = sqlite3.connect("rubrica.db")

# 2. creo il cursore
cur = conn.cursor()

# Creo la tabella contatti
# cur.execute(

# """
# CREATE TABLE IF NOT EXISTS contatti (
#     id 			INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome 		VARCHAR(30) NOT NULL,
#    telefono 	VARCHAR(20))
# """)

# Salvo le modifiche
# conn.commit()

# 3. creo una lista di tuple con i tre contatti
# contatti = [
#     ("Mario Rossi", "3331234567"),
#     ("Anna Bianchi", "3479876543"),
#     ("Luca Verdi", "3394567890")]

# 4. Inserisco i contatti nella tabella
# cur.executemany("INSERT INTO contatti (nome, telefono) VALUES (?, ?)",contatti)

# conn.commit()

# 5. Seleziono tutti i contatti
cur.execute("SELECT * FROM contatti")

# 6. Recupero i risultati in una lista di tuple
risultati = cur.fetchall()

# 7. Stampo tutti i contatti e spacchetto le tuple
for id, nome, telefono in risultati:
    print(id, nome, telefono)

# 8. Chiudo la connessione
conn.close()