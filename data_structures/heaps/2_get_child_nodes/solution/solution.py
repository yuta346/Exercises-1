
def get_child_nodes(heap,index):
    result = []
    left_index = 2*index+1
    right_index = 2*index+2
    if len(heap)>left_index:
        result.append(heap[left_index])
    if len(heap)>right_index:
        result.append(heap[right_index])
    return result

print(get_child_nodes([2, 3, 4, 5, 10], 0))
print(get_child_nodes([2, 3, 4, 5, 10], 3))
print(get_child_nodes([2, 3, 4, 5, 10, 11], 2))