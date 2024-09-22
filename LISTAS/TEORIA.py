#LISTAS
numeros=[1,2,3,4,5]
mi_lista= [1,"Hola",3.1,True]
print(numeros[0])
print(numeros[-1])
numeros[2]=10
print(numeros)
numeros.append(6)
print(numeros)
numeros.insert(2,7)
print(numeros)
numeros.remove(10)
print(numeros)
numeros.pop(3)
print(numeros)
del numeros[1]
print(numeros)
for numero in numeros:
    print(numero,end=" "+"\n")
if 5 in numeros:
    print("EL NÚMERO 5 SE ENCUENTA EN LA LISTA")

tamaño= len(numeros)
print(tamaño)