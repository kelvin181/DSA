class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        arr = []
        res = 1

        l = 0
        for r in range(1, len(nums)):
            if nums[r] >= nums[r - 1]:
                continue
            arr.append((l, r - 1))
            l = r
        
        arr.append((l, len(nums) - 1))
        if l == 0:
            return len(nums)

        for i in range(len(arr) - 1):
            l, r = arr[i]
            res = max(res, r - l + 2)
            
            dl, dr = arr[i + 1]
            if dr - dl > 0 and nums[dl + 1] >= nums[r]:
                res = max(res, dr - l + 1)
            if r - 1 >= 0 and l != r and nums[dl] >= nums[r - 1]:
                res = max(res, dr - l + 1)
            
        return max(res, arr[-1][1] - arr[-1][0] + 2)
