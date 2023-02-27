from fastapi import APIRouter, Body

from services import products, login
from models import user

# declaramos las rutas y le agregamos un context path.
router = APIRouter(prefix="/fastapi/v1/api") 


# declaramos todas la rutas de nuestra api
@router.get(path="/", status_code=200)
async def server_start():
    return "My first api with FastApi"


@router.post(path="/login", status_code=200)
async def login(user:user.User = Body(...)):
    return login.login(user)


@router.get(path="/products", status_code=200, tags=["products"])
async def get_products():
    return products.get()