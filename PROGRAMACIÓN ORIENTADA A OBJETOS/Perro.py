class Perro:
    def __init__(self, nombre, raza):
        self.nombre= nombre
        self.raza= raza
    
    def ladrar(self):
        print(f"{self.nombre} está ladrando: ¡Guau,guau!")
        
        
mi_perro= Perro("Rex","Pastor Alemán")
mi_perro.ladrar()
print(f"El perro se llama: {mi_perro.nombre} su raza es: {mi_perro.raza}")