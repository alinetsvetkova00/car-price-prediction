from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("car_price_model.pkl")

@app.get("/")
def root():
    return {"message": "API works"}

@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return {"price": float(prediction[0])}