class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    
def NthPreorder(root, n):
    result = _NthPreorder(root)
    if len(result)>=n:
        return result[n-1]
    return "no 8-th element"
    
def _NthPreorder(root):
    if root is None:
        return []
    return  [root.key]+ _NthPreorder(root.left)+_NthPreorder(root.right)


items = Node(5)
items.left = Node(6)
items.right = Node(7)
items.left.left = Node(8)
items.left.right = Node(9)

print(NthPreorder(items,3)) #== 8
print(NthPreorder(items,6)) #== "no 6-th element"