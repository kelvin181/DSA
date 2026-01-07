1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxProduct(self, root: Optional[TreeNode]) -> int:
9        MOD = 10 ** 9 + 7
10        self.res = 0
11        total = 0
12
13        if not root:
14            return 0
15        
16        def dfs(curr):
17            if not curr:
18                return 0
19            
20            nonlocal total
21            
22            val_left = dfs(curr.left)
23            self.res = max(self.res, val_left * (total - val_left))
24            val_right = dfs(curr.right)
25            self.res = max(self.res, val_right * (total - val_right))
26            
27            return curr.val + val_left + val_right
28        
29        total = dfs(root)
30        dfs(root)
31        return self.res % MOD
32