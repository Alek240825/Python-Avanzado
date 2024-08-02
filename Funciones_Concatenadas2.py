def convertir_a_mayusculas(mensaje):
    return mensaje.upper()

def invertir_mensaje(mensaje):
    return mensaje[::-1]

def encriptar_mensaje(mensaje):
    mensaje_mayusculas = convertir_a_mayusculas(mensaje)
    mensaje_invertido = invertir_mensaje(mensaje_mayusculas)
    return mensaje_invertido

# Recibir el mensaje a encriptar a través de un input
mensaje = input("Ingrese el mensaje a encriptar: ")

# Encriptar el mensaje
mensaje_encriptado = encriptar_mensaje(mensaje)

# Imprimir el mensaje encriptado
print("Mensaje encriptado:", mensaje_encriptado)