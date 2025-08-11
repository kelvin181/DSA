class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        string = bin(n)[2:][::-1]

        pre = [1]
        for i in range(len(string)):
            if int(string[i]):
                pre.append(pre[-1] * 2 ** i)
                
        res = []
        for a, b in queries:
            res.append(int(pre[b + 1] / pre[a]) % MOD)

        return res
