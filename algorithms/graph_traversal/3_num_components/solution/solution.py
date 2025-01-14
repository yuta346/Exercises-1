adj_matrix3 = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

adj_matrix2 = [
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]

adj_matrix1 = [
        [0, 1, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ]

def num_components(adj_list):
    visited = [0]*len(adj_list)
    count = 0
    for vertex in range(len(visited)):
        if visited[vertex] == 0:
            dfs(vertex, adj_list, visited)
            count += 1
    return count

def dfs(vertex, adj_list, visited):    
    stack = [vertex]
    while stack:
        current = stack.pop()
        for vertex in range(len(adj_list[0])):
            if  adj_list[current][vertex] and visited[vertex] == 0:
                visited[vertex] = 1
                stack.append(vertex)


print(num_components(adj_matrix3)) == 3
print(num_components(adj_matrix2)) == 1
print(num_components(adj_matrix1)) == 2
