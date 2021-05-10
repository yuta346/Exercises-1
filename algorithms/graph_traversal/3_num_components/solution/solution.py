adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0]
]

def num_components(adj_list):
    visited = [0]*len(adj_list)
    stack=[0]
    while stack:
        current = stack.pop(0)
        for vertex in range(len(visited)):
            if adjacency_matrix[current][vertex] and visited[vertex]==0:
                visited[vertex]=1
                stack.append(vertex)
    return sum(visited)


print(num_components(adjacency_matrix)) == 2
