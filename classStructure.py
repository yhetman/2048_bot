#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classStructure.py                                                        *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

import copy
import numpy as np

class Structure:
    def __init__(self, neurons_per_layer):
        self.neurons_per_layer = neurons_per_layer
        self.n_layers = len(self.neurons_per_layer)
        self.n_outputs = self.neurons_per_layer[-1]
        self.n_inputs = self.neurons_per_layer[0]


    def copy(self):
        neurons_per_layer_copy = copy.deepcopy(self.neurons_per_layer)
        return Structure(neurons_per_layer_copy)


    def get_number_of_weights_per_layer(self, n):
        if n == 0: return 2 * self.n_inputs
        return self.neurons_per_layer[n] * (self.neurons_per_layer[n - 1] + 1)


    def get_number_of_inputs_per_layer(self, n):
        if n == 0: return 1
        return self.neurons_per_layer[n - 1]


    def get_number_of_neurons_per_layer(self, n):
        return self.neurons_per_layer[n]


    def get_number_of_outputs(self):
        return self.n_outputs


    def get_number_of_layers(self):
        return self.n_layers



    def get_number_of_inputs(self):
        return self.n_inputs

