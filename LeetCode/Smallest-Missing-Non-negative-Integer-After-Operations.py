class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = {i: 0 for i in range(value)}

        for num in nums:
            count[num % value] += 1
        
        target = min(count.values())
        for i in range(value):
            if count[i] == target:
                return value * target + i
        
        return -1
