from flask import Flask
import pickle
import json
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sklearn
locations=None
model=None
artifacts_column=None
def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=artifacts_column.index(location.lower())
    except:
        loc_index=-1
    x =np.zeros(len(artifacts_column))
    x[0]=sqft
    x[1]=bhk
    x[2]=bath
    if loc_index>=0:
        x[loc_index]=1
    return round(model.predict([x])[0],2) 
def get_location_names():
     return locations
def load_artifacts():
    print("Artifacts start loaded")
    global locations
    global model
    global artifacts_column
    with open("C:/Users/sarvesh/OneDrive/Desktop/machine learning/ML AND DEEP LEARNING/Real_estate_project/server/Artifacts/real_estate_column.json",'r') as f:
       global artifacts_column
       artifacts_column=json.load(f)['column_name']
       global locations
       locations=artifacts_column[3:]
    print("columns loaded successfully")
    with open("C:/Users/sarvesh/OneDrive/Desktop/machine learning/ML AND DEEP LEARNING/Real_estate_project/server/Artifacts/real_estate_model.pickle",'rb') as f:
        model=pickle.load(f)
    print("model loaded successfully")

if __name__=='__main__':
    load_artifacts()
    get_location_names()
    print(get_estimated_price('1st phase jp nagar',2000,4,4))