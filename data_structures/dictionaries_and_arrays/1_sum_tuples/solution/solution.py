#Completed
def sum_tuples(tlst):
    result = []
    for tup in tlst:
        Sum = sum(list(tup))
        result.append(Sum)
    return result





tlst = [(4, 2), (5, 5), (-1, 2)]
print(sum_tuples(tlst)) #== [6, 10, 1]