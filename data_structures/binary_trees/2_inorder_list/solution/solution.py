class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    

def Inorder(root):
    if root is None: 
        return []
    return Inorder(root.left) + [root.key] + Inorder(root.right)
    

items = Node(6)
items.left = Node(4)
items.right = Node(7)
items.left.left = Node(3)
items.left.right = Node(5)
Inorder(items) == [3, 4, 5, 6, 7]
            
#                         Inorder(11) + [6] + Inorder(9)
#   Inorder(7) + [11] + Inorder(None) + [6] + Inorder(15) + [9] + Inorder(8)
                                      