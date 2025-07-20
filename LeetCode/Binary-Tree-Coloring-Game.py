# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        # dfs to find parent of each node and x node
        x_node: TreeNode = None 
        parent = {} # current: parent
        stack = [(None, root)] # parent, current
        
        while stack:
            parent_node, current_node = stack.pop()
            if current_node.val == x:
                x_node = current_node
            parent[current_node] = parent_node
            if current_node.left:
                stack.append((current_node, current_node.left))
            if current_node.right:
                stack.append((current_node, current_node.right))

        def count_nodes(parent, x_node, start_node) -> int:
            q = deque([start_node])
            visited = set([x_node, start_node])
            node_count = 0
            
            while q:
                current_node = q.popleft()
                node_count += 1
                if current_node.left and current_node.left not in visited:
                    q.append(current_node.left)
                    visited.add(current_node.left)
                if current_node.right and current_node.right not in visited:
                    q.append(current_node.right)
                    visited.add(current_node.right)
                if parent[current_node] and parent[current_node] not in visited:
                    q.append(parent[current_node])
                    visited.add(parent[current_node])
            
            return node_count 
        
        parent_node_count =  left_node_count = right_node_count = 0
        
        # count nodes in parent subtree
        if parent[x_node]:
            parent_node_count = count_nodes(parent, x_node, parent[x_node])
            
        # count nodes in left subtree
        if x_node.left:
            left_node_count = count_nodes(parent, x_node, x_node.left)
        
        # count nodes in right subtree    
        if x_node.right:
            right_node_count = count_nodes(parent, x_node, x_node.right)
        
        return max(parent_node_count, left_node_count, right_node_count) > n // 2
