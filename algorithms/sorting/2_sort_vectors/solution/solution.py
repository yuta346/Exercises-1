import math

def sort_vectors(vector_lst):
    return sorted(vector_lst, key = lambda x: magnitude(x))


def magnitude(tups):
    return math.sqrt((tups[0][0] - tups[1][0])**2 + (tups[0][1] - tups[1][1])**2)





vector_lst = [((1, 3), (2, 6)), ((1, 5), (3, 4)), ((2, 6), (2, 9))]
print(sort_vectors(vector_lst)) 