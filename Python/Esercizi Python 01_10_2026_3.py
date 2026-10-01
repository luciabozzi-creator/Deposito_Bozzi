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
   
3. 	Acquisizione e Controllo Dati (Ciclo while): Usa un ciclo infinito
    per chiedere i dati all'utente. Applica i seguenti controlli:
    
- 	Studente: Se l'utente scrive "fine", il ciclo si interrompe.
- 	Classe: Deve essere una stringa di 2 caratteri (es. "3A", "5B").
    Se non lo è, mostra un errore e richiedila.
- 	Materia: L'utente inserisce la materia. Il programma deve controllare
     se la materia esiste nella tupla dei docenti. Se non esiste, mostra
     le materie disponibili e richiedila.
- 	Voto: Deve essere un numero decimale compreso tra 2 e 10. Gestisci
     anche l'errore nel caso in cui l'utente inserisca lettere al posto
     di numeri.
4. 	Resoconto Finale (Cicli for): Al termine dell'inserimento, usa i cicli
    per stampare il riepilogo di tutti i voti e calcolare la media generale
    della scuola.
"""

# 1 Creo una tupla fissa contenente le materie e i rispettivi docenti

materie_docenti = (
    ("STORIA", "ROSSI"),
    ("GEOGRAFIA", "GIALLI"),
    ("ITALIANO", "VERDI")
)

# 2 Creo una lista vuota chiamata registro_voti

registro_voti = []

# 3 Chiedo all'utente il nome dello studente.
nome_studente = input("Inserisci il nome dello studente: ")
nome_studente = nome_studente.upper()

# 4 Controllo se l'utente ha scritto "fine":
# - Se SÌ -> termino l'inserimento e passo al resoconto finale
# - Se NO -> continuo

if nome_studente == "FINE":
    break

# 5 Chiedo la classe dello studente
classe = input("Inserisci la classe dello studente: ")
classe = classe.upper()

# 6 Controllo che la classe abbia 2 caratteri:
# - Se NO -> mostro un errore e richiedo la classe
# - Se SÌ -> continuo

while len(classe) != 2:
    print("Errore: la classe deve avere 2 caratteri")
    classe = input("Inserisci nuovamente la classe: ")

# 7 Chiedo la materia

materia = input("Inserisci la materia: ")
materia = materia.upper()

# 8 Controllo se la materia è presente nella tupla delle materie:
# - Se NO -> mostro un errore, mostro le materie disponibili e richiedo la materia
# - Se SÌ -> continuo

materia_valida = False

for elemento in materie_docenti:
    if materia == elemento[0]:
        materia_valida = True

# 9 Chiedo il voto

voto = input("Inserisci il voto: ")

# 10 Controllo che il voto sia un numero:
# - Se vengono inserite lettere -> mostro un errore e richiedo il voto
# - Se è un numero -> continuo

voto_valido = False

while voto_valido == False:
    voto = input("Inserisci il voto: ")
else:
    print("Errore: il voto deve essere un numero")

# 11 Controllo che il voto sia compreso tra 2 e 10:
# - Se NO -> mostro un errore e richiedo il voto
# - Se SÌ -> continuo




# 12 Creo una tupla con: (Nome_Alunno, Classe, Materia, Voto)
#Aggiungo la tupla alla lista registro_voti

# 13 Torno allo STEP 3 e chiedo il nome di un nuovo studente

# 14 Quando l'utente scrive "fine", termino l'inserimento e uso un ciclo for per stampare tutti i voti registrati

# 15 Calcolo la somma di tutti i voti

# 16 Calcolo la media generale: media generale = somma dei voti / numero dei voti

# 17 Stampo la media generale della scuola.

# 18 FINE

