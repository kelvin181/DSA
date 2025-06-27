class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) == x:
            return len(nums)

        l = 0
        curr = 0
        target = sum(nums) - x
        res = -1

        for r, num in enumerate(nums):
            curr += num
            while l < r and curr > target:
                curr -= nums[l]
                l += 1
            if curr == target:
                res = max(res, r - l + 1)
        
        return len(nums) - res if res != -1 else -1
