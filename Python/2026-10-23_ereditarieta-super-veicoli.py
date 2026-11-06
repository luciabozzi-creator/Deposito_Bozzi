# Ereditarietà: riutilizzare metodi con super().


# Classe base (genitore).
class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_info(self):
        return f"Veicolo: {self.marca} {self.modello}"


# Classe derivata (figlia) da Veicolo.
class Auto(Veicolo):
    def __init__(self, marca, modello, numero_porte):
        # super() richiama il costruttore della classe genitore.
        super().__init__(marca, modello)
        self.numero_porte = numero_porte

    def mostra_info(self):
        # Riutilizza le informazioni del genitore e aggiunge le porte.
        info_base = super().mostra_info()
        return f"{info_base} con {self.numero_porte} porte"


# Prova del codice con un oggetto della classe figlia e uno della classe base.
mia_auto = Auto("Fiat", "500", 3)
mia_auto2 = Veicolo("Lancia", "Giulia")

# Auto usa mostra_info() ridefinito e aggiunge il numero di porte.
print(mia_auto.mostra_info())
# Output: Veicolo: Fiat 500 con 3 porte

# Veicolo usa il proprio metodo mostra_info().
print(mia_auto2.mostra_info())
# Output: Veicolo: Lancia Giulia
