#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classHumanGUI.py                                                         *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by Yuliia Hetman                            *#
#*                                                                            *#
#* ************************************************************************** *#

import tkinter as tk
from classHumanBoard import HumanBoard
from classGame2048 import Game2048

class HumanGUI(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        self.game = Game2048(4)
        self.board = HumanBoard(self, self.game)
        self.board.pack(side = tk.LEFT, padx = 1, pady = 1)
        self.focus_set()
        self.bind('<Left>', lambda event: self.board.perform_move("left"))
        self.bind('<Up>', lambda event: self.board.perform_move("up"))
        self.bind('<Down>', lambda event: self.board.perform_move("down"))
        self.bind('<Right>', lambda event: self.board.perform_move("right"))
