import tkinter as tk
from tkinter.messagebox import askyesno
from tkinter.messagebox import showinfo

ventana = tk.Tk()
ventana.title("Cuestionario")

preguntas = [
    "¿Hoy es un día frio?",
    "¿Te gustan los días cálidos?",
    "¿Has salido de casa hoy?",
    "¿Has comido algo saludable hoy?",
    "¿Te sientes feliz hoy?"
]

respuestas_correctas = [False, True, True, True, True]
contador_correctas = 0

def hacer_pregunta(indice):
    global contador_correctas
    if indice < len(preguntas):
        respuesta = askyesno(title=f"Pregunta N° {indice + 1}", message=preguntas[indice])
        if respuesta == respuestas_correctas[indice]:
            contador_correctas += 1
        hacer_pregunta(indice + 1)
    else:
        showinfo(title="Resultados", message=f"Respuestas correctas: {contador_correctas} de {len(preguntas)}")

hacer_pregunta(0)

ventana.mainloop()