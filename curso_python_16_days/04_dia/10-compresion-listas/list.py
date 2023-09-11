"""
Comprension de listas
"""

# forma tradicional de iterar
palabra = "python"

lista = []
for letra in palabra:
	lista.append(letra)

print(lista)


# se realiza con list comprehesions
lista = [letra for letra in palabra]
print(lista)


# se pueden agregar condiciones
lista = [numero for numero in range(0, 21) if numero % 2 == 0]
print(lista)

# si se agrega el else se cambia la estructura
lista = [numero if numero % 2 == 0 else 'no' for numero in range(0, 21)]
print(lista)