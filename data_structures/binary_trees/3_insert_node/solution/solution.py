#Write your solutions here
class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    


    def insert(self,key):
        if self is not None:
            return self._insert(self,key)
        
    def _insert(self,node,key):
        if node.left is None:
            new_node = Node(key)
            node.left = new_node
        self._insert(node.left,key)
        self._insert(node.right,key)
        return node


        
    

items = Node(6)
items.left = Node(11)
items.right = Node(9)
items.left.left = Node(7)
items.right.left = Node(15)
items.right.right = Node(8)
items.insert(12)