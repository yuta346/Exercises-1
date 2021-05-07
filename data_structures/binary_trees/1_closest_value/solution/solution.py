
class Node:
    def __init__(self,key=None,left=None,right=None):
        self.key = key  
        self.left = left
        self.right = right
    
def closest_value(node, target):
    result = node.key
    prev = []
    while node is not None:
        if abs(node.key-target) <= abs(result-target):
            result = node.key
            prev.append(result)
        if target < node.key:
            node = node.left
        else: node = node.right
    return min(prev)

root = Node(6)
root.left = Node(4)
root.right = Node(10)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(8)
root.right.right = Node(12)
print(closest_value(root, 7)) == 6