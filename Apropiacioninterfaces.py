import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")

        self.pantalla = tk.Entry(self.ventana, width=20)
        self.pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'Retroceso'
        ]

        self.crear_botones()

        # Configura las filas y columnas para que se expandan uniformemente
        for i in range(5):
            self.ventana.rowconfigure(i, weight=1)
        for j in range(4):
            self.ventana.columnconfigure(j, weight=1)

    def crear_botones(self):
        fila = 1
        columna = 0
        for boton in self.botones:
            if boton == '=':
                tk.Button(self.ventana, text=boton, command=self.calcular).grid(row=fila, column=columna, columnspan=2, sticky="nsew")
                columna += 1  # Ocupará dos columnas
            elif boton == 'Retroceso':
                tk.Button(self.ventana, text=boton, command=self.retroceso).grid(row=fila, column=columna, columnspan=2, sticky="nsew")
            else:
                tk.Button(self.ventana, text=boton, command=lambda boton=boton: self.agregar_boton(boton)).grid(row=fila, column=columna, sticky="nsew")
            columna += 1
            if columna == 4:
                fila += 1
                columna = 0

    def agregar_boton(self, boton):
        self.pantalla.insert(tk.END, boton)

    def retroceso(self):
        texto = self.pantalla.get()
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(tk.END, texto[:-1])

    def calcular(self):
        try:
            resultado = eval(self.pantalla.get())
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, resultado)
        except Exception as e:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, "Error")

    def run(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.run()