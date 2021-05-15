

  
class ListNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    @classmethod
    def from_range(cls, start, end):
        if start > end:
            return cls()
        current_node = ListNode(start)
        rest_of_the_list = cls.from_range(start+1, end)
        current_node.next = rest_of_the_list.head
        rest_of_the_list.head = current_node
        return rest_of_the_list
    
    def sort_ll(self):
        self._sort_ll(self.head)
        
    def _sort_ll(self,head):
        if not head or head.next is None:
            return 
        mid = head
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next
        mid.next = None
        left_list = self._sort_ll(head)
        right_list = self._sort_ll(slow)
        return self.merge(left_list, right_list)
    
    def merge(self,left_list, right_list):
        temp = ListNode(None)
        curr = temp
        while left_list and right_list:
            if left_list.value < right_list.value:
                curr.next = left_list
                left_list = left_list.next
            else: 
                curr.next = right_list
                right_list = right_list.next
            curr = curr.next
        
        while left_list:
            curr.next = left_list
            left_list = left_list.next
        
        while right_list:
            curr.next = right_list
            right_list = right_list.next
        return temp.next
                
    def display(self):
            curr = self.head
            while curr.next:
                print(curr.value)
                curr = curr.next

myList = LinkedList.from_range(1,4)
myList.display()
myList.sort_ll()
myList.display()



        



