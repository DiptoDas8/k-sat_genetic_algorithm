from random import uniform

def bit_flip_mutation(gene):
    l = len(gene)
    p = 1.0/l

    for i in range(l):
        if p >= uniform(0.0, 1.0):
            gene[i] = (gene[i]+1)%2

    return gene
