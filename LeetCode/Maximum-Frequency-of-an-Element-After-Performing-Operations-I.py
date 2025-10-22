class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        count = Counter(nums)
        
        l = 0
        r = 0
        res = 1

        for target in range(nums[0], nums[-1] + 1):
            while r < len(nums) and nums[r] <= target + k:
                r += 1
            
            while nums[l] < target - k:
                l += 1

            res = max(res, min(r - l, count.get(target, 0) + numOperations))
        
        return res
