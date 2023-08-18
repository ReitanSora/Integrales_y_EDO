
import tkinter as tk
from tkinter import ttk
from functions import events as event
from functions.funcion_integrales import FuncionIntegrales
from static import style


class Integral(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background=style.BG)
        self.init_widgets()

    def calcular(self):
        self.texto_alerta_integral.set('')
        funciones = FuncionIntegrales()
        if self.seleccion.get() == 'x':
            self.texto_alerta_variable.set('')
            self.resultado.set(funciones.integralx(self.valor_integral.get()))
        elif self.seleccion.get() == 'y':
            self.texto_alerta_variable.set('')
            self.resultado.set(funciones.integraly(self.valor_integral.get()))
        else:
            self.texto_alerta_variable.set('Elija una variable para integrar')

    def verificar(self):
        try:
            self.calcular()
        except (ValueError, TypeError, SyntaxError):
            self.texto_alerta_integral.set('Ingrese una integral válida')

    def init_widgets(self):
        # label titulo
        tk.Label(
            self,
            text="Integrales",
            **style.STYLE_TITTLE,
        ).pack(side=tk.TOP, fill=tk.X, pady=(20, 30))

        # frame para el ingreso de datos y presentación de resultado
        input_frame = tk.Frame(self, background=style.BG)
        input_frame.columnconfigure(0, weight=1)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(2, weight=1)
        input_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # label integral
        tk.Label(input_frame,
                 text='Integral',
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=0, column=0, pady=(20, 10))

        # label tipo
        tk.Label(input_frame,
                 text='Variable\na integrar',
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=1, column=0, pady=(30, 20))

        # label resultado
        tk.Label(input_frame,
                 text='Resultado',
                 **style.STYLE_SUBTITTLE,
                 ).grid(row=2, column=0, pady=(20, 10))

        # entry para el valor de la integral
        borde_entry_1 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_1.grid(row=0, column=1, pady=(20, 10), sticky=tk.EW)

        self.valor_integral = tk.StringVar()
        entry_valor_integral = tk.Entry(borde_entry_1,
                                        textvariable=self.valor_integral,
                                        **style.STYLE_ENTRY,
                                        )
        entry_valor_integral.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_1 = tk.Canvas(
            borde_entry_1, **style.STYLE_CANVAS, width=450)
        canvas_linea_1.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_1.create_line(0, 0, 450, 0, **style.STYLE_CANVAS_LINE)

        self.texto_alerta_integral = tk.StringVar()
        tk.Label(borde_entry_1,
                 textvariable=self.texto_alerta_integral,
                 **style.STYLE_WARNING,
                 ).pack()

        # variable que guardará el valor escogido por el usuario
        self.seleccion = tk.StringVar()

        opciones = [
            "Seleccione",
            "x",
            "y"
        ]

        self.option_add('*TCombobox*Listbox*Background',
                        style.COLOR_MAGENTA_NORMAL)
        self.option_add('*TCombobox*Listbox*Foreground', style.COLOR_BLANCO)
        self.option_add('*TCombobox*Listbox*selectBackground',
                        style.COLOR_MAGENTA_CLARO)
        self.option_add('*TCombobox*Listbox*selectForeground',
                        style.COLOR_BLANCO)
        self.option_add('*TCombobox*Listbox*justify', 'center')
        self.option_add('*TCombobox*Listbox*font', ("Corbel", '14', "bold"))
        self.seleccion.set(opciones[0])

        estilo = ttk.Style()
        estilo.theme_use('alt')
        estilo.configure('TCombobox',
                         background=style.COLOR_MAGENTA_CLARO,
                         fieldbackground=style.COLOR_MAGENTA_NORMAL,
                         darkcolor=style.BG,
                         lightcolor=style.BG,
                         foreground="#FFF",
                         highlightthickness=0,
                         highlightcolor=style.COLOR_MAGENTA_NORMAL,
                         borderwidth=0,
                         relief='flat'
                         )

        estilo.map('TCombobox', fieldbackground=[
                   ('readonly', style.COLOR_MAGENTA_NORMAL)])
        estilo.map('TCombobox', selectbackground=[
                   ('readonly', style.COLOR_MAGENTA_NORMAL)])

        borde_entry_2 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_2.grid(row=1, column=1, pady=(30, 20))

        self.drop = ttk.Combobox(borde_entry_2, values=opciones, justify='center', font=(
            "Corbel", 14, "bold"), state='readonly', textvariable=self.seleccion)
        self.drop.current(0)
        self.drop.pack()
        self.drop.bind('<<ComboboxSelected>>', )

        self.texto_alerta_variable = tk.StringVar()
        tk.Label(borde_entry_2,
                 textvariable=self.texto_alerta_variable,
                 **style.STYLE_WARNING,
                 ).pack()

        # entry desactivado para mostrar el resultado
        borde_entry_3 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_3.grid(row=2, column=1, pady=(20, 10), sticky=tk.EW)

        self.resultado = tk.StringVar()
        entry_resultado = tk.Entry(borde_entry_3,
                                   textvariable=self.resultado,
                                   **style.STYLE_ENTRY_DES
                                   )
        entry_resultado.pack(side=tk.TOP, fill=tk.X, expand=True)

        canvas_linea_2 = tk.Canvas(
            borde_entry_3, **style.STYLE_CANVAS, width=450)
        canvas_linea_2.pack(side=tk.TOP, anchor=tk.CENTER)
        canvas_linea_2.create_line(0, 0, 450, 0, **style.STYLE_CANVAS_LINE)

        # boton para calcular
        borde_entry_4 = tk.LabelFrame(input_frame, **style.STYLE_ENTRY_BORDER)
        borde_entry_4.grid(row=0, rowspan=3, column=2)

        borde_1 = tk.LabelFrame(borde_entry_4, **style.STYLE_BUTTON_BORDER)
        borde_1.pack()

        boton_calculo = tk.Button(borde_1,
                                  text="Calcular",
                                  **style.STYLE_BUTTON,
                                  command=self.verificar,
                                  )
        boton_calculo.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        boton_calculo.bind('<Enter>', event.on_enter)
        boton_calculo.bind('<Leave>', event.on_leave)
