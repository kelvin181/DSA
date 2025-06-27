class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pre = [0]
        seen = {}
        res = -inf

        for num in nums:
            pre.append(num + pre[-1])

        for i, num in enumerate(nums):
            if num + k in seen:
                res = max(res, pre[i + 1] - pre[seen[num + k]])
            if num - k in seen:
                res = max(res, pre[i + 1] - pre[seen[num - k]])

            if num not in seen:
                seen[num] = i
            else:
                if pre[i] - pre[seen[num]] < 0:
                    seen[num] = i
        
        return res if res != -inf else 0
