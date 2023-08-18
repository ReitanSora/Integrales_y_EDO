# Tema: EDO
# Grupo #6
# - Tulcanza Juan          CI: 1755962485
# Ingeniería en Sistemas de la información
# Paralelo: SI3 - 002
# Fecha de entrega: 17/08/2023

import tkinter as tk

from static import style


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BG)
        self.controller = controller
        self.init_widgets()

    def init_widgets(self):
        self.container = tk.Canvas(
            self, background=style.BG, bd=0, relief="flat", highlightthickness=0)
        self.container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)

        container_frame = tk.Frame(self.container, background=style.BG)
        container_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.container.create_window((0, 0), window=container_frame)

        # label titulo bienvenida
        tk.Label(
            container_frame,
            text="Bienvenido al programa\n De Integrales\n Ecuaciones Diferenciales Ordinarias (1er & 2do Orden)",
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, pady=(20, 30))

        # label titulo bienvenida

        tk.Label(container_frame,
                 text="Integrales:\n\n     Con las integrales podemos calcular diferentes elementos, como la longitud de arco de una curva, el valor promedio de una función, la presión que ejerce un fluido, el trabajo que ha de realizarse para mover un objeto de un punto a otro, la velocidad de un objeto móvil o incluso el superávit del consumido.",
                 **style.STYLE_TEXT,
                 ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        tk.Label(container_frame,
                 text="Ecuación Diferencial Ordinaria:\n\n     Se llama ecuación diferencial ordinaria (E. D. O.) a una ecuación diferencial en la que aparecen derivadas ordinarias de una o más variables dependientes respecto a una única variable independiente.",
                 **style.STYLE_TEXT,
                 ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        tk.Label(
            container_frame,
            text="\nPrograma:\n\n Este código crea una interfaz gráfica de usuario (GUI) utilizando la biblioteca Tkinter en Python. La GUI proporciona una variedad de funcionalidades relacionadas con cálculos matemáticos, resolución de ecuaciones diferenciales, integración de funciones y visualización de gráficos.",
            **style.STYLE_TEXT,
        ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        tk.Label(container_frame,
                 text="Integración de Funciones:\n\n     • Las funciones integralx() e integraly() permiten al usuario ingresar una función y realizar la integración con respecto a la variable 'x' o 'y', respectivamente.\n     • Las funciones utilizan la biblioteca SymPy para realizar la integración y muestran el resultado en etiquetas en la GUI.\n",
                 **style.STYLE_TEXT,
                 ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        tk.Label(container_frame,
                 text="Resolución de Ecuaciones Diferenciales:\n\n     • a función calcular() toma una ecuación diferencial ingresada por el usuario en la forma de y' = f(x, y) o y'' = f(x, y, y').\n     • Puede resolver la ecuación diferencial usando la biblioteca SymPy, ya sea con o sin condiciones iniciales proporcionadas por el usuario.\n     • Muestra la solución en la GUI.\n",
                 **style.STYLE_TEXT,
                 ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        tk.Label(container_frame,
                 text="Visualización de Gráficos:\n\n     • La función Solve(x, S) resuelve una ecuación diferencial ordinaria de primer orden utilizando el método odeint de la biblioteca SciPy.\n     • Grafica la solución utilizando Matplotlib y muestra la gráfica en una ventana emergente.\n   • Los valores de entrada 'x', 'min' y 'max' determinan los parámetros para la solución y la visualización.\n",
                 **style.STYLE_TEXT,
                 ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        tk.Label(container_frame,
                 text="Interfaz Gráfica:\n\n     • Crea una ventana de GUI con diferentes elementos, como etiquetas, campos de entrada y botones, que permiten al usuario interactuar con las funcionalidades mencionadas anteriormente.\n     • Los elementos de la interfaz gráfica incluyen campos para ingresar funciones, ecuaciones diferenciales y parámetros para visualización.\n     • Los botones permiten al usuario realizar operaciones como integración, resolución de ecuaciones diferenciales y visualización de gráficos.\n     • El botón Salir permite cerrar la aplicación.\n",
                 **style.STYLE_TEXT,
                 ).pack(side=tk.TOP, fill=tk.X, pady=(0, 20))

        info_frame = tk.Frame(container_frame, background=style.BG)
        info_frame.columnconfigure(0, weight=1)
        info_frame.pack(side=tk.TOP, fill=tk.BOTH, padx=20)

        tk.Label(info_frame,
                 text="Librerías usadas:\n\n     • tkinter\n     • math\n     • numpy\n     • matplotlib",
                 **style.STYLE_TEXT,
                 ).grid(row=0, column=0, sticky=tk.NW, pady=(0, 20))

        tk.Label(info_frame,
                 text="Integrantes:\n\n          • Juan Tulcanaza\n  ",
                 **style.STYLE_TEXT,
                 ).grid(row=1, column=0, sticky=tk.NW)

        self.scroll = tk.Scrollbar(self,
                                   border=0,
                                   orient="vertical",
                                   command=self.container.yview,
                                   )
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.container.configure(yscrollcommand=self.scroll.set)
        self.container.bind('<Configure>', lambda e: self.container.configure(
            scrollregion=self.container.bbox(tk.ALL)))
