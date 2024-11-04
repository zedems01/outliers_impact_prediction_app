from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# from fastapi.responses import PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# model = pickle.load(open("../data/regmodel.pkl", 'rb'))
# scaler = pickle.load(open('../data/stdscaler.pkl', 'rb'))
with open('../data/CatBoostRegressor.pkl', 'rb') as f:
    best_model = pickle.load(f)

templates = Jinja2Templates(directory="templates")

# Road to the form
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Defining the type of inputs
class ModelFeatures(BaseModel):
    MedInc: float  
    HouseAge: float  
    AveRooms: float  
    AveBedrms: float  
    Population: float  
    AveOccup: float  
    Latitude: float  
    Longitude: float 

# Getting inputs and making predictions
@app.post("/predict")
async def predict(features: ModelFeatures):
    data = [ features.MedInc, features.HouseAge, features.AveRooms, features.AveBedrms,
             features.Population, features.AveOccup, features.Latitude, features.Longitude
            ]
    columns = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    input_data = pd.DataFrame([data], columns=columns)
    
    # scaled_data = scaler.transform(input_data)
    prediction = best_model.predict(input_data)
    return {"prediction": prediction[0]}