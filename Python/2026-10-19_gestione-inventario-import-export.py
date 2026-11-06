"""
Esercizio: Gestione Inventario Negozio.

Creare un programma che gestisce i prodotti di un negozio
nome, prezzo e quantità.

In questa versione vengono gestiti gli errori tecnici
durante l'importazione e l'esportazione dei dati.
"""

# la funzione mostra all'utente le opzioni che può selezionare
def menu():
    print("\n--- GESTIONE INVENTARIO ---")
    print("1. Aggiungi un prodotto")
    print("2. Elimina un prodotto")
    print("3. Modifica il prezzo di un prodotto")
    print("4. Modifica la quantità di un prodotto")
    print("5. Calcola il totale dell'inventario")
    print("6. Mostra tutto l'inventario")
    print("7. Importa l'inventario da file")
    print("8. Esporta l'inventario su file")
    print("0. Esci")


def aggiungi_prodotto():
    descrizione = input("Inserisci il nome del prodotto: ")
    if descrizione in inventario:
        print("Prodotto già presente")
    else:
        prezzo = float(input("Inserisci il prezzo del prodotto: "))
        quantita = int(input("Inserisci la quantità di prodotto: "))
        inventario[descrizione] = {"prezzo": prezzo, "quantità": quantita}


def elimina_prodotto():
    descrizione = input("Inserisci il nome del prodotto: ")
    if descrizione in inventario:
        del inventario[descrizione]
    else:
        print("Prodotto non presente")


def modifica_prezzo():
    descrizione = input("Inserisci il nome del prodotto: ")
    if descrizione in inventario:
        nuovo_prezzo = float(input("Inserisci il nuovo prezzo del prodotto: "))
        inventario[descrizione]["prezzo"] = nuovo_prezzo
    else:
        print("Prodotto non presente")


def modifica_prodotto():
    descrizione = input("Inserisci il nome del prodotto: ")
    if descrizione in inventario:
        nuova_quantita = int(input("Inserisci la nuova quantità del prodotto: "))
        inventario[descrizione]["quantità"] = nuova_quantita
    else:
        print("Prodotto non presente")


def calcola_inventario():
    totale = 0.0
    for descrizione, prodotto in inventario.items():
        totale_prodotto = prodotto["prezzo"] * prodotto["quantità"]
        print(f"Totale prodotto {descrizione}: {totale_prodotto}")
        totale += totale_prodotto
    print(f"\nValore totale inventario: {totale}")


def mostra_inventario():
    print("\n--- INVENTARIO ---")
    for descrizione, prodotto in inventario.items():
        print(
            f"Prodotto {descrizione} - "
            f"Prezzo: {prodotto['prezzo']} - "
            f"Quantità: {prodotto['quantità']}"
        )


# la funzione consente di leggere prodotti importati da un file di testo
def importa_inventario():
    # try prova a eseguire tutte le istruzioni di importazione.
    # Se si verifica un errore tecnico, il programma passa a except.
    try:
        # Apro il file in sola lettura e recupero il testo.
        nome_file = open("mio_file.txt", "r")
        contenuto = nome_file.read()
        nome_file.close()

        # Verifico che il testo finisca con un a capo.
        if contenuto and contenuto[-1] != "\n":
            contenuto += "\n"

        # Definisco un indice per scorrere i caratteri della stringa.
        indice_corrente = 0

        # Elimino la riga di intestazione usando find.
        prima_riga = contenuto.find("\n", indice_corrente)
        indice_corrente = prima_riga + 1
        lunghezza_testo = len(contenuto)

        # Scansiono il testo riga per riga usando find.
        while indice_corrente < lunghezza_testo:
            fine_riga = contenuto.find("\n", indice_corrente)
            riga = contenuto[indice_corrente:fine_riga].strip()
            indice_corrente = fine_riga + 1

            if riga:
                primo_spazio = riga.find(" ")
                ultimo_spazio = riga.rfind(" ")

                if primo_spazio != -1 and ultimo_spazio != -1 and primo_spazio != ultimo_spazio:
                    prodotto = riga[0:primo_spazio].strip()
                    prezzo = float(riga[primo_spazio:ultimo_spazio].strip())
                    quantita = int(riga[ultimo_spazio:].strip())

                    if prodotto and prezzo and quantita:
                        inventario[prodotto] = {
                            "prezzo": prezzo,
                            "quantità": quantita
                        }

        print("Inventario importato correttamente.")

    # except gestisce il caso in cui il file non esista.
    except FileNotFoundError:
        print("Errore: il file mio_file.txt non è stato trovato.")


