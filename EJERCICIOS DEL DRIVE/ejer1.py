# Escribe un programa que solicite al usuario dos números y muestre su
# suma, resta, multiplicación, división, división entera y residuo (módulo).

num1= float(input("Ingresa el primer número: "))
num2= float(input("Ingresa el segundo número: "))
#SUMA
suma= num1+num2
#RESTA
resta= num1-num2
#MULTIPLICACIÓN
mult= num1*num2
#DIVISION
div= num1/num2 if num2!=0 else "No se puede ejecutar"

#DIVISION_ENTERA
division_entera= num1//num2 if num2!=0 else "No se puede dividir por 0"

#RESIDUO
residuo= num1%num2 if num2!=0 else "No se puede calcular el residuo con cero"

print(f"Suma: {suma} ")
print(f"Resta: {resta}")
print(f"Multiplicacion: {mult}")
print(f"Division: {div}")
print(f"Division entera: {division_entera}")
print(f"residup: {residuo}")