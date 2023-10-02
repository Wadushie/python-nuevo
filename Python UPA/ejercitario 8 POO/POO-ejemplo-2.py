class Vuelo:
    def __init__(self, origen, destino, horario, aerolinea, asientos_disponibles, precios):
        self.origen = origen
        self.destino = destino
        self.horario = horario
        self.aerolinea = aerolinea
        self.asientos_disponibles = asientos_disponibles
        self.precios = precios

    def reservar_vuelo(self, numero_asientos, clase_de_vuelo):
        if clase_de_vuelo not in ["Economica", "Primera Clase", "Ejecutiva"]:
            print("Clase de vuelo no válida. Por favor, seleccione 'Economica', 'Primera Clase' o 'Ejecutiva'.")
            return None

        if self.asientos_disponibles >= numero_asientos:
            self.asientos_disponibles -= numero_asientos
            reserva = Reserva(self, numero_asientos, clase_de_vuelo)
            return reserva
        else:
            print("Lo siento, no hay suficientes asientos disponibles.")
            return None

class Reserva:
    def __init__(self, vuelo, numero_asientos, clase_de_vuelo):
        self.vuelo = vuelo
        self.numero_asientos = numero_asientos
        self.clase_de_vuelo = clase_de_vuelo
        self.pagos = []

    def agregar_pago(self, pago):
        self.pagos.append(pago)

    def __str__(self):
        return f"Reserva para {self.numero_asientos} asiento(s) en la clase {self.clase_de_vuelo} del vuelo de {self.vuelo.origen} a {self.vuelo.destino}."

class Pago:
    def __init__(self, monto, numero_tarjeta, fecha_expiracion, cvv):
        self.monto = monto
        self.numero_tarjeta = numero_tarjeta
        self.fecha_expiracion = fecha_expiracion
        self.cvv = cvv

class Usuario:
    def __init__(self):
        self.reservas = []

    def informacion_pasajero(self, nombre, apellido, pasaporte, fecha_de_nacimiento, nacionalidad, informacion_de_contacto):
        self.nombre = nombre
        self.apellido = apellido
        self.pasaporte = pasaporte
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.nacionalidad = nacionalidad
        self.informacion_de_contacto = informacion_de_contacto

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def confirmar_reserva(self, numero_reserva):
        if 1 <= numero_reserva <= len(self.reservas):
            reserva = self.reservas[numero_reserva - 1]
            print(f"Confirmación de Reserva: {reserva}")
            monto_pago = float(input("Ingrese el monto del pago: "))
            numero_tarjeta = input("Ingrese el número de tarjeta: ")
            fecha_expiracion = input("Ingrese la fecha de expiración de la tarjeta: ")
            cvv = input("Ingrese el CVV de la tarjeta: ")
            pago = Pago(monto_pago, numero_tarjeta, fecha_expiracion, cvv)
            reserva.agregar_pago(pago)
            print("Pago exitoso. Su reserva ha sido confirmada.")
            return True
        else:
            print("Número de reserva no válido.")
            return False

class Aerolineas:
    def __init__(self):
        self.lista_vuelos = []

    def agregar_vuelo(self, vuelo):
        self.lista_vuelos.append(vuelo)

aerolinea = Aerolineas()
vuelo1 = Vuelo("Asuncion", "Miami", "10:00 AM", "Aerolinea Paraguay", 150, 700)
vuelo2 = Vuelo("Asuncion", "Buenos Aires", "11:30 AM", "Aerolinea Paraguay", 100, 450)
vuelo3 = Vuelo("Asuncion", "Madrid", "02:00 PM", "Aerolinea Internacional", 200, 1200)
vuelo4 = Vuelo("Asuncion", "Sao Paulo", "03:30 PM", "Aerolinea Paraguay", 120, 550)
vuelo5 = Vuelo("Asuncion", "New York", "05:00 PM", "Aerolinea Internacional", 180, 800)

aerolinea.agregar_vuelo(vuelo1)
aerolinea.agregar_vuelo(vuelo2)
aerolinea.agregar_vuelo(vuelo3)
aerolinea.agregar_vuelo(vuelo4)
aerolinea.agregar_vuelo(vuelo5)

print("Bienvenido al menú de vuelos desde el Aeropuerto Internacional Silvio Pettirossi")
usuario = None

while True:
    print("\nElija entre las siguientes opciones:")
    print("1- Registrar al pasajero")
    print("2- Reservar vuelo")
    print("3- Ver Reservas")
    print("4- Salir")
    seleccion = int(input())

    if seleccion == 1:
        if usuario is None:
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            pasaporte = input("Ingrese su número de pasaporte: ")
            fecha_de_nacimiento = input("Ingrese su fecha de nacimiento: ")
            nacionalidad = input("Ingrese su nacionalidad: ")
            informacion_de_contacto = input("Ingrese su información de contacto: ")

            usuario = Usuario()
            usuario.informacion_pasajero(nombre, apellido, pasaporte, fecha_de_nacimiento, nacionalidad, informacion_de_contacto)

            print("Se ha registrado al pasajero correctamente.")
        else:
            print("El pasajero ya está registrado.")

    elif seleccion == 2:
        if usuario is not None:
            print("\nVuelos Disponibles desde Asunción:")
            for i, vuelo in enumerate(aerolinea.lista_vuelos, start=1):
                if vuelo.origen == "Asuncion":
                    print(f"{i}. Destino: {vuelo.destino}, Horario: {vuelo.horario}, Asientos Disponibles: {vuelo.asientos_disponibles}")

            numero_vuelo = int(input("Ingrese el número del vuelo que desea reservar: "))
            clase_de_vuelo = input("Ingrese la clase de vuelo (Economica, Primera Clase, Ejecutiva): ")
            numero_asientos = int(input("Ingrese el número de asientos a reservar: "))

            vuelo_seleccionado = None
            for i, vuelo in enumerate(aerolinea.lista_vuelos, start=1):
                if vuelo.origen == "Asuncion" and i == numero_vuelo:
                    reserva = vuelo.reservar_vuelo(numero_asientos, clase_de_vuelo)
                    if reserva:
                        vuelo_seleccionado = vuelo
                        usuario.agregar_reserva(reserva)
                        print(reserva)
                        break

            if vuelo_seleccionado:
                confirmar = input("¿Desea confirmar esta reserva? (S/N): ")
                if confirmar.lower() == "s":
                    usuario.confirmar_reserva(len(usuario.reservas))  # Confirmar la última reserva
            else:
                print("No se encontró el vuelo seleccionado o no hay suficientes asientos disponibles.")

        else:
            print("Primero debe registrar al pasajero.")

    elif seleccion == 3:
        if usuario is not None:
            print("\nReservas del Pasajero:")
            for i, reserva in enumerate(usuario.reservas, start=1):
                print(f"{i}. {reserva}")
        else:
            print("Primero debe registrar al pasajero.")

    elif seleccion == 4:
        print("¡Gracias por utilizar nuestro servicio de reservas de Barack Obama Bin Laden Airlines! Hasta luego.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
