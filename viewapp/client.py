import requests
import json

def get_token():
    url ="http://192.168.0.41:3000/api/users/login/"
    response = requests.post(url, data={ "email" : "admin@example.com", "password": "1234"})

 
    return response.json()



def get_data():
    url = "http://192.168.0.41:3000/api/sliders/all"
    header = {'Authorization':f'Token{get_token()}'}
    response = requests.get(url,headers=header)
    emp_data = response.json()
    for e in emp_data:
        print(e)
