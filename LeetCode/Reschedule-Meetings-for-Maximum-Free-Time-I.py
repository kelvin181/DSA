class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        left = 0
        curr = 0
        res = 0

        for r in range(len(startTime)):
            if r >= k:
                res = max(res, startTime[r] - left - curr)
                left = endTime[r - k]
                curr -= (endTime[r - k] - startTime[r - k])
            curr += endTime[r] - startTime[r]

        res = max(res, eventTime - left - curr)
        return res
