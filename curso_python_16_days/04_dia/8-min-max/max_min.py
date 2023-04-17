"""
Se utliza para conocer el minimo y el mayor de una serie de datos
"""

lista = [1,2,3,4,5,6,7,8,910]

print(f"El numero menor es {min(lista)} el mayor es {max(lista)}")


"""
Tambien se puede utilizar con palabras
"""

nombres = ["chanchito", "puerquito", "pinguino", "cangre"]

print(f"El primer nombre es: {min(nombres)} el ultimo nombre es: {max(nombres)}")

# hace el orden buscando primero por letras mayusculas y despues minusculas
print(f"De la palabre {nombres[0]} la primer letra segun el oriden alfavtico es {min(nombres[0])}")


# cuando se busca en un diccionario si no se especifica nada busca por llave por default
diccionario = {'c1': 45, 'c2': 15}
print(min(diccionario))
# si accedemos a los valores nos regresa el minimo o mayor segun lo pedido
print(min(diccionario.values()))
