import os

class Config:
    MODEL_PATH = os.getenv("MODEL_PATH", "models/fraud_model.pkl")
    DATA_PATH = os.getenv("DATA_PATH", "data/transactions.csv")