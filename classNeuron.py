#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classNeuron.py                                                           *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

import math
import numpy as np
from utils import *

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self.fwd_sum = 0


    def forward(self, inputs):
        self.fwd_sum = np.clip(np.sum(self.weights * inputs) + self.bias, -CLIP_LIMIT, CLIP_LIMIT)
        return self.activation_fn()


    def activation_fn(self):
        try:
            return tanh_fn(self.fwd_sum)
        except:
            print(self.fwd_sum)
            raise ValueError("Math Error")



