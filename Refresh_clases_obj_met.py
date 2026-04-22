class Perro:

    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        return 'Guauu'

    def andar(self,pasos):
        return f'Estoy andando {pasos} pasos'



perro1 = Perro('Rex','Pequines')
perro2 = Perro('Chuchi','Pastor Aleman')

print(perro1.nombre)
print(perro1.raza)

print(perro2.nombre)
print(perro2.raza)




