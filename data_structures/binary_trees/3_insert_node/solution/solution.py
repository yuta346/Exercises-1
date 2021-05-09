#Write your solutions here
class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    


    def insert(self,key):
        result = Preorder(self)
        for node in result:
            if node.left is None:
                new_node = Node(key)
                node.left = new_node
                return 
            elif node.right is None:
                new_node = Node(key)
                node.right = new_node
                return 


def Preorder(root):
    if root is None: 
        return []
    return [root]+ Preorder(root.left)  + Preorder(root.right)
           

items = Node(6)
items.left = Node(11)
items.right = Node(9)
items.left.left = Node(7)
items.right.left = Node(15)
items.right.right = Node(8)
items.insert(12)