from fastapi import FastAPI
from routes import routes


server = FastAPI()

# Incluir las rutas desde otro archivo
server.include_router(routes.router)