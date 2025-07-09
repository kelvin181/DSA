class Solution:
    def maxSatisfaction(self, arr: List[int]) -> int:
        arr.sort(reverse=True)
        curr = 0
        total = 0
        res = 0

        for i in range(len(arr)):
            curr += arr[i]
            if curr < 0:
                break
            total += curr
            res = max(res, total)

        return res
