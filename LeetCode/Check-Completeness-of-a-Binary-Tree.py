# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        # once you reach the first missing node, there shouldn't be any nodes after

        if not root:
            return True

        q = deque([root])
        end = False

        while q:
            curr = q.popleft()

            if not curr:
                end = True
            else:
                if end:
                    return False
                q.append(curr.left)
                q.append(curr.right)
            
        return True
