from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get('/')
def hello_world():
    return {"Hello" :"Vanakkam"}

@app.get('/component/{component_id}')  #path parameter
def get_component(component_id:int):
    return{"component_id":component_id}

@app.get('/component/')                 # Query parameter
def read_component(number: int, text:str):
    return{"number": number, "text": text}
