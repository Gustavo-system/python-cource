# imports del core de python
from typing import Optional

# imports de librerias externas
from pydantic import BaseModel


# import de fastApi
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

# Definicion de modelos
class Persona(BaseModel):
    nombre: str
    apellido: str
    edad: int
    casado: Optional[bool]


@app.get('/')
async def home():
    return {"saludo" : "Hello word"}
    # agregamos la siguente linea en la terminal de comandos para levantar el servidor
    # uvicorn <nombre_archivo> : <objeto_app> --reload


@app.get('/saludo/{nombre}') # en este caso siempre se solicita de forma oblugatoria la variable por path
async def saludo(nombre:str):
    return {"saludo" : (f'Hola {nombre}')}
    # /saludo/gustavo


@app.get('/despedida/{nombre}') # se sigue solicitando un parametro obligatorio
async def despedida(nombre:str, apellido: str = "", edad: int = 0): # en este caso las querys son opcionales
    return {"saludo" : (f'Hola {nombre} {apellido} tiene {edad}')}
    # /despedida/gustavo?apellido=feliz&edad=24


# Request and Response Body
@app.post('/persona')
async def create_persona(persona: Persona = Body(...)): # recibe en el body un objeto de tipo persona, con los tres puntos es obligatorio
    return persona
    # /despedida/gustavo?apellido=feliz&edad=24


# validaciones: Query Parameters
@app.get('/validando/query')
async def validaciones(
        nombre:Optional[str] = Query(None, min_length=1, max_length=10), 
        edad:Optional[int] = Query(...) # lo mejor es que los querys parameters no son obligatorios, esto es un ejemplo de lo que no se debe hacer
    ):
    return {"validacion": {nombre : edad}}


"""
Cuando utilizamos strings tenemos:
max_length
min_length
regex

Cuando validamos números:
Ge = greater or equal than >=
le = less or equal than <=
ge = Greater than >
le = less than <
"""

# validaciones: Path Parameters
@app.get('/validando/paths/{persona_id}')
async def validaciones_path(
        persona_id:int = Path(..., ge=0) # este parametro es obligatorio y se agrega una validacion
    ):
    return {"validacion_path": persona_id}