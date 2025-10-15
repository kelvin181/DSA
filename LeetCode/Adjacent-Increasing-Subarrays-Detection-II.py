class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        curr = 1
        res = 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += 1
            else:
                prev, curr = curr, 1
            
            res = max(res, curr // 2, min(curr, prev))
        
        return res
