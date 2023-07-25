"""Permiten modificar el comportamiento de una funcion"""

def decorador_time_ejecutor(any_function):
    def funcion_decorada(*args, **kwargs):
        print("***** MI DECORADOR *****")
    return funcion_decorada


@decorador_time_ejecutor
def funcion_comun():
    print("mi funcion comun")


funcion_comun()