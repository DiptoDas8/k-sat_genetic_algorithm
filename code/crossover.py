from random import randint
from copy import deepcopy

def one_point_crossover(v, w):
    first_vector = deepcopy(v)
    second_vector = deepcopy(w)
    c = randint(0, len(first_vector)) % len(first_vector)

    for i in range(c, len(first_vector)):
        first_vector[i], second_vector[i] = second_vector[i], first_vector[i]

    return first_vector, second_vector

def two_point_crossover(v, w):
    first_vector = deepcopy(v)
    second_vector = deepcopy(w)
    c = 0
    d = 0
    while c == d:
        c = randint(0, len(first_vector)) % len(first_vector)
        d = randint(0, len(second_vector)) % len(second_vector)

    if c > d:
        c, d = d, c

    for i in range(c, d-1):
        first_vector[i], second_vector[i] = second_vector[i], first_vector[i]

    return first_vector, second_vector
