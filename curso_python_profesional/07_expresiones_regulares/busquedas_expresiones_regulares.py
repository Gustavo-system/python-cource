import re


# buscar un caracter en una cadena
print(re.search(r'z', 'Taza'))


# buscar numeros definidos en una cadena
# por medio de las \d se indica la cantidad de numeros a buscar
print(re.search(r'\d\d\d', 'Taza123'))


# obtenemos el valor de la busqueda
mi_patron = re.compile(r'\d\d\d')
valor_encontrado = mi_patron.search('Taza456').group()
print(f"se obtiene solo el valor de la busqueda: {valor_encontrado}")