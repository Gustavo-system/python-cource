class Circulo:
	"""
	Se declaran las properties
    como si fuera una variable de instancia
    """


	def __init__(self, radio) -> None:
		self.radio = radio


	@property
	def area(self):
		return 1.99 * (self.radio ** 2)
	

circulo = Circulo(20)
print(circulo.area)