from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Carico il dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Divido i dati in training set e test set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Creo e addestra KNN con 5 vicini
KNN = KNeighborsClassifier(n_neighbors=5)
KNN.fit(X_train, y_train)

# Predico le specie del test set e calcola l'accuratezza
y_pred = KNN.predict(X_test)
accuratezza = accuracy_score(y_test, y_pred)

print(accuratezza)
