class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    

def search(root,key):
    if root is None:
        return False
    if root.key == key:
        return True
    elif root.key > key:
        return search(root.left,key)
    else:
        return search(root.right,key)



items = Node(6)
items.left = Node(4)
items.right = Node(9)
items.left.left = Node(3)
items.left.right = Node(5)
items.right.left = Node(7)
items.right.right = Node(11)
print(search(items,11))
print(search(items,8))