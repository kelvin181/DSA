# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def height(node):
            if not node:
                return None, 0

            left_lca, left_height = height(node.left)
            right_lca, right_height = height(node.right)
            
            if left_height > right_height:
                return left_lca, left_height + 1
            elif right_height > left_height:
                return right_lca, right_height + 1
            else:
                return node, left_height + 1
        
        return height(root)[0]
