import pickle
import numpy as np
from pathlib import Path

MODEL_PATH = Path("model/trained_model.pkl")

class MLModel:
    def __init__(self):
        with open(MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, features: list):
        features_array = np.array(features).reshape(1, -1)
        prediction = self.model.predict(features_array)
        return int(prediction[0])

