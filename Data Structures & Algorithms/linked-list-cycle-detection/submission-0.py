# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:


        # Tracks visited nodes
        visited = set()
        node = head

        while node:

            # If we have already visited the node, there is a cycle
            if (node in visited):
                return True

            # Otherwise, add the node
            else:
                visited.add(node)
                node = node.next
            

        # List has no cycles
        return False
        