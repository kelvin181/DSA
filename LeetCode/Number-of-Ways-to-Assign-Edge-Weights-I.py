class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        adj = {i + 1: [] for i in range(len(edges) + 1)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        q = deque([1])
        height = 0
        visited = set([1])
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for neigh in adj[curr]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
            height += 1

        return 2 ** (height - 2) % MOD
    