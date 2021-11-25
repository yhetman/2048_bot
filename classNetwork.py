#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classNetwork.py                                                          *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

import numpy as np
from classLayer import Layer


class Network:
    def __init__(self, weights, bias):
        self.n_layers = len(weights)
        L0 = [Layer(weights[0],bias[0],True)]
        L1 = [Layer(weights[i],bias[i]) for i in range(1, self.n_layers)]
        self.layers = L0 + L1


    def evaluate(self, inputs):
        if inputs.shape[0] != self.layers[0].get_input_size():
            raise ValueError('Incorrectly sized input')
        intermediate_values = [inputs]
        for i in range(1, self.n_layers + 1):
            intermediate_values.append(self.layers[i - 1].evaluate(intermediate_values[i - 1]))
        return intermediate_values[-1]
