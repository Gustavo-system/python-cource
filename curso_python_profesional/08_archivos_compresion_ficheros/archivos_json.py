import json

PATH_FILE = '/Users/gsolar/learning_new/python-curso/curso_python_profesional/08_archivos_compresion_ficheros/json.txt'


with open(PATH_FILE, 'r') as file:
    data = json.load(file)

print(f"data: {data}")

# acceder a los valores del json
print(f"data del cliente 1: {data.get('cliente1')}")