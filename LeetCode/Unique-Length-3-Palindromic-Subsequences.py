class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        
        for i in range(26):
            first = s.find(chr(ord('a') + i))
            if first == -1:
                continue
            last = s.rfind(chr(ord('a') + i))
            res += len(set(list(s[first + 1: last])))
        
        return res
