#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classAgent.py                                                            *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

import math
import numpy as np
from classNetwork import Network
from classGenome import Genome
from classStructure import Structure
from classBoard import Board
from classGame2048 import Game2048
from utils import *
import time


class Agent:
    def __init__(self, nn_structure, genome=None):
        if not type(nn_structure) is Structure:
            raise ValueError('Input structure must be of Structure type')
        self.nn_structure = nn_structure
        self.genome = genome if genome and type(genome) is Genome else Genome(self.nn_structure)
        self.network = self.genome.generate_network()
        self.game_size = math.sqrt(self.nn_structure.get_number_of_inputs())
        self.game_random_state = np.random.RandomState(np.random.randint(10000))
        self.previous_game_random_seed = -1
        if self.game_size % 1 != 0:
            raise ValueError('Input layer must be a square number!')
        else:
            self.game_size = int(self.game_size)


    def get_genome(self):
        return self.genome


    def mutate_genome(self,rate):
        self.genome.mutate(rate)


    def copy(self):
        new_genome = self.genome.copy()
        new_struct = new_genome.get_structure()
        return Agent(new_struct,new_genome)


    def evaluate_network(self, input_state):
        if type(input_state) is list:
            input_state = np.array(input_state)
        if input_state.shape[0] != self.nn_structure.get_number_of_inputs():
            raise ValueError('Input is incorrect size for this Agent')
        return self.network.evaluate(input_state)


    def choose_action(self, input_state):
        weighted_actions = self.evaluate_network(input_state)
        max_idx = np.argmax(weighted_actions)
        if max_idx == 0: action = 'left'
        elif max_idx == 1: action = 'right'
        elif max_idx == 2: action = 'up'
        elif max_idx == 3: action = 'down'
        else: raise ValueError('Invalid action')
        return action


    def check_for_agent_stuck(self, state):
        if np.all(state == self.old_state):
            self.stuck_counter = self.stuck_counter + 1
        else:
            self.stuck_counter = 0
            self.old_state = state
        return (True if self.stuck_counter > 2 else False)
        


    def check_for_game_over(self, game, flat_state):
        end_state = game.check_for_game_over()
        if end_state == 'WIN': return True, True
        elif end_state == 'LOSE': return True, False
        elif self.check_for_agent_stuck(flat_state): return True, False
        else: return False, False



    def play_game(self, gui_root = None):
        self.previous_game_random_seed = self.game_random_state.get_state()
        game = Game2048(self.game_size, random_stream = self.game_random_state)
        game_over = False
        win = False
        self.stuck_counter = 0
        self.old_state = game.get_state(flat = True)

        if gui_root:
            board = Board(gui_root, game)
            board.pack(side = tk.LEFT, padx = 1, pady = 1)

        while not game_over:
            flat_state = np.copy(game.get_state(flat = True))
            action = self.choose_action(flat_state)
            game.swipe(action)
            (game_over,win) = self.check_for_game_over(game, flat_state)
            if gui_root:
                board.update_tiles()
                gui_root.update()
                time.sleep(MOVE_PAUSE_TIME)
        return game.get_score(), win


    def replay_previous_game(self, gui_root):
        if self.previous_game_random_seed != -1:
            old_seed = self.game_random_state.get_state()
            self.game_random_state.set_state(self.previous_game_random_seed)
            score,win = self.play_game(gui_root)
            tmp = self.game_random_state.get_state()
            self.game_random_state.set_state(old_seed)
            return score,win
        else:
            raise ValueError("A game must be played before attempting to replay it!")


