# Last updated: 11/06/2026, 21:32:33
import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Push the head of each non-empty list into the min-heap
        # We use a unique index 'i' to avoid object comparison errors when node values are equal
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))
        
        # Create a dummy node to easily build the merged linked list
        dummy = ListNode(0)
        current = dummy
        
        # Extract the minimum node and push its next element until the heap is empty
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # If there is a next node in the current list, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next