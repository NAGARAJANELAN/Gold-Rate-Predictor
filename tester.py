
import json
import requests


url = 'http://127.0.0.1:8000/gold_rate_prediction'

input_data_for_model = {
    
    'SPX' : 764.900024,
    'USO' : 26,
    'SLV' : 13.49,
    'EURUSD' : 1.272426
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)


print(response.text)