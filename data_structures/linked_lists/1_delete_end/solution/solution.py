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
                