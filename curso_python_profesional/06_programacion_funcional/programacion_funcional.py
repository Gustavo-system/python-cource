"""Programacion funcional"""

def arrow_function(elementos): return elementos.lower()

lista_nombres = ["MARIA", "PEPE", "CHURRUMINO"]

print(list(map(arrow_function, lista_nombres)))

# otra manera de hacerlo
print([nombre.lower() for nombre in lista_nombres])