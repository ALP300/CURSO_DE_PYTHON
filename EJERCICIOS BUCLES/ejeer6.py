'''
Escribir un programa que pida al usuario un número entero y muestre por 
pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****

'''

altura= int(input("Introduce la altura del triángulo: "))
for i in range(altura):
    for j in range(i+1):
        print("*", end="")
    print("")