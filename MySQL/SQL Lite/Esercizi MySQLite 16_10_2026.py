"""

Esercizio 2
Nel database ordini.db crea le tabelle
- clienti (id, nome, citta)
- ordini (id, cliente_id, importo) con almeno 4 clienti e 8 ordini,
attivando le chiavi esterne.

Usando row_factory,
stampa per ogni cliente
il totale speso (suggerimento: SUM e GROUP BY).

Poi stampa tutti gli ordini
di quel cliente, oppure "Cliente non trovato" se il nome non esiste.

"""

import sqlite3

# Apro la connessione al database ordini.db
conn = sqlite3.connect("ordini.db")

# Imposto il risultato delle SELECT come righe leggibili per nome di colonna
conn.row_factory = sqlite3.Row

# Creo il cursore per eseguire le istruzioni SQL
cur = conn.cursor()

# Attivo il controllo delle chiavi esterne
cur.execute("PRAGMA foreign_keys = ON")

# Elimino le tabelle precedenti per poter rieseguire l'esercizio
cur.execute("DROP TABLE IF EXISTS ordini")
cur.execute("DROP TABLE IF EXISTS clienti")

# Creo la tabella dei clienti
cur.execute("""
CREATE TABLE clienti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    citta TEXT)
""")

# Creo la tabella degli ordini con la chiave esterna verso clienti
cur.execute("""
CREATE TABLE ordini (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    importo REAL,
    FOREIGN KEY (cliente_id) REFERENCES clienti(id))
""")

# Preparo i dati dei clienti
clienti = [
    ("Cliente 1", "Citta 1"),
    ("Cliente 2", "Citta 2"),
    ("Cliente 3", "Citta 3"),
    ("Cliente 4", "Citta 4")]

# Inserisco i clienti con un'unica operazione executemany
cur.executemany("""INSERT INTO clienti (nome, citta) VALUES (?, ?)""", clienti)

# Preparo gli ordini collegandoli agli id dei clienti con i relativi importi
ordini = [(1, 10.50), (1, 22.00), (2, 23.99), (2, 5.90), (2, 87.00), (3, 23.50), (3, 74.00), (4, 5.00)]

# Inserisco gli ordini con un'unica operazione executemany
cur.executemany(""" INSERT INTO ordini (cliente_id, importo) VALUES (?, ?) """, ordini)

# Salvo le tabelle e i dati nel database
conn.commit()

# Calcolo il totale speso da ogni cliente con JOIN, SUM e GROUP BY
cur.execute("""

SELECT
    clienti.nome,
    clienti.citta,
    SUM(ordini.importo) AS totale_speso

FROM clienti

INNER JOIN ordini
    ON clienti.id = ordini.cliente_id

GROUP BY clienti.id, clienti.nome, clienti.citta
ORDER BY totale_speso DESC

""")

# Leggo tutte le righe restituite dalla SELECT
report_clienti = cur.fetchall()

# Stampo il totale speso da ogni cliente
print("Totale speso da ogni cliente:")

for record in report_clienti:
    print(record["nome"], record["totale_speso"])

# Chiudo la connessione al database
conn.close()
