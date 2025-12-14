import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
from pathlib import Path

# Sample dataset
data = {
    "feature_1": [10, 20, 30, 40, 50, 60],
    "feature_2": [1, 2, 3, 4, 5, 6],
    "label": [0, 0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["feature_1", "feature_2"]]
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

MODEL_PATH = Path("model/trained_model.pkl")
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully")
