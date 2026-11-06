"""
ESERCIZIO - GARA DI MARATONA

Gestire i risultati di una gara di maratona.

Per ogni corridore acquisire:
- nome
- cognome
- nazionalità
- età
- sesso

Ad ogni corridore viene assegnato un ID gara.

Acquisire i tempi:
- dopo 10 km
- dopo 20 km
- dopo 30 km
- al traguardo

Ad ogni rilevazione visualizzare:
- i primi 5 uomini
- le prime 5 donne
- i primi 5 over 50

Al termine della gara visualizzare i primi 3
delle tre categorie assegnando le medaglie:
- ORO
- ARGENTO
- BRONZO

In caso di parità al traguardo viene preferito
il corridore più anziano.

Utilizzare liste, tuple, while e for.
"""


# Creo la lista dei corridori. ID, nome, cognome, nazionalità, età, sesso.

corridori = [
    (1, "LUCA", "ROSSI", "ITA", 35, "M"),
    (2, "MARCO", "BIANCHI", "ITA", 45, "M"),
    (3, "PAOLO", "VERDI", "ITA", 55, "M"),
    (4, "ANDREA", "NERI", "FRA", 58, "M"),
    (5, "MATTEO", "GIALLI", "ESP", 62, "M"),
    (6, "ANNA", "ROMANO", "ITA", 28, "F"),
    (7, "SARA", "CONTI", "ITA", 42, "F"),
    (8, "ELENA", "COSTA", "ITA", 52, "F"),
    (9, "LAURA", "MARTIN", "FRA", 57, "F"),
    (10, "GIULIA", "LOPEZ", "ESP", 61, "F")]

# Tempi ID, ore, minuti, secondi
tempi_10 = [
    (1, 0, 40, 10),
    (2, 0, 39, 20),
    (3, 0, 41, 30),
    (4, 0, 38, 50),
    (5, 0, 42, 10),
    (6, 0, 40, 40),
    (7, 0, 43, 20),
    (8, 0, 39, 50),
    (9, 0, 41, 10),
    (10, 0, 42, 40)]

tempi_20 = [
    (1, 1, 20, 20),
    (2, 1, 18, 40),
    (3, 1, 22, 30),
    (4, 1, 17, 50),
    (5, 1, 24, 10),
    (6, 1, 21, 30),
    (7, 1, 25, 20),
    (8, 1, 19, 50),
    (9, 1, 23, 10),
    (10, 1, 24, 40)]

tempi_30 = [
    (1, 2, 1, 10),
    (2, 1, 59, 20),
    (3, 2, 3, 30),
    (4, 1, 57, 50),
    (5, 2, 5, 10),
    (6, 2, 2, 40),
    (7, 2, 7, 20),
    (8, 2, 0, 50),
    (9, 2, 4, 10),
    (10, 2, 6, 40)]

tempi_traguardo = [
    (1, 2, 45, 10),
    (2, 2, 42, 20),
    (3, 2, 48, 30),
    (4, 2, 40, 50),
    (5, 2, 48, 30),
    (6, 2, 46, 40),
    (7, 2, 52, 20),
    (8, 2, 43, 50),
    (9, 2, 49, 10),
    (10, 2, 51, 40)]

# Inserisco le quattro liste dei tempi in una nuova lista.
# indice 0 = 10 KM
# indice 1 = 20 KM
# indice 2 = 30 KM
# indice 3 = TRAGUARDO

tempi_rilevazioni = [
    tempi_10,
    tempi_20,
    tempi_30,
    tempi_traguardo]


# Creo una lista vuota con tutti i tempi trasformati in secondi e i corridori

tempi_in_secondi = []
numero_rilevazione = 0

# 0 = 10 KM
# 1 = 20 KM
# 2 = 30 KM
# 3 = TRAGUARDO

