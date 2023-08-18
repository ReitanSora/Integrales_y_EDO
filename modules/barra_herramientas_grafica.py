
import tkinter as tk

from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk


class VerticalNavigationToolbar2Tk(NavigationToolbar2Tk):
    def __init__(self, canvas, window):
        super().__init__(canvas, window, pack_toolbar=False)
        self.toolitems = (
            ('Home', 'Vista predeterminada', 'home', 'home'),
            ('Pan', 'Mover', 'move', 'pan'),
            ('Zoom', 'Zoom +', 'zoom_to_rect', 'zoom'),
            ('Save', 'Guardar imágen', 'filesave', 'save_figure')
        )
        NavigationToolbar2Tk.__init__(self, canvas, window)

    # override _Button() to re-pack the toolbar button in vertical direction
    def _Button(self, text, image_file, toggle, command):
        b = super()._Button(text, image_file, toggle, command)
        # re-pack button in vertical direction
        b.pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=(0,2))
        return b
    
    # disable showing mouse position in toolbar
    def set_message(self, s):
        pass

    
