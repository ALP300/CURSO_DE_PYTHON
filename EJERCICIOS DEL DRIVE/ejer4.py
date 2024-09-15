# Escribe un programa que solicite al usuario un número entero y calcule
# si es divisible por 3 y por 5.
num= int(input("Ingresa un número entero: "))
if num%3==0 and num%5==0:
    print(f"{num} es divisible por 3 y por 5")
else:
    print(f"{num} no es divisible por 3 y por 5")