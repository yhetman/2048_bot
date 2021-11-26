#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classGame2048GUI.py                                                      *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by Yuliia Hetman                            *#
#*                                                                            *#
#* ************************************************************************** *#

import tkinter as tk
from classBoard import Board
from classHumanGUI import HumanGUI

class Game2048GUI(tk.Frame):
    def __init__(self, master, game):
        tk.Frame.__init__(self, master)
        self.game = game
        self.board = Board(self, self.game)
        self.board.pack(side = tk.LEFT, padx = 1, pady = 1)
        self.focus_set()


    def update_gui(self):
        self.board.update_tiles()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("2048 Game")
    HumanGUI(root).pack()
    root.mainloop()