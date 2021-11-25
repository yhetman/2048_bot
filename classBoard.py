#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classBoard.py                                                            *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

import tkinter as tk
from classTile import Tile

class Board(tk.Frame):
    def __init__(self, master, game):
        tk.Frame.__init__(self, master)
        self.game = game
        self.n = game.n
        self.tiles = []
        for row in range(self.n):
            row_tiles = []
            for col in range(self.n):
                tile = Tile(self, game.get_tile(row, col))
                tile.grid(row = row, column = col, padx = 1, pady = 1)
                row_tiles.append(tile)
            self.tiles.append(row_tiles)


    def update_tiles(self):
        for row in range(self.n):
            for col in range(self.n):
                self.tiles[row][col].set_state(self.game.get_tile(row, col))
