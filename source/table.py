import numpy as np
from point import Point


def generate_table(range=(-50, 50), N=10, seed=420):
    np.random.seed(seed)
    table = np.random.randint(range[0], high=range[1], size=(4, N))
    return table


def get_sum_of_elements(table):
    return np.sum(table)


def table_to_vec(table):
    vec = table.flatten()
    vec = vec.tolist()
    i = 0
    for j in range(len(vec)):
        vec[j] = Point(vec[j], i, j % table.shape[1], max_col=table.shape[1])
        if j % table.shape[1] == table.shape[1] - 1:
            i += 1

    return vec


def get_negative_values(table):
    vec = table_to_vec(table)
    negative_values = []
    for item in vec:
        if item.get_value() < 0:
            negative_values.append(item)
    return negative_values


def get_result(table, hidden_coords):
    new_table = np.copy(table)
    for item in hidden_coords:
        new_table[item[1], item[0]] = 0
    return new_table