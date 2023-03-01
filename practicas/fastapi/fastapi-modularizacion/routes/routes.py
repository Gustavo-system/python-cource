from fastapi import APIRouter, HTTPException,Body

from services import login, products
from utils.responses_utils import ( general_response_success, general_response_error_500, general_response_select )
from schemas import user

# declaramos las rutas y le agregamos un context path.
router = APIRouter(prefix="/fastapi/v1/api") 


# declaramos todas la rutas de nuestra api
@router.get(path="/", status_code=200)
async def server_start():
    return "My first api with FastApi"


@router.post(path="/login", status_code=200, tags=["login"])
async def loginn(user:user.User = Body(...)):
    if isinstance(login.login(user), Exception):
        raise HTTPException(status_code=500, detail=general_response_error_500())
    return general_response_success(200, "Login exitoso")


@router.get(path="/products", status_code=200, tags=["products"])
async def get_products():
    if isinstance(products.get(), Exception):
        raise HTTPException(status_code=500, detail=general_response_error_500())
    return general_response_select("products", products.get())