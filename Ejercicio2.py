class Cliente:
    def __init__(self, numero_cuenta, nombre, direccion, correo, telefono, saldo):
        self.__numero_cuenta = numero_cuenta
        self.__nombre = nombre
        self.__direccion = direccion
        self.__correo = correo
        self.__telefono = telefono
        self.__saldo = saldo

    # Getters
    def get_numero_cuenta(self):
        return self.__numero_cuenta

    def get_nombre(self):
        return self.__nombre

    def get_direccion(self):
        return self.__direccion

    def get_correo(self):
        return self.__correo

    def get_telefono(self):
        return self.__telefono

    def get_saldo(self):
        return self.__saldo

    # Setters
    def set_numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_correo(self, correo):
        self.__correo = correo

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_saldo(self, saldo):
        self.__saldo = saldo

# Capturar datos del usuario
numero_cuenta = int(input("Ingrese el número de cuenta: "))
nombre = input("Ingrese el nombre del cliente: ")
direccion = input("Ingrese la dirección del cliente: ")
correo = input("Ingrese el correo del cliente: ")
telefono = int(input("Ingrese el teléfono del cliente: "))
saldo = float(input("Ingrese el saldo del cliente: "))

# Crear una instancia de la clase Cliente
p = Cliente(numero_cuenta, nombre, direccion, correo, telefono, saldo)

# Imprimir los datos del cliente
print(p.get_numero_cuenta())
print(p.get_nombre())
print(p.get_direccion())
print(p.get_correo())
print(p.get_telefono())
print(p.get_saldo())