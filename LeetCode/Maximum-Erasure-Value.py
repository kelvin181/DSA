class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curr = 0
        res = 0
        l = 0
        seen = {}

        for r, num in enumerate(nums):
            if num in seen:
                while l <= seen[num]:
                    curr -= nums[l]
                    l += 1
            seen[num] = r
            curr += num
            res = max(res, curr)
        
        return res
