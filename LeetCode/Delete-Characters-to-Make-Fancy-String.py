class Solution:
    def makeFancyString(self, s: str) -> str:
        l = 0
        res = []

        for r in range(len(s)):
            if s[l] != s[r]:
                if r - l == 1:
                    res.append(s[l])
                else:
                    res.append(s[l])
                    res.append(s[l])
                l = r
        
        if len(s) - l == 1:
            res.append(s[l])
        else:
            res.append(s[l])
            res.append(s[l])
        return "".join(res)
