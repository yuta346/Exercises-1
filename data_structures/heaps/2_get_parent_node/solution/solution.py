

def get_parent_node(heap,index):
    if index>=len(heap):
        return f"{index} is not a valid index in the heap"
    if index==0: return heap[0]
    return heap[(index-1)//2]
print(get_parent_node([2,3,4,5,10], 4)) == 3
print(get_parent_node([2,3,4,5,10], 0)) == 2
print(get_parent_node([2,3,4,5,10], 5)) == "5 is not a valid index in the heap"