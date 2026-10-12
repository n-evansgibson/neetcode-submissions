# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# x --> x --> x-->

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Set pointers
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

        





        