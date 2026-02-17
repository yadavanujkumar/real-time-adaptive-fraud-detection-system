import pickle
from sklearn.ensemble import RandomForestClassifier

class FraudDetectionModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save_model(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)

    def load_model(self, path):
        with open(path, 'rb') as f:
            self.model = pickle.load(f)