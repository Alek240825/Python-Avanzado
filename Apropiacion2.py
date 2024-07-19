import math

# Clase base
class Figura:
    def calcular_area(self):
        pass

# Subclase Circulo
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

# Subclase Cuadrado
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

# Subclase Triangulo
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

# Función para obtener las medidas y calcular el área
def obtener_medidas_y_calcular_area():
    figuras = []
    while True:
        figura = input("Ingrese el tipo de figura (circulo, cuadrado, triangulo) o 'salir' para terminar: ").lower()
        if figura == 'salir':
            break

        if figura == "circulo":
            radio = float(input("Ingrese el radio del círculo: "))
            figuras.append(Circulo(radio))

        elif figura == "cuadrado":
            lado = float(input("Ingrese el lado del cuadrado: "))
            figuras.append(Cuadrado(lado))

        elif figura == "triangulo":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            figuras.append(Triangulo(base, altura))

        else:
            print("Figura no reconocida. Por favor, intente de nuevo.")

    for figura in figuras:
        print(f"Área del {figura.__class__.__name__.lower()}: {figura.calcular_area()}")

# Llamada a la función
obtener_medidas_y_calcular_area()
