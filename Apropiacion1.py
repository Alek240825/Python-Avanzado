class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo, moneda):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__saldo = saldo
        self.__moneda = moneda

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def moneda(self):
        return self.__moneda

    def depositar(self, monto):
        if isinstance(monto, (int, float)) and monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo} {self.__moneda}")
        else:
            print("El monto a depositar debe ser un número positivo.")

    def retirar(self, monto):
        if not isinstance(monto, (int, float)):
            print("El monto a retirar debe ser un número.")
            return
        if monto <= 0:
            print("El monto a retirar debe ser positivo.")
            return
        if monto > self.__saldo:
            print("Fondos insuficientes.")
            return
        self.__saldo -= monto
        print(f"Retiro exitoso. Nuevo saldo: {self.__saldo} {self.__moneda}")

    def transferir(self, otra_cuenta, monto):
        if not isinstance(monto, (int, float)):
            print("El monto a transferir debe ser un número.")
            return
        if self.__moneda != otra_cuenta.moneda:
            print("Las transferencias solo pueden realizarse entre cuentas de la misma moneda.")
            return
        if monto <= 0:
            print("El monto a transferir debe ser positivo.")
            return
        if monto > self.__saldo:
            print("Fondos insuficientes.")
            return
        self.__saldo -= monto
        otra_cuenta.depositar(monto)
        print(f"Transferencia exitosa. Nuevo saldo: {self.__saldo} {self.__moneda}")

    def realizar_transferencia(self, destinatario, monto):
        self.transferir(destinatario, monto)

# Crear cuentas de ejemplo
cuenta1 = CuentaBancaria("123456789", "Juan Pérez", 1000, "COP")
cuenta2 = CuentaBancaria("987654321", "Ana Gómez", 500, "COP")
cuenta3 = CuentaBancaria("111222333", "Carlos López", 1500, "COP")
cuenta4 = CuentaBancaria("444555666", "María Rodríguez", 2000, "COP")
cuenta5 = CuentaBancaria("777888999", "Luis Fernández", 2500, "COP")

# Función para verificar la cuenta
def verificar_cuenta(numero_cuenta):
    cuentas = [cuenta1, cuenta2, cuenta3, cuenta4, cuenta5]
    for cuenta in cuentas:
        if numero_cuenta == cuenta.numero_cuenta:
            return cuenta
    return None

# Función para capturar datos y realizar operaciones
def operaciones_bancarias():
    numero_cuenta = input("Ingrese el número de cuenta: ")
    cuenta = verificar_cuenta(numero_cuenta)
    
    if cuenta:
        print(f"Bienvenido, {cuenta.titular}!")
        while True:
            print("\nSeleccione una operación:")
            print("1. Depositar dinero")
            print("2. Retirar dinero")
            print("3. Transferir dinero")
            print("4. Salir")
            opcion = input("Ingrese el número de la operación: ")

            if opcion == "1":
                try:
                    monto = float(input("Ingrese el monto a depositar: "))
                    cuenta.depositar(monto)
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            elif opcion == "2":
                try:
                    monto = float(input("Ingrese el monto a retirar: "))
                    cuenta.retirar(monto)
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            elif opcion == "3":
                try:
                    monto = float(input("Ingrese el monto a transferir: "))
                    destinatario_numero = input("Ingrese el número de cuenta destinatario: ")
                    destinatario = verificar_cuenta(destinatario_numero)
                    if destinatario:
                        cuenta.realizar_transferencia(destinatario, monto)
                    else:
                        print("Cuenta destinatario no encontrada.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

            elif opcion == "4":
                print("Saliendo del sistema.")
                break

            else:
                print("Opción no válida. Intente de nuevo.")
    else:
        print("Número de cuenta no encontrado.")

# Ejecutar las operaciones bancarias
operaciones_bancarias()
