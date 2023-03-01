"""
Retorna una respuesta exitosa
"""
def general_response_success(status_code:int, message:str) -> dict:
    return {
        "status": status_code,
        "message": message,
        "success": True
    }


"""
Retorna una respuesta exitosa
"""
def general_response_select(name:str, data:dict or list) -> dict:
    return {
        "status": 200,
        "message": "datos obtenidos",
        "success": True,
        "data" : {name : data}
    }


"""
Retorna un error interno del servidor
"""
def general_response_error_500() -> dict:
    return {
        "status": 500,
        "message": "Problemas al procesar la solicitud",
        "success": False
    }