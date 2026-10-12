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

    # 0. Esci dal programma

    elif scelta == "0":
        print("Programma terminato!")
        break

    # Gestisce l'errore di scelta

    else:
        print("Opzione non valida. Scegli un numero nel menu")   