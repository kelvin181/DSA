1class Solution:
2    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
3        ROWS = len(nums1)
4        COLS = len(nums2)
5
6        dp = [[-inf] * COLS for _ in range(ROWS)]
7
8        for c in range(COLS):
9            for r in range(ROWS):
10                res = nums1[r] * nums2[c]
11                if r != 0:
12                    res = max(res, dp[r - 1][c])
13                if c != 0:
14                    res = max(res, dp[r][c - 1])
15                if c != 0 and r != 0:
16                    res = max(res, nums1[r] * nums2[c] + dp[r - 1][c - 1])
17                dp[r][c] = res
18
19        return dp[-1][-1]
20