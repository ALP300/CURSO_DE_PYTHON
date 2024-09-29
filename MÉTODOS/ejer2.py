'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA 
y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

'''

def NuevoTotal(cantidad, iva=21):
    montoTotal= cantidad+ cantidad*iva/100
    return montoTotal

print(NuevoTotal(1000,10))
print(NuevoTotal(1000))
