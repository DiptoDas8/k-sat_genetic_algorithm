'''This driver.py contains all the steps specific to the problem, in this case the k-sat problem.'''
# print('Hello world')
lines = []
with open('../data/random_ksat.dimacs') as file:
    lines = file.read().splitlines()

lines = lines[2:]
clauses_count = len(lines)
for clause in range(len(lines)):
    current_clause = [int(s) for s in lines[clause].split(' ')]
    current_clause.remove(0)
    lines[clause] = current_clause
literal_per_clause = len(lines[0])-1

variables = set()
for y in lines:
    for x in y:
        if x>0:
            variables.add(abs(x))

# print(lines)

if __name__ == '__main__':
    from ga import genetic_algorithm
    genetic_algorithm(lines, len(variables))


def assess_fitness(individual):
    '''individual consists of 0/1 values and is of size equal to variables count
        where 0th index of individual indicates 1st variable's boolean value
    '''
    fitness_value = 0
    for clause in lines:
        clause_bool_value = False
        for literal in clause:
            variable = abs(literal)
            if literal < 0:
                clause_bool_value = clause_bool_value or not(int_to_bool(individual[variable-1]))
            else:
                clause_bool_value = clause_bool_value or int_to_bool(individual[variable-1])

            if clause_bool_value == True:
                fitness_value += 1
                break

    return fitness_value


def int_to_bool(bit):
    if bit == 0:
        return False
    elif bit == 1:
        return True

