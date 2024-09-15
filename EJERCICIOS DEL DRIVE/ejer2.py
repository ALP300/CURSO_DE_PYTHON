import math
#Escribe un programa que solicite al usuario un número entero y calcule
#su cuadrado y su cubo.

num= int(input("Ingresa un número entero: "))
cuadrado= math.pow(num,2)
cubo= math.pow(num,3)
cuarta= math.pow(num,4)
potencia= num**2
raiz= math.sqrt(16)
raizCuadrada= math.pow(num,1/8)

#PORCENTAJES
#20% = 0.2
porcentaje20= num*0.2
precioConDescuento= num-porcentaje20

print("El cuadrado es: ", cuadrado)
print("El cubo es: ", cubo)
print("Cuarta: ", cuarta)
print("Cuadrado: ", potencia)
print("Raíz cuadrada: ", raiz)
print("Raíz 2 cuadrada: ", raizCuadrada)
print("El 20 porciento es: ", porcentaje20)
print("El precio con descuento es: ", precioConDescuento)