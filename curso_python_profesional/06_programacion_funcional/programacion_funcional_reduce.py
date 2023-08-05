from functools import reduce

numeros_tupla = (1,2,3,4,5)

def sumar(x:int, y:int) -> int : return x + y


suma = reduce(sumar, numeros_tupla)
print(f"resultado de la suma : {suma}")