# la funzione consente di scrivere i prodotti dell'inventario su un file di testo
def esporta_inventario():
    # try prova a eseguire le istruzioni di esportazione.
    # Se il file non esiste, il programma passa a except.
    try:
        # Leggo il contenuto attuale del file.
        file = open("mio_file.txt", "r")
        contenuto = file.read()
        file.close()

        # Assicuro che il testo termini correttamente con un a capo.
        if contenuto and contenuto[-1] != "\n":
            contenuto += "\n"

        nuovo_testo = ""
        prodotto_trovato = False
        duplicato_esatto = False

        indice_corrente = 0
        prima_riga = contenuto.find("\n", indice_corrente)
        indice_corrente = prima_riga + 1
        lunghezza_testo = len(contenuto)

        # Controllo i dati dei prodotti dell'inventario.
        for prodotto in inventario:
            prodotto_input = prodotto
            prezzo_input = inventario[prodotto]["prezzo"]
            quantita_input = inventario[prodotto]["quantità"]

            # Analizzo il file riga per riga usando find.
            while indice_corrente < lunghezza_testo:
                fine_riga = contenuto.find("\n", indice_corrente)
                riga = contenuto[indice_corrente:fine_riga].strip()
                indice_corrente = fine_riga + 1

                if riga:
                    primo_spazio = riga.find(" ")
                    ultimo_spazio = riga.rfind(" ")

                    if primo_spazio != -1 and ultimo_spazio != -1 and primo_spazio != ultimo_spazio:
                        prodotto_corrente = riga[0:primo_spazio].strip()
                        prezzo_corrente = float(riga[primo_spazio:ultimo_spazio].strip())
                        quantita_corrente = int(riga[ultimo_spazio:].strip())

                        if prodotto_corrente == prodotto_input:
                            prodotto_trovato = True

                            if prezzo_corrente == prezzo_input and quantita_corrente == quantita_input:
                                duplicato_esatto = True
                                nuovo_testo += riga + "\n"
                            else:
                                nuovo_testo += (
                                    prodotto_input + " "
                                    + str(prezzo_input) + " "
                                    + str(quantita_input) + "\n"
                                )
                        else:
                            nuovo_testo += riga + "\n"
                    else:
                        nuovo_testo += riga + "\n"

            if duplicato_esatto:
                print("Operazione annullata: dati già presenti.")
                continue

            if not prodotto_trovato:
                nuovo_testo += (
                    prodotto_input + " "
                    + str(prezzo_input) + " "
                    + str(quantita_input) + "\n"
                )
                print("Nuovo articolo salvato con successo nel file.")
            else:
                print("Articolo esistente aggiornato con successo nel file.")

            # Riscrivo il file aggiornato.
            file = open("mio_file.txt", "w")
            file.write(nuovo_testo)
            file.close()
            return

    # Gestisce soltanto il caso in cui il file non venga trovato.
    except FileNotFoundError:
        print("Errore: il file mio_file.txt non è stato trovato.")


inventario = {}


# Codice principale del programma.
while True:
    menu()
    scelta = input("\nSeleziona una delle opzioni: ").strip()

    if scelta == "1":
        aggiungi_prodotto()
    elif scelta == "2":
        elimina_prodotto()
    elif scelta == "3":
        modifica_prezzo()
    elif scelta == "4":
        modifica_prodotto()
    elif scelta == "5":
        calcola_inventario()
    elif scelta == "6":
        mostra_inventario()
    elif scelta == "7":
        importa_inventario()
    elif scelta == "8":
        esporta_inventario()
    elif scelta == "0":
        print("Programma terminato!")
        break
    else:
        print("Opzione non valida. Scegli un numero nel menu.")
