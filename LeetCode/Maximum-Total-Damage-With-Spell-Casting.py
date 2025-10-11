class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = Counter(power)
        power = sorted(list(set(power)))

        @cache
        def dp(i):
            if i >= len(power):
                return 0

            val = count[power[i]] * power[i]
            res = val

            if i + 1 < len(power) and power[i + 1] > power[i] + 2:
                res = val + dp(i + 1)
            elif i + 2 < len(power) and power[i + 2] > power[i] + 2:
                res = val + dp(i + 2)
            elif i + 3 < len(power):
                res = val + dp(i + 3)
            
            return max(res, dp(i + 1))

        return dp(0)
