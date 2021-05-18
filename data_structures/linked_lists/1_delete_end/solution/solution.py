class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self, head=None):
        self.head = head
    
    def delete_at_end(self):
        if self.head is None:
            return None
        curr = self.head
        while curr.next.next:
           curr = curr.next
        curr.next = None
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


myList = linkedlist()
myList.head = Node(20)
myList.head.next = Node(10)
myList.head.next.next = Node(30)
myList.head.next.next.next = Node(50)
myList.display()
myList.delete_at_end()
myList.display()
