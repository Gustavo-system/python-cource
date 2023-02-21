from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home():
    return {"saludo" : "Hello word"}
    # agregamos la siguente linea en la terminal de comandos para levantar el servidor
    # uvicorn <nombre_archivo> : <objeto_app> --reload


@app.get('/saludo/{nombre}') # en este caso siempre se solicita de forma oblugatoria la variable por path
async def home(nombre:str):
    return {"saludo" : (f'Hola {nombre}')}
    # /saludo/gustavo


@app.get('/despedida/{nombre}') # se sigue solicitando un parametro obligatorio
async def home(nombre:str, apellido: str = "", edad: int = 0): # en este caso las querys son opcionales
    return {"saludo" : (f'Hola {nombre} {apellido} tiene {edad}')}
    # /despedida/gustavo?apellido=feliz&edad=24