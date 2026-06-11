# Last updated: 11/06/2026, 21:32:30
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node simplifies tracking the new head of the list
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Find the k-th node of the current group
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break  # If there aren't enough nodes left, we're done
                
            group_next = kth.next
            
            # Reverse the current group of k nodes
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            # Rearrange the outer pointers to link the reversed group back
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            
        return dummy.next

    def getKthNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr