#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classLayer.py                                                            *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

import numpy as np
from classNeuron import Neuron

class Layer:
    def __init__(self, weights, bias, type_input = False):
        if weights.shape[0] != bias.shape[0]:
            raise ValueError('Number of nodes must match length of bias vector')
        self.n_neurons = weights.shape[0]
        self.type_input = type_input
        if type_input:
            self.n_inputs = self.n_neurons
        else:
            self.n_inputs = weights.shape[1]
        weights = np.clip(weights,-10, 10)
        bias = np.clip(bias, -10, 10)
        self.neurons = [Neuron(weights[i,:],bias[i]) for i in range(self.n_neurons)]


    def evaluate(self, inputs):
        if inputs.shape[0] != self.n_inputs:
            raise ValueError('Input size must match layer size')
        if self.type_input:
            return np.array([self.neurons[i].forward(inputs[i]) for i in range(self.n_neurons)])
        else:
            return np.array([self.neurons[i].forward(inputs) for i in range(self.n_neurons)])


    def get_layer_size(self):
        return self.n_neurons


    def get_input_size(self):
        return self.n_inputs

