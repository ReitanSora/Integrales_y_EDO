# Tema: Técnicas de diseño de algoritmos - Divide y Vencerás
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Carrera: Ingeniería en Sistemas de la Información
# Paralelo: SI4 - 002
# Fecha de entrega: 19/07/2023

import tkinter as tk

import functions.events as event
from static import style


class Navegacion (tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent
        self.init_widgets(parent)

    # función para colorear un botón y dar feedback al usuario sabiendo donde se encuentra
    def colorear_boton(self):
        if self.ubicacion.get() == 1:
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_NORMAL,)
            self.boton_inicio1.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_integrales.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.boton_edo.configure(background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()
        elif self.ubicacion.get() == 2:
            self.boton_inicio1.configure(background=style.COLOR_MAGENTA_NORMAL)
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_integrales.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.boton_edo.configure(background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()
        elif self.ubicacion.get() == 3:
            self.boton_integrales.configure(
                background=style.COLOR_MAGENTA_NORMAL)
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_inicio1.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_edo.configure(background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()
        elif self.ubicacion.get() == 4:
            self.boton_edo.configure(background=style.COLOR_MAGENTA_NORMAL)
            self.boton_inicio.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_inicio1.configure(background=style.COLOR_MAGENTA_CLARO)
            self.boton_integrales.configure(
                background=style.COLOR_MAGENTA_CLARO)
            self.deshabilitar_eventos()

    # fcunción para cambiar los eventos .bind de los botones del menú
    def deshabilitar_eventos(self):
        if self.ubicacion.get() == 1:
            self.boton_inicio.bind('<Leave>', event.on_enter_nav)
            self.boton_inicio1.bind('<Leave>', event.on_leave_nav)
            self.boton_integrales.bind('<Leave>', event.on_leave_nav)
            self.boton_edo.bind('<Leave>', event.on_leave_nav)
        elif self.ubicacion.get() == 2:
            self.boton_inicio1.bind('<Leave>', event.on_enter_nav)
            self.boton_inicio.bind('<Leave>', event.on_leave_nav)
            self.boton_integrales.bind('<Leave>', event.on_leave_nav)
            self.boton_edo.bind('<Leave>', event.on_leave_nav)
        elif self.ubicacion.get() == 3:
            self.boton_integrales.bind('<Leave>', event.on_enter_nav)
            self.boton_inicio.bind('<Leave>', event.on_leave_nav)
            self.boton_inicio1.bind('<Leave>', event.on_leave_nav)
            self.boton_edo.bind('<Leave>', event.on_leave_nav)
        elif self.ubicacion.get() == 4:
            self.boton_edo.bind('<Leave>', event.on_enter_nav)
            self.boton_inicio.bind('<Leave>', event.on_leave_nav)
            self.boton_inicio1.bind('<Leave>', event.on_leave_nav)
            self.boton_integrales.bind('<Leave>', event.on_leave_nav)

    # funciones de navegación
    def home(self):
        self.controller.move_to_home()
        self.ubicacion.set(value=1)
        self.colorear_boton()

    def instrucciones(self):
        self.controller.move_to_instrucciones()  # Asegúrate de que el controlador tenga el método move_to_home1()
        self.ubicacion.set(value=2)
        self.colorear_boton()

    def integral(self):
        self.controller.move_to_integral()
        self.ubicacion.set(value=3)
        self.colorear_boton()

    def edo(self):
        self.controller.move_to_edo()
        self.ubicacion.set(value=4)
        self.colorear_boton()

    # función para inicializar los widges que se mostrarán en el menú
    def init_widgets(self, parent):
        nav_frame = tk.Frame(parent)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)
        nav_frame.configure(
            background=style.COLOR_MAGENTA_CLARO, borderwidth=0)

        self.ubicacion = tk.IntVar(value=1)
        self.boton_inicio = tk.Button(nav_frame,
                                      text="Inicio",
                                      **style.STYLE_BUTTON_NAV,
                                      command=self.home
                                      )
        self.boton_inicio.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.boton_inicio.config(background=style.COLOR_MAGENTA_NORMAL)
        self.boton_inicio.bind('<Enter>', event.on_enter_nav)

        self.boton_inicio1 = tk.Button(nav_frame,
                                  text="Instrucciones",
                                  **style.STYLE_BUTTON_NAV,
                                  command=self.instrucciones
                                  )
        self.boton_inicio1.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.boton_inicio1.bind('<Enter>', event.on_enter_nav)
        self.boton_inicio1.bind('<Leave>', event.on_leave_nav)

        self.boton_integrales = tk.Button(nav_frame,
                                         text="Integrales",
                                         **style.STYLE_BUTTON_NAV,
                                         command=self.integral,
                                         )
        self.boton_integrales.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.boton_integrales.bind('<Enter>', event.on_enter_nav)
        self.boton_integrales.bind('<Leave>', event.on_leave_nav)

        self.boton_edo = tk.Button(nav_frame,
                                      text="Ecuaciones\nDiferenciales",
                                      **style.STYLE_BUTTON_NAV,
                                      command=self.edo,
                                      )
        self.boton_edo.pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        self.boton_edo.bind('<Enter>', event.on_enter_nav)
        self.boton_edo.bind('<Leave>', event.on_leave_nav)

        # label de información - footer
        tk.Label(nav_frame,
                 text="Integrales\nEcuaciones Diferenciales (E.D.O)\nGrupo-6",
                 font=("Corbel", 10, "normal"),
                 background=style.COLOR_MAGENTA_CLARO,
                 foreground="#FFF",
                 justify="center"
                 ).pack(side=tk.BOTTOM, fill=tk.BOTH)
