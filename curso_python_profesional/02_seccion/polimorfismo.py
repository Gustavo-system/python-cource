class Perro:
    def avanzar(self):
        print("yo, perro camino en 4 patas")


class Pajaro:
    def avanzar(self):
        print("yo, pajaro vuelo")


def moverse(animal):
    # si el metodo no se encuentra en la instancia, detorana un AttributeError
    animal.avanzar()


# se pasa por parametro la instancia de un objeto
perro = Perro()
pajaro = Pajaro()

moverse(perro)
moverse(pajaro)
