#Completed
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

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

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next  = self.head
        self.head = new_node

    def insert_at_end(self,data):
        curr = self.head
        if curr.next is None:
           new_node = Node(data)
           curr.next = new_node
        else:
            while curr.next:
                curr = curr.next
            new_node = Node(data)
            curr.next = new_node

    def insert_at_index(self,index,data):
        indx = 1
        curr = self.head
        while curr:
            if indx+1==index:
                new_node = Node(data)
                temp = curr.next
                curr.next = new_node
                new_node.next = temp
            curr = curr.next
            indx+=1

    def delete_item_by_value(self,x):
        curr = self.head
        prev = self.head
        if curr.data == x:
            self.head = curr.next
            return 
        while curr:
            if curr.data== x:
                prev.next = curr.next
            prev = prev.next
            curr = curr.next.next

    def search(self, x):
        curr = self.head
        while curr:
            if curr.data == x:
                return True
            curr = curr.next
        return False

    def get_count(self):
        count = 0
        if self.head is None:
            return 0
        curr = self.head
        while curr:
            count+=1
            curr = curr.next
        return count

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev



    
# myList = linkedList.from_range(1,4)
# myList.display()
# myList.insert_after_item(2,5)
# myList.display()
items = linkedList()
items.head = Node(20)
items.insert_at_start(40)
items.insert_at_start(50)
items.insert_at_start(10)
# # items.delete_item_by_value(40)
# # items.display()
# items.insert_at_end(100)
# # items.traverse()
# # print(items.search(100))
# # print(items.get_count())
# # items.reverse()
items.insert_at_index(2,300)
items.traverse()

# items = linkedList()
# items.head = Node(1)
# e2 = Node(2)
# items.head.next = e2
# items.traverse()


        