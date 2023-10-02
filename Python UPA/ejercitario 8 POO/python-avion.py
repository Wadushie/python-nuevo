class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
p1 = Persona('Jose', 21)
print(p1.nombre)
print(p1.edad)
print(p1.nombre, p1.edad)