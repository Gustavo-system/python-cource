from schemas.user import User


def login(user:User):
    try:
        result = user
        print(result)
        numero = 10 / 0
    except Exception as ex:
        print(f"Algo a ocurrido al intentar hacer login {ex}")
        return ex