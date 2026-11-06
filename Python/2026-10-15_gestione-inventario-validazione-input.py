"""
Esercizio: Gestione Inventario Negozio.

Creare un programma che gestisce i prodotti di un negozio (nome, prezzo, quantità)

1. aggiungere un prodotto
2. togliere un prodotto
3. modificare il prezzo
4. modificare la quantità
5. calcolare il totale dell'inventario (quantità * prezzo per ogni prodotto)

"""

# la funzione mostra all'utente le opzioni che può selezionare

def menu ():
    print ("\n--- GESTIONE INVENTARIO ---")
    print ("1. Aggiungi un prodotto ")
    print ("2. Elimina un prodotto  ")
    print ("3. Modifica il prezzo di un prodotto  ")
    print ("4. Modifica la quantità un prodotto  ")
    print ("5. Calcola il totale dell'inventario  ")
    print ("6. Mostra tutto l'inventario  ")
    print ("7. Importa l'inventario da file ")
    print ("8. Esporta l'inventario su file ")
    print ("0. Esci ")

# la funzione consente di aggiungere un prodotto all'inventario

def aggiungi_prodotto ():
    descrizione = input ("Inserisci il nome del prodotto: ")
    # verificare se è presente
    if descrizione in inventario:
        print ("Prodotto già presente")
        #inventario.pop(descrizione)
    else:
        prezzo = float (input ("Inserisci il prezzo del prodotto: "))
        quantita = int (input ("inserisci la quantità di prodotto: "))
        inventario [descrizione] = {"prezzo": prezzo, "quantità": quantita}
    #return

# la funzione consente di eeliminare un prodotto dall'inventario

def elimina_prodotto ():
    descrizione = input ("Inserisci il nome del prodotto: ")
    if descrizione in inventario:
        del inventario [descrizione]
        #inventario.pop(descrizione)
    else:
        print ("Prodotto non presente")
    #return

# la funzione consente di modificare il prezzo di un prodotto nell'inventario

def modifica_prezzo ():
    descrizione = input ("Inserisci il nome del prodotto: ")
    if descrizione in inventario:
        nuovo_prezzo = float (input ("Inserisci il nuovo prezzo del prodotto: "))
        inventario [descrizione]["prezzo"] = nuovo_prezzo
    else:
        print ("Prodotto non presente")
    #return

# la funzione consente di modificare la quantità di un prodotto nell'inventario

def modifica_prodotto ():
    descrizione = input ("Inserisci il nome del prodotto: ")
    if descrizione in inventario:
        nuova_quantita = int (input ("Inserisci la nuova quantità del prodotto: "))
        inventario [descrizione]["quantità"] = nuova_quantita
    else:
        print ("Prodotto non presente")
    #return

# la funzione consente di calcolare il valore dei beni nell'inventario

def calcola_inventario ():
    totale = 0.0
    for descrizione, prodotto in inventario.items ():
        #totale += (prodotto["prezzo"] * prodotto["quantità"])
        totale_prodotto = prodotto["prezzo"] * prodotto["quantità"]
        print(f"Totale prodotto {descrizione}: {totale_prodotto}")
        totale += totale_prodotto
    print (f"\nValore totale inventario: {totale}")    
    #return

# la funzione consente di mostrare i prodotti presenti nell'inventario

def mostra_inventario ():
    print (f"\n---INVENTARIO---")
    for descrizione, prodotto in inventario.items ():
        print(f"Prodotto {descrizione} - Prezzo: {prodotto["prezzo"]}\
 - Quantità: {prodotto["quantità"]}")
    #return

# la funzione consente di leggere prodotti importati da un file di testo

def importa_inventario ():
    # Apro il file in sola lettura e recupero tutti i dati di testo
    nome_file = open("mio_file.txt", 'r')
    contenuto = nome_file.read ()
    nome_file.close ()
    #print (contenuto)
    
    # Verifico che il testo finisca con un a capo
    if contenuto and contenuto[-1] != "\n":
        contenuto += "\n"
        
    # Definisco un indice per scorrere i caratteri della stringa
    indice_corrente = 0
    
    # Elimino la riga di intestazione usando find
    prima_riga = contenuto.find("\n", indice_corrente)
    indice_corrente = prima_riga + 1
    lunghezza_testo = len(contenuto)
    
    # Scansiono il testo riga per riga usando find
    while indice_corrente < lunghezza_testo:
        fine_riga = contenuto.find("\n", indice_corrente)
        # Seleziono una riga dal contenuto
        riga = contenuto[indice_corrente:fine_riga].strip()
        # Aggiorno l'indice per passare alla riga successiva
        indice_corrente = fine_riga + 1
        
        if riga:
            primo_spazio = riga.find(" ")
            ultimo_spazio = riga.rfind(" ")
            
            if primo_spazio != -1 and ultimo_spazio != -1 and primo_spazio != ultimo_spazio:
                prodotto = riga[0:primo_spazio].strip()
                prezzo = float (riga[primo_spazio:ultimo_spazio].strip())
                quantita = int (riga[ultimo_spazio:].strip())
                
                if prodotto and prezzo and quantita:
                    # Associo al nome del prodotto il dizionario con prezzo e quantità
                    inventario[prodotto] = {
                        "prezzo": prezzo,
                        "quantità": quantita
                    }
                    
