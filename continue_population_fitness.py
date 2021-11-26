#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   continue_population_fitness.py                                           *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by Yuliia Hetman                            *#
#*                                                                            *#
#* ************************************************************************** *#

import math, copy
import numpy as np
from classNeuron import Neuron
from classNetwork import Network
import numpy as np
from classGame2048 import Game2048
import math
import tkinter as tk
import time
import pickle
import concurrent.futures
from utils import *
from classGeneticLearner import GeneticLearner


gen_to_load = 297
fname = 'models/model_'
generations_per_batch = 1
n_batches = 1000
total_generations = generations_per_batch * n_batches
full_filename = fname+str(gen_to_load)+'.p'
print('Loading ' + full_filename + ' and running ' + str(total_generations) + ' more generations')
try:
    G = load_model_state(full_filename)
except:
    raise ValueError('File does not exist: ' + full_filename)
for i in range(n_batches):
    print("Starting batch "+str(i))
    G.run_n_generations(generations_per_batch)
    gen_num = (1 + i)*generations_per_batch + gen_to_load
    save_model_state(G,fname + str(gen_num) + '.p')
    print("Model " + str(gen_num) + " Saved")

