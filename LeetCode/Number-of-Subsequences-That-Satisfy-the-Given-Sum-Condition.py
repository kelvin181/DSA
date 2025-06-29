class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        res = 0
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += pow(2, r - l, MOD)
                l += 1
        
        return res % MOD
