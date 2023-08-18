from sympy import *
from sympy.parsing.sympy_parser import parse_expr # Leer función introducida
from tkinter import *
import sympy
import numpy as np



class FuncionEDO:

    sympy.init_printing(use_latex='mathjax')
    x= symbols('x'); 
    y= Function('y')

    def calcular(self, expresion: str):
        x = sympy.Symbol("x")
        y = sympy.Function("y")
        expression = expresion
        expression = expression.replace(" ", "") # remover los espacios en blanco
        expression = expression.replace("dy/dx", "y(x).diff()") # derivada de primer orden
        expression = expression.replace("d2y/dx2", "y(x).diff(x, 2)") # derivada de segundo orden
        expression = expression.replace("d3y/dx3", "y(x).diff(x, 3)") # derivada de tercer orden
        expression_split = expression.split("=")

        ecuacion_diferencial = sympy.Eq(parse_expr(expression_split[0]), parse_expr(expression_split[1]))
        
        res = sympy.dsolve(ecuacion_diferencial, y(x))
        res_str = str(res)
        res_str = res_str.replace("Eq(", "")
        res_str = res_str.replace(", ", " = ")
        res_str = res_str[:-1]
        
        return res_str
    
    def dSdx(self, x, S):
        x, v = S
        return [v, -v**2 + np.sin(x)]
    