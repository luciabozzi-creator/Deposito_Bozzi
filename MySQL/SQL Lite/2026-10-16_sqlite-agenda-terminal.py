"""Es3 - Agenda da terminale."""

import sqlite3


NOME_DB = "agenda.db"


def connetti():
    conn = sqlite3.connect(NOME_DB)
    conn.row_factory = sqlite3.Row
    return conn


def crea_tabella():
    conn = connetti()
    try:
        with conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS appuntamenti (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    titolo TEXT NOT NULL,
                    luogo TEXT NOT NULL
                )
                """
            )
    finally:
        conn.close()


def aggiungi_appuntamento(data, titolo, luogo):
    dati = (data.strip(), titolo.strip(), luogo.strip())
    if not all(dati):
        print("Data, titolo e luogo sono obbligatori.")
        return False

    conn = connetti()
    try:
        with conn:
            conn.execute(
                """
                INSERT INTO appuntamenti (data, titolo, luogo)
                VALUES (?, ?, ?)
                """,
                dati,
            )
        return True
    except sqlite3.Error as errore:
        print("Errore del database:", errore)
        return False
    finally:
        conn.close()


def elenco_appuntamenti():
    conn = connetti()
    try:
        return conn.execute(
            """
            SELECT id, data, titolo, luogo
            FROM appuntamenti
            ORDER BY data, id
            """
        ).fetchall()
    except sqlite3.Error as errore:
        print("Errore del database:", errore)
        return []
    finally:
        conn.close()


def appuntamenti_del_giorno(data):
    conn = connetti()
    try:
        return conn.execute(
            """
            SELECT id, data, titolo, luogo
            FROM appuntamenti
            WHERE data = ?
            ORDER BY id
            """,
            (data.strip(),),
        ).fetchall()
    except sqlite3.Error as errore:
        print("Errore del database:", errore)
        return []
    finally:
        conn.close()


def modifica_titolo(id_appuntamento, nuovo_titolo):
    nuovo_titolo = nuovo_titolo.strip()
    if not nuovo_titolo:
        print("Il titolo non può essere vuoto.")
        return False

    conn = connetti()
    try:
        with conn:
            cur = conn.execute(
                "UPDATE appuntamenti SET titolo = ? WHERE id = ?",
                (nuovo_titolo, id_appuntamento),
            )
        if cur.rowcount == 0:
            print("Appuntamento non trovato.")
            return False
        return True
    except sqlite3.Error as errore:
        print("Errore del database:", errore)
        return False
    finally:
        conn.close()


def elimina_appuntamento(id_appuntamento):
    conn = connetti()
    try:
        with conn:
            cur = conn.execute(
                "DELETE FROM appuntamenti WHERE id = ?", (id_appuntamento,)
            )
        if cur.rowcount == 0:
            print("Appuntamento non trovato.")
            return False
        return True
    except sqlite3.Error as errore:
        print("Errore del database:", errore)
        return False
    finally:
        conn.close()


def leggi_id():
    try:
        return int(input("ID dell'appuntamento: ").strip())
    except ValueError:
        print("L'ID deve essere un numero intero.")
        return None


def stampa_appuntamenti(appuntamenti):
    if not appuntamenti:
        print("Nessun appuntamento trovato.")
        return

    for appuntamento in appuntamenti:
        print(
            f'{appuntamento["id"]}: {appuntamento["data"]} - '
            f'{appuntamento["titolo"]} ({appuntamento["luogo"]})'
        )


def menu():
    while True:
        print("\n1. Aggiungi appuntamento")
        print("2. Mostra tutti gli appuntamenti")
        print("3. Mostra gli appuntamenti di un giorno")
        print("4. Modifica il titolo")
        print("5. Elimina un appuntamento")
        print("0. Esci")
        scelta = input("Scelta: ").strip()

        if scelta == "1":
            data = input("Data (AAAA-MM-GG): ")
            titolo = input("Titolo: ")
            luogo = input("Luogo: ")
            aggiungi_appuntamento(data, titolo, luogo)
        elif scelta == "2":
            stampa_appuntamenti(elenco_appuntamenti())
        elif scelta == "3":
            data = input("Data (AAAA-MM-GG): ").strip()
            stampa_appuntamenti(appuntamenti_del_giorno(data))
        elif scelta == "4":
            id_appuntamento = leggi_id()
            if id_appuntamento is not None:
                titolo = input("Nuovo titolo: ")
                modifica_titolo(id_appuntamento, titolo)
        elif scelta == "5":
            id_appuntamento = leggi_id()
            if id_appuntamento is not None:
                elimina_appuntamento(id_appuntamento)
        elif scelta == "0":
            print("Programma terminato.")
            break
        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    crea_tabella()
    menu()
