from empleado import Empleado

class Gerente(Empleado):
   
    def __init__(self, nombre, id_empleado, salario, departamento):
        super().__init__(nombre, id_empleado, salario)
        self.departamento= departamento
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Departamento: {self.departamento}")