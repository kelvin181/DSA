class Solution:
    def maxIncreasingSubarrays(self, arr: List[int]) -> int:
        current_length = 1
        previous_length = 1
        res = 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                current_length += 1
            else:
                previous_length = current_length
                current_length = 1
            res = max(res, current_length // 2, min(current_length, previous_length))

        return res