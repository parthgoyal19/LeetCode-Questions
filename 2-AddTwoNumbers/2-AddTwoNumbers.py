# Last updated: 11/06/2026, 21:33:15
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head acts as a placeholder to easily return the head of the new list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Continue looping if there are nodes left in l1 or l2, or if there is a leftover carry
        while l1 or l2 or carry:
            # Get values from current nodes, default to 0 if a list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum and the new carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            
            # Create a new node with the single-digit result
            current.next = ListNode(total_sum % 10)
            current = current.next
            
            # Move to the next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy_head.next