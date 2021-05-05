#Completed
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.tail_node:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next = new_node
            self.tail_node = new_node

    def dequeue(self):
        if not self.head_node:
            raise IndexError
        value = self.head_node.value
        self.head_node = self.head_node.next
        if not self.head_node:
            self.tail_node = None
        return value

    def empty(self):
        if self.head_node:
            return False
        return True

    def __bool__(self):
        # return not self.head_node == None
        return self.head_node is not None

    def __len__(self):
        count = 0
        cur =  self.head_node
        while cur:
            count+=1
            cur = cur.next
        return count
        
    def __eq__(self,other):
        cur1 = self.head_node
        cur2 = other.head_node
        if len(self) == len(other):
            while cur1 and cur2:
                if cur1.value == cur2.value:
                    cur1 = cur1.next
                    cur2 = cur2.next
                return True
        return False
        
