1class Solution:
2    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
3        ROWS = len(mat)
4        COLS = len(mat[0])
5
6        pre = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
7        for r in range(ROWS):
8            for c in range(COLS):
9                pre[r + 1][c + 1] = mat[r][c] + pre[r + 1][c] + pre[r][c + 1] - pre[r][c]
10
11        def valid(r, c, size):
12            return pre[r + size][c + size] - pre[r][c + size] - pre[r + size][c] + pre[r][c] <= threshold
13        
14        def find(size):
15            for r in range(ROWS - size + 1):
16                for c in range(COLS - size + 1):
17                    if valid(r, c, size):
18                        return True
19            return False
20
21        l = 0
22        r = min(ROWS, COLS)
23        res = 0
24
25        while l <= r:
26            m = l + (r - l) // 2
27            if find(m):
28                res = max(res, m)
29                l = m + 1
30            else:
31                r = m - 1
32        
33        return res