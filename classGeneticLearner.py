#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   classGeneticLearner.py                                                   *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

import numpy as np
from classNetwork import Network
from classStructure import Structure
from classAgent import Agent
import concurrent.futures
from sampling import *
from classGenome import Genome


def crossover(genome1, genome2):
    if genome1.get_length() != genome2.get_length():
        raise ValueError('Genomes are not the same length!')
    n = int(np.random.randint(1, genome1.get_length(), 1))
    dna1 = genome1.get_dna()
    dna2 = genome2.get_dna()
    tmp = np.copy(dna1[n:])
    dna1[n:] = dna2[n:]
    dna2[n:] = tmp
    structure = genome1.get_structure()
    genome3 = Genome(structure)
    genome4 = Genome(structure)
    genome3.set_dna(dna1)
    genome4.set_dna(dna2)
    return genome3, genome4



class GeneticLearner:
    def __init__(self, n_agents, layer_sizes, seed=0):
        np.random.seed(seed)
        self.nn_struct = Structure(layer_sizes)
        self.n_agents = n_agents
        self.agents = [Agent(self.nn_struct) for i in range(self.n_agents)]
        self.agent_scores = []
        self.win = []
        self.survival_rate = 0.5
        self.mutation_rate = 0.001
        self.crossover_rate = 0.7
        self.best_always_survives = True
        self.n_to_keep = int(self.n_agents * self.survival_rate)
        self.n_to_create = self.n_agents - self.n_to_keep
        if self.n_to_create % 2 != 0:
            self.n_to_keep = self.n_to_keep + 1
            self.n_to_create = self.n_to_create - 1
        self.population_fitness_test()


    def run_one_generation(self):
        self.select_survivors()
        self.generate_offspring()
        self.mutate()
        self.population_fitness_test()



    def population_fitness_test(self):
        self.agent_scores = [self.agents[i].play_game() for i in range(self.n_agents)]


    def population_fitness_test_multithread(self):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            futures = [ executor.submit(self.agents[i].play_game) for i in range(self.n_agents)]
            concurrent.futures.wait(futures)
            self.agent_scores = [f.result() for f in futures]


    def select_survivors(self):
        scores = np.array([self.agent_scores[i][0] for i in range(self.n_agents)])
        if self.best_always_survives:
            idx_best = np.argmax(scores)
            scores[idx_best] = 0
            idx_survived = sampling_without_replacement(scores, self.n_to_keep - 1)
            idx_survived = np.append(idx_survived, idx_best )
        else: idx_survived = sampling_without_replacement(scores, self.n_to_keep)
        idx_survived = tuple(idx_survived)
        self.agents = [ self.agents[i] for i in range(self.n_agents) if i in idx_survived]
        self.agent_scores = [ self.agent_scores[i] for i in range(self.n_agents) if i in idx_survived]



    def select_parents(self):
        cur_num_agents = len(self.agent_scores)
        pairs_of_parents_needed = int(self.n_to_create / 2)
        scores = np.array([self.agent_scores[i][0] for i in range(cur_num_agents)])
        return [tuple(sampling_without_replacement(scores, 2)) for i in range(pairs_of_parents_needed)]



    def generate_offspring(self):
        parent_idx = self.select_parents()
        new_generation = []
        for p1idx, p2idx in parent_idx:
            if np.random.uniform() < self.crossover_rate:
                genome1,genome2 = crossover(self.agents[int(p1idx)].get_genome(), self.agents[int(p2idx)].get_genome())
                new_generation = new_generation + [Agent(self.nn_struct,genome1), Agent(self.nn_struct,genome2)]
            else:
                new_generation = new_generation + [self.agents[int(p1idx)].copy(), self.agents[int(p1idx)].copy()]
        self.agents = self.agents + new_generation



    def mutate(self):
        for i in range(self.n_agents):
            self.agents[i].mutate_genome(self.mutation_rate)


    def get_current_generation_statistics(self):
        scores = self.get_score_array()
        return np.max(scores), np.median(scores), np.min(scores)


    def run_n_generations(self, n):
        for i in range(n):
            self.run_one_generation()
            maximum, med, minimum = self.get_current_generation_statistics()
            print("Generation " + str(i) + " - maximum: " + str(maximum) + "  median: " + str(med) + " minimum: " + str(minimum))


   def get_score_array(self):
        return np.array([self.agent_scores[i][0] for i in range(self.n_agents)])


    def get_best_agent(self):
        scores = self.get_score_array()
        idx = np.argmax(scores)
        return self.agents[idx]

    def get_worst_agent(self):
        scores = self.get_score_array()
        idx = np.argmin(scores)
        return self.agents[idx]

    def get_median_agent(self):
        scores = self.get_score_array()
        median = np.median(scores)
        median_idx = np.argmax(scores == median) 
        return self.agents[median_idx]