#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   bot_game.py                                                              *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by Yuliia Hetman                            *#
#*                                                                            *#
#* ************************************************************************** *#

from classGeneticLearner import GeneticLearner
from utils import *
import tkinter as tk
import time

fname = 'models/model_241'
n_new_games = 2
G = load_model_state(fname + '.p')
A = G.get_best_agent()
root = tk.Tk()
root.title("2048 Game")
score,win = A.replay_previous_game(root)
print('Agent score: '+str(score)+' Win status: '+ str(win))
time.sleep(0.5)
for i in range(n_new_games):
    score, win = A.play_game(root)
    print('Agent score: ' + str(score) + ' Win status: ' + str(win))
    time.sleep(0.5)

input("Press Enter to end...")