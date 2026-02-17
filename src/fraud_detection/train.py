import pandas as pd
from src.fraud_detection.model import FraudDetectionModel
from src.fraud_detection.preprocess import preprocess_data

def train_model(data_path, model_path):
    data = pd.read_csv(data_path)
    X = data.drop(columns=['is_fraud'])
    y = data['is_fraud']

    X_preprocessed = preprocess_data(X)

    model = FraudDetectionModel()
    model.train(X_preprocessed, y)
    model.save_model(model_path)

if __name__ == "__main__":
    train_model("data/transactions.csv", "models/fraud_model.pkl")