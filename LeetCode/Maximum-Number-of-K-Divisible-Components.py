1class Solution:
2    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
3        adj = {i: [] for i in range(n)}
4
5        for a, b in edges:
6            adj[a].append(b)
7            adj[b].append(a)
8        
9        visited = set()
10
11        def dfs(node):
12            visited.add(node)
13            sum_children = 0
14            total_comps = 0
15
16            for child in adj[node]:
17                if child not in visited:
18                    total, comps = dfs(child)
19                    sum_children += total
20                    total_comps += comps
21            
22            if (sum_children + values[node]) % k == 0:
23                return (0, 1 + total_comps)
24            return (sum_children + values[node], total_comps)
25        
26        return dfs(0)[1]
27