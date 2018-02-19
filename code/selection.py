from driver import assess_fitness
from random import randint

def tournament_selection(population):
    t = 5 #tournament size

    best = population[randint(0, len(population)-1)]
    for i in range(1, t):
        next = population[randint(0, len(population)-1)]
        if assess_fitness(next) > assess_fitness(best):
            best = next

    return best
