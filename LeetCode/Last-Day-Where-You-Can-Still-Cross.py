1class Solution:
2    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
3        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
4        
5        for i in range(len(cells)):
6            cells[i][0] -= 1
7            cells[i][1] -= 1
8
9        def dfs(day):
10            cant = set([tuple(pair) for pair in cells[:day]])
11            s = []
12            visited = set()
13
14            for c in range(col):
15                if (0, c) not in cant:
16                    s.append((0, c))
17                    visited.add((0, c))
18            
19            while s:
20                r, c = s.pop()
21                if r == row - 1:
22                    return True
23
24                for dr, dc in d:
25                    if ((r + dr, c + dc) not in visited and 
26                        (r + dr, c + dc) not in cant and 
27                        0 <= r + dr < row and 
28                        0 <= c + dc < col
29                    ):
30                        s.append((r + dr, c + dc))
31                        visited.add((r + dr, c + dc))
32
33            return False
34
35        
36        l = col - 1
37        r = row * (col - 1)
38        res = 0
39
40        while l <= r:
41            m = l + (r - l) // 2
42            if dfs(m):
43                res = max(res, m)
44                l = m + 1
45            else:
46                r = m - 1
47        
48        return res
49