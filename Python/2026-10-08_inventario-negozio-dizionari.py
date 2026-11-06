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

# Creo un dizionario con alcuni prodotti
prodotti = {
    "1": {"nome": "Pane", "prezzo": 2.50, "quantita": 10},
    "2": {"nome": "Latte", "prezzo": 1.80, "quantita": 15},
    "3": {"nome": "Pasta", "prezzo": 1.20, "quantita": 20}}


#1 Aggiungere un prodotto
def aggiungi_prodotto():
    
    codice = input("AGGIUNGI PRODOTTO: Inserisci il codice del prodotto: ")

    if codice in prodotti: print("Prodotto già presente")

    else:
        nome = input("Inserisci il nome del prodotto: ")
        prezzo = float(input("Inserisci il prezzo: "))
        quantita = int(input("Inserisci la quantità: "))

        prodotti[codice] = {
            "nome": nome,
            "prezzo": prezzo,
            "quantita": quantita}
        print("Prodotto aggiunto correttamente")


#2 Togliere un prodotto
def elimina_prodotto():

    codice = input("TOGLI PRODOTTO: Inserisci il codice del prodotto da eliminare: ")

    if codice in prodotti:
        del prodotti[codice]
        print("Prodotto eliminato correttamente")

    else:
        print("Prodotto non presente")


#3 Modificare il prezzo
def modifica_prezzo():

    codice = input("MODIFICA PREZZO: Inserisci il codice del prodotto: ")

    if codice in prodotti:
        nuovo_prezzo = float(input("Inserisci il nuovo prezzo: "))
        prodotti[codice]["prezzo"] = nuovo_prezzo
        print("Prezzo modificato correttamente")

    else:
        print("Prodotto non presente")

#4 Modificare la quantità
def modifica_quantita():

    codice = input("MODIFICA QUANTITA: Inserisci il codice del prodotto: ")

    if codice in prodotti:
        nuova_quantita = int(input("Inserisci la nuova quantità: "))
        prodotti[codice]["quantita"] = nuova_quantita
        print("Quantità modificata correttamente")

    else:
        print("Prodotto non presente")


#5 Calcolare il totale dell'inventario
def totale_inventario():

    totale = 0
    for codice in prodotti:

        Nome = prodotti[codice]["nome"]
        prezzo = prodotti[codice]["prezzo"]
        quantita = prodotti[codice]["quantita"]

        valore_prodotto = prezzo * quantita
        
        print()
        print("Codice:", codice, nome, "- Prezzo:", prezzo, "- Quantità:", quantita, "- Totale:", valore_prodotto)
        totale = totale + valore_prodotto
        
    print()
    print("VALORE TOTALE INVENTARIO:", totale)

# aggiungi_prodotto()
# elimina_prodotto()
modifica_prezzo()
# modifica_quantita()
totale_inventario()