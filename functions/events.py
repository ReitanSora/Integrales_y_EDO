# Tema: Técnicas de diseño de algoritmos - Divide y Vencerás
# Grupo #3
# Integrantes:
# - Stiven Pilca           CI: 1750450262
# - Tulcanza Juan          CI: 1755962485
# Carrera: Ingeniería en Sistemas de la Información
# Paralelo: SI4 - 002
# Fecha de entrega: 19/07/2023

from static import style

# eventos para efecto de hover en botones
def on_enter(e):
    e.widget.config(**style.STYLE_BUTTON_ENTER)


def on_leave(e):
    e.widget.config(**style.STYLE_BUTTON)


def on_enter_nav(e):
    e.widget.config(**style.STYLE_BUTTON_NAV_ENTER)


def on_leave_nav(e):
    e.widget.config(**style.STYLE_BUTTON_NAV)
