from fastapi import APIRouter
from pydantic import BaseModel
from src.fraud_detection.model import FraudDetectionModel
from src.fraud_detection.preprocess import preprocess_data
import pandas as pd

router = APIRouter()

model = FraudDetectionModel()
model.load_model("models/fraud_model.pkl")

class Transaction(BaseModel):
    transaction_data: dict

@router.post("/predict")
def predict(transaction: Transaction):
    data = pd.DataFrame([transaction.transaction_data])
    preprocessed_data = preprocess_data(data)
    prediction = model.predict(preprocessed_data)
    return {"is_fraud": bool(prediction[0])}