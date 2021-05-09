class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    
def NthInorder(root, n):
    result = _NthInorder(root)
    if len(result)>=n:
        return result[n-1]
    return f"no {n}-th element"
    
def _NthInorder(root):
    if root is None:
        return []
    return  _NthInorder(root.left)+[root.key]+_NthInorder(root.right)


items = Node(5)
items.left = Node(6)
items.right = Node(7)
items.left.left = Node(8)
items.left.right = Node(9)

print(NthInorder(items,4)) #== 5
# print(NthInorder(items,6)) #== "no 6-th element