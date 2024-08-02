def validar_contrasena(contrasena):
    def longitud_valida(cadena):
        return len(cadena) >= 8

    def caracteres_especiales(cadena):
        caracteres = "!@#$%^&*(),.?\":{}|<>"
        return any(char in caracteres for char in cadena)

    return longitud_valida(contrasena) and caracteres_especiales(contrasena)

def mostrar_menu():
    print("\nMenú:")
    print("1. Intentar de nuevo")
    print("2. Salir")

while True:
    contrasena = input("Ingrese la contraseña: ")
    es_valida = validar_contrasena(contrasena)

    if es_valida:
        print("La contraseña es válida.")
        break
    else:
        print("La contraseña no es válida.")
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '2':
            print("Saliendo del programa...")
            break
        elif opcion != '1':
            print("Opción no válida. Inténtelo de nuevo.")
