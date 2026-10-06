"""
Esercizio: Il Registro Elettronico

Scenario: Devi creare un programma per registrare i voti degli alunni di
          una scuola.
          
1. La struttura dati fissa (Tupla): Definisci le materie scolastiche valide
   e i relativi docenti usando una tupla di tuple immutabile. Ogni elemento
   deve essere (Nome_Materia, Nome_Docente).
2. La struttura dati dinamica (Lista): Crea una lista vuota chiamata
   registro_voti. Ogni volta che inserisci un voto valido, aggiungerai
   alla lista una nuova tupla strutturata così: (Nome_Alunno, Classe,
   Materia, Voto).
3. Acquisizione e Controllo Dati (Ciclo while): Usa un ciclo infinito
   per chiedere i dati all'utente. Applica i seguenti controlli:
	• Studente: Se l'utente scrive "fine", il ciclo si interrompe.
	• Classe: Deve essere una stringa di 2 caratteri (es. "3A", "5B").
	  Se non lo è, mostra un errore e richiedila.
	• Materia: L'utente inserisce la materia. Il programma deve controllare
	  se la materia esiste nella tupla dei docenti. Se non esiste, mostra
	  le materie disponibili e richiedila.
	• Voto: Deve essere un numero decimale compreso tra 2 e 10. Gestisci
	  anche l'errore nel caso in cui l'utente inserisca lettere al posto
	  di numeri.
4. Resoconto Finale (Cicli for): Al termine dell'inserimento, usa i cicli
   per stampare il riepilogo di tutti i voti e calcolare la media generale
   della scuola.

"""
# 1. STRUTTURA FISSA: Materie disponibili e relativi docenti (Immutabile)
CONFIG_MATERIE = (
    ("Matematica", "Prof. Rossi"),
    ("Italiano", "Prof.ssa Bianchi"),
    ("Inglese", "Prof. Smith")
)

# Estraiamo solo i nomi delle materie in minuscolo per facilitare i controlli
materie_valide = [materia[0].lower() for materia in CONFIG_MATERIE]

# 2. STRUTTURA DINAMICA: Registro che conterrà i voti inseriti
registro_voti = []

print("=== GESTIONE REGISTRO SCOLASTICO ===")
print("Inserisci i dati richiesti. Digita 'fine' come nome studente per terminare.\n")

# 3. CICLO WHILE PER ACQUISIZIONE E CONTROLLO DATI
while True:
    alunno = input("Nome Alunno: ").strip()
    if alunno.lower() == "fine":
        break
        
    if not alunno:
        print("Il nome non può essere vuoto! Riprova.")
        continue

    # Controllo Classe (es. 3A, 4B)
    while True:
        classe = input("Classe (es. 3A): ").strip().upper()
        # Controlliamo che sia lunga 2 caratteri, che il primo sia un numero e il secondo una lettera
        if len(classe) == 2 and classe[0].isdigit() and classe[1].isalpha():
            break
        print("Errore! La classe deve essere composta da un numero e una lettera (es. 5B).")

    # Controllo Materia
    while True:
        materia_input = input("Materia: ").strip()
        if materia_input.lower() in materie_valide:
            # Recuperiamo il nome con la formattazione corretta dalla tupla originale
            materia_corretta = ""
            for mat, doc in CONFIG_MATERIE:
                if mat.lower() == materia_input.lower():
                    materia_corretta = mat
            break
        
        elenco_materie = ", ".join([m[0] for m in CONFIG_MATERIE])
        print(f"Errore! Materia non esistente. Scegli tra: {elenco_materie}")

    # Controllo Voto SENZA TRY-EXCEPT
    while True:
        voto_stringa = input("Voto (da 2 a 10): ").strip()
        
        # Rimpiazziamo il primo punto trovato con il vuoto per verificare se restano solo cifre.
        # Questo permette di validare sia interi (es. "8") sia decimali (es. "7.5").
        if voto_stringa.replace('.', '', 1).isdigit() and voto_stringa != ".":
            voto = float(voto_stringa) # Ora siamo sicuri che la conversione non fallirà
            
            if 2.0 <= voto <= 10.0:
                break
            print("Errore! Il voto deve essere compreso tra 2 e 10.")
        else:
            print("Errore! Devi inserire un numero valido (usa il punto per i decimali, es: 7.5).")

    # Salvataggio dei dati validati nel registro come Tupla
    registro_voti.append((alunno, classe, materia_corretta, voto))
    print(f"-> Voto registrato con successo per {alunno}!\n")


# 4. RESOCONTO FINALE CON CICLI FOR
print("\n=== RESOCONTO GENERALE DEI VOTI ===")

if not registro_voti:
    print("Nessun dato inserito nel registro.")
else:
    somma_voti = 0
    
    # Scorriamo la lista di tuple usando il disimpacchettamento nel ciclo FOR
    for studente, classe, materia, voto in registro_voti:
        # Troviamo il docente associato alla materia scorrendo la tupla di configurazione
        docente_corrente = ""
        for mat, doc in CONFIG_MATERIE:
            if mat == materia:
                docente_corrente = doc
                
        print(f"[{classe}] {studente:<15} | Materia: {materia:<12} ({docente_corrente}) | Voto: {voto:>4.1f}")
        somma_voti += voto

    # Calcolo della media generale usando la funzione len() sulla lista
    media_generale = somma_voti / len(registro_voti)
    print("-" * 65)
    print(f"Numero totale di valutazioni: {len(registro_voti)}")
    print(f"Media generale dell'istituto: {media_generale:.2f}")
