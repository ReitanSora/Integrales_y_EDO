# Tema: EDO
# Grupo #6
# - Tulcanza Juan          CI: 1755962485
# Ingeniería en Sistemas de la información
# Paralelo: SI3 - 002
# Fecha de entrega: 17/08/2023

import tkinter as tk

from static import style


class Instrucciones(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    # función para inicializar los widges que se mostrarán en la ventana

    def init_widgets(self):

        # label titulo bienvenida
        tk.Label(
            self,
            text="Instrucciones para el uso del aplicativo\n",
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, pady=(20, 30))

        # label titulo bienvenida

        tk.Label(self,
                 text="Instrucciones:\n\n     • Integrales: solo poner la funcion --> a**n para un numero a elevado a la n potencia\n     • Integrales: solo poner la funcion --> a*x para un numero a multiplicado por la variable x o y\n     • Ejemplo: La integral de 3x^3 o la integral de 3xy^2 se escribe 3*x**3 o 3*x*y**2\n",
                 **style.STYLE_TEXT,
                 ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        tk.Label(self,
                 text="Ecuación Diferencial Ordinaria:\n\n     • Ejemplos de ecuaciones Primer orden: la ecuación y+ 3y = 5x + 3 se escribe dy/dx + 3*y(x) = 5*x + 3n\n     • Segundo orden: la ecuación y'' + 5y' - 3y = 0 se escribe d2y/dx2 + 5*dy/dx - 3*y(x) = 0\n",
                 **style.STYLE_TEXT,
                 ).pack(side=tk.TOP, fill=tk.X)
