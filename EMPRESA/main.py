# main.py

from gerente import Gerente
from programador import Programador

def main():
    # Crear una instancia de Gerente
    gerente = Gerente("Carlos Pérez", 101, 7500.0, "Recursos Humanos")
    
    # Crear una instancia de Programador
    programador = Programador("Lucía Gómez", 202, 6500.0, ["Python", "JavaScript", "C++"])
    
    # Mostrar información del Gerente
    print("Información del Gerente:")
    gerente.mostrar_informacion()
    print("\n-----------------------------\n")
    
    # Mostrar información del Programador
    print("Información del Programador:")
    programador.mostrar_informacion()

if __name__ == "__main__":
    main()
