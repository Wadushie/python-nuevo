import csv

# La palabra clave with en Python se utiliza para envolver la ejecución de un bloque de código
# con métodos definidos por un administrador de contexto. En el caso de open(), el administrador
# de contexto asegura que el archivo se cierre automáticamente cuando el bloque de código dentro
# del with se haya completado, sin importar si la finalización fue debido a un error o durante la
# ejecución normal. Esto es beneficioso porque garantiza que los recursos, como los archivos abiertos,
# se limpien adecuadamente.

# Abre el archivo CSV en modo lectura
with open('datos.csv', 'r') as archivo:  # el archivo abierto se asigna como objeto a la variable archivo
    # Crea un objeto lector usando el módulo csv
    lector_csv = csv.reader(archivo)  # lector_csv es un objeto del tipo _csv.reader
    print(type(lector_csv))

    # Itera sobre cada fila del CSV
    for fila in lector_csv:  # cuando se itera el objeto, retorna cada fila del archivo csv
        # fila es una lista que contiene los datos de la fila actual
        print(fila)  # Ejemplo: ['Juan', '30', 'Madrid']

    # Si deseas acceder a los datos por columna, puedes hacer lo siguiente:
    archivo.seek(0)  # Regresa al inicio del archivo
    # headers = next(lector_csv)  # Obtén los encabezados (primera fila)
    # for fila in lector_csv:
    #    print(f"{headers[0]}: {fila[0]}, {headers[1]}: {fila[1]}, {headers[2]}: {fila[2]}")
    # Ejemplo: nombre: Juan, edad: 30, ciudad: Madrid