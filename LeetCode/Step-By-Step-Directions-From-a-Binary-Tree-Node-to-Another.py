# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        # find LCA
        def find_LCA(curr):
            if not curr:
                return None
            
            left = find_LCA(curr.left)
            right = find_LCA(curr.right)

            if curr.val == startValue or curr.val == destValue or (left and right):
                return curr
            
            if left:
                return left
            if right:
                return right
            return None

        LCA = find_LCA(root)

        # find depth start and LCA depth
        start_depth_from_LCA = 0
        found = False
        q = deque([LCA])
        d = 0

        while not found and q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.val == startValue:
                    found = True
                    start_depth_from_LCA = d
                    break
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            d += 1

        # find route from LCA to dest
        path_lca_to_dest = []
        path = []

        def dfs(curr):
            if not curr:
                return
            
            if curr.val == destValue:
                nonlocal path_lca_to_dest
                path_lca_to_dest = path.copy()
                return
            
            if curr.left:
                path.append("L")
                dfs(curr.left)
                path.pop()
            if curr.right:
                path.append("R")
                dfs(curr.right)
                path.pop()
            
        dfs(LCA)
        res = ["U" * start_depth_from_LCA] + path_lca_to_dest
        
        return "".join(res)
