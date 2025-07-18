class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        # make graph
        adj = {i: [] for i in range(n)}
        in_deg = {i: 0 for i in range(n)}

        for a, b in richer:
            adj[a].append(b)
            in_deg[b] += 1
        
        # top sort
        s = []
        for i in range(n):
            if in_deg[i] == 0:
                s.append(i)
        
        min_ancestor = {i: [quiet[i], i] for i in range(n)}

        while s:
            curr = s.pop()
            for child in adj[curr]:
                if min_ancestor[curr][0] < min_ancestor[child][0]:
                    min_ancestor[child] = min_ancestor[curr]
                in_deg[child] -= 1
                if in_deg[child] == 0:
                    s.append(child)

        # process min_ancestor to make res
        res = [-1] * n
        for key in min_ancestor:
            res[key] = min_ancestor[key][1]

        return res
