# Last updated: 11/06/2026, 21:31:05
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        max_sum = float('-inf')
        best_level = 1
        current_level = 1
        
        # Initialize queue for Level Order Traversal (BFS)
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            # Process all nodes present at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                # Push children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update max_sum and track the smallest level index if a strict maximum is found
            if level_sum > max_sum:
                max_sum = level_sum
                best_level = current_level
                
            current_level += 1
            
        return best_level