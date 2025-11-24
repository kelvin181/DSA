class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        res = total
        min_one1 = inf
        min_one2 = inf
        min_two1 = inf
        min_two2 = inf

        for num in nums:
            if num % 3 == 1:
                if num < min_one1:
                    min_one2 = min_one1
                    min_one1 = num
                elif num < min_one2:
                    min_one2 = num
            elif num % 3 == 2:
                if num < min_two1:
                    min_two2 = min_two1
                    min_two1 = num
                elif num < min_two2:
                    min_two2 = num

        if total % 3 == 0:
            return res
        elif total % 3 == 1:
            res = 0
            if min_one1 != inf:
                res = total - min_one1
            if min_two1 != inf and min_two2 != inf:
                res = max(res, total - min_two1 - min_two2)
            return res
        else:
            res = 0
            if min_two1 != inf:
                res = total - min_two1
            if min_one1 != inf and min_one2 != inf:
                res = max(res, total - min_one1 - min_one2)
            return res

        return -1
