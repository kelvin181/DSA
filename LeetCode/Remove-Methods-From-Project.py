class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # make graph
        adj = {i : set() for i in range(n)}
        for a, b in invocations:
            adj[a].add(b)

        # find nodes in network
        network = set([k])
        s = [k]

        while s:
            curr = s.pop()
            for child in adj[curr]:
                if child not in network:
                    network.add(child)
                    s.append(child)
        
        # check if we remove network

        # remove by checking neighs of nodes
        # remove = True
        # for i in range(n):
        #     if i in network:
        #         continue
        #     for child in adj[i]:
        #         if child in network:
        #             remove = False
        
        # remove by checking each edge
        remove = True
        for a, b in invocations:
            if a not in network and b in network:
                remove = False

        # nodes after removing
        res = []
        for i in range(n):
            if i in network:
                if not remove:
                    res.append(i)
            else:
                res.append(i)

        return res
