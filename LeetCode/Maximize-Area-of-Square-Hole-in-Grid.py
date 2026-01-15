1class Solution:
2    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
3        hBars.sort()
4        vBars.sort()
5        h = 1
6        v = 1
7        currh = 1
8        currv = 1
9
10        for i in range(1, len(hBars)):
11            if hBars[i] == hBars[i - 1] + 1:
12                currh += 1
13            else:
14                currh = 1
15            h = max(h, currh)
16        
17        for i in range(1, len(vBars)):
18            if vBars[i] == vBars[i - 1] + 1:
19                currv += 1
20            else:
21                currv = 1
22            v = max(v, currv)
23        
24        return (min(h, v) + 1) ** 2
25