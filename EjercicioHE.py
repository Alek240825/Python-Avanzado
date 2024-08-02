class Persona:
    def __init__(self, nombre, documento, direccion):
        self.__nombre = nombre
        self.__documento = documento
        self.__direccion = direccion

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_documento(self):
        return self.__documento

    def set_documento(self, documento):
        self.__documento = documento

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion


class Empleado(Persona):
    def __init__(self, nombre, documento, direccion, codigo, cargo, empresa, sueldo):
        super().__init__(nombre, documento, direccion)
        self.__codigo = codigo
        self.__cargo = cargo
        self.__empresa = empresa
        self.__sueldo = sueldo

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_empresa(self):
        return self.__empresa

    def set_empresa(self, empresa):
        self.__empresa = empresa

    def get_sueldo(self):
        return self.__sueldo

    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo


class Estudiante(Persona):
    def __init__(self, nombre, documento, direccion, codigo, programa, trimestre):
        super().__init__(nombre, documento, direccion)
        self.__codigo = codigo
        self.__programa = programa
        self.__trimestre = trimestre

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_programa(self):
        return self.__programa

    def set_programa(self, programa):
        self.__programa = programa

    def get_trimestre(self):
        return self.__trimestre

    def set_trimestre(self, trimestre):
        self.__trimestre = trimestre

def main():
    global persona
    global empleado
    global estudiante
    
    while True:
        print("¿Qué tipo de persona deseas crear?")
        print("1. Empleado")
        print("2. Estudiante")
        print("3. Ver personas guardadas")
        print("4. Ver empleados guardados")
        print("5. Ver estudiantes guardados")
        print("6. Salir")
        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del empleado: ")
            documento = input("Ingrese el documento del empleado: ")
            direccion = input("Ingrese la dirección del empleado: ")
            codigo = input("Ingrese el código del empleado: ")
            cargo = input("Ingrese el cargo del empleado: ")
            empresa = input("Ingrese la empresa del empleado: ")
            sueldo = input("Ingrese el sueldo del empleado: ")

            nuevo_empleado = Empleado(nombre, documento, direccion, codigo, cargo, empresa, sueldo)
            persona.append(nuevo_empleado)
            empleado.append(nuevo_empleado)
            print("Empleado creado con éxito!")

        elif opcion == "2":
            nombre = input("Ingrese el nombre del estudiante: ")
            documento = input("Ingrese el documento del estudiante: ")
            direccion = input("Ingrese la dirección del estudiante: ")
            codigo = input("Ingrese el código del estudiante: ")
            programa = input("Ingrese el programa del estudiante: ")
            trimestre = input("Ingrese el trimestre del estudiante: ")

            nuevo_estudiante = Estudiante(nombre, documento, direccion, codigo, programa, trimestre)
            persona.append(nuevo_estudiante)
            estudiante.append(nuevo_estudiante)
            print("Estudiante creado con éxito!")

        elif opcion == "3":
            print("Personas guardadas:")
            for i, p in enumerate(persona):
                if isinstance(p, Empleado):
                    print(f"Persona {i+1}:")
                    print(f"Nombre: {p.get_nombre()}")
                    print(f"Documento: {p.get_documento()}")
                    print(f"Dirección: {p.get_direccion()}")
                    print(f"Código: {p.get_codigo()}")
                    print(f"Cargo: {p.get_cargo()}")
                    print(f"Empresa: {p.get_empresa()}")
                    print(f"Sueldo: {p.get_sueldo()}")
                    print()
                elif isinstance(p, Estudiante):
                    print(f"Persona {i+1}:")
                    print(f"Nombre: {p.get_nombre()}")
                    print(f"Documento: {p.get_documento()}")
                    print(f"Dirección: {p.get_direccion()}")
                    print(f"Código: {p.get_codigo()}")
                    print(f"Programa: {p.get_programa()}")
                    print(f"Trimestre: {p.get_trimestre()}")
                    print()

        elif opcion == "4":
            print("Empleados guardados:")
            for i, empleado in enumerate(empleado):
                print(f"Empleado {i+1}:")
                print(f"Nombre: {empleado.get_nombre()}")
                print(f"Documento: {empleado.get_documento()}")
                print(f"Dirección: {empleado.get_direccion()}")
                print(f"Código: {empleado.get_codigo()}")
                print(f"Cargo: {empleado.get_cargo()}")
                print(f"Empresa: {empleado.get_empresa()}")
                print(f"Sueldo: {empleado.get_sueldo()}")
                print()

        elif opcion == "5":
            print("Estudiantes guardados:")
            for i, estudiante in enumerate(estudiante):
                print(f"Estudiante {i+1}:")
                print(f"Nombre: {estudiante.get_nombre()}")
                print(f"Documento: {estudiante.get_documento()}")
                print(f"Dirección: {estudiante.get_direccion()}")
                print(f"Código: {estudiante.get_codigo()}")
                print(f"Programa: {estudiante.get_programa()}")
                print(f"Trimestre: {estudiante.get_trimestre()}")
                print()

        elif opcion == "6":
            break

        else:
            print("Opción inválida")

persona = []
empleado = []
estudiante = []

if __name__ == "__main__":
    main()