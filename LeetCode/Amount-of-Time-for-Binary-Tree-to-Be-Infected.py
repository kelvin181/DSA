# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # find start node and make parent hashmap
        parent = {} # node: parent
        start_node = None # TreeNode of start node
        stack = [(None, root)] # parent, current
        
        while stack:
            parent_node, current_node = stack.pop()
            parent[current_node] = parent_node
            if current_node.val == start:
                start_node = current_node
            if current_node.left:
                stack.append((current_node, current_node.left))
            if current_node.right:
                stack.append((current_node, current_node.right))
            
        # bfs from the start node and find the maximum depth
        result = -1
        visited = set([start_node])
        q = deque([start_node])
        
        while q:
            for _ in range(len(q)):
                current_node = q.popleft()
                # add parent
                if parent[current_node] and parent[current_node] not in visited:
                    q.append(parent[current_node])
                    visited.add(parent[current_node])
                # add left child
                if current_node.left and current_node.left not in visited:
                    q.append(current_node.left)
                    visited.add(current_node.left)
                # add right child
                if current_node.right and current_node.right not in visited:
                    q.append(current_node.right)
                    visited.add(current_node.right)
            result += 1
        
        return result

