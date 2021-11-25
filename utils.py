#*                                                                            *#
#*   utils.py                                                                 *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#


import math
import pickle

MOVE_PAUSE_TIME = 0.15
RANDOMNESS = 0.75
MAX_SCORE_SCALE = 10
SUM_SCORE_SCALE = 1
SCALE = 1
CLIP_LIMIT = 300


def sigmoid_fn(x):
    return 1.0 / (1.0 + math.exp(-x))


def tanh_fn(x):
    return 2 * sigmoid_fn(2 * x) - 1


def save_model_state(model, fname):
    pickle.dump(model, open(fname, "wb"))


def load_model_state(fname):
    return pickle.load(open(fname, "rb"))

