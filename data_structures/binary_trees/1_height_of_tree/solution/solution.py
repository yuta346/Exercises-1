
class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    

def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height,right_height)


root = Node(6)
root.left = Node(4)
root.right = Node(10)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(8)
root.right.right = Node(12)

print(height(root))