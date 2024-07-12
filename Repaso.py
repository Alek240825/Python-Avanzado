class Factura:
    def __init__(self, codigo_producto, nombre_producto, cantidad, valor_unitario, valor_total):
        self.__codigo_producto = codigo_producto
        self.__nombre_producto = nombre_producto
        self.__cantidad = cantidad
        self.__valor_unitario = valor_unitario
        self.__valor_total = valor_total

    def obtener_factura(self):
        subtotal = self.__cantidad * self.__valor_unitario
        iva = subtotal * 0.19
        self.__valor_total = subtotal + iva
        return subtotal, iva, self.__valor_total

    def capturar_informacion(self):
        self.__codigo_producto = input("Ingresa el código del producto: ")
        self.__nombre_producto = input("Ingresa el nombre del producto: ")
        self.__cantidad = int(input("Ingresa la cantidad: "))
        self.__valor_unitario = float(input("Ingresa el valor unitario: "))

# Create a list to store the Factura objects
facturas = []

# Capture information for 3 products
for i in range(3):
    print(f"Producto {i+1}:")
    p = Factura("", "", 0, 0, 0)
    p.capturar_informacion()
    facturas.append(p)

# Calculate the total subtotal and total IVA
total_subtotal = 0
total_iva = 0
total_valor_total = 0

# Print the invoices and calculate the total values
print("Facturas:")
print("==========")
print("Código\tNombre\tCantidad\tValor Unitario\tSubtotal\tValor Total")
for p in facturas:
    subtotal, iva, valor_total = p.obtener_factura()
    total_subtotal += subtotal
    total_iva += iva
    total_valor_total += valor_total
    print(f"{p._Factura__codigo_producto}\t{p._Factura__nombre_producto}\t{p._Factura__cantidad}\t{p._Factura__valor_unitario:.2f}\t{subtotal:.2f}\t{valor_total:.2f}")

# Print the total values
print("\nTotales:")
print("========")
print(f"Subtotal:\t{total_subtotal:.2f}")
print(f"Iva (19%):\t{total_iva:.2f}")
print(f"Valor Total:\t{total_valor_total:.2f}")