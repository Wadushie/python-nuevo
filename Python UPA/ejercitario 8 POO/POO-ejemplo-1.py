# crear una clase de estudiante
"""
self = atributo para un objeto, le asigna junto un nombre que recibe un parametro
"""
suma = 0
class Estudiante:
    def __init__(self, nombre, nota):     # Inicializador del objeto creado, constructor
        self.nombre = nombre        # Parametros para el estudiante, que tiene un estudiante?
        self.nota = nota
    def devolverNota(self):
        return self.nota
    def nombre(self):
        return self.nombre

class Institucion_Educativa:
    def __init__(self, nombre, estudiantes = []):
        self.nombre = nombre
        self.estudiantes = estudiantes  # En la parte de estudiantes, se creará una lista a ese parametro solamente

    def matricular(self, nuevo_estudiante):
        self.estudiantes.append(nuevo_estudiante)   # Agregan los nuevos estud a la lista de estudiantes

    def estudiante_destacado(self):
        for estudiante in self.estudiantes:
            estudiante.devolverNota()   # Algoritmo que busca la nota más alta dentro de estudiantes

   # def promedio_notas(self):
opcion_elegida = 0
while opcion_elegida != 4:

    print("1- Matricular Estudiante nuevo a la universidad")
    print("2- Estudiante destacado")
    print("3- Calcular promedio de los alumnos")
    print("4- Salir")
    opcion_elegida = int(input("\n Elija una de las 3 opciones (1/2/3/4)"))

    lista_estudiantes = []
    institucion = Institucion_Educativa('upa', lista_estudiantes)

    if opcion_elegida == 1:
        print("Registro de Estudiantes")
        print("Ingrese el nombre del alumno")
        nombre = input()
        print("Ingrese la nota del estudiante")
        nota = int(input())
        estudiante1 = Estudiante(nombre, nota)
        institucion.matricular(estudiante1) # cargar el estudiante a matricula
    elif opcion_elegida == 2:
        print("EL estudiante más destacado actualmente es: ")
        institucion.estudiante_destacado()
    elif opcion_elegida == 3:
        print("hola")
