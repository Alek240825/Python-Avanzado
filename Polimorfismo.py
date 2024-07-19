class Vehiculo:
    def hacer_movimiento(self):
        pass

class Avion(Vehiculo):
    def hacer_movimiento(self):
        print("Vuela")

class Tren(Vehiculo):
    def hacer_movimiento(self):
        print("Corre")

class Barco(Vehiculo):
    def hacer_movimiento(self):
        print("Navega")

class Moto(Vehiculo):
    def hacer_movimiento(self):
        print("Veloz")

###############################################

def hacer_movimiento_vehiculo(vehiculo):
    if isinstance  (vehiculo, Vehiculo):
        vehiculo.hacer_movimiento()
    else:
        print("No es un vehiculo")

###############################################

avion = Avion()
tren = Tren()
barco = Barco()
moto = Moto()
otro_objeto = object()

hacer_movimiento_vehiculo(avion)
hacer_movimiento_vehiculo(tren)
hacer_movimiento_vehiculo(barco)
hacer_movimiento_vehiculo(moto)
hacer_movimiento_vehiculo(otro_objeto)