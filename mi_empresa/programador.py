from Gerente import Gerente


class Programador(Gerente):
    def __init__(self, nombre, id_empleado, salario, departamento, lenguajes):
        super().__init__(nombre, id_empleado, salario, departamento)
        self.lenguajes= lenguajes
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        lenguajes_str= ', '.join(self.lenguajes)
        print(f"Lenguajes de programación: {lenguajes_str}")
        
    
     