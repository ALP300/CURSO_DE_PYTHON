'''
mi_tupla=(1,"Hola",3.14,True)
otra_tupla= 1,2,3,4
tupla_vacía=()
un_elemento=(3,)

print(mi_tupla[0])
print(mi_tupla[-1])'''

tupla1= (1,2,3)
tupla2=(4,5,6)
tupla_concatenada= tupla1+tupla2
print(tupla_concatenada)
tupla_repetida= tupla1*3
print(tupla_repetida)

tupla3=(1,2,3,2,2,2,2,4,1,1,1)
print(tupla3.count(2))
print(tupla3.index(4))
tupla4=(1,2,3)
tupla5=(1,2,5)
print(tupla4==tupla5)
print(tupla4<tupla5)
tupla_anidadas= (1,(2,3),(4,5,6),(7,8,9))
print(tupla_anidadas[1])
print(tupla_anidadas[1][0])
print(tupla_anidadas[2][2])