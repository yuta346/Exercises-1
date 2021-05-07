class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    

def Preorder(root):
    if root is None: 
        return []
    left_node = Preorder(root.left) 
    right_node = Preorder(root.right)
    return [root.key]+left_node + right_node
           
items = Node(6)
items.left = Node(4)
items.right = Node(7)
items.left.left = Node(3)
items.left.right = Node(5)
Preorder(items) == [3, 4, 5, 6, 7]
            