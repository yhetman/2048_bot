#*                                                                            *#
#*   sampling.py                                                              *#
#*                                                                            *#
#*   By: Yuliia Hetman <juliagetman5@knu.ua>                                  *#
#*                                                                            *#
#*   Created: 2021/11/20 13:09:32 by Yuliia Hetman                            *#
#*   Updated: 2021/11/25 20:41:39 by Yuliia Hetman                            *#
#*                                                                            *#
#* ************************************************************************** *#


import numpy as np

def random_step_selection(scores,selection_points):
    idx_to_keep = []
    cummulateive_scores = np.cumsum(scores)
    count = 0
    for P in selection_points:
        while cummulateive_scores[count] < P:
            count += 1
        idx_to_keep.append(count)
    return np.array(idx_to_keep)


def sampling_without_replacement(population_scores_in,number_to_keep):
    idx_to_keep = []
    population_scores = np.copy(population_scores_in)
    for i in range(number_to_keep):
        selection_point = np.random.uniform(0, sum(population_scores), 1)
        idx = random_step_selection(population_scores, selection_point)
        idx_to_keep = np.append(idx_to_keep, idx)
        population_scores[idx] = 0
    return np.array(idx_to_keep)


def universal_sampling(population_scores, number_to_keep):
    delta =  sum(population_scores) / number_to_keep
    start_point = np.random.uniform(0, delta, 1)
    points = np.array([start_point + i * delta for i in range(number_to_keep - 1)])
    return random_step_selection(population_scores, points)

