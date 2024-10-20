from Gerente import Gerente
from programador import Programador

def main():
    #nombre, id_empleado, salario, departamento
    gerente= Gerente("Carlos Pérez",101,2000,"Recursos Humanos")
    #nombre, id_empleado, salario, departamento, lenguajes
    programador= Programador("Juan", 3,1000,"Software",["Python","JS", "Java"])
    
    print("INFORMACIÓN DEL GERENTE: ")
    gerente.mostrar_informacion()
    
    print("\n..........................\n")
    print("Información del programador: ")
    programador.mostrar_informacion()
    
main()
# :D
