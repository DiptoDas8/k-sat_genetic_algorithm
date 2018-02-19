from random import randint
from driver import assess_fitness
from selection import tournament_selection
from crossover import one_point_crossover, two_point_crossover
from mutation import bit_flip_mutation


def genetic_algorithm(lines, variables_count):
    popsize = 20

    '''Create initial population'''
    # Keep the members of initial population unique
    init_members = set()
    population = []

    # Size of individual is equal to the number of literals
    l = variables_count
    while len(population) < popsize:
        individual = [randint(0, 1) for i in range(l)]
        individual_str = ''.join(str(e) for e in individual)
        if individual_str not in init_members:
            init_members.add(individual_str)
            population.append(individual)

    '''Repeat until best is found or maximum number of iterations is reached'''
    best = population[randint(0, len(population))]
    max_iteration = 50000
    i = 0
    while (True):
        if i > max_iteration:
            break

        if assess_fitness(best) == len(lines):
            break

        for current_individual in population:
            if assess_fitness(current_individual) > assess_fitness(best):
                best = current_individual

        '''Genetic Operations'''
        # Do
        created_population = []
        for i in range(int(popsize / 2)):
            parent_a = tournament_selection(population)
            parent_b = tournament_selection(population)
            child_a, child_b = one_point_crossover(parent_a, parent_b)
            child_a, child_b = bit_flip_mutation(child_a), bit_flip_mutation(child_b)
            child_c, child_d = two_point_crossover(parent_a, parent_b)
            child_c, child_d = bit_flip_mutation(child_c), bit_flip_mutation(child_d)
            for child in [child_a, child_b, child_c, child_d]:
                created_population.append(child)

        population = created_population

    print(best, assess_fitness(best))
    return best
