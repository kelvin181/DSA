class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = [0]
        res = 0 

        for num in nums:
            
            while s[-1] > num:
                s.pop()
                res += 1
            
            if s[-1] != num:
                s.append(num)
        
        return res + len(s) - 1
