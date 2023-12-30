"""
A partir de python 3.10 se puede utilizar el match que se convierte en nun switch en otros lenguajes
"""

valor = 1


match valor:
	case 1:
		print("entra en el caso 1")
	case 2:
		print("entra en el caso 2")
	# para indicar que no haga match con algo
	case _:
		print("no hace match con ningun caso")