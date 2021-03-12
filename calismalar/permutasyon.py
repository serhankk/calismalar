from itertools import permutations

def permutation(iterable, test):
    permutation_list = permutations(iterable, test)
    return list(permutation_list)
