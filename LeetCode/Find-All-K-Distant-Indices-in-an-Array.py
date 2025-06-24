class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        prev = -1

        for i in range(len(nums)):
            if i - prev <= k and prev != -1:
                res.add(i)
            if nums[i] == key:
                prev = i
                res.add(i)
        
        prev = len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if prev - i <= k and prev != len(nums):
                res.add(i)
            if nums[i] == key:
                prev = i
                res.add(i)
        
        return sorted(list(res))
