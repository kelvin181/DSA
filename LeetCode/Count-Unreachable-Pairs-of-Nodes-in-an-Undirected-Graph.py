class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        pairs = (n * (n - 1)) // 2

        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        sizes = []

        def dfs(node):
            size = 1

            for neigh in adj[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    size += dfs(neigh)
            
            return size

        for i in range(n):
            if i not in visited:
                visited.add(i)
                sizes.append(dfs(i))

        for num in sizes:
            pairs -= (num * (num - 1)) // 2
        
        return pairs
