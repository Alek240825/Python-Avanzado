class Vehiculo:
    def __init__(self, nombre_comprador, documento, N_documento, correo):
        self.nombre_comprador = nombre_comprador
        self.documento = documento
        self.N_documento = N_documento
        self.correo = correo

    def get_nombre(self):
        return self.nombre_comprador

    def get_documento(self):
        return self.documento

    def get_correo(self):
        return self.correo

    def get_numero(self):
        return self.N_documento

    def informacion(self):
        print(f"Nombre del comprador: {self.get_nombre()}")
        print(f"Documento: {self.get_documento()}")
        print(f"Correo: {self.get_correo()}")
        print(f"Número de documento: {self.get_numero()}")

class Automovil(Vehiculo):
    def __init__(self, nombre_comprador, documento, correo, N_documento, marca, modelo, color, valor):
        super().__init__(nombre_comprador, documento, correo, N_documento)
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.valor = valor

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_color(self):
        return self.color

    def get_valor(self):
        return self.valor

    def calcular_matricula(self):
        return self.valor * 0.5

    def calcular_impuesto(self):
        return self.calcular_matricula() * 0.1

    def calcular_total(self):
        return self.valor + self.calcular_matricula() + self.calcular_impuesto()

    def informacion(self):
        super().informacion()
        print(f"Marca: {self.get_marca()}")
        print(f"Modelo: {self.get_modelo()}")
        print(f"Color: {self.get_color()}")
        print(f"Valor: ${self.get_valor():,.2f}")
        print(f"Matrícula: ${self.calcular_matricula():,.2f}")
        print(f"Impuesto: ${self.calcular_impuesto():,.2f}")
        print(f"Total: ${self.calcular_total():,.2f}")

class Moto(Vehiculo):
    def __init__(self, nombre_comprador, documento, correo, N_documento, marca, linea, cilindraje, valor):
        super().__init__(nombre_comprador, documento, correo, N_documento)
        self.marca = marca
        self.linea = linea
        self.cilindraje = cilindraje
        self.valor = valor

    def get_marca(self):
        return self.marca

    def get_linea(self):
        return self.linea

    def get_cilindraje(self):
        return self.cilindraje

    def get_valor(self):
        return self.valor

    def calcular_soat(self):
        if self.cilindraje <= 250:
            return self.valor * 0.03
        elif self.cilindraje <= 500:
            return self.valor * 0.1
        else:
            return self.valor * 0.2

    def calcular_total(self):
        return self.valor + self.calcular_soat()

    def informacion(self):
        super().informacion()
        print(f"Marca: {self.get_marca()}")
        print(f"Línea: {self.get_linea()}")
        print(f"Cilindraje: {self.get_cilindraje()} cc")
        print(f"Valor: ${self.get_valor():,.2f}")
        print(f"SOAT: ${self.calcular_soat():,.2f}")
        print(f"Total: ${self.calcular_total():,.2f}")

marcas_automoviles = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
modelos_automoviles = ["Corolla", "Civic", "Focus", "Camaro", "Altima"]
marcas_motos = ["Honda", "Yamaha", "Suzuki", "Kawasaki", "Harley-Davidson"]
lineas_motos = ["CBR", "YZF", "GSX", "Ninja", "Softail"]
cilindrajes_motos = [100, 125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000]
vehiculos = [
    Vehiculo("Juan Pérez", "Cedula", "12345678", "juanperez@example.com"),
    Vehiculo("María Gómez", "Targeta de identidad", "98765432", "mariagomez@example.com"),
    Vehiculo("Pedro Rodríguez", "Pasaporte", "11111111", "pedrorodriguez@example.com"),
    Vehiculo("Ana Sánchez", "Pasaporte", "22222222", "anasanchez@example.com"),
    Vehiculo("Luis González", "Targeta de identidad", "33333333", "luisgonzalez@example.com"),
    Vehiculo("Sofía Pérez", "Pasaporte", "44444444", "sofiaperez@example.com"),
    Vehiculo("Carlos Martínez", "Cedula", "55555555", "carlosmartinez@example.com"),
    Vehiculo("Julia Gómez", "Cedula", "66666666", "juliagomez@example.com"),
    Vehiculo("Rosa López", "Cedula", "77777777", "rosalopez@example.com"),
    Vehiculo("Miguel Díaz", "Targeta de identidad", "88888888", "migueldiaz@example.com")
]

documento = input("Ingrese su documento: ")
N_documento = input("Ingrese su número de documento: ")

