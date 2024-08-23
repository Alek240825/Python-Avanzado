import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.title ("Yes/No")

respuesta = askyesno(title="Pregunta", message= "¿Quieres salir de este programa?")
if respuesta:
    ventana.destroy()
else:
    showinfo(title="Supeer", message="Bienvenido")

ventana.mainloop