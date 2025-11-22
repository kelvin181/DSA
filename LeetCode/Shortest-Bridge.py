class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        res = 0
        visited = set(q)

        def dfs(r, c):
            s = [(r, c)]

            while s:
                r, c = s.pop()
                grid[r][c] = 2
                q.append((r, c))

                for dr, dc in d:
                    if (
                        0 <= r + dr < ROWS and
                        0 <= c + dc < COLS and
                        grid[r + dr][c + dc] == 1
                    ):
                        s.append((r + dr, c + dc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
            else:
                continue
            break
                
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] == 1:
                    return res - 1
                for dr, dc in d:
                    if (
                        0 <= r + dr < ROWS and
                        0 <= c + dc < COLS and
                        (r + dr, c + dc) not in visited
                    ):
                        q.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
            res += 1
        
        return -1
