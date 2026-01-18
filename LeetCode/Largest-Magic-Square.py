1class Solution:
2    def largestMagicSquare(self, grid: List[List[int]]) -> int:
3        ROWS = len(grid)
4        COLS = len(grid[0])
5
6        rows = []
7        cols = []
8
9        for row in grid:
10            rows.append([0] + list(accumulate(row)))
11        
12        for c in range(COLS):
13            arr = [0]
14            for r in range(ROWS):
15                arr.append(arr[-1] + grid[r][c])
16            cols.append(arr)
17        
18        def valid(r, c, size):
19            diag1 = 0
20            diag2 = 0
21
22            i = r
23            j = c
24            for _ in range(size):
25                diag1 += grid[i][j]
26                i += 1
27                j += 1
28            
29            i = r
30            j = c + size - 1
31            for _ in range(size):
32                diag2 += grid[i][j]
33                i += 1
34                j -= 1
35            
36            target = diag1
37
38            if any(rows[row][c + size] - rows[row][c] != target for row in range(r, r + size)):
39                return False
40            
41            if any(cols[col][r + size] - cols[col][r] != target for col in range(c, c + size)):
42                return False
43            
44            return diag1 == diag2
45
46        def check(size):
47            for r in range(ROWS - size + 1):
48                for c in range(COLS - size + 1):
49                    if valid(r, c, size):
50                        return True
51            return False
52
53        for size in range(min(ROWS, COLS), 0, -1):
54            if check(size):
55                return size
56
57        return -1