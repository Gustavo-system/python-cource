from fastapi import FastAPI, Query, Path
from pydantic import BaseModel


class Profile(BaseModel):
    name: str
    email: str
    age: int
    

class User(BaseModel):
    used_id: int
    user_name: str
    password: str


app = FastAPI()


@app.get(path="/")
def index():
    """Check server started"""
    return {"Server", "UP"}


@app.get(path="/property/{id}")
def with_property(id):
    """First endpoint with parameter in path"""
    return {"Your select id": id}


@app.get(path="/typing_property/{number}")
def with_typing_property(number:int):
    """Typing parameter in path"""
    return {"property with type number": number}


# Query params
# http://localhost:8000/query_parms?kay=valor&key=valor

# example
# http://localhost:8000/query_parms?name=demo&edad=20
@app.get(path="/query_params")
def with_quiery_params(name, edad):
    """Query params in path"""
    return { "With query params": {"name" : name, "edad": edad } }


@app.get(path="/query_params_default_value")
def with_quiery_params_default_value(name:str="prueba", edad:int=25):
    """Query params in path"""
    return { "With query params": {"name" : name, "edad": edad } }


# using Path and Query by fastapi
@app.get(path="/params/{user_id}/coments")
def params(user_id:str = Path(...), coment_id:str = Query(...)):
    """Using Path of fastapi"""
    return { "user id": user_id, "coment id" : coment_id }


@app.post(path="/profile")
def new_profile(user: User, profile: Profile):
    """Pydantic Models in request body"""
    return { "data": { "user": user, "profile": profile} }
