

  
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
        self.head = self._sort_ll(self.head)
        
    def _sort_ll(self, head):
        if head is None or head.next is None:
            return head
        mid = head
        slow = head
        fast = head
        
        while fast and fast.next:
            mid = slow
            slow = slow.next
            fast = fast.next.next
        mid.next = None
        left = self._sort_ll(head)
        right = self._sort_ll(slow)
        return self.merge(left,right)
    
    def merge(self,left,right):
        dummy = ListNode(None)
        cur = dummy
        while left and right:
            if left.value < right.value:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return dummy.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

myList = LinkedList()
myList.head = ListNode(5)
myList.head.next  = ListNode(9)
myList.head.next.next  = ListNode(7)
myList.display()
myList.sort_ll()
myList.display()



        



