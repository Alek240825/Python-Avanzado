import tkinter as tk

ventana_principal = tk.Tk()
etiqueta = tk.Label(ventana_principal, text= "Luis Alejandro Galicia Novoa")
etiqueta.pack()
etiqueta = tk.Label(ventana_principal, text = "iglesiag1908@gmail.com")
etiqueta.pack()
etiqueta = tk.Label(ventana_principal, text = "3144682723")
etiqueta.pack()
ventana_principal.title ("Mis datos")
ventana_principal.geometry("800x400+250+250")
ventana_principal.resizable(False, True)
ventana_principal.attributes("-alpha", 10)
ventana_principal.mainloop()