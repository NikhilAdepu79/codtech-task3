# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI(title="Iris Classifier API")

# Load trained model
model = joblib.load("model.pkl")

# Request schema
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API 🚀"}

@app.post("/predict")
def predict(data: IrisData):
    input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(input_data)[0]
    return {"prediction": int(prediction)}
