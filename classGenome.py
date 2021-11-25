#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classGenome.py                                                           *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

import numpy as np
from classNetwork import Network
from utils import *


class Genome:
    def __init__(self, structure):
        self.structure = structure
        self.gene_sizes = [self.structure.get_number_of_weights_per_layer(i) for i in range(self.structure.get_number_of_layers())]
        self.gene_start_index = np.cumsum(self.gene_sizes) - self.gene_sizes
        self.genome_length = sum(self.gene_sizes)
        self.dna = SCALE * (np.random.uniform(-SCALE, SCALE, self.genome_length ))


    def copy(self):
        new_structure = self.structure.copy()
        new_dna = self.get_dna()
        new_genome = Genome(new_structure)
        new_genome.set_dna(new_dna)
        return new_genome


    def set_dna(self,dna):
        if len(dna) != self.genome_length:
            raise ValueError('DNA sequence is of incorrect length!')
        self.dna = dna


    def get_structured_genome(self):
        weights = []
        bias = []
        for i in range(self.structure.get_number_of_layers()):
            n_rows = self.structure.get_number_of_neurons_per_layer(i)
            n_cols = self.structure.get_number_of_inputs_per_layer(i)
            gene_end_index = self.gene_start_index[i] + self.gene_sizes[i]
            weight_end_index = gene_end_index - n_rows
            weights_flat = self.dna[self.gene_start_index[i]:weight_end_index]
            bias_flat = self.dna[weight_end_index:gene_end_index]
            weights.append(weights_flat.reshape(n_rows,n_cols))
            bias.append(bias_flat)
        return weights, bias


    def mutate(self,rate):
        mutation_dna = np.random.uniform(-SCALE, SCALE, self.genome_length )
        self.dna = np.array([self.dna[i] if np.random.uniform() > rate else mutation_dna[i] for i in range(self.genome_length)])


    def generate_network(self):
        (weights, bias) = self.get_structured_genome()
        return Network(weights, bias)


    def get_dna(self):
        return np.copy(self.dna)

    def get_length(self):
        return self.genome_length

    def get_structure(self):
        return self.structure


