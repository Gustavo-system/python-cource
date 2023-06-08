"""
Cree una clase Persona la cual el constructor reciba los siguientes parámetros:  nombre, edad, nacionalidad  DNI. Luego, cree los métodos de instancia que devuelvan el nombre, la edad y un método de clase que devuelva DNI y nacionalidad. Por ultimo, un método especial __str__ que al pintar el objeto nos muestre todos los datos.
"""

class Persona():


    def __init__(self, nombre, edad, nacionalidad, dni):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.dni = dni


    def devuelve_nombre(self):
        return self.nombre


    def devuelve_edad(self):
        return self.edad


    @classmethod
    def devuelve_DNI(cls, dni):
        return dni


    @classmethod
    def devuelve_nacionalidad(cls, nacionalidad):
        return nacionalidad


    def __str__(self):
        return f"nombre: {self.nombre}, edad: {self.edad}, nacionalidad: {self.nacionalidad}, DNI: {self.dni}"


persona = Persona("Luis", 20, "Mexicano", "123456")