class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = {i: set() for i in range(n)}
        adj = {i: [] for i in range(n)}
        ins = {i: 0 for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            ins[b] += 1

        q = deque()

        for node in range(n):
            if ins[node] == 0:
                q.append(node)

        while q:
            curr = q.popleft()
            for child in adj[curr]:
                ancestors[child].update(ancestors[curr])
                ancestors[child].add(curr)
                ins[child] -= 1
                if ins[child] == 0:
                    q.append(child)

        return [sorted(list(ancestors[node])) for node in range(n)]
