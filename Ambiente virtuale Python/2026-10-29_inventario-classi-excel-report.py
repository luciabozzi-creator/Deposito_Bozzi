from openpyxl import Workbook
from openpyxl.styles import Font
from pathlib import Path


# Il file Excel si trova sempre nella stessa cartella di questo script.
NOME_FILE = Path(__file__).parent / "inventario.xlsx"
NOME_REPORT = Path(__file__).parent / "report_inventario.xlsx"


# Classe generale: contiene i dati comuni a tutti i prodotti.
class Prodotto:
    categoria = "Generico"

    def __init__(self, codice, nome, quantita, prezzo, descrizione):
        self.codice = codice
        self.nome = nome
        self.quantita = quantita
        self.prezzo = prezzo
        self.descrizione = descrizione

    def mostra(self):
        print(self.codice, self.nome, self.quantita, self.prezzo, self.categoria, self.descrizione)

    def riga_excel(self):
        return {"codice": self.codice, "nome": self.nome, "quantita": self.quantita, "prezzo": self.prezzo, "categoria": self.categoria, "descrizione": self.descrizione}


# Queste classi ereditano i dati e i metodi da Prodotto.
class ProdottoDeperibile(Prodotto):
    def __init__(self, codice, nome, quantita, prezzo, descrizione):
        super().__init__(codice, nome, quantita, prezzo, descrizione)
        self.categoria = "Deperibile"


class ProdottoElettronico(Prodotto):
    def __init__(self, codice, nome, quantita, prezzo, descrizione):
        super().__init__(codice, nome, quantita, prezzo, descrizione)
        self.categoria = "Elettronica"


class ProdottoNeonati(Prodotto):
    def __init__(self, codice, nome, quantita, prezzo, descrizione):
        super().__init__(codice, nome, quantita, prezzo, descrizione)
        self.categoria = "Neonati"


class ProdottoGiardino(Prodotto):
    def __init__(self, codice, nome, quantita, prezzo, descrizione):
        super().__init__(codice, nome, quantita, prezzo, descrizione)
        self.categoria = "Giardino"


def scegli_categoria():
    print("1. Deperibile")
    print("2. Elettronica")
    print("3. Neonati")
    print("4. Giardino")

    scelta = input("Scegli la categoria: ")

    if scelta == "1":
        return "Deperibile"
    elif scelta == "2":
        return "Elettronica"
    elif scelta == "3":
        return "Neonati"
    elif scelta == "4":
        return "Giardino"
    else:
        raise ValueError("Scelta non valida.")


def crea_prodotto(categoria, codice, nome, quantita, prezzo, descrizione):
    if categoria == "Deperibile":
        return ProdottoDeperibile(codice, nome, quantita, prezzo, descrizione)
    elif categoria == "Elettronica":
        return ProdottoElettronico(codice, nome, quantita, prezzo, descrizione)
    elif categoria == "Neonati":
        return ProdottoNeonati(codice, nome, quantita, prezzo, descrizione)
    else:
        return ProdottoGiardino(codice, nome, quantita, prezzo, descrizione)


def carica_prodotti():
    magazzino = []

    if NOME_FILE.exists():
        from openpyxl import load_workbook
        foglio = load_workbook(NOME_FILE, data_only=True).active
        intestazioni = [cella.value for cella in foglio[1]]

        for valori in foglio.iter_rows(min_row=2, values_only=True):
            riga = dict(zip(intestazioni, valori))
            if riga["codice"] is not None:
                descrizione = riga["descrizione"] or ""
                prodotto = crea_prodotto(str(riga["categoria"]), str(riga["codice"]), str(riga["nome"]), int(riga["quantita"]), float(riga["prezzo"]), str(descrizione))
                magazzino.append(prodotto)

    return magazzino


def salva_prodotti(magazzino):
    cartella = Workbook()
    foglio = cartella.active
    foglio.title = "Inventario"
    foglio.append(["codice", "nome", "quantita", "prezzo", "categoria", "descrizione"])

    for prodotto in magazzino:
        foglio.append([prodotto.codice, prodotto.nome, prodotto.quantita, prodotto.prezzo, prodotto.categoria, prodotto.descrizione])

    cartella.save(NOME_FILE)


