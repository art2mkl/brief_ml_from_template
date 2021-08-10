
#basic
from fastapi import FastAPI
import pandas as pd
import numpy as np
import json

from fastapi.middleware.cors import CORSMiddleware


#Basics
import seaborn as sns

#System
import sys

#imports models
from sklearn.ensemble import RandomForestClassifier

#Classes
from ml_pinguins_pkg.pinguins_ml import Pinguins_ml
from ml_pinguins_pkg.pinguins_viz import Pinguins_viz
from ml_pinguins_pkg.pinguins_model import Pinguins_model

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#creation du model
df = sns.load_dataset('penguins')
model = Pinguins_model(df,'species')
model.prepare_model(RandomForestClassifier())



@app.get('/')
async def root():
    return 'api is ready'

@app.get('/df')
async def data():
    return json.loads(df.to_json())
    

@app.get('/prediction')

async def prediction(island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex):
    					
    quest = pd.DataFrame({
        'species': "query",
        'island': [str(island)],
        'bill_length_mm': [float(bill_length_mm)],
        'bill_depth_mm': [float(bill_depth_mm)],
        'flipper_length_mm': [float(flipper_length_mm)],
        'body_mass_g': [float(body_mass_g)],
        'sex': [str(sex)]                         
    })

    model.transform_null(quest)
    pred = model.predict_model(model.model, model.X)[0]
    return [pred]

@app.get('/save')

async def save():
    model.save_model(model.model, 'pinguins.joblib')
    return None

@app.get('/predict_after_load')

async def predict_after_load(island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex):
    model.model = model.load_model('pinguins.joblib')
    
    quest = pd.DataFrame({
        'species': "query",
        'island': [str(island)],
        'bill_length_mm': [float(bill_length_mm)],
        'bill_depth_mm': [float(bill_depth_mm)],
        'flipper_length_mm': [float(flipper_length_mm)],
        'body_mass_g': [float(body_mass_g)],
        'sex': [str(sex)]                         
    })

    model.transform_null(quest)
    pred = model.predict_model(model.model, model.X)[0]
    return [pred]




