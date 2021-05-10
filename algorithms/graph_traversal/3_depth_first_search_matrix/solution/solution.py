matrix = [
        [1, 1, 0, 1],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 0, 0, 1]
    ]
def exists_path(matrix,origin,destination):
    if origin > len(matrix)-1 or destination > len(matrix)-1:
        return False
    visited = [0]*len(matrix)
    stack = [origin]
    while stack:
        current = stack.pop(0)
        for vertex in range(len(visited)):
            if matrix[current][vertex]==1 and visited[vertex]==0:
                visited[vertex]=1
                stack.append(vertex)
    if visited[destination] == 1: 
        return True
    else:
         return False


print(exists_path(matrix, 0, 2)) == True
print(exists_path(matrix, 1, 0)) == True
print(exists_path(matrix, 4, 2)) == False
print(exists_path(matrix, 0, 4)) == False
print(exists_path(matrix, 3, 1)) == False