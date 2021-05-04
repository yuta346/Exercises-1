#Completed
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    @classmethod
    def from_range(cls, start, end):
        if start > end:
            return cls()
        current_node = Node(start)
        rest_of_the_list = cls.from_range(start+1, end)
        current_node.next = rest_of_the_list.head
        rest_of_the_list.head = current_node
        return rest_of_the_list
    

    def insert_after_item(self,x,data):
        if self.head is None:
            return None
        if self.head.next is None:
            new_node = Node(data)
            self.head.next = new_node

        curr = self.head
        while curr.next:
            if curr.data == x:
                new_node = Node(data)
                temp = curr.next
                curr.next = new_node
                new_node.next = temp
                curr = curr.next
            curr = curr.next

    def display(self):
        curr = self.head
        while curr.next:
            print(curr.data)
            curr = curr.next

myList = linkedList.from_range(1,4)
# myList.display()
myList.insert_after_item(2,5)
myList.display()


        