"""
En el loop for se itera cada posicion de la lista para obtener el valor.

sintaxis:

para elemento en elementos:
	imprime(elemento)

"""

lista_letras = ['a', 'b', 'c']


for letra in lista_letras:
    print(f"Letra -> {letra}")
    

for letra in lista_letras:
    indice_letra = lista_letras.index(letra) + 1
    print(f"Letra numero {indice_letra} es {letra}")
    

lista_nombres = ['Chanchito feliz', 'Chanchito triste', 'Guacamaya', 'Loro', 'Caballito']


for nombre in lista_nombres:
    if nombre.lower().startswith('c'):
        print(nombre)


palabra = "python "


for letra in palabra:
    print(letra)


for letra in "python":
    print(letra)


diccionario = {"saludar" : "Hola", "despedida": "adios"}

# iterar diccionarios
for llave, valor in diccionario.items():
    print(f"llave = {llave} : valor = {valor}")


"""
Loop while se itera cada una de las posiciones hasta que se cumpla una condición

sintaxis:
while condicion:
	codigo

"""
