import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data = {
    "edad": [5, 12, 17, 18, 25, 30, 40],
    "categoria": ["niño", "niño", "adolescente", "adulto", "adulto", "adulto", "adulto"]
}

df = pd.DataFrame(data)

X = df[["edad"]]
y = df["categoria"]

modelo = DecisionTreeClassifier()
modelo.fit(X, y)

joblib.dump(modelo, "model.pkl")

print("Modelo entrenado y guardado")