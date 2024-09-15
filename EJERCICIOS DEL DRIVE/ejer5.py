"""Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F"""

calificacion= int(input("Ingresa la calificación entre (0-100): "))
if 90<=calificacion<=100:
    print("Calificación A")
elif 80<=calificacion<90:
    print("Calificación B")
elif 70<=calificacion<80:
    print("Calificación C")
elif 60<=calificacion<70:
    print("Calificación D")
else:
    print("Calificación F")