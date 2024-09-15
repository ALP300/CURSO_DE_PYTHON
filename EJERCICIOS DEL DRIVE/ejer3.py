#Escribe un programa que lea un número entero y determine si es
#positivo, negativo o cero.

#DATO CURIOSO
#if(num>0){
#    print("Número es positivo")
#}

num= int(input("Ingresa un número entero: "))
if num>0:
    print(f"{num} es positivo")
elif num<0:
    print(f"{num} es negativo")
else:
    print("El número es 0")