# Angie Mesa
# implementar dos clases una de perro y otra de gato, 
# cuyos objetos instanciados, puedan ladrar y maullar. 
# Los datos de los animales deben ser ingresados por consola

class Perro:
    def __init__(self, raza):
        self.raza = raza

    def ladrar (self):
        print(f"El {self.raza} está ladrando, guau guau !! ")

class Gato:
    def __init__(self, raza):
        self.raza = raza

    def maullar (self):
        print(f"El {self.raza} está maullando, miau miau !! ")

razadelperro= input(" ingresa la raza de tu perro:")
perro= Perro(razadelperro)

razadelgato= input ("ingresa la raza de tu gato:")
gato= Gato (razadelgato)

perro.ladrar()
gato.maullar()