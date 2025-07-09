# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parent_vals = {} # parent node: sum of children
        dummy = TreeNode()
        dummy.left = root
        
        q = deque([(dummy, root)]) # parent, curr
        while q:
            row_sum = 0
            row = q.copy()

            for _ in range(len(q)):
                par, curr = q.popleft()
                parent_vals[par] = parent_vals.get(par, 0) + curr.val
                row_sum += curr.val
                if curr.left:
                    q.append((curr, curr.left))
                if curr.right:
                    q.append((curr, curr.right))
            
            for par, node in row:
                node.val = row_sum - parent_vals[par]
        
        return root
