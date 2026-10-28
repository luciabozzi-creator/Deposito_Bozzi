"""
Keras Esercizio: Classificazione di Cifre Scritte a Mano con Keras
￼
In questo esercizio, costruiremo e addestreremo un semplice
modello di rete neurale utilizzando Keras per classificare le
cifre scritte a mano del dataset MNIST.
Questo dataset contiene immagini in scala di grigi di cifre da 0
a 9, dimensionate a 28x28 pixel.
Obiettivi:
- Caricare e preprocessare il dataset MNIST.
- Costruire un modello sequenziale con strati densi.
- Compilare il modello specificando ottimizzatore, funzione di
perdita e metriche.
- Addestrare il modello sui dati di addestramento.
- Valutare le prestazioni del modello sui dati di test.
- Utilizzare il modello per fare predizioni su nuove immagini.

"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical


# 1. Caricamento e preprocessing del dataset MNIST.
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Visualizza un esempio come indicato nel manuale.
plt.imshow(X_train[0], cmap="gray")
plt.title(f"Etichetta: {y_train[0]}")
plt.show()

# Normalizza i pixel e appiattisce ciascuna immagine 28x28 in 784 valori.
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0
X_train = X_train.reshape(-1, 28 * 28)
X_test = X_test.reshape(-1, 28 * 28)

# Converte le etichette in vettori one-hot per la classificazione multiclasse.
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# 2. Costruzione del modello sequenziale
model = Sequential()
model.add(Dense(units=128, activation="relu", input_shape=(784,)))
model.add(Dense(units=64, activation="relu"))
model.add(Dense(units=10, activation="softmax"))

# 3. Compilazione del modello.
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

# 4. Addestramento del modello.
history = model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.1,
)

# 5. Valutazione sui dati di test.
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Perdita sul test set: {test_loss:.4f}")
print(f"Accuratezza sul test set: {test_accuracy:.4f}")

# 6. Visualizzazione dell'accuratezza e della perdita.
plt.plot(history.history["accuracy"], label="Accuratezza Training")
plt.plot(history.history["val_accuracy"], label="Accuratezza Validazione")
plt.xlabel("Epoca")
plt.ylabel("Accuratezza")
plt.legend()
plt.title("Andamento dell'Accuratezza")
plt.show()

plt.plot(history.history["loss"], label="Perdita Training")
plt.plot(history.history["val_loss"], label="Perdita Validazione")
plt.xlabel("Epoca")
plt.ylabel("Perdita")
plt.legend()
plt.title("Andamento della Perdita")
plt.show()

# 7. Predizioni e confronto con le classi vere.
predictions = model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)
true_classes = np.argmax(y_test, axis=1)

# Matrice di confusione.
conf_matrix = confusion_matrix(true_classes, predicted_classes)
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues")
plt.title("Matrice di Confusione")
plt.xlabel("Classe Predetta")
plt.ylabel("Classe Vera")
plt.show()

# Report con precisione, richiamo e F1-score.
report = classification_report(true_classes, predicted_classes)
print("Report di Classificazione:")
print(report)

# Visualizza cinque predizioni casuali con etichetta vera e predetta.
num_images = 5
random_indices = np.random.choice(len(X_test), num_images)
plt.figure(figsize=(15, 3))
for i, idx in enumerate(random_indices):
    image = X_test[idx].reshape(28, 28)
    true_label = true_classes[idx]
    predicted_label = predicted_classes[idx]

    plt.subplot(1, num_images, i + 1)
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.title(f"T:{true_label}, P:{predicted_label}")
plt.show()
