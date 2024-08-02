def a_mayuscula(texto):
    return texto.upper()

def reemplazar(texto, antiguo, nuevo):
    return texto.replace(antiguo, nuevo)

def invertir(texto):
    return texto[::-1]

texto = "Este es un ejemplo de funciones anidadas en Python"
resultado = invertir(a_mayuscula(reemplazar(texto, "funciones anidadas", "Composision de ")))
print(resultado)