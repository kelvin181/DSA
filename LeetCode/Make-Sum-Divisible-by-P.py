1class Solution:
2    def minSubarray(self, nums: List[int], p: int) -> int:
3        total = sum(nums)
4        end = total % p
5
6        if total % p == 0:
7            return 0
8        if total < p:
9            return -1
10
11        prev = {0: -1}
12        curr = 0
13        res = len(nums)
14
15        for i, num in enumerate(nums):            
16            curr += num
17            curr %= p
18
19            if (curr - end) % p in prev:
20                res = min(res, i - prev[(curr - end) % p])
21            prev[curr % p] = i
22        
23        if res == len(nums):
24            return -1
25        return res