# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 06:56:16 2023

@author: YOGIRAJ
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio

app=FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int
    
diabetes_model=pickle.load(open('C:\\Users\\YOGIRAJ\\OneDrive\\Desktop\\ML model-public API\\diabetes_model1.sav','rb'))

@app.post('/diabetes_prediction')
def diabetes_predd(input_parameters:model_input):
    input_data=input_parameters.json()
    input_dictionary=json.loads(input_data)
    
    preg=input_dictionary['Pregnancies']
    glus=input_dictionary['Glucose']
    bp=input_dictionary['BloodPressure']
    skin=input_dictionary['SkinThickness']
    insulin=input_dictionary['Insulin']
    bmi=input_dictionary['BMI']
    dpf=input_dictionary['DiabetesPedigreeFunction']
    age=input_dictionary['Age']
    
    input_list=[preg,glus,bp,skin,insulin,bmi,dpf,age]
    prediction=diabetes_model.predict([input_list])
    
    if (prediction[0]==0):
        return 'The Person is not Dibetic'
    else:
        return 'The person is Diabetic'