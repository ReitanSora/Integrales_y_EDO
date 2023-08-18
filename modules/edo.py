
import tkinter as tk
import matplotlib.figure
import numpy as np
from scipy.integrate import odeint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import events as event
from functions.funcion_edo import FuncionEDO
from modules.barra_herramientas_grafica import VerticalNavigationToolbar2Tk
from static import style


class EcuacionesDiferenciales(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def graficar(self):
        x = int(self.valor_x .get())
        S = [int(self.valor_min.get()), int(self.valor_max.get())]

        funciones = FuncionEDO()
        self.ax.clear()
        self.ax.axhline(0)
        funciones.dSdx(x, S)
        x_0, v_0 = S
        S_0 = (x_0, v_0)
        x = np.linspace(0,1,100)
        sol = odeint(funciones.dSdx, y0=S_0, t=x, tfirst=True)
        x_sol = sol.T[0]
        y_sol = sol.T[1]
        self.ax.plot(x, x_sol, label="Solucion x")
        self.ax.plot(x, y_sol, label="Solucion y")
        self.ax.grid(alpha=0.2, lw=1.75, ls="--" )
        
        self.ax.legend(loc="upper left", facecolor=style.BG, edgecolor= style.BG, labelcolor=style.COLOR_BLANCO)
        self.canvas_figura.draw()

        self.ax.plot()

    def calcular_edo(self):
        funciones = FuncionEDO()
        self.texto_alerta_ecuacion.set('')
        self.resultado.set(funciones.calcular(self.valor_ecuacion.get()))

    def verificar_graficar(self):
        try:
            self.graficar()
        except (ValueError, TypeError):
            self.texto_alerta_grafica.set('No se puede graficar')

    def verificar(self):
        try:
            self.calcular_edo()
        except (IndexError, SyntaxError):
            self.texto_alerta_ecuacion.set('Ingrese una ecuación correcta')


    def init_widgets(self):

        # label para el titulo
        tk.Label(
            self,
            text="Ecuaciones Diferenciales",
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, pady=(20, 30))

        # frame para resolucion de ecuaciones diferenciales
        input_frame_1 = tk.Frame(self, background=style.BG)
        input_frame_1.columnconfigure(0, weight=1)
        input_frame_1.columnconfigure(1, weight=1)
        input_frame_1.columnconfigure(2, weight=1)
        input_frame_1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #label ecuacion
        tk.Label(input_frame_1,
                 text='Ecuación',
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column = 0, pady=(20,10))
        
        #label ecuacion
        tk.Label(input_frame_1,
                 text='Resultado',
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column = 0, pady=(20,10))
        
        # entry para el valor de la ecuacion
        borde_entry_1 = tk.LabelFrame(input_frame_1, **style.STYLE_ENTRY_BORDER)
        borde_entry_1.grid(row=0, column=1, pady=(20, 10), sticky=tk.EW)

        self.valor_ecuacion = tk.StringVar()
        entry_valor_ecuacion = tk.Entry(borde_entry_1,
                                 textvariable=self.valor_ecuacion,
                                 **style.STYLE_ENTRY,
                                 width=6,
                                 )
        entry_valor_ecuacion.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=475)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 475, 0, **style.STYLE_CANVAS_LINE)

        self.texto_alerta_ecuacion = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_ecuacion,
                 **style.STYLE_WARNING,
                 ).pack()
        
        # entry desactivado para el resultado
        borde_entry_2 = tk.LabelFrame(input_frame_1, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=1, column=1, pady=(10, 0), sticky=tk.EW)

        self.resultado = tk.StringVar()
        entry_resultado = tk.Entry(borde_entry_2,
                                   textvariable=self.resultado,
                                   **style.STYLE_ENTRY_DES,
                                   )
        entry_resultado.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_2 = tk.Canvas(
            borde_entry_2, **style.STYLE_CANVAS, width=475)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 475, 0, **style.STYLE_CANVAS_LINE)
        
        # boton para calcular
        borde_entry_3 = tk.LabelFrame(input_frame_1, **style.STYLE_ENTRY_BORDER)
        borde_entry_3.grid(row=0, rowspan=2, column=2)

        borde_1 = tk.LabelFrame(borde_entry_3, **style.STYLE_BUTTON_BORDER)
        borde_1.pack()

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.verificar,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)



        input_frame_2 = tk.Frame(self, background=style.BG)
        input_frame_2.columnconfigure(0, weight=1)
        input_frame_2.columnconfigure(1, weight=1)
        input_frame_2.columnconfigure(2, weight=1)
        input_frame_2.columnconfigure(3, weight=1)
        input_frame_2.columnconfigure(4, weight=1)
        input_frame_2.columnconfigure(5, weight=1)
        input_frame_2.columnconfigure(6, weight=1)
        input_frame_2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # label valor x
        tk.Label(input_frame_2,
                 text="Valor de x:",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=(20, 0))
        
        # label valor min
        tk.Label(input_frame_2,
                 text="; min",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=2, pady=(20, 0))
        
        # label valor min
        tk.Label(input_frame_2,
                 text="; max",
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=4, pady=(20, 0))
        
        # entry para el valor x
        borde_entry_4 = tk.LabelFrame(input_frame_2, **style.STYLE_ENTRY_BORDER)
        borde_entry_4.grid(row=0, column=1, padx=(20, 0))

        self.valor_x = tk.StringVar()
        entry_valor_x = tk.Entry(borde_entry_4,
                                 textvariable=self.valor_x,
                                 **style.STYLE_ENTRY,
                                 width=6,
                                 )
        entry_valor_x.pack(side=tk.TOP, fill=tk.X, expand = True)

        canvas_linea_4 = tk.Canvas(
            borde_entry_4, **style.STYLE_CANVAS, width=50)
        canvas_linea_4.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_4.create_line(0, 0, 50, 0, **style.STYLE_CANVAS_LINE)
        
        # entry para el valor min
        borde_entry_5 = tk.LabelFrame(input_frame_2, **style.STYLE_ENTRY_BORDER)
        borde_entry_5.grid(row=0, column=3, padx=(20, 0))

        self.valor_min = tk.StringVar()
        entry_valor_min = tk.Entry(borde_entry_5,
                                 textvariable=self.valor_min,
                                 **style.STYLE_ENTRY,
                                 width=6,
                                 )
        entry_valor_min.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_5= tk.Canvas(
            borde_entry_5, **style.STYLE_CANVAS, width=50)
        canvas_linea_5.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_5.create_line(0, 0, 50, 0, **style.STYLE_CANVAS_LINE)

        # entry para el valor max
        borde_entry_6 = tk.LabelFrame(input_frame_2, **style.STYLE_ENTRY_BORDER)
        borde_entry_6.grid(row=0, column=5, padx=(20, 0))

        self.valor_max = tk.StringVar()
        entry_valor_max = tk.Entry(borde_entry_6,
                                 textvariable=self.valor_max,
                                 **style.STYLE_ENTRY,
                                 width=6,
                                 )
        entry_valor_max.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_6 = tk.Canvas(
            borde_entry_6, **style.STYLE_CANVAS, width=50)
        canvas_linea_6.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_6.create_line(0, 0, 50, 0, **style.STYLE_CANVAS_LINE)
        
        # boton para graficar
        borde_entry_7 = tk.LabelFrame(input_frame_2, **style.STYLE_ENTRY_BORDER)
        borde_entry_7.grid(row=0, column=6)

        borde_2 = tk.LabelFrame(borde_entry_7, **style.STYLE_BUTTON_BORDER)
        borde_2.pack()

        boton_calculo = tk.Button(borde_2,
                                  text="Graficar",
                                  **style.STYLE_BUTTON,
                                  command= self.verificar_graficar,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.X, expand=True)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)

        # label alerta
        self.texto_alerta_grafica = tk.StringVar()
        tk.Label(borde_entry_7,
                 textvariable=self.texto_alerta_grafica,
                 **style.STYLE_WARNING
                 ).pack()
        
        output_frame = tk.Frame(self, background=style.BG)
        output_frame.pack(side=tk.TOP, fill=tk.BOTH,
                          expand=True, padx=10, pady=(0,10))
        
        # Gráfica
        self.fig = matplotlib.figure.Figure(facecolor=style.BG)
        self.ax = self.fig.add_subplot(facecolor=style.BG)

        self.ax.spines['bottom'].set_color(style.COLOR_AQUA)
        self.ax.spines['bottom'].set_linewidth(2)
        self.ax.spines['left'].set_color(style.COLOR_AQUA)
        self.ax.spines['left'].set_linewidth(2)
        self.ax.spines['right'].set_color(style.COLOR_AQUA)
        self.ax.spines['right'].set_linewidth(2)
        self.ax.spines['top'].set_color(style.COLOR_AQUA)
        self.ax.spines['top'].set_linewidth(2)

        self.ax.tick_params(axis='both', colors=style.COLOR_AQUA,
                            labelsize=10, size=7, width=2)

        self.canvas_figura = FigureCanvasTkAgg(self.fig, master=output_frame)
        self.canvas_figura.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,
                                                expand=True)
        
        toolbar = VerticalNavigationToolbar2Tk(self.canvas_figura, output_frame)
        toolbar.config(background=style.COLOR_MAGENTA_CLARO, bd=3, relief="flat")
        toolbar.winfo_children()[0].config(**style.STYLE_BUTTON_TOOLBAR)
        toolbar.winfo_children()[1].config(**style.STYLE_BUTTON_TOOLBAR)
        toolbar.winfo_children()[2].config(**style.STYLE_BUTTON_TOOLBAR)
        toolbar.winfo_children()[3].config(**style.STYLE_BUTTON_TOOLBAR)
        toolbar.winfo_children()[4].config(state="disable", cursor="", background=style.COLOR_MAGENTA_CLARO)
        toolbar.winfo_children()[5].config(state="disable", cursor="", background=style.COLOR_MAGENTA_CLARO)
        toolbar.update()
        toolbar.pack(side=tk.LEFT, fill= tk.Y, pady=15)