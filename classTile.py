#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classTile.py                                                             *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by Yuliia Hetman                            *#
#*                                                                            *#
#* ************************************************************************** *#

import tkinter as tk
from collections import defaultdict

class Tile(tk.Canvas):
    colors = {
        0: '#dddddd',
        2: '#f4f0ed',
        4: '#f7e2d2',
        8: '#f9c59d',
        16: '#efa56b',
        32: '#e86f47',
        64: '#d14314',
        128: '#f7f091',
        256: '#f9f06d',
        512: '#f9ee4a',
        1024: '#ede136',
        2048: '#e5d714'
    }
    color_map = defaultdict(lambda: "#23231f",colors)


    def __init__(self, master, number, size=50):
        tk.Canvas.__init__(self, master, height=size, width=size, background=Tile.color_map[number])
        t = str(int(number)) if not number == 0 else ""
        self.text = tk.Canvas.create_text(self, 25, 25, anchor = tk.CENTER, text = t)

        
    def set_state(self, number):
        self.configure(background = Tile.color_map[number])
        t = str(int(number)) if not number == 0 else ""
        self.itemconfigure(self.text, text = t) 