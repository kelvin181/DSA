class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r, c))
                    grid[r][c] = 0
                else:
                    grid[r][c] = inf
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in d:
                    if (0 <= r + dr < ROWS 
                        and 0 <= c + dc < COLS 
                        and dist + 1 < grid[r + dr][c + dc]
                    ):
                        q.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = min(grid[r + dr][c + dc], dist + 1)
            dist += 1
        
        return dist - 1 if dist - 1 != 0 else -1
