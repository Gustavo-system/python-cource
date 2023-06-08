class Persona():

	def __init__(self) -> None:
		pass
	
	def saludo(self) -> None:
		print("Estoy saludando - con metodo de instancia")


	@classmethod
	def despedida(cls) -> None:
		print(f"Despedida - con metodo de clase")


	@staticmethod # se agrega este docorador para saber que es un metodo estatico
	def accion() -> None: # se declara un metodo estatico
		print("estoy haciendo algo - metodo estatico")


Persona.accion() # se llama al metodo estaticos
