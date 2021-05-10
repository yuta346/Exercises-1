adjacency_list = {
    0: [1,3,5],
    1: [0,1,3,6],
    2: [],
    3: [0,1,2,3],
    4: [],
    5: [4]
}
def most_neighbours(adjacency_list):
    max_count = 0
    node = 0
    for vertex in adjacency_list:
        if max_count < len(adjacency_list[vertex]):
            max_count = len(adjacency_list[vertex])
            node = vertex
    return node
print(most_neighbours(adjacency_list)) == 1