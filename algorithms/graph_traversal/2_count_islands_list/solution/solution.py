adjacency_list = {
    0: [1,3,5],
    1: [0,1,3,6],
    2: [],
    3: [0,3],
    4: [],
    5: [6],
    6: [3,5]
}
def count_islands(adjacency_List):
    count = 0
    for vertex in list(adjacency_List):
        if adjacency_List[vertex]==[]:
            count+=1
    return count

print(count_islands(adjacency_list)) == 2