# la funzione consente di scrivere i prodotti dell'inventario su un file di testo

def esporta_inventario ():
    # 1. LEGGO IL CONTENUTO ATTUALE DEL FILE
    file = open("mio_file.txt", "r")
    contenuto = file.read()
    file.close()
    
    # Assicuro che il testo termini correttamente con un a capo
    if contenuto and contenuto[-1] != "\n":
        contenuto += "\n"
        
    nuovo_testo = ""
    prodotto_trovato = False
    duplicato_esatto = False
    
    # Definisco un indice per scorrere i caratteri della stringa
    indice_corrente = 0
    
    # Elimino la riga di intestazione usando find
    prima_riga = contenuto.find("\n", indice_corrente)
    indice_corrente = prima_riga + 1
    lunghezza_testo = len(contenuto)
    
    # Controllo i dati dei prodotti dell'inventario
    for prodotto in inventario:
        prodotto_input = prodotto
        print (prodotto)
        prezzo_input = inventario[prodotto]["prezzo"]
        quantita_input = inventario[prodotto]["quantità"]
        
        # 2. ANALIZZO IL FILE RIGA PER RIGA USANDO IL METODO FIND
        while indice_corrente < lunghezza_testo:
            fine_riga = contenuto.find("\n", indice_corrente)
            riga = contenuto[indice_corrente:fine_riga].strip()
            indice_corrente = fine_riga + 1
            
            if riga:
                primo_spazio = riga.find(" ")
                ultimo_spazio = riga.rfind(" ")
                
                if primo_spazio != -1 and ultimo_spazio != -1 and primo_spazio != ultimo_spazio:
                    prodotto_corrente = riga[0:primo_spazio].strip()
                    print (prodotto_corrente)
                    prezzo_corrente = float (riga[primo_spazio:ultimo_spazio].strip())
                    quantita_corrente = int (riga[ultimo_spazio:].strip())
                    
                    # Controllo se il prodotto esiste già
                    if prodotto_corrente == prodotto_input:
                        prodotto_trovato = True
                        
                        # Controllo se i dati inseriti sono identici a quelli presenti (copia)
                        if prezzo_corrente == prezzo_input and quantita_corrente == quantita_input:
                            duplicato_esatto = True
                            nuovo_testo += riga + "\n"
                        else:
                            # AGGIORNAMENTO: Sostituisco i vecchi dati con i nuovi
                            nuovo_testo += prodotto_input + " " + str (prezzo_input) + " " + str (quantita_input) + "\n"
                    else:
                        # Riga di un altro prodotto, la mantengo invariata
                        nuovo_testo += riga + "\n"
                else:
                    nuovo_testo += riga + "\n"

        # 3. VALUTO SE SCRIVERE I DATI SUL FILE
        if duplicato_esatto:
            print("Operazione annullata: I dati inseriti sono un duplicato esatto di quelli già presenti.")
            continue
            
        if not prodotto_trovato:
            # NUOVO INSERIMENTO: Aggiungo l'articolo in fondo
            nuovo_testo += prodotto_input + " " + str (prezzo_input) + " " + str (quantita_input) + "\n"
            print("Nuovo articolo salvato con successo nel file.")
        else:
            print("Articolo esistente aggiornato con successo nel file.")
            
        # 4. RISCRIVO IL FILE AGGIORNATO
        file = open("mio_file.txt", "w")
        file.write(nuovo_testo)
        file.close()
        return
    

# Definisco le variabili globali                     
inventario = {}

# Definisco il codice principale del programma
while True:
    
    # Richiamo il menu finchè l'utente non digita 0
    
    menu()
    
    # Chiedo all'utente di effettuare una scelta in base al menu
    
    scelta = input ("\nSeleziona una delle opzioni: ").strip ()
    
    # 1. Aggiungi un prodotto
    
    if scelta == "1":
        aggiungi_prodotto ()
        
    # 2. Elimina un prodotto
    elif scelta == "2":
        elimina_prodotto ()
        
    # 3. Modifica il prezzo di un prodotto
    elif scelta == "3":
        modifica_prezzo ()    
        
    # 4. Modifica la quantità di un prodotto
    elif scelta == "4":
        modifica_prodotto ()     
    
    # 5. Calcola il totale dell'inventario
    elif scelta == "5":
        calcola_inventario ()  
    
    # 6. Mostra tutto l'inventario 
    elif scelta == "6":
        mostra_inventario ()    
    
    # 7. Importa l'inventario da un file testo 
    elif scelta == "7":
        importa_inventario ()
        
    # 8. Esport l'inventario su un file testo 
    elif scelta == "8":
        esporta_inventario ()  
            
    # 0. Mostra tutto l'inventario 
    elif scelta == "0":
        print ("Programma terminato!")
        break
    
    # Gestisce l'errore di scelta
    else:
        print ("Opzione non valida. Scegli un numero nel menu")
