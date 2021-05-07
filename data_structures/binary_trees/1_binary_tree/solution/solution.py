
class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right


left_node = Node(4)
right_node = Node(7)
sample_tree = Node(5,left_node,right_node)