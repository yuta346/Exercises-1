class Tree:
  def __init__(self, root_node=None):
      self.root_node = root_node

class TreeNode:
  def __init__(self, value, left=None, right=None):
      self.value = value
      self.left = left
      self.right = right


def is_complete(tree):
    count = count_node(tree.root_node)
    print(count)
    # return _is_complete(tree.root_node)

# def _is_complete(root):
#     if root is None:
#         return True
    

def count_node(root):
    if root is None:
        return 0
    return count_node(root.left)+count_node(root.right)+1

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3, n1, n2)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6, n4, n5)
n7 = TreeNode(7, n3, n6)
tree = Tree(n7)
# print(tree.root_node.left.value)
is_complete(tree)
# is_complete(tree) == True