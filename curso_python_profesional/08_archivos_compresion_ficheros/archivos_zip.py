import zipfile
from zipfile import ZipFile


PATH_FILE = '/Users/gsolar/learning_new/python-curso/curso_python_profesional/08_archivos_compresion_ficheros/demo.zip'
PATH_FILE_JSON = '/Users/gsolar/learning_new/python-curso/curso_python_profesional/08_archivos_compresion_ficheros/json.txt'


"""
los parametos que se le pasan a la funcion ZipFile son 
1. el nombre del fichero
2. el modo en que se abre el archivo
"""
with zipfile.ZipFile(PATH_FILE, 'w') as fileZip:
    fileZip.write(PATH_FILE_JSON)
    fileZip.printdir()
    fileZip.extractall() # extrae todo lo que contenga el archivo .zip
    