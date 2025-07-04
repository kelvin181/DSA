def get_sum(start, end):
    # sum of numbers up to and including end - 1 minus the sum of numbers up to and including start
    sum_to_end = ((end - 1) * end) // 2
    sum_to_start = ((start + 1) * start) // 2
    return sum_to_end - sum_to_start

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        res = 0
        
        nums.sort()
        
        if nums[0] != 1:
            diff = nums[0] - 1
            res += get_sum(0, min(k + 1, nums[0]))
            k -= min(k, nums[0] - 1)
        
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i] - 1
            if diff <= 0:
                continue
            elif diff <= k:
                res += get_sum(nums[i], nums[i + 1])
                k -= diff
            else:
                res += get_sum(nums[i], nums[i] + k + 1)
                k = 0
            if k == 0:
                break
        
        if k >= 1:
            res += get_sum(nums[-1], nums[-1] + k + 1)

        return res
