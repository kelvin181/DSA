class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()

        def count_pairs(n):
            i = 0
            count = 0
            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= n:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count

        l = 0
        r = nums[-1] - nums[0]
        res = inf

        while l <= r:
            m = l + (r - l) // 2
            num = count_pairs(m)
            if num >= p:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res
