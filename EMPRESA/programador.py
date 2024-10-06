# programador.py

from empleado import Empleado

class Programador(Empleado):
    def __init__(self, nombre, id_empleado, salario, lenguajes):
        super().__init__(nombre, id_empleado, salario)
        self.lenguajes = lenguajes  # Lista de lenguajes de programación

    def mostrar_informacion(self):
        super().mostrar_informacion()
        lenguajes_str = ', '.join(self.lenguajes)
        print(f"Lenguajes de programación: {lenguajes_str}")
