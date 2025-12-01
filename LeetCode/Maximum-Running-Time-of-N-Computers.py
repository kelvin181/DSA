1class Solution:
2    def maxRunTime(self, n: int, batteries: List[int]) -> int:
3        batteries.sort()
4        total = sum(batteries)
5
6        while batteries[-1] > total // n:
7            n -= 1
8            total -= batteries.pop()
9        
10        return total // n