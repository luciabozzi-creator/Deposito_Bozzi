"""
Esercizio: Gestione Inventario Negozio.

Creare un programma che gestisce i prodotti di un negozio
(nome, prezzo, quantità).

1. Aggiungere un prodotto
2. Togliere un prodotto
3. Modificare il prezzo
4. Modificare la quantità
5. Calcolare il totale dell'inventario

"""

# 1. creo e accedo al database negozio.db
import sqlite3
# conn = sqlite3.connect("/PATH/negozio.db")

# 2. creo il cursore
cur = conn.cursor()

# Creo la tabella prodotti
cur.execute(

"""
    CREATE TABLE IF NOT EXISTS prodotti (
    id 			INTEGER PRIMARY KEY AUTOINCREMENT,
    nome 		VARCHAR(30) NOT NULL,
    prezzo	 	REAL(20),
    quantita	INTEGER)
""")

### Cancello tabella ###cur.execute(""" DROP TABLE prodotti """)

# Salvo le modifiche
# conn.commit()

# 3. creo una lista di tuple con i tre contatti

Lista_prodotti = [
        ("Pane", "2.50", "10"),
        ("Latte", "1.80","15"),
        ("Pasta", "1.20","20")]

# 4. Inserisco i prodotti nella tabella
cur.executemany("INSERT INTO prodotti (nome, prezzo, quantita) VALUES (?, ?, ?)",Lista_prodotti)
# conn.commit()
# print("Prodotti creati con successo!")


# 5. Stampa report
cur.execute("SELECT * FROM prodotti")
Tabella_prodotti = cur.fetchall()
for id, nome, prezzo, quantita in Tabella_prodotti:
    print(id, nome, prezzo, quantita)
    
# 6. Togliere un prodotto
ID_prodotto_delete = input("Quale ID prodotto vuoi eliminare? ")
cur.execute("DELETE FROM prodotti WHERE id = ?",(ID_prodotto_delete,))
conn.commit()
print("Il prodotto è eliminato con successo!")

# 7. Seleziono tutti i contatti
cur.execute("SELECT * FROM prodotti")

# 8. Recupero i risultati in una lista di tuple
Tabella_prodotti = cur.fetchall()

# 9. Stampo tutti i prodotti e spacchetto le tuple
for id, nome, prezzo, quantita in Tabella_prodotti:
        print(id, nome, prezzo, quantita)
    
        
# 10. Modifico il prezzo
ID_prodotto_mod_prezzo = input("Di quale ID vuoi modificare il prezzo? ")
Prezzo_nuovo = input("Inserisci il nuovo prezzo: ")

cur.execute("UPDATE prodotti SET prezzo = ? WHERE id = ?", (Prezzo_nuovo, ID_prodotto_mod_prezzo))

conn.commit()
print("Il prezzo è aggiornato con successo!")

# 11. Stampa report
cur.execute("SELECT * FROM prodotti WHERE id = ?", (ID_prodotto_mod_prezzo,))

Tabella_prodotti = cur.fetchall()
for id, nome, prezzo, quantita in Tabella_prodotti:
    print(id, nome, prezzo, quantita)
    
# 12. Modifico la quantità di un prodotto

ID_prodotto_mod_quantita = input("Quale ID vuoi modificare la quantita? ")
Quantita_nuova = input("Inserisci la nuova quantità: ")

cur.execute("UPDATE prodotti SET quantita = ? WHERE id = ?", (Quantita_nuova, ID_prodotto_mod_quantita))

conn.commit()

print("La quantità è stata aggiornata con successo!")

# 13. Visualizzo i prodotti aggiornati
cur.execute("SELECT * FROM prodotti WHERE id = ?", (ID_prodotto_mod_quantita,))
Tabella_prodotti = cur.fetchall()
for id, nome, prezzo, quantita in Tabella_prodotti:
    print(id, nome, prezzo, quantita)
    
# 14. Calcolo il totale dell'inventario

cur.execute("SELECT nome, prezzo, quantita FROM prodotti")
righe = cur.fetchall()

totale = 0.0

print("--- INVENTARIO ATTUALE ---")

for nome, prezzo, quantita in righe:
    subtotale = prezzo * quantita
    totale += subtotale
    print(f"{nome}: {quantita} pz x {prezzo:.2f}€ = {subtotale:.2f}€")

print(f"TOTALE COMPLESSIVO: {totale:.2f}€")

# Elimino tutti i prodotti solo se confermato

Risposta = input("Vuoi eliminare tutti i prodotti? (si/no): ")

if Risposta == "si":
    cur.execute("DELETE FROM prodotti")
    cur.execute("DELETE FROM sqlite_sequence WHERE name = 'prodotti'")
    conn.commit()
    
# 15. Chiudo la connessione
conn.close()

