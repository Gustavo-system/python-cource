class Persona():

	edad = 23 # variables de clase

	def __init__(self, nombre, nacionalidad) -> None: # se define un contructor
		# se definen las variables de instancia
		self.nombre = nombre
		self.nacionalidad = nacionalidad


# esta es una variable de instancia
persona = Persona("Chanchito", "Autraliano")
print(persona.nombre) # se accede a la variable de instancia
print(Persona.edad) # se accede a la varable de clase
