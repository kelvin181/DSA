1class Solution:
2    def maxSubarraySum(self, nums: List[int], k: int) -> int:
3
4        if k == len(nums):
5            return sum(nums)
6
7        mods = {i: inf for i in range(k)}
8        mods[0] = 0
9        curr = 0
10        res = -inf
11
12        for i, num in enumerate(nums):
13            curr += num
14            if i >= k - 1:
15                res = max(res, curr - mods[(i + 1) % k])
16            mods[(i + 1) % k] = min(mods[(i + 1) % k], curr)
17        
18        return res
19