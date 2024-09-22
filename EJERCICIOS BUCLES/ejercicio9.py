'''
Escribe un programa que genere un número aleatorio entre 
1 y 100 y le pida al usuario que lo adivine. El programa
debe indicar si el número ingresado es mayor o menor que el 
número aleatorio hasta que el usuario lo adivine correctamente.
'''
import random
numero_secreto= random.randint(1,100)
intento= None
print("¡ADIVINA EL NÚMERO SECRETO ENTRE 1 Y 100")

while intento!=numero_secreto:
    intento= int(input("Introduce tu intento: "))
    if intento<numero_secreto:
        print("EL NÚMERO ES MAYOR")
    elif intento> numero_secreto:
        print("EL NÚMERO ES MENOR")
    else:
        print("FELICIDADES HAS ADIVINADO EL NÚMERO")