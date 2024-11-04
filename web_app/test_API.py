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
    
# @app.get("/Persos/{var}")
# async def test_func(var: str = '', age: int = 0):
#     return {"Personnage": var, "Age": age}

@app.get("/")
async def welcome():
    return "WELCOME TO MY ML PROJECT MOTHERFUCK !!!!!!"

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    # data = json.loads(body)
    name = data.get("name")
    age = data.get("age")
    message =  f"Sobriquet: {name}\nLife: {age}"
    return PlainTextResponse(message)

# @app.post("/predict")


# if __name__ == "__main__":
#     uvicorn.run(app)