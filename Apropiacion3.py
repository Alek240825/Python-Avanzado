from abc import ABC, abstractmethod
import random

class Juego(ABC):
    @abstractmethod
    def iniciar(self):
        pass

    @abstractmethod
    def mostrar_puntaje(self):
        pass

    @abstractmethod
    def terminar(self):
        pass

class JuegoAdivinanza(Juego):
    def __init__(self):
        self.numero_adivinar = 0
        self.intentos = 0
        self.puntaje = 10.0
        self.historial_puntajes = []
        self.juego_iniciado = False

    def iniciar(self):
        self.numero_adivinar = random.randint(1, 100)
        self.intentos = 0
        self.puntaje = 10.0
        self.juego_iniciado = True
        print("¡Bienvenido al juego de adivinanza!")
        print("He pensado en un número entre 1 y 100. ¡Intenta adivinarlo!")

    def mostrar_puntaje(self):
        print(f"Número de intentos: {self.intentos}")
        print(f"Puntaje: {self.puntaje:.1f}")

    def terminar(self):
        print("¡Felicidades! Has adivinado el número.")
        self.mostrar_puntaje()
        self.historial_puntajes.append(self.puntaje)

    def jugar(self):
        while True:
            try:
                adivinanza = int(input("Introduce tu adivinanza: "))
                self.intentos += 1
                if adivinanza < self.numero_adivinar:
                    print("El número es mayor.")
                    self.puntaje -= 0.5
                elif adivinanza > self.numero_adivinar:
                    print("El número es menor.")
                    self.puntaje -= 0.5
                else:
                    self.terminar()
                    break

                if self.puntaje <= 0:
                    print("Has perdido. El puntaje ha llegado a 0.")
                    self.historial_puntajes.append(0)
                    break
            except ValueError:
                print("Por favor, introduce un número válido.")

    def mostrar_historial_puntajes(self):
        print("Historial de puntajes:")
        for i, puntaje in enumerate(self.historial_puntajes, 1):
            print(f"Juego {i}: {puntaje:.1f}")

def menu():
    juego = JuegoAdivinanza()
    while True:
        print("\nMenú:")
        print("1. Jugar")
        print("2. Mostrar puntajes")
        print("3. Volver a jugar")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            juego.iniciar()
            juego.jugar()
        elif opcion == "2":
            juego.mostrar_historial_puntajes()
        elif opcion == "3":
            if juego.juego_iniciado:
                juego.iniciar()
                juego.jugar()
            else:
                print("Debes jugar al menos una vez antes de poder volver a jugar.")
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

if __name__ == "__main__":
    menu()