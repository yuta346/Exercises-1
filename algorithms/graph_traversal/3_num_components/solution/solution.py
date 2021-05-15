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
        if vertex not in visited:
            _num_components(vertex, adj_list,visited)
            count+=1
    return count
        
def _num_components(vertex,adj_list,visited):    
    stack=[vertex]
    while stack:
        current = stack.pop()
        for vertex in range(len(visited)):
            if  adj_list[current][vertex] and visited[vertex]==0:
                visited[vertex]=1
                stack.append(vertex)


print(num_components(adj_matrix3)) == 3
print(num_components(adj_matrix2)) == 2
print(num_components(adj_matrix1)) == 2
