# Calcular la cantidad de alumnos que obtuvieron nota inferior al promedio del curso
# en cierta materia. Hay 20 alumnos, y todos rindieron. Las notas van del 0 al 100 (se
# asume que todas las notas son correctas).
import random
alumnos = 20
notas = []
vec2 = []
suma = 0
for i in range(20):
    nota = random.randint(1,100)
    notas.append(nota)
print("Los valores del vector son: ", notas)

for nota in notas:
    suma = suma + nota
print("La suma de los valores del vector son: ",suma)
# calcula el promedio
promedio = suma / alumnos
print("El promedio de las notas es: ",promedio)

# calcular del promedio, mostrar cuales son los alumnos con notas bajas que el promedio
for nota in notas:
    if nota < promedio:
        vec2.append(nota)
        nota = nota + 1
print("Los alumnos que tuvieron la nota menor al promedio son: ", vec2)
print('la cantidad de alumnos con notas inferior al promedio es: ',len(vec2))
# Ingresar la nota
# que el programa diga si la nota ingresada pasa o no
