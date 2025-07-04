# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        parent = {}
        q = deque([root])

        # find parents of each node
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    parent[curr.left] = curr
                    q.append(curr.left)
                if curr.right:
                    parent[curr.right] = curr
                    q.append(curr.right)
        
        visited = set()
        q = deque([target])
        dist = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                visited.add(curr)

                if dist == k:
                    res.append(curr.val)
                    continue

                if curr.left and curr.left not in visited:
                    q.append(curr.left)
                
                if curr.right and curr.right not in visited:
                    q.append(curr.right)
                
                if curr in parent and parent[curr] not in visited:
                    q.append(parent[curr])
            
            dist += 1
        
        return res
