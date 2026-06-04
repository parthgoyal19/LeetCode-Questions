# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_subtree_sums = []
        
        # Helper function to compute subtree sums
        def calculate_sums(node):
            if not node:
                return 0
            
            left_sum = calculate_sums(node.left)
            right_sum = calculate_sums(node.right)
            
            # Total sum of the subtree rooted at the current node
            current_sum = node.val + left_sum + right_sum
            all_subtree_sums.append(current_sum)
            
            return current_sum
            
        # First Pass: Compute all subtree sums and determine the global total sum
        total_sum = calculate_sums(root)
        
        # Second Pass: Find the maximum product from all collected subtree splits
        max_prod = 0
        for s_sum in all_subtree_sums:
            current_prod = s_sum * (total_sum - s_sum)
            if current_prod > max_prod:
                max_prod = current_prod
                
        # Return the maximum product modulo 10^9 + 7
        return max_prod % (10**9 + 7)