def crea_report(magazzino, categoria):
    cartella = Workbook()
    foglio = cartella.active
    foglio.title = "Report"
    foglio.append(["codice", "nome", "quantita", "prezzo", "categoria", "descrizione"])
    numero_prodotti = 0

    for prodotto in magazzino:
        if categoria is None or prodotto.categoria == categoria:
            foglio.append([prodotto.codice, prodotto.nome, prodotto.quantita, prodotto.prezzo, prodotto.categoria, prodotto.descrizione])
            numero_prodotti += 1

    for cella in foglio[1]:
        cella.font = Font(bold=True)
    foglio.freeze_panes = "A2"
    foglio.auto_filter.ref = foglio.dimensions
    cartella.save(NOME_REPORT)
    return numero_prodotti


def menu():
    # Il magazzino è una lista di prodotti.
    magazzino = carica_prodotti()

    while True:
        print("\n--- MENU MAGAZZINO ---")
        print("1. Mostra i prodotti")
        print("2. Aggiungi un prodotto")
        print("3. Modifica un prodotto")
        print("4. Elimina un prodotto")
        print("5. Report per categoria")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        try:
            if scelta == "1":
                if len(magazzino) == 0:
                    print("Il magazzino è vuoto. Usa l'opzione 2 per aggiungere un prodotto.")
                else:
                    for prodotto in magazzino:
                        prodotto.mostra()

            elif scelta == "2":
                categoria = scegli_categoria()
                codice = input("Codice alfanumerico: ")
                nome = input("Nome: ")
                quantita = int(input("Quantità: "))
                prezzo = float(input("Prezzo: ").replace(",", "."))
                descrizione = input("Descrizione: ")

                prodotto = crea_prodotto(categoria, codice, nome, quantita, prezzo, descrizione)
                magazzino.append(prodotto)
                salva_prodotti(magazzino)
                print("Prodotto aggiunto.")

            elif scelta == "3":
                codice_cercato = input("Codice del prodotto da modificare: ")
                trovato = False

                for indice in range(len(magazzino)):
                    if magazzino[indice].codice == codice_cercato:
                        trovato = True
                        print("Inserisci i nuovi dati del prodotto.")
                        categoria = scegli_categoria()
                        codice = input("Nuovo codice: ")
                        nome = input("Nuovo nome: ")
                        quantita = int(input("Nuova quantità: "))
                        prezzo = float(input("Nuovo prezzo: ").replace(",", "."))
                        descrizione = input("Nuova descrizione: ")

                        prodotto = crea_prodotto(categoria, codice, nome, quantita, prezzo, descrizione)
                        magazzino[indice] = prodotto
                        salva_prodotti(magazzino)
                        print("Prodotto modificato.")
                        break

                if trovato == False:
                    print("Prodotto non trovato.")

            elif scelta == "4":
                codice_cercato = input("Codice del prodotto da eliminare: ")
                trovato = False

                for prodotto in magazzino:
                    if prodotto.codice == codice_cercato:
                        magazzino.remove(prodotto)
                        salva_prodotti(magazzino)
                        print("Prodotto eliminato.")
                        trovato = True
                        break

                if trovato == False:
                    print("Prodotto non trovato.")

            elif scelta == "5":
                print("0. Tutte le categorie")
                print("1. Deperibile")
                print("2. Elettronica")
                print("3. Neonati")
                print("4. Giardino")
                filtro = input("Scegli il filtro del report: ")
                categorie = {"1": "Deperibile", "2": "Elettronica", "3": "Neonati", "4": "Giardino"}

                if filtro == "0":
                    categoria = None
                elif filtro in categorie:
                    categoria = categorie[filtro]
                else:
                    raise ValueError("Filtro non valido.")

                numero_prodotti = crea_report(magazzino, categoria)
                print("Report Excel salvato in:", NOME_REPORT)
                print("Prodotti inclusi nel report:", numero_prodotti)

            elif scelta == "0":
                print("Arrivederci!")
                break

            else:
                print("Opzione non valida.")

        except ValueError as errore:
            print("Errore:", errore)


if __name__ == "__main__":
    menu()
