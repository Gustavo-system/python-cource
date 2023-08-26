import gzip


PATH_FILE = '/Users/gsolar/learning_new/python-curso/curso_python_profesional/08_archivos_compresion_ficheros/demo_gzio.gz'
PATH_FILE_JSON = '/Users/gsolar/learning_new/python-curso/curso_python_profesional/08_archivos_compresion_ficheros/json.txt'

with open(PATH_FILE_JSON, 'rb') as file:
    with gzip.open(PATH_FILE, 'wb') as ficheroGzip:
        ficheroGzip.writelines(file)