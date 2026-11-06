# Ereditarietà e polimorfismo: Animale, Cane e Gatto.


# Classe base (genitore): contiene il nome e un verso generico.
class Animale:
    def __init__(self, nome):
        self.nome = nome

    # Metodo ereditato da Cane e Gatto.
    def presentati(self):
        print(f"Sono {self.nome}")

    def verso(self):
        print("Questo animale fa un verso genericamente.")


# Classe figlia: eredita nome e costruttore da Animale.
# Ridefinisce verso() per descrivere il verso del cane.
class Cane(Animale):
    def verso(self):
        print(f"{self.nome} dice: Bau Bau!")


# Classe figlia: eredita nome e costruttore da Animale.
# Ridefinisce verso() per descrivere il verso del gatto.
class Gatto(Animale):
    def verso(self):
        print(f"{self.nome} dice: Miao!")


# Creo un animale generico, un cane e un gatto.
animaleGenerico = Animale("No name")
fido = Cane("Fido")
whiskers = Gatto("Whiskers")

# Cane e Gatto ereditano presentati() da Animale.
fido.presentati()
whiskers.presentati()

# Ogni oggetto esegue la propria versione di verso().
animaleGenerico.verso()
fido.verso()
whiskers.verso()
