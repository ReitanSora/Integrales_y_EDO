
import sympy
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


class FuncionIntegrales:

    sympy.init_printing(use_latex='mathjax')
    x = sympy.Symbol('x')
    y = sympy.Function('y')

    def integralx(self, expresion: str):
        x = sympy.symbols('x')  # Declarar variable independiente
        fun_escrita = expresion
        h = parse_expr(fun_escrita)
        integral = sympy.integrate(h, x)
        return integral

    def integraly(self, expresion: str):
        y = sympy.symbols('y')  # Declarar variable independiente
        fun_escrita2 = expresion
        g = parse_expr(fun_escrita2)
        integral = sympy.integrate(g, y)
        return integral
