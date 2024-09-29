# Importar la clase Animal desde Animal.py
from Animal import Animal

# Definir la clase Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        super().__init__(nombre)  # Llama al constructor de la clase padre
        self.color = color

    # Sobrescribir el método de la clase padre
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

# Crear un objeto de la clase Gato
mi_gato = Gato("Pelusa", "blanco")

# Acceder a métodos heredados y sobrescritos
mi_gato.hacer_sonido()  # Salida: Pelusa dice: ¡Miau!

