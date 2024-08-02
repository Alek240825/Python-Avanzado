def crear_usuario(nombre, contraseña):
    if len(contraseña) < 6:
        return "La contraseña debe tener al menos 6 caracteres."
    if not any(char.isupper() for char in contraseña):
        return "La contraseña debe tener al menos una letra mayúscula."
    if not any(char.islower() for char in contraseña):
        return "La contraseña debe tener al menos una letra minúscula."
    if not any(char.isdigit() for char in contraseña):
        return "La contraseña debe tener al menos un número."
    if not any(char in "!@#$%^&*()-_+=" for char in contraseña):
        return "La contraseña debe tener al menos un carácter especial."
    return "success"

def login(usuario, contraseña, usuarios):
    for u in usuarios:
        if u["nombre"] == usuario and u["contraseña"] == contraseña:
            return "Login exitoso."
    return "Nombre de usuario o contraseña incorrectos."

usuarios = []

# Crear usuarios
for i in range(3):
    nombre = input(f"Introduce el nombre del usuario {i+1}: ")
    while True:
        contraseña = input(f"Introduce la contraseña del usuario {i+1}: ")
        resultado = crear_usuario(nombre, contraseña)
        if resultado == "success":
            print(f"Usuario {nombre} creado con éxito.")
            usuarios.append({"nombre": nombre, "contraseña": contraseña})
            break
        else:
            print(resultado)

print("Usuarios creados:", usuarios)

# Login con reintentos
max_intentos = 3

print("Iniciar sesión:")
for intento in range(max_intentos):
    usuario_login = input("Introduce tu nombre de usuario: ")
    contraseña_login = input("Introduce tu contraseña: ")

    resultado_login = login(usuario_login, contraseña_login, usuarios)
    if resultado_login == "Login exitoso.":
        print(resultado_login)
        break
    else:
        print(resultado_login)
        if intento < max_intentos - 1:
            print(f"Tienes {max_intentos - intento - 1} intentos restantes.")
        else:
            print("Has agotado todos los intentos.")
