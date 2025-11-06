class Union:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, target):
        if self.parent[target] != target:
            self.parent[target] = self.find(self.parent[target])
        return self.parent[target]
    
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        self.parent[pa] = pb

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        union = Union(c)
        online = [True] * (c + 1)
        heaps = {}
        res = []

        for a, b in connections:
            union.union(a, b)
        
        for i in range(1, c + 1):
            root = union.find(i)
            if root not in heaps:
                heaps[root] = []
            heappush(heaps[root], i)
        
        for o, i in queries:
            if o == 1:
                if online[i]:
                    res.append(i)
                    continue
                root = union.find(i)
                heap = heaps[root]
                while heap and not online[heap[0]]:
                    heappop(heap)
                res.append(heap[0] if heap else -1)
            else:
                online[i] = False
        
        return res
