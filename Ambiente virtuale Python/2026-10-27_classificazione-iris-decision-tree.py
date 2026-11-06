"""
Esercizio della lezione del 27 ottobre:
prevedere la specie di un fiore Iris a partire dalle sue misure.

La traccia richiede di:
1. caricare il dataset Iris;
2. standardizzare le caratteristiche con StandardScaler;
3. dividere i dati in training (70%) e test (30%);
4. addestrare un DecisionTreeClassifier;
5. valutare precision, recall e F1-score con classification_report;
6. visualizzare la matrice di confusione.
"""

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

# Carica 150 fiori Iris. Ogni fiore è descritto da quattro misure in centimetri:
# lunghezza e larghezza del sepalo, poi lunghezza e larghezza del petalo.
iris = load_iris()

# X contiene le quattro misure di ciascun fiore: sono gli input del modello.
X = iris.data

# y contiene la specie corretta di ciascun fiore: è ciò che il modello deve imparare
# a prevedere. Le tre specie sono setosa, versicolor e virginica.
y = iris.target

# Metti da parte il 30% dei fiori per verificare il modello su esempi non usati
# durante l'addestramento: 45 fiori su 150. Il restante 70% (105 fiori) serve
# per l'addestramento.
#
# stratify=y mantiene le proporzioni delle tre specie: 15 fiori di ogni specie
# nel test e 35 di ogni specie nel training.
#
# random_state=42 fissa la divisione: rieseguendo il programma ritroviamo gli
# stessi fiori nei due gruppi. 42 è una scelta convenzionale; si può usare
# qualsiasi altro numero intero.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y,
)

# Standardizza le misure per metterle su scale confrontabili. La traccia lo
# richiede; per un albero decisionale la standardizzazione in genere non è
# necessaria, ma la applichiamo per rispettare l'esercizio.
#
# Lo scaler impara media e deviazione standard solo dal training. Poi trasforma
# sia il training sia il test con quegli stessi valori, senza far trapelare
# informazioni dal test nell'addestramento.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crea l'albero decisionale: durante l'addestramento impara regole basate sulle
# misure dei fiori per distinguere le tre specie.
#
# Anche qui random_state=42 rende ripetibile l'eventuale casualità interna
# dell'algoritmo. Gli altri parametri restano ai valori predefiniti.
modello = DecisionTreeClassifier(random_state=42)

# Mostra al modello le misure e le specie corrette del gruppo di training.
modello.fit(X_train_scaled, y_train)

# Chiede al modello di prevedere la specie dei 45 fiori del gruppo di test.
# y_test non viene usato per fare le previsioni: serve dopo per controllarle.
y_pred = modello.predict(X_test_scaled)

# Confronta le previsioni (y_pred) con le specie reali (y_test).
# Il report calcola precision, recall e F1-score per ogni specie:
# precision = correttezza tra i fiori assegnati a una specie;
# recall = quanti fiori reali di quella specie sono stati riconosciuti;
# F1-score = equilibrio tra precision e recall.
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# La matrice confronta specie reali e specie previste:
# righe = specie reali; colonne = specie previste.
# La diagonale (dall'alto a sinistra al basso a destra) contiene le previsioni
# corrette. I numeri fuori dalla diagonale mostrano quali specie sono state confuse.
#
# Lettura del risultato osservato in questa esecuzione:
# - riga setosa: 15 fiori setosa riconosciuti correttamente;
# - riga versicolor: 12 riconosciuti correttamente e 3 classificati come virginica;
# - riga virginica: 14 riconosciuti correttamente e 1 classificato come versicolor.
# La somma di tutte le celle è 45: è il totale dei fiori nel gruppo di test.
# In tutto, il modello ha classificato correttamente 41 fiori su 45.
# Questi conteggi dipendono dalla divisione e dai parametri usati.
ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    display_labels=iris.target_names,
    cmap="Blues",
    values_format="d",
)
plt.title("Matrice di confusione - Iris")
plt.tight_layout()
plt.show()