vehiculo = None
while vehiculo is None:
    for v in vehiculos:
        if v.get_documento() == documento and v.get_numero() == N_documento:
            vehiculo = v
            break
    if vehiculo is None:
        print("No se encontró el Usuario. Por favor, inténtelo de nuevo.")
        documento = input("Ingrese su documento: ")
        N_documento = input("Ingrese su número de documento: ")

vehiculos_ingresados = {}

while True:
    print("Bienvenido al sistema de vehículos")
    print("1. Ingresar vehículo")
    print("2. Ver vehículos ingresados")
    print("3. Salir")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        if vehiculo:
            print("Bienvenido", vehiculo.get_nombre())
            print("¿Qué tipo de vehículo desea ingresar?")
            print("1. Moto")
            print("2. Carro")
            opcion_vehiculo = input("Ingrese su opción: ")
            while opcion_vehiculo not in ["1", "2"]:
                print("Opción no válida. Por favor, ingrese una opción válida.")
                opcion_vehiculo = input("Ingrese su opción: ")

            if opcion_vehiculo == "1":
                marca = input("Ingrese la marca de la moto: ")
                while marca not in marcas_motos:
                    print("Marca no válida. Por favor, ingrese una marca válida.")
                    marca = input("Ingrese la marca de la moto: ")
                linea = input("Ingrese la línea de la moto: ")
                while linea not in lineas_motos:
                    print("Línea no válida. Por favor, ingrese una línea válida.")
                    linea = input("Ingrese la línea de la moto: ")
                cilindraje = int(input("Ingrese el cilindraje de la moto: "))
                while cilindraje not in cilindrajes_motos:
                    print("Cilindraje no válido. Por favor, ingrese un cilindraje válido.")
                    cilindraje = int(input("Ingrese el cilindraje de la moto: "))
                valor = float(input("Ingrese el valor de la moto (entre 50 millones y 150 millones): "))
                while valor < 50000000 or valor > 150000000:
                    print("Valor no válido. Por favor, ingrese un valor entre 50 millones y 150 millones.")
                    valor = float(input("Ingrese el valor de la moto: "))
                moto = Moto(vehiculo.get_nombre(), vehiculo.get_documento(), vehiculo.get_correo(), vehiculo.get_numero(), marca, linea, cilindraje, valor)
                if cilindraje <= 250:
                    costo_soat = valor * 0.03
                elif cilindraje <= 500:
                    costo_soat = valor * 0.10
                else:
                    costo_soat = valor * 0.20
                print("Moto ingresada correctamente.")
                print("Costo del SOAT: $", costo_soat)
                moto.informacion()
                # Agregamos la moto al diccionario de vehículos ingresados
                vehiculos_ingresados[vehiculo.get_documento()] = moto
            elif opcion_vehiculo == "2":
                marca = input("Ingrese la marca del carro: ")
                while marca not in marcas_automoviles:
                    print("Marca no válida. Por favor, ingrese una marca válida.")
                    marca = input("Ingrese la marca del carro: ")
                modelo = input("Ingrese el modelo del carro: ")
                while modelo not in modelos_automoviles:
                    print("Modelo no válido. Por favor, ingrese un modelo válido.")
                    modelo = input("Ingrese el modelo del carro: ")
                color = input("Ingrese el color del carro: ")
                valor = float(input("Ingrese el valor del carro (entre 50 millones y 150 millones): "))
                while valor < 50000000 or valor > 150000000:
                    print("Valor no válido. Por favor, ingrese un valor entre 50 millones y 150 millones.")
                    valor = float(input("Ingrese el valor del carro: "))
                valor_matricula = valor * 0.05
                valor_impuesto = valor_matricula * 0.10
                automovil = Automovil(vehiculo.get_nombre(), vehiculo.get_documento(), vehiculo.get_correo(), vehiculo.get_numero(), marca, modelo, color, valor)
                print("Carro ingresado correctamente.")
                print("Valor de la matrícula: $", valor_matricula)
                print("Valor del impuesto: $", valor_impuesto)
                automovil.informacion()
                # Agregamos el carro al diccionario de vehículos ingresados
                vehiculos_ingresados[vehiculo.get_documento()] = automovil
        else:
            print("Debe ingresar su información personal antes de ingresar un vehículo.")

    elif opcion == "2":
        cedula = input("Ingrese su cédula: ")
        numero_cedula = input("Ingrese su número de cédula: ")
        if cedula in vehiculos_ingresados:
            vehiculo_ingresado = vehiculos_ingresados[cedula]
            print("Información del vehículo:")
            vehiculo_ingresado.informacion()
        else:
            print("No se encontró ningún vehículo con esa cédula.")

    elif opcion == "3":
        print("Gracias por utilizar el sistema de vehículos.")
        break

    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")