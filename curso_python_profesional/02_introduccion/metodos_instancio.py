class Persona():

	nacionalidad: str = "Mexicana"

	def __init__(self, nombre:str, edad:int) -> None:
		self.nombre = nombre
		self.edad = edad

	# metodo de instancia
	def informacion_personal(self) -> None: # se declara un metodo de instancia con la palabra self
		print(f"Hola me llamo {self.nombre} y tengo {self.edad}")


persona = Persona("Chanchito", 23)
persona.informacion_personal()
