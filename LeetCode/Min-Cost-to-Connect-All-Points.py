class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 0
        visited = set([0]) # point index
        heap = [] # edge weight, point index
        
        # init heap with all neighs of points[0] first
        for i, (x, y) in enumerate(points[1:]):
            distance = abs(points[0][0] - x) + abs(points[0][1] - y)
            heapq.heappush(heap, (distance, i + 1))

        for _ in range(n - 1):
            # pop to find next edge made and find next point
            while heap:
                edge_weight, i = heapq.heappop(heap)
                if i not in visited:
                    break
            
            # add the edge weight to the result
            result += edge_weight
            visited.add(i)
            
            # add all possible edges to unvisited points
            for j, (x, y) in enumerate(points):
                if j not in visited:
                    distance = abs(points[i][0] - x) + abs(points[i][1] - y)
                    heapq.heappush(heap, (distance, j))
        
        return result
