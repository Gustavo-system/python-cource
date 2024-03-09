# Entornos Virtuales con PIPENV

La ventaja de utilizar pipenv es que todo el enviroment queda guardado en la carpeta del proyecto y no a niver general como otros entornos.


### instalar PIPENV
comprobamos nuestra version de python y comprobamos que se tenga python de forma global

```
- Windows
python --version
pip install pipenv

- Mac
python3 --version
pip3 install pipenv
```


### conceptos basicos de pipenv

- conocer los comandos por terminal disponibles de pipenv

	```
	pipenv --help
	```

- crear un entorno virtual

	1. debemos estar en nuestro workspace y comprobar la version de python que tenemos en nuestro equipo ya que se creara el entorno virtual con esa version.

	```
	pipenv --python <version>

	ejemplo:
	pipenv --python 3.10
	```

- eliminar un entorno virutal
	```
	pipenv --rm
	```

- activar el entorno virtual
	```
	pipenv shell
	```

- activar el interprete del python en el entorno virtual
	```
	pipenv run python
	```

- instalar un paquete en el entorno virtual

	1- si no se ha creado un entorno virtual el siguente comando antes de instalar el paquete lo creara

	```
	pipenv install <nombre_paquete>
	```

	2- instalar todos los paquets
	```
	pipenv install
	```

- desinstalar un paquete del entorno virtual
	```
	pipenv uninstall <nombre_paquete>
	```

- saber los paquetes instalados en el entorno virutal
	```
	pipenv graph
	```

- saber el path de nuestro entorno virual
	```
	pipenv --venv
	```

- saber la ruta del python instalado en entorno virtual
	```
	pipenv --py
	```
