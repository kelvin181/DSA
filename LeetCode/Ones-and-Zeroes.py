class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dp(i, curr0, curr1):
            if i >= len(strs):
                return 0

            s = strs[i]
            c0 = s.count("0")
            c1 = s.count("1")
            res = 0

            # take
            if curr0 + c0 <= m and curr1 + c1 <= n:
                res += 1
                res = max(res, 1 + dp(i + 1, curr0 + c0, curr1 + c1))

            # leave
            res = max(res, dp(i + 1, curr0, curr1))

            return res

        return dp(0, 0, 0)
