class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []
        curr = 1

        for _ in range(n):
            res.append(curr)

            if curr * 10 <= n:
                # always add a 0 first if you can
                curr *= 10
            else:
                # backtrack to find the next lexicographically smallest number
                if curr >= n:
                    curr //= 10
                curr += 1
                while curr % 10 == 0:
                    curr //= 10
        return res