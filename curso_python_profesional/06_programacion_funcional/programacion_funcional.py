"""Programacion funcional"""

def arrow_function(elementos): return elementos.lower()

lista_nombres = ["MARIA", "PEPE", "CHURRUMINO"]

print(f"Arrow map : {list(map(arrow_function, lista_nombres))}")

# otra manera de hacerlo
print(f"Arrow in one line : {[nombre.lower() for nombre in lista_nombres]}")