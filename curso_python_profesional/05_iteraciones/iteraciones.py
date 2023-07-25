"""Iteraciones en python"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    numero *= 10
    print(f"numero {numero}")


# iterando sobre un fichero
for valor in open("/Users/gsolar/learning_new/python-curso/curso_python_profesional/05_iteraciones/docs.txt", "r"):
    print(f"numero en txt -> {valor}")