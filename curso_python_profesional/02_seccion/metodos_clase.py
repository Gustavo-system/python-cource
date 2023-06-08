class Persona():

	def __init__(self) -> None:
		pass
	
	def saludo() -> None:
		print("Estoy saludando - metodo de clase")

	@classmethod
	def despedida(cls, valor) -> None:
		print(f"Despedida - con paremetro y decorador \nvalor : {valor} \ndecorador : @classmethod")


Persona.saludo()
Persona.despedida(300)
