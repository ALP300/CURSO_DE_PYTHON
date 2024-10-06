# empleado.py

class Empleado:
    def __init__(self, nombre, id_empleado, salario):
        self.nombre = nombre
        self.id_empleado = id_empleado
        self.salario = salario

    def mostrar_informacion(self):
        print(f"Empleado: {self.nombre}, ID: {self.id_empleado}, Salario: ${self.salario}")
