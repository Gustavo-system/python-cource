class Intro():
    
	def __init__(self, valor) -> None:
		self.valor = valor

	def segundo(self):
		print("segundo")

	def tercero(self):
		print("tercero")


dato = Intro("valor")

print(isinstance(dato, Intro)) # validamos la instancia de un objeto

print(hasattr(dato, 'perro')) # nos devuelve si existe ese calor en la instacia del objeto
