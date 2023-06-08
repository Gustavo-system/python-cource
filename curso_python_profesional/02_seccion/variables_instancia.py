class Persona():
	def __init__(self, nombre, nacionalidad) -> None: # se define un contructor
		self.nombre = nombre
		self.nacionalidad = nacionalidad


# esta es una variable de instancia
persona = Persona("Chanchito", "Autraliano")
print(persona)
print(persona.nombre) # se accede a la variable de instancia
