
class BaseResponse():

	code = ""
	message = ""
	data = None


	def __init__(self, code, message, data = None) -> None:
		self.code = code
		self.message = message
		self.data = data
	

	def general_response(self) -> dict:
		return {
			"status": self.code,
			"message": self.message,
			"data": self.data,
		}