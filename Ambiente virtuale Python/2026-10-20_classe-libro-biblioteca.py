"""
Esercizio: Biblioteca

Traccia: Create una classe chiamata Libro.

• Deve avere un metodo costruttore __init__ che accetta due attributi:
  titolo e autore.
  
• Aggiungere un metodo chiamato descrizione che stampa una frase del tipo:
  "Il libro 'Titolo' è stato scritto da Autore."
  
• Crea un oggetto (istanza) di questa classe e chiama il metodo descrizione.

"""

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def descrizione(self):
        print(f"Il libro '{self.titolo}' è stato scritto da {self.autore}.")


libro_inserito = Libro("I promessi sposi", "Alessandro Manzoni")
libro_inserito.descrizione()

