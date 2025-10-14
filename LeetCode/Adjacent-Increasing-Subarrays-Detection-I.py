class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev = 0
        curr = 1

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += 1
            else:
                prev, curr = curr, 1
            
            if curr >= k and prev >= k or curr == 2 * k:
                return True
        
        return False
