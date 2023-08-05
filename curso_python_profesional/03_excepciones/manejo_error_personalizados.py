class ExceptionPersonalizada(Exception):
    
	def __init__(self, message) -> None:
		self.message = message
		print(self.message)



try:
	raise TypeError
except Exception:
	ExceptionPersonalizada(f"ocurruo un problema de tipo {Exception}")