# adj_list = {
#     0: [1,3,5],
#     1: [0,1,3,6],
#     2: [],
#     3: [0,3,5],
#     4: [],
#     5: [6],
#     6: [3,5]
# }

adj_list = {
        0: [1,4,5],
        1: [0,2,3,6],
        2: [0],
        3: [],
        4: [1,5],
        5: [6],
        6: [3,5]
    }

def _hops_away(adj_list,node,num_hops):
    if node > len(adj_list):
        return []
    if num_hops == 0:
        return [node]
    neighbors = []
    for neighbor in adj_list[node]:
        print(neighbor)
        neighbors.extend(hops_away(adj_list, neighbor,num_hops-1))
        print(neighbors)
    return list(set(neighbors))

def hops_away(adj_list,node,num_hops):
    return list(set(_hops_away(adj_list,node,num_hops)))




print(hops_away(adj_list, 0, 2)) == [0, 1, 3, 6, 5]
# hops_away(adj_list, 1, 0) == [1]
# hops_away(adj_list, 7, 4) == []
# hops_away(adj_list, 4, 3) == []