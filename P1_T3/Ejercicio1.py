class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Banco(metaclass=SingletonMeta):
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def obtener_numero_clientes(self):
        return len(self.clientes)

    def obtener_clientes(self):
        return self.clientes

    def ver_info_clientes(self):
        for cliente in self.clientes:
            print(f"Cédula: {cliente.cedula}, Nombre: {cliente.nombre}")
            for cuenta in cliente.cuentas:
                print(f"\tCuenta: {cuenta.numero}, Tipo: {cuenta.tipo}, Saldo: {cuenta.saldo}")

    def total_saldos_ahorros(self):
        total = 0
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.tipo == "ahorros":
                    total += cuenta.saldo
        return total

    def total_saldos_corriente(self):
        total = 0
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                if cuenta.tipo == "corriente":
                    total += cuenta.saldo
        return total

class Cliente:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.cuentas = []

    def adicionar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

class Cuenta:
    def __init__(self, numero, tipo, saldo):
        self.numero = numero
        self.tipo = tipo
        self.saldo = saldo

# Ejemplo de uso
banco = Banco("Banco Ejemplo")
banco.cambiar_nombre("Banco Actualizado")

cliente1 = Cliente("1234567890", "Juan Perez")
cliente1.adicionar_cuenta(Cuenta("001", "ahorros", 1500.0))
cliente1.adicionar_cuenta(Cuenta("002", "corriente", 2000.0))

cliente2 = Cliente("0987654321", "Maria Gomez")
cliente2.adicionar_cuenta(Cuenta("003", "ahorros", 3000.0))
cliente2.adicionar_cuenta(Cuenta("004", "corriente", 1000.0))

banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

banco.ver_info_clientes()
print("Total saldos ahorros:", banco.total_saldos_ahorros())
print("Total saldos corriente:", banco.total_saldos_corriente())
