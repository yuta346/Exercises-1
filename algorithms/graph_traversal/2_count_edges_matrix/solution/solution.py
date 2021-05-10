matrix = [
    [0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0]
]
def count_edges(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                total+=1
    return total

count_edges(matrix) == 10