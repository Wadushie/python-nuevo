class Usuario:
    def __init__(self):
        self.reservar_vuelo = None

    def informacion_pasajero(self, nombre, apellido, pasaporte, fecha_de_nacimiento, nacionalidad, informacion_de_contacto):
        self.nombre = nombre
        self.apellido = apellido
        self.pasaporte = pasaporte
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.nacionalidad = nacionalidad
        self.informacion_de_contacto = informacion_de_contacto

class Vuelo:
    def __init__(self, origen, destino, horarios, aerolineas, asientos_disponibles, precios):
        self.origen = origen
        self.destino = destino
        self.horarios = horarios
        self.aerolineas = aerolineas
        self.asientos_disponibles = asientos_disponibles
        self.precios = precios

    def reservar_vuelo(self, numero_asientos, clase_de_vuelo):
        if clase_de_vuelo not in ["Economica", "Primera Clase", "Ejecutiva"]:
            print("Clase de vuelo no válida. Por favor, seleccione 'Economica', 'Primera Clase' o 'Ejecutiva'.")
            return

        if self.asientos_disponibles >= numero_asientos:
            self.asientos_disponibles -= numero_asientos
            print(f"Reserva exitosa para {numero_asientos} asiento(s) en la clase {clase_de_vuelo} del vuelo de {self.origen} a {self.destino}.")
        else:
            print("Lo siento, no hay suficientes asientos disponibles.")

    def horario_llegada(self):
        return self.horarios

class Aerolineas:
    def __init__(self):
        self.lista_vuelos = []

    def agregar_vuelo(self, vuelo):
        self.lista_vuelos.append(vuelo)

######################################### MENU ############################################################
print("Bienvenido al menú de vuelos de la aerolínea Obama Bin Laden")
while True:
    print("Elija entre las siguientes opciones\n")
    print("1- Registrar al pasajero")
    print("2- Reservar vuelo")
    print("3- Salir")
    seleccion = int(input())
    if seleccion == 1:
        informacion_pasajero = input("Ingrese los siguientes datos, Nombre, Apellido, Fecha de Nacimiento, Nacionalidad, Pasaporte, Informacion de contacto: ")
        usuario = Usuario()
        Usuario.nombre = input("Ingrese su nombre")
        Usuario.apellido = input("Ingrese su apellido")
        Usuario.fecha_de_nacimiento = input("Ingrese su fecha de nacimiento")
        Usuario.nacionalidad = input("Ingrese su nacionalidad")
        Usuario.pasaporte = input("Ingrese su numero de pasaporte")
        Usuario.informacion_de_contacto = input("Ingrese su informacion para contactar si ocurre un problema con el vuelo")
        #usuario.informacion_pasajero(*informacion_pasajero.split())
        print("Se ha agregado correctamente")
    if seleccion == 2:
    if seleccion == 3:
        break
