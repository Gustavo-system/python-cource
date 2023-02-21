from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home():
    return {"saludo" : "Hello word"}
    # agregamos la siguente linea en la terminal de comandos para levantar el servidor
    # uvicorn <nombre_archivo> : <objeto_app> --reload