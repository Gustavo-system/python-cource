
products_list = ["producto 1", "producto 2", "producto 3", "producto 4"]


# desarrollamos la logica que se requiere en el api
def get() -> list or Exception:
    try:
        return products_list
    except Exception as ex:
        print(ex)
        return ex


def post() -> bool:
    try:
        return True
    except Exception as ex:
        print(ex)
        return ex