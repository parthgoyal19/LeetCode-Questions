# Last updated: 11/06/2026, 21:31:17
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Helper function returns: (deepest_depth_in_subtree, lca_node)
        def dfs(node: Optional[TreeNode]) -> tuple[int, Optional[TreeNode]]:
            if not node:
                return 0, None
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            # If the left side goes deeper, the answer lies in the left subtree
            if left_depth > right_depth:
                return left_depth + 1, left_lca
                
            # If the right side goes deeper, the answer lies in the right subtree
            if right_depth > left_depth:
                return right_depth + 1, right_lca
                
            # If both sides have equal maximum depth, the current node is the 
            # smallest subtree containing all deepest leaves beneath it.
            return left_depth + 1, node

        # We only care about the node returned by our DFS
        return dfs(root)[1]