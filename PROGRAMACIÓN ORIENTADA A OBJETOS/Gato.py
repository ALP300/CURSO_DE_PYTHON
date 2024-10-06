from Animal import Animal

class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color= color
    
    def hacer_sonido(self):
        print(f"{self.nombre} dice ¡Miau!")
        

mi_gato= Gato("Pelusa","Oscuro")
print(f"El nombre del gato es: {mi_gato.nombre}")
mi_gato.hacer_sonido()
