adj_list = {
    0: [1,3,5],
    1: [0,1,3,6],
    2: [],
    3: [0,3,5],
    4: [],
    5: [6],
    6: [3,5]
}

hops_away(adj_list, 0, 2) == [0, 1, 3, 6, 5]
# hops_away(adj_list, 1, 0) == [1]
# hops_away(adj_list, 7, 4) == []
# hops_away(adj_list, 4, 3) == []