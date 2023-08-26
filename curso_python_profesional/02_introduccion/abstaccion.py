"""Ocultar la complejidad"""


class Lavadora():
    def __init__(self):
        pass
    

    def lavar(self, temperatura='caliente'):
        print("Iniciando  el proceso de lavar")
        self._llenar_tanque_de_agua(temperatura)
    
	# los metodos privados se declaran con un _ al inicio
    def _llenar_tanque_de_agua(self, temperatura):
        print(f'llenando el tanque de agua {temperatura}')
        

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar('fira')
