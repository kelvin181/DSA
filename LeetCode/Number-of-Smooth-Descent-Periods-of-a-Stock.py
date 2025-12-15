1class Solution:
2    def getDescentPeriods(self, prices: List[int]) -> int:
3        res = 0 
4        l = 0
5
6        for r in range(1, len(prices)):
7            if prices[r] == prices[r - 1] - 1:
8                continue
9            diff = r - l
10            res += (diff * (diff + 1)) // 2
11            l = r
12        
13        diff = len(prices) - l
14        res += (diff * (diff + 1)) // 2
15    
16        return res
17