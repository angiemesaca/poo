#Angie Mesa

class Perro:
    def __init__(self,ojos,edad,raza,nombre):
        self.ojos= ojos
        self.edad= edad 
        self.raza= raza
        self.nombre = nombre
    
    def acariciar(self):
        print(f" acariciaste a {self.nombre},esta feliz ")
    def comer(self):
        print(f"le diste de comer a {self.nombre}, esta feliz ")
    def pasear (self):
        print(f"sacaste a pasear a {self.nombre}, esta feliz ")

mi_perro = Perro("marron","6","cocker","Sasha")

mi_perro.comer()
mi_perro.acariciar()