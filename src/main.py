from fastapi import FastAPI
from src.api.endpoints import router
from src.utils.logger import setup_logger

app = FastAPI()
setup_logger()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Real-Time Adaptive Fraud Detection System"}