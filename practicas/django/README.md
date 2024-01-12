# Primeros pasos en Django

### Crear un entorno virtual
```
python3 -m venv <name_env>
```

### activar el entorno virtual
```
python3 source <name_env>/bin/activate

# (name_env) <ruta_folder>
```


### instalar dependencias en el proyecto
- nota: usar el gestor de paquetes de su preferencia
```
pipenv install <paquete>
```


### crear un proyecto de django
```
django-admin startproject <name_proyect>
```

### crear una applicacion del proyecto
```
python3 manage.py startapp <name_proyect>
```

### correr un servidor local de django
```
python3 manage.py runserver
```

### crear migraciones
```
python3 manage.py makemigrations <name_migration>
```

### ejcutar migraciones
```
python3 manage.py migrate
```

### crear un super usuario
```
python3 manage.py createsuperuser
python3 manage.py createsuperuser --username admin --email admin@example.com
```