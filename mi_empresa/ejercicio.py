'''
Objetivo del Ejercicio
Crear una jerarquía de clases para gestionar diferentes tipos de empleados en una empresa, utilizando herencia y organizando cada clase en archivos separados.

Estructura del Proyecto
Primero, definiremos cómo se organizarán los archivos en el proyecto. Supongamos que nuestro proyecto se llama mi_empresa. La estructura de directorios será la siguiente:

css
Copiar código
mi_empresa/
│
├── empleados/
│   ├── __init__.py
│   ├── empleado.py
│   ├── gerente.py
│   └── programador.py
└── main.py
empleados/: Carpeta que contiene todas las clases relacionadas con empleados.
__init__.py: Archivo que indica a Python que empleados es un paquete. Puede estar vacío o puede utilizarse para importar las clases de manera más conveniente.
empleado.py: Define la clase base Empleado.
gerente.py: Define la clase derivada Gerente.
programador.py: Define la clase derivada Programador.
main.py: Script principal que utiliza las clases definidas anteriormente para crear instancias y mostrar información.
'''