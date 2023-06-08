class Vehiculo():
    
	def __init__(self, nombre, paginas, autor) -> None:
		self.nombre = nombre
		self.paginas = paginas
		self.autor = autor

	def describir(self):
		print(f"Nuevo libro {self.nombre} - con paginas {self.paginas} - autor {self.autor}")


	# es un metodo que se usa para que no se imprima el espacio en memoria y se  imprima su contenido
	def __str__(self) -> str:
		return f"Nuevo libro {self.nombre} - paginas {self.paginas} - autor {self.autor}"
	

	# es un metodo para describir la longitude de los atributos de la clase
	def __len__(self):
		return self.paginas

	
	# es un metodo para mostrar algo despues de eliminar una instancia
	def __del__(self):
		print("Se elimino la instancia")
	

vehiculo = Vehiculo("Curso de python profesional", 200, "El pollo loco")
print(vehiculo)
print(len(vehiculo))

del vehiculo
