from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel


app = FastAPI()


# declaracion de modelo
class User(BaseModel):
    id:int
    name:str
    last_name:str
    age:int


# usuarios dummy
users_list = [
    User(id=1, name="tunas", last_name="panfilo", age=20),
    User(id=2, name="luna", last_name="luz", age=23),
    User(id=3, name="guacamaio", last_name="feliz", age=40)
]


# declaracion de rutas
@app.get("/users")
async def get_users():
    return users_list


@app.get("/user/{user_id}")
async def get_user(user_id:int):
    # user = list(filter(lambda user:user.id == user_id, users_list))
    # print(type(user))
    # return user
    return searh_user(user_id=user_id)


@app.get(path="/user", status_code=201)
async def post_user(user:User = Body(...)):
    if type(searh_user(user.id)) == User:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    users_list.append(user)
    return {"Menssage": "Usuario creado exitosamente", "User" : user}


# funcion para buscar un usuario
def searh_user(user_id:int):
    user = list(filter(lambda user:user.id == user_id, users_list))
    try:
        return list(user)[0]
    except Exception as ex:
        return {"Error" : "No se encontro el usuario", "Value": f"{ex}"}