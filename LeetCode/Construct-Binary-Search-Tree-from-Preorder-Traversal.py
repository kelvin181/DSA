# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def build(i, mn, mx):
            if i >= len(preorder) or preorder[i] < mn or preorder[i] > mx:
                return

            node = TreeNode(preorder[i])

            # make left subtree (all smaller that current)
            if i + 1 < len(preorder) and preorder[i + 1] < node.val:
                node.left = build(i + 1, mn, node.val)

            # make right subtree (all larger than current)
            j = i + 1
            while j < len(preorder) and preorder[j] < node.val:
                j += 1
            if j < len(preorder):
                node.right = build(j, node.val, mx)

            return node

        return build(0, -inf, inf)
