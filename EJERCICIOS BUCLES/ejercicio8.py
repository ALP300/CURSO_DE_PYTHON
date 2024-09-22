'''
Escribe un programa que solicite al usuario números enteros y los sume hasta 
que el usuario ingrese un 0. Cuando ingrese un 0, el programa 
debe mostrar la suma total y finalizar.
'''

suma=0
numero= int(input("Introduce un número (0 para terminar): "))
while numero!=0:
    suma+=numero
    numero=int(input("Introduce otro número(0 para terminar): "))
    
print("La suma total es", suma)