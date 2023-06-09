from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    SPX : float
    USO : float
    SLV : float
    EURUSD : float

# loading the saved model
gold_predictor_model = pickle.load(open('gold_rate_predictor.sav', 'rb'))

@app.get("/")
def root():
    return 'API RUNNING...'

@app.post('/gold_rate_prediction')
def gold_prediction(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    spx = input_dictionary['SPX']
    uso = input_dictionary['USO']
    slv = input_dictionary['SLV']
    eurusd = input_dictionary['EURUSD']
    
    
    input_list = [spx,uso,slv,eurusd]
    
    prediction = gold_predictor_model.predict([input_list])
    # return 'ok'
    
    return prediction[0]