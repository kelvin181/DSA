1class Solution:
2    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
3        total = 0
4        count = 0
5        smallest = inf
6
7        for row in matrix:
8            for num in row:
9                total += abs(num)
10                smallest = min(smallest, abs(num))
11
12                if num < 0:
13                    count += 1
14        
15        if count % 2 == 0:
16            return total
17        return total - (2 * smallest)