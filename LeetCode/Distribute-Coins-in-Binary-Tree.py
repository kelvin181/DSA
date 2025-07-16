# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def dfs(curr):
            if not curr:
                return 0, 0

            left_moves, left_excess = dfs(curr.left)
            right_moves, right_excess = dfs(curr.right)

            excess = left_excess + right_excess + curr.val - 1

            return left_moves + right_moves + abs(excess), excess
        
        return dfs(root)[0]