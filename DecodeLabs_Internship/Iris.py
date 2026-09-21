from sklearn.datasets import load_iris
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, confusion_matrix,
    classification_report, precision_score,
    recall_score, f1_score
)


iris = load_iris()

X = iris.data          # the 4 features: sepal length, sepal width, petal length, petal width
y = iris.target        # the labels: 0=Setosa, 1=Versicolor, 2=Virginica

df = pd.DataFrame(X, columns=iris.feature_names)
df['species'] = [iris.target_names[i] for i in y]
print(df.head())
print(df['species'].value_counts())

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y,
    test_size=0.2,      # 80% train, 20% test
    random_state=42,    # makes the "random" shuffle repeatable
    stratify=y          # keeps class proportions equal in both sets
)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

predictions = model.predict(X_test)


# 1. Accuracy — the raw headline number
acc = accuracy_score(y_test, predictions)
print(f"Accuracy: {acc:.2%}")

# 2. Confusion Matrix — where exactly did it go wrong?
cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(cm)

# 3. Full report — precision, recall, F1 per class
print(classification_report(y_test, predictions, target_names=iris.target_names))