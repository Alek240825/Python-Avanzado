def transformar_lista(lista, tipo_transformacion):
    def siguiente():
        return [x + 1 for x in lista]

    def anterior():
        return [x - 1 for x in lista]

    def duplicar():
        return [x * 2 for x in lista]

    transformaciones = {
        '1': siguiente,
        '2': anterior,
        '3': duplicar
    }

    if tipo_transformacion in transformaciones:
        return transformaciones[tipo_transformacion]()
    else:
        return "Tipo de transformación no válido."

def mostrar_menu():
    print("\nSeleccione el tipo de transformación:")
    print("1. Siguiente (incrementar cada número en 1)")
    print("2. Anterior (decrementar cada número en 1)")
    print("3. Duplicar (duplicar cada número)")
    print("5. Salir")

entrada = input("Ingrese los números separados por comas: ")
lista = list(map(int, entrada.split(',')))

while True:
    mostrar_menu()
    tipo_transformacion = input("Ingrese el número de la transformación deseada: ")

    if tipo_transformacion == '5':
        print("Saliendo del programa.")
        break
    else:
        resultado = transformar_lista(lista, tipo_transformacion)
        print("Resultado de la transformación:", resultado)
