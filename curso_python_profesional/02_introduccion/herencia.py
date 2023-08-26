class Personal():
	def __init__(self, sueldo:int, antiguedad:int, especialidad:str) -> None:
		self.sueldo = sueldo
		self.antiguedad = antiguedad
		self.especialidad = especialidad
	
	def sueldos(self):
		if str(self.especialidad).lower() == 'ingeniero':
			return self.antiguedad * self.sueldo
		return self.antiguedad * self.sueldo
		

class Supervisor(Personal):
	def __init__(self, sueldo, antiguedad, especialidad) -> None:
		super().__init__(sueldo, antiguedad, especialidad)
	

class Colaborador(Personal):
	def __init__(self, sueldo, antiguedad, especialidad) -> None:
		super().__init__(sueldo, antiguedad, especialidad)


if __name__ == '__main__':
	supervisor = Supervisor(100, 5, 'ingeniero')
	sueldo = supervisor.sueldos()
	print(f'El suedo del {supervisor.especialidad} es de {sueldo}')