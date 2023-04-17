"""
Se utiliza para cambinar dos o mas listas.
"""

nombres = ["Chanchito", "Chanchita", "Pinguino"]
edades = [20, 25, 40]

# esto solo imprime la referencia de memoria la que fue asignada, se requiere convertir a una lista
# combinados = zip(nombres, edades)
combinados = list(zip(nombres, edades))
print(combinados)

# ejemplo 2

ciudades = ["Mexico", "Pachuca", "Guerrero"]

combinados = list(zip(nombres, edades, combinados))

print("Tres listas unidad", combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene la edad de {edad} y vive en {ciudad}")
