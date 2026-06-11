# Last updated: 11/06/2026, 21:32:32
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as a placeholder before the real head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Loop as long as there is a pair left to swap
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = prev.next.next
            
            # Rearrange the pointers to execute the swap
            first.next = second.next
            second.next = first
            prev.next = second
            
            # Skip over the swapped pair for the next iteration
            prev = first
            
        return dummy.next