class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        while heap:
            cost, r, c = heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return cost
            
            for dr, dc in d:
                if 0 <= r + dr < ROWS and 0 <= c + dc < COLS and (r + dr, c + dc) not in visited:
                    heappush(heap, (max(cost, grid[r + dr][c + dc]), r + dr, c + dc))
                    visited.add((r + dr, c + dc))
        
        return -1
