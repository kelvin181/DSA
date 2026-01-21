1class Solution:
2    def minBitwiseArray(self, nums: List[int]) -> List[int]:        
3        res = []
4
5        for num in nums:
6            ans = -1
7            curr = 1
8
9            while num | curr == num:
10                ans = num & ~curr
11                curr <<= 1
12
13            res.append(ans)
14        
15        return res
16