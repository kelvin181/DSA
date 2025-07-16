class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = {0: 0, 1: 0}

        for num in nums:
            counts[num % 2] += 1

        # all even or all odd
        res = max(counts[0], counts[1])

        # take alternating starting with odd
        prev = False
        count = 0
        for num in nums:
            if not prev:
                if num % 2:
                    prev = not prev
                    count += 1
            else:
                if num % 2 == 0:
                    prev = not prev
                    count += 1
        res = max(res, count)

        # take alternating starting with even
        prev = True
        count = 0
        for num in nums:
            if not prev:
                if num % 2:
                    prev = not prev
                    count += 1
            else:
                if num % 2 == 0:
                    prev = not prev
                    count += 1

        return max(res, count)
