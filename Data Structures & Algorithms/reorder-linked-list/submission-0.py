# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Edge cases: list of one or two
        if not head.next: return
        if not head.next.next: return

        tail = None

        # Iterate through the list while there is a remainder
        # of at least two
        while (head and head.next):

            # Find the tail
            curr = head
            while curr.next.next:
                curr = curr.next
            tail = curr.next
            curr.next = None
            
            if head.next == tail: return
    
            # Move the tail in between head and rest of list
            rest = head.next
            head.next = tail
            tail.next = rest

            # Move head pointer
            head = rest

        return 



        








        