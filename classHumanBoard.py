#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classHumanBoard.py                                                       *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by Yuliia Hetman                            *#
#*                                                                            *#
#* ************************************************************************** *#

import tkinter as tk
from classBoard import Board


class HumanBoard(Board):
    def __init__(self,master,game):
        Board.__init__(self, master, game)


    def perform_move(self, move_dir):
        self.game.swipe(move_dir)
        self.update_tiles()
        game_over_state = self.game.check_for_game_over()
        if game_over_state: print(game_over_state)