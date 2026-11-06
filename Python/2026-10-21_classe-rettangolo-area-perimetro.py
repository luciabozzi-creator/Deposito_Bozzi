"""
Esercizio: Crea una classe chiamata Rettangolo.

• Il costruttore deve ricevere come parametri la base e l' altezza.

• Aggiungi un metodo calcola_area che calcola e restituisce (usa return)
  l'area del rettangolo (base × altezza).
  
• Aggiungi un metodo calcola_perimetro che calcola e restituisce il perimetro
  (2 × (base + altezza)).
  
• Crea un rettangolo con base 5 e altezza 3, poi stampa a schermo la sua area
  e il suo perimetro.

"""

class Rettangolo:

    def __init__(self, base, altezza):

# Salva le dimensioni ricevute nel costruttore.

        self.base = base
        self.altezza = altezza

    def calcola_area(self):

# Restituisce base per altezza.

        area = self.base * self.altezza
        return area

    def calcola_perimetro(self):
        
# Restituisce due volte la somma di base e altezza.

        perimetro = 2 * (self.base + self.altezza)
        return perimetro


# Crea il rettangolo richiesto dalla consegna.

rett = Rettangolo(5, 3)
area = rett.calcola_area()
perimetro = rett.calcola_perimetro()



# Stampa i risultati: area 15 e perimetro 16.

print()
print(f"Area: {area}")
print()
print(f"Perimetro: {perimetro}")
