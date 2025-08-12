class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            val = i ** x
            for j in range(n, val - 1, -1):
                dp[j] += dp[j - val] 
                dp[j] %= MOD
        
        return dp[-1]
