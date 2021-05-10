############
# Question 1:
############

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root_node=None):
        self.root_node = root_node

my_tree = Tree()
my_tree = TreeNode(4)
my_tree.left = TreeNode(2)
my_tree.right = TreeNode(6)
my_tree.left.left = TreeNode(1)
my_tree.left.right = TreeNode(3)
my_tree.right.left = TreeNode(5)
my_tree.right.right = TreeNode(7)
print(my_tree.value)
print(my_tree.left.value)
print(my_tree.right.right.value)

############
#Question 2:
############

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    @classmethod
    def from_range(cls, start, end):
        if start > end:
            return cls()
        current_node = ListNode(start)
        rest_of_the_list = cls.from_range(start+1, end)
        current_node.next = rest_of_the_list.head_node
        rest_of_the_list.head_node = current_node
        return rest_of_the_list

    def remove_tail(self):
        if self.head_node is None:
            return None
        curr = self.head_node
        while curr.next.next:
           curr = curr.next
        curr.next = None

    def display(self):
        curr = self.head_node
        while curr.next:
            print(curr.value)
            curr = curr.next

myList = LinkedList.from_range(1,4)
print('Original linked list')
myList.display()
myList.remove_tail()
print('After deletion')
myList.display()
