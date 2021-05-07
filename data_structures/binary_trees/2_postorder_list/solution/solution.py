class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    

def Postorder(root):
    if root is None: 
        return []
    left_node = Postorder(root.left) 
    right_node = Postorder(root.right)
    return left_node + right_node+ [root.key]
           

items = Node(6)
items.left = Node(4)
items.right = Node(7)
items.left.left = Node(3)
items.left.right = Node(5)
Postorder(items) == [3, 4, 5, 6, 7]
            