# Last updated: 11/06/2026, 21:32:38
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify matching and tracking the head
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists until one runs out of nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Move our sorting pointer forward
            current = current.next
            
        # Append the remaining nodes from whichever list isn't empty
        current.next = list1 if list1 else list2
        
        # Return the actual head of the merged sorted list
        return dummy.next