from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import uvicorn
import pandas as pd
import pickle
from pydantic import BaseModel
import json

app = FastAPI()

model = pickle.load(open("../data/regmodel.pkl", 'rb'))
scaler = pickle.load(open('../data/stdscaler.pkl', 'rb'))

class Features(BaseModel):
    MedInc: float
    HouseAge: int | float
    AveRooms: float
    AveBedrms: float
    Population: int | float
    AveOccup: float
    Latitude: float
    Longitude: float
    
@app.get("/")
async def welcome():
    return "WELCOME TO MY ML PROJECT MOTHERFUCK !!!!!!"

@app.post("/predict")
async def predict(data: Features):
    data = pd.json_normalize(data.model_dump(mode='python'))
    # data = pd.DataFrame(data.model_dump(mode='python'))
    scaled_data = scaler.transform(data)
    pred = model.predict(scaled_data)
    output = f"Median House Price Prediction: {pred[0]}"
    return PlainTextResponse(output)
# @app.post("/predict")


# if __name__ == "__main__":
#     uvicorn.run(app)