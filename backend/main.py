from fastapi import FastAPI
from pathlib import Path
import pickle
import numpy as np
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Linear Regression Model API")
import os
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ci-cd-pipeline-1-paam.onrender.com"],  # Or ["https://ci-cd-pipeline-1-paam.onrender.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    raise RuntimeError(f"Failed to load model from {MODEL_PATH}: {e}")
    


# Input schema
class InputData(BaseModel):
    area: float
    bedrooms: int

@app.get("/")
def health_check():
    return {"status": "API is running"}


# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    X = np.array([[data.area, data.bedrooms]])
    prediction = model.predict(X)[0]
    return {"predicted_price": float(prediction)}