while numero_rilevazione < 4:
    tabella_secondi = []
    for tempo in tempi_rilevazioni[numero_rilevazione]:
        id_corridore = tempo[0]
        ore = tempo[1]
        minuti = tempo[2]
        secondi = tempo[3]

        tempo_secondi = (ore * 3600 + minuti * 60 + secondi)


# Aggiungo alla tabella una tupla contenente: ID corridore, tempo totale in secondi

        tabella_secondi.append((id_corridore, tempo_secondi))

# Aggiungo l'intera tabella alla lista.

    tempi_in_secondi.append(tabella_secondi)

# Passo alla rilevazione successiva.
    numero_rilevazione += 1

print("10 KM")
print(tempi_in_secondi[0])

print("20 KM")
print(tempi_in_secondi[1])

print("30 KM")
print(tempi_in_secondi[2])

print("TRAGUARDO")
print(tempi_in_secondi[3])

# Facciamo le classifiche per ciascuna categoria e rilevazione
# 0 = 10 KM
# 1 = 20 KM
# 2 = 30 KM
# Il traguardo è il podio finale


# CATEGORIZZAZIONE DEI CORRIDORI


# Elaboro le tre rilevazioni parziali:
# 0 = 10 KM
# 1 = 20 KM
# 2 = 30 KM

numero_rilevazione = 0

while numero_rilevazione < 3:

# Creo le tre categorie vuote per la rilevazione corrente

    uomini = []
    donne = []
    over50 = []


# Leggo i tempi della rilevazione corrente

    for tempo in tempi_in_secondi[numero_rilevazione]:

        # Nella tabella dei tempi:
        # [0] = ID
        # [1] = tempo in secondi

        id_corridore = tempo[0]
        tempo_secondi = tempo[1]


# Cerco il corridore corrispondente all'ID

        for corridore in corridori:

            if corridore[0] == id_corridore:

# Creo il risultato con tempo in secondi e ID

                risultato = (
                    tempo_secondi,
                    id_corridore
                )

# Categoria uomini

                if corridore[5] == "M":
                    uomini.append(risultato)


# Categoria donne

                if corridore[5] == "F":
                    donne.append(risultato)


# Categoria over 50

                if corridore[4] > 50:
                    over50.append(risultato)


# Stampo le categorie create per i parziali

    print("\nRILEVAZIONE", numero_rilevazione, "- UOMINI")
    print(uomini)
    print("\nRILEVAZIONE", numero_rilevazione, "- DONNE")
    print(donne)
    print("\nRILEVAZIONE", numero_rilevazione, "- OVER 50")
    print(over50)

# Passo alla rilevazione successiva

    numero_rilevazione += 1
    

# Categorizzazione al traguardo, creo le tre categorie vuote

uomini_finale = []
donne_finale = []
over50_finale = []


# Prendo i tempi del traguardo, tempi_in_secondi[3] = TRAGUARDO

for tempo in tempi_in_secondi[3]:

# Nella tabella dei tempi: [0] = ID , [1] = tempo in secondi

    id_corridore = tempo[0]
    tempo_secondi = tempo[1]


# Cerco il corridore corrispondente all'ID

    for corridore in corridori:

        if corridore[0] == id_corridore:


# Creo il risultato finale. Per ora inserisco: [0] = tempo in secondi e [1] = ID

            risultato_finale = (
                tempo_secondi,
                id_corridore)

# Traguardo ategorie uomini

            if corridore[5] == "M":
                uomini_finale.append(risultato_finale)

# Traguardo ategorie donne

            if corridore[5] == "F":
                donne_finale.append(risultato_finale)

# Traguardo categoria over 50

            if corridore[4] > 50:
                over50_finale.append(risultato_finale)

# Stampo le tre categorie per il podio

print("\nTRAGUARDO - UOMINI")
print(uomini_finale)

print("\nTRAGUARDO - DONNE")
print(donne_finale)

print("\nTRAGUARDO - OVER 50")
print(over50_finale)