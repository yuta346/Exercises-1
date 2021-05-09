

def is_leaf(heap,index):
    if index < len(heap) and index >= (len(heap) // 2):
        return True
    return False

print(is_leaf([1, 2, 3, 4, 5, 6, 7 ], 6))
print(is_leaf([1, 2, 3, 4, 5, 6], 1))