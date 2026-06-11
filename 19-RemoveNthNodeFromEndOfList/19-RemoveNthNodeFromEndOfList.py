# Last updated: 11/06/2026, 21:32:44
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify corner cases (e.g., removing the head node)
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Move the fast pointer so there is a gap of n nodes between fast and slow
        for _ in range(n + 1):
            fast = fast.next
            
        # Move fast to the end, maintaining the gap
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        # slow.next is the node to be deleted, skip it
        slow.next = slow.next.next
        
        # Return the actual head of the modified list
        return dummy.next