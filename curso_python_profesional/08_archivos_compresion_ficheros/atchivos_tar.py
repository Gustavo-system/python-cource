import tarfile


PATH_FILE = '/Users/gsolar/learning_new/python-curso/curso_python_profesional/08_archivos_compresion_ficheros/demo_gzio_tar.gz'
PATH_FILE_JSON = '/Users/gsolar/learning_new/python-curso/curso_python_profesional/08_archivos_compresion_ficheros/json.txt'

file_tar = tarfile.open(PATH_FILE, 'w:gz')
file_tar.add(PATH_FILE_JSON) # si el archivo no existe caera en una exception
file_tar.close()
