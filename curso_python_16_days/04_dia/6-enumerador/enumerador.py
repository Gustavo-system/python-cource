"""
Se utiliza para acceder al indice - posicion de una lista
"""
numeros_lista = ['a','b','c','d','e','f','g']
indice = 0

# esta forma para obtener el indice si bien lo hace, no es la forma adecuada
for numero in numeros_lista:
    print(f"indice {indice} - valor {numero}")
    indice += 1


# se obtiene con el unumerador, es mas sintetico y mas eficiente
for index, item in enumerate(numeros_lista):
    print(f"indice {indice} - valor {numero}")


# ejemplo
for index, item in enumerate(range(50, 56)):
    print(f"indice {indice} - valor {numero}")


# se puede usar para hacer casting a una tupple
numeros_tupla = enumerate(numeros_lista)
print(numeros_tupla)
