#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classGame2048.py                                                         *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by Yuliia Hetman                            *#
#*                                                                            *#
#* ************************************************************************** *#

import numpy as np
import math
from utils import *

class Game2048:
    def __init__(self, n, random_stream = np.random.RandomState()):
        self.n = n
        self.game_state = np.zeros([n, n])
        self.random_stream = random_stream
        self.generate_tile()
        self.generate_tile()


    def get_tile(self, row, col):
        return self.game_state[row][col]


    def get_empty_idx(self):
        idx = np.arange(self.n**2)
        return idx[np.reshape(self.game_state, -1) == 0]


    def generate_tile(self):
        tile_idx = self.random_stream.choice(self.get_empty_idx(), 1)
        tile_val = 2 if self.random_stream.random_sample() < RANDOMNESS else 4
        self.place_tile(tile_idx, tile_val)


    def place_tile(self, idx, val):
        if idx.shape[0] == 1: self.game_state[tuple(self.idx_lin2vec(idx))] = val
        elif idx.shape[0] == 2: self.game_state[idx] = val
        else: raise ValueError('Invalid array size')


    def idx_lin2vec(self, idx_lin):
        x = math.floor(idx_lin / self.n)
        y = idx_lin - x * self.n
        return [x, y]


    def idx_vec2lin(self, idx_vec):
        return self.n * idx_vec[0] + idx_vec[1]


    def show_state(self):
        print(self.game_state)



    def swipe(self, swipe_direction):
        old_state = np.copy(self.game_state)
        if swipe_direction == 'left':
            for i in range(self.n):
                self.move_col(i, -1)
        elif swipe_direction == 'right':
            for i in range(self.n - 1, -1, -1):
                self.move_col(i, 1)
        elif swipe_direction == 'up':
            for i in range(self.n):
                self.move_row(i, -1)
        elif swipe_direction == 'down':
            for i in range(self.n-1, -1, -1):
                self.move_row(i, 1)
        else: raise ValueError('invalid direction')
        if not np.array_equal(old_state,self.game_state):
            self.generate_tile()


    def check_for_game_over(self):
        if np.any(self.game_state == 2048):
            return "WIN"
        if self.is_board_full() and self.check_for_valid_moves() == False:
            return "LOSE"
        else:
            return None


    def check_for_valid_moves(self):
        valid_moves = False
        old_state = np.copy(self.game_state)
        for move in ['up','down','left','right']:
            self.swipe(move)
            if not np.array_equal(old_state, self.game_state):
                valid_moves = True
                self.game_state = np.copy(old_state)
                break
            else:
                self.game_state = np.copy(old_state)
        return valid_moves



    def is_board_full(self):
        return np.all(self.game_state != 0)


    def move_row(self, row, direction):
        for i in range(self.n):
            self.move_val(np.array([row, i]), np.array([direction, 0]))


    def move_col(self, col, direction):
        for i in range(self.n):
            self.move_val(np.array([i, col]), np.array([0, direction]))


    def move_val(self, idx, vec):
        val = self.game_state[idx[0], idx[1]]
        blocked = False
        while not blocked:
            move_type = self.check_move_type(idx, vec)
            if move_type == 0:
                blocked = True
            elif move_type == 1:
                idx_new = idx + vec
                self.game_state[idx[0], idx[1]] = 0
                self.game_state[idx_new[0], idx_new[1]] = val
                idx = idx_new
            else:
                idx_new = idx + vec
                self.game_state[idx[0], idx[1]] = 0
                self.game_state[idx_new[0], idx_new[1]] += val
                blocked = True


    def check_move_type(self,idx,vec):
        moved_idx = idx + vec
        if np.any(np.logical_or(moved_idx < 0, moved_idx >= self.n)):
            return 0
        adjacent_val = self.game_state[moved_idx[0], moved_idx[1]]
        current_val = self.game_state[idx[0], idx[1]]
        if adjacent_val == 0:
            return 1
        elif adjacent_val == current_val:
            return 2
        else:
            return 0


    def get_state(self, flat=False):
        if flat:
            return self.game_state.reshape(-1)
        else:
            return self.game_state

        
    def get_score(self):
        max_val = np.max(np.max(self.game_state))
        board_sum = np.sum(np.sum(self.game_state))
        score = MAX_SCORE_SCALE * max_val + SUM_SCORE_SCALE * board_sum
        return score

