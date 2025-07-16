class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # make graph
        adj = {i: [] for i in range(n)}
        for a, b, c in flights:
            adj[a].append((b, c))

        # traverse graph using bfs
        costs = {i: inf for i in range(n)}
        costs[src] = 0
        q = deque([(0, src)])

        while k >= 0 and q:
            for _ in range(len(q)):
                total, curr = q.popleft()
                for neigh, cost in adj[curr]:
                    if total + cost < costs[neigh]:
                        costs[neigh] = total + cost
                        q.append((costs[neigh], neigh))
            k -= 1

        if costs[dst] == inf:
            return -1
        return costs[dst]
