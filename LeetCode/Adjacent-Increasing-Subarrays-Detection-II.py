class Solution:
    def maxIncreasingSubarrays(self, arr: List[int]) -> int:
        # find lengths of increasing subarrays
        lengths = []
        current_length = 1
        
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                current_length += 1
            else:
                lengths.append(current_length)
                current_length = 1
        
        lengths.append(current_length)
        
        # check pairs of adjacent increasing subarrays
        res = 0
        for i in range(len(lengths) - 1):
            res = max(res, lengths[i] // 2)
            res = max(res, min(lengths[i], lengths[i + 1]))
        
        res = max(res, lengths[-1] // 2)

        return res
