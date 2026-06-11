# Last updated: 11/06/2026, 21:31:03
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_values = []
        
        # Step 1: Perform an in-order traversal to get a sorted array of values
        def inorder_traversal(node):
            if not node:
                return
            inorder_traversal(node.left)
            sorted_values.append(node.val)
            inorder_traversal(node.right)
            
        inorder_traversal(root)
        
        # Step 2: Rebuild a balanced BST from the sorted array
        def build_balanced_bst(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
                
            # Choose the middle element as the root to maintain height balance
            mid = (left + right) // 2
            
            root_node = TreeNode(sorted_values[mid])
            
            # Recursively build the left and right subtrees
            root_node.left = build_balanced_bst(left, mid - 1)
            root_node.right = build_balanced_bst(mid + 1, right)
            
            return root_node
            
        return build_balanced_bst(0, len(sorted_values) - 1)