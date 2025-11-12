class Solution:
    def minOperations(self, nums: List[int]) -> int:
        one_count = nums.count(1)
        if one_count > 0:
            return len(nums) - one_count
        
        res = inf
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr = gcd(curr, nums[j])
                if curr == 1:
                    res = min(res, j - i)
                    break
        
        return res + len(nums) - 1 if res != inf else -1
