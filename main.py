from pydantic.class_validators import make_generic_validator
import uvicorn
from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel

class Package(BaseModel):
    name : str
    number: str
    description: Optional[str] = None

app = FastAPI(debug = True)

@app.get('/')
def hello_world():
    return {"Hello" :"Vanakkam"}

@app.get('/component/{component_id}')  #path parameter
def get_component(component_id:int):
    return{"component_id":component_id}

@app.get('/component/')                 # Query parameter
def read_component(number: int, text:str):
    return{"number": number, "text": text}

@app.post('/package/{priority}')
def make_package(priority : int , package:Package, value:bool):
    return {"priority":priority, **package.dict(), "value":value}


