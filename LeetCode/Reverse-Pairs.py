class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def merge(a, b):
            j = 0
            res = 0
            arr = []

            for i in range(len(a)):
                # find j where every element in b[:j] satisfies the condition with a[i]
                while j < len(b) and a[i] > 2 * b[j]:
                    j += 1
                res += j
            
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    arr.append(a[i])
                    i += 1
                else:
                    arr.append(b[j])
                    j += 1
            
            arr.extend(a[i:])
            arr.extend(b[j:])

            return res, arr
        
        def rev(nums):
            if not nums or len(nums) == 1:
                return 0, nums

            half = len(nums) // 2
            countA, a = rev(nums[:half])
            countB, b = rev(nums[half:])
            countC, c = merge(a, b)
            
            return countA + countB + countC, c

        count, arr = rev(nums)
        return count
