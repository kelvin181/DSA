1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9
10        def dfs(curr):
11            if not curr:
12                return 0, None
13            
14            left = dfs(curr.left)
15            right = dfs(curr.right)
16            if left[0] > right[0]:
17                return left[0] + 1, left[1]
18            if right[0] > left[0]:
19                return right[0] + 1, right[1]
20            return left[0] + 1, curr
21        
22        return dfs(root)[1]
23