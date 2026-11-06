"""
Esercizio: gestione conto corrente.

• Crea una classe chiamata ContoBancario per gestire un saldo.

• Il costruttore deve accettare il nome del titolare e impostare
  un attributo saldo iniziale che parte sempre da 0.
  
• Crea un metodo deposita che accetta un importo e lo somma al
  saldo attuale.
  
• Crea un metodo preleva che accetta un importo. Se il saldo è
  sufficiente, sottrae l'importo dal saldo; altrimenti, stampa
  un messaggio di errore (es. "Fondi insufficienti").
  
• Crea un metodo mostra_saldo che stampa il saldo attuale.

"""

# La classe e' il modello da cui si possono creare diversi conti bancari.
class ContoBancario:
    """Gestisce il saldo di un conto bancario."""

    def __init__(self, titolare):
# __init__ e' il costruttore: viene chiamato quando creiamo un conto.
# self indica il conto specifico che stiamo creando.
        self.titolare = titolare

# Attributi di istanza: ogni conto mantiene i propri valori.
        self.saldo = 0

    def deposita(self, importo):
# Metodo che modifica il saldo dell'istanza corrente.
        self.saldo += importo

    def preleva(self, importo):
# Controlla che il saldo basti prima di effettuare il prelievo.
        if self.saldo >= importo: self.saldo -= importo
        else:
            print("Fondi insufficienti")

    def mostra_saldo(self):
# print mostra a schermo i dati dell'istanza corrente.
        print(f"Saldo di {self.titolare}: {self.saldo}")


# input chiede il nome del titolare e restituisce il testo digitato.
nome_titolare = input("Inserisci il nome del titolare: ")

# Crea un'istanza della classe usando il nome inserito.
conto = ContoBancario(nome_titolare)

# Mostra il saldo iniziale impostato dal costruttore.
conto.mostra_saldo()

# input restituisce testo; int lo converte in un numero intero.
importo_deposito = int(input("Quanto vuoi depositare? "))
conto.deposita(importo_deposito)
conto.mostra_saldo()

# Chiede un importo da prelevare e lo passa al metodo preleva.
importo_prelievo = int(input("Quanto vuoi prelevare? "))
conto.preleva(importo_prelievo)
conto.mostra_saldo()
