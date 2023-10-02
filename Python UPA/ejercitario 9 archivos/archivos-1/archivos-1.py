"""
Una institución académica quiere contar con un programa que procese los puntajes de los
exámenes que tienen los alumnos para obtener la calificación final. Los puntajes obtenidos por los
alumnos en cada examen se encuentran en un archivo. Cada línea del archivo tiene el siguiente
formato:

código_alumno, código_examen, puntaje

dónde:
- código_alumno: es un identificador único del alumno. Del alumno se almacenan otros datos
que se muestra en la Tabla 1.
- código_examen: es un identificador único del examen. Del examen se almacenan otros datos
que se muestran en la Tabla 2.
- puntaje: es el puntaje obtenido por el alumno en el examen.
El programa deberá procesar el archivo de entrada y generar la información solicitada.
"""
import csv
class Alumno:
    def __init__(self,codigo_alumno, nombre_alumno, carrera_alumno):
        self.codigo_alumno = codigo_alumno
        self.nombre_alumno = nombre_alumno
        self.carrera_alumno = carrera_alumno

class Examen:
    def __init__(self, codigo_examen, prim_parcial, seg_parcial, ter_parcial, final_prim, final_segun):
        self.codigo_examen = codigo_examen
        self.prim_parcial = prim_parcial
        self.seg_parcial = seg_parcial
        self.ter_parcial = ter_parcial
        self.final_prim = final_prim
        self.final_segun = final_segun

# Abrir archivo alumnos
with open('alumnos.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)
    print(type(lector_csv))
# Imprime el archivo alumnos en forma de lista
    # Itera sobre cada fila del CSV
    for fila in lector_csv:
        print(fila)


with open('tipo_examen.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)
    print(type(lector_csv))
    for fila in lector_csv:
        print(fila)

with open('notas.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)
    print(type(lector_csv))
    print("['Nombre_alumno'], ['Tipo_examen], [Nota]")
    for fila in lector_csv:
        print(fila)
def calcular_promedio_ponderado():


"""
lista_alumnos = []
for fila in lector_csv:
    lista_alumnos = Alumno(fila[0],fila[1],fila[3])
"""
# Calcular Promedio Ponderado
"""
final = (0,100)
Prom_ponder = (Primer_Parcial + Segundo_Parcial)/2
Punt_final = ((Prom_ponder * 0,4) * (final * 0,6))
"""
