# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Shift left by 1 bit (multiply by 2) and add the current node's value
            current_sum = (current_sum << 1) | node.val
            
            # If it's a leaf node, return the completed path value
            if not node.left and not node.right:
                return current_sum
            
            # Otherwise, sum the results from both left and right subtrees
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)