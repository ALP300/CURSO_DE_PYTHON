'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y 
en función de su respuesta le muestre un menú con los ingredientes disponibles para que
elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están 
en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana
o no y todos los ingredientes que lleva.

'''
print("BIENVENIDO A BELLA NAPOLI. \nTipos de pizza \n \t1- Vegetariana\n \t2- No Vegetariana")
tipo= input("Introduce el número correspondiente al tipo de pizza que quieres: ")
if tipo=="1":
    print("Ingredientes de la pizza Vegetarianas: \n\t1- Pimiento \n\t2- Tofu\n")
    ingrediente= input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomato y ", end="")
    if ingrediente=="1":
        print("pimiento")
    else:
        print("tofu")

else:
    print("Ingredientes de la pizza No Vegetarianas: \n\t1- Peperoni \n\t2- Jamón\n\t3- Salmón\n")
    ingrediente= input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomato y ", end="")
    if ingrediente=="1":
        print("peperoni")
    elif ingrediente=="2":
        print("jamón")
    else:
        print("salmón")