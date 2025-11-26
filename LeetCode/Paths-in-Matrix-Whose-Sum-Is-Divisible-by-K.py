class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        ROWS = len(grid)
        COLS = len(grid[0])
        arr = [[[0] * k for j in range(COLS)] for _ in range(ROWS)]
        arr[0][0][grid[0][0] % k] += 1

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    continue
                
                curr = grid[r][c] % k

                if r - 1 >= 0:
                    for i in range(k):
                        remainder = (i + curr) % k
                        arr[r][c][remainder] += arr[r - 1][c][i]
                        arr[r][c][remainder] %= MOD

                if c - 1 >= 0:
                    for i in range(k):
                        remainder = (i + curr) % k
                        arr[r][c][remainder] += arr[r][c - 1][i]
                        arr[r][c][remainder] %= MOD
        
        return arr[-1][-1][0]
