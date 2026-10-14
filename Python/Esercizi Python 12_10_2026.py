"""
Esercizio: Gestione Inventario Negozio.

Creare un programma che gestisce i prodotti di un negozio
(nome, prezzo, quantità).

1. Aggiungere un prodotto
2. Togliere un prodotto
3. Modificare il prezzo
4. Modificare la quantità
5. Calcolare il totale dell'inventario (quantità * prezzo per ogni prodotto)
6. Mostrare tutto l'inventario

"""

# La funzione mostra all'utente le opzioni che può selezionare

def menu():
    print("\n--- GESTIONE INVENTARIO ---")
    print("1. Aggiungi un prodotto")
    print("2. Elimina un prodotto")
    print("3. Modifica il prezzo di un prodotto")
    print("4. Modifica la quantità di un prodotto")
    print("5. Calcola il totale dell'inventario")
    print("6. Mostra tutto l'inventario")
    print("7. Importa inventario da txt")
    print("0. Esci")


# La funzione consente di aggiungere un prodotto all'inventario

def aggiungi_prodotto():

    codice = input("AGGIUNGI PRODOTTO - Inserisci il codice prodotto: ")

    if codice in inventario:
        print("Prodotto già presente")
    else:
        nome = input("Inserisci il nome del prodotto: ")
        prezzo = float(input("Inserisci il prezzo: "))
        quantita = int(input("Inserisci la quantità: "))

        inventario[codice] = {
            "nome": nome,
            "prezzo": prezzo,
            "quantita": quantita}

        print("Prodotto aggiunto correttamente")


# La funzione consente di eliminare un prodotto dall'inventario

def elimina_prodotto():

    codice = input("ELIMINA PRODOTTO - Inserisci il codice prodotto: ")

    if codice in inventario:
        del inventario[codice]
        print("Prodotto eliminato correttamente")
    else:
        print("Prodotto non presente")


# La funzione consente di modificare il prezzo di un prodotto nell'inventario

def modifica_prezzo():

    codice = input("MODIFICA PREZZO - Inserisci il codice prodotto: ")

    if codice in inventario:
        nuovo_prezzo = float(input("Inserisci il nuovo prezzo: "))
        inventario[codice]["prezzo"] = nuovo_prezzo
        print("Prezzo modificato correttamente")
    else:
        print("Prodotto non presente")


# La funzione consente di modificare la quantità di un prodotto nell'inventario

def modifica_prodotto():

    codice = input("MODIFICA QUANTITÀ - Inserisci il codice prodotto: ")
    if codice in inventario:
        nuova_quantita = int(input("Inserisci la nuova quantità: "))
        inventario[codice]["quantita"] = nuova_quantita
        print("Quantità modificata correttamente")
    else:
        print("Prodotto non presente")


# La funzione consente di calcolare il valore dei beni nell'inventario

def calcola_inventario():

    totale = 0

    for codice in inventario:
        nome = inventario[codice]["nome"]
        prezzo = inventario[codice]["prezzo"]
        quantita = inventario[codice]["quantita"]
        valore_prodotto = prezzo * quantita
        print()
        print("Codice", codice, "- Nome", nome, "- Prezzo", prezzo, "- Quantità", quantita, "- Totale", valore_prodotto)

        totale = totale + valore_prodotto
    print()
    print("VALORE TOTALE INVENTARIO:", round(totale, 2))


# La funzione consente di mostrare i prodotti presenti nell'inventario

def mostra_inventario():

    print("\n--- PRODOTTI PRESENTI NELL'INVENTARIO ---")

    for codice in inventario:
            nome = inventario[codice]["nome"]
            prezzo = inventario[codice]["prezzo"]
            quantita = inventario[codice]["quantita"]
            print("Codice", codice, "- Nome", nome, "- Prezzo", prezzo, "- Quantità", quantita)

# La funzione consente di leggere prodotti importati da un file di testo

def importa_inventario():
    
    nome_file = open("mio_file.txt", 'r')
    contenuto = nome_file.read()
    print (contenuto)

# La funzione importa i prodotti da un file di testo

def importa_inventario():

# Apro il file in modalità lettura
    nome_file = open("mio_file.txt", "r")

# Salto la prima riga che contiene le intestazioni
    nome_file.readline()

# Leggo tutto il contenuto del file
    contenuto = nome_file.read()
    nome_file.close()

# Inizializzo il codice del prodotto come stringa
    codice = "1"

# Ripeto il ciclo finché ci sono prodotti da leggere (non ci sono piu spazi o a capo)
    while contenuto.strip() != "":

# Individuo la posizione del primo e del secondo spazio
        primo_spazio = contenuto.find(" ")
        secondo_spazio = contenuto.find(" ", primo_spazio + 1)

# Individuo la posizione del primo a capo
        primo_acapo = contenuto.find("\n")

# Estraggo il nome del prodotto
        nome = contenuto[:primo_spazio]

# Estraggo il prezzo e lo converto in numero decimale
        prezzo = float(contenuto[primo_spazio + 1:secondo_spazio])

# Estraggo la quantità e la converto in numero intero
        quantita = int(contenuto[secondo_spazio + 1:primo_acapo])

# Se il codice esiste già, lo incremento di uno
        while codice in inventario:
            codice = str(int(codice) + 1)

# Inserisco il prodotto nel dizionario inventario
        inventario[codice] = {"nome": nome, "prezzo": prezzo, "quantita": quantita}

# Incremento il codice per il prodotto successivo
        codice = str(int(codice) + 1)

# Elimino dal contenuto la parte del prodotto appena letto
        contenuto = contenuto[primo_acapo + 1:]

# Comunico che l'importazione è terminata
    print("Inventario importato correttamente!")

# Visualizzo tutti i prodotti presenti nell'inventario
    mostra_inventario()

# Dizionario che contiene i prodotti del negozio
# Inizialmente contiene tre prodotti di esempio

inventario = {
    "1": {"nome": "Pane", "prezzo": 2.50, "quantita": 10},
    "2": {"nome": "Latte", "prezzo": 1.80, "quantita": 15},
    "3": {"nome": "Pasta", "prezzo": 1.20, "quantita": 20}}


# Ciclo principale del programma
# Il menu viene mostrato finché l'utente non sceglie di uscire

while True:

    menu()

    scelta = input("\nSeleziona una delle opzioni: ").strip()

    # 1. Aggiungi un prodotto

    if scelta == "1":
        aggiungi_prodotto()

    # 2. Elimina un prodotto

    elif scelta == "2":
        elimina_prodotto()

    # 3. Modifica il prezzo di un prodotto

    elif scelta == "3":
        modifica_prezzo()

    # 4. Modifica la quantità di un prodotto

    elif scelta == "4":
        modifica_prodotto()

    # 5. Calcola il totale dell'inventario

    elif scelta == "5":
        calcola_inventario()

    # 6. Mostra tutto l'inventario

    elif scelta == "6":
        mostra_inventario()
        
    # 7. Importa inventario

    elif scelta == "7":
        importa_inventario()    
        
        
    # 0. Esci dal programma

    elif scelta == "0":
        print("Programma terminato!")
        break

    # Gestisce l'errore di scelta

    else:
        print("Opzione non valida. Scegli un numero nel menu")   