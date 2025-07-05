class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False

        need = {}

        for i in range(len(s)):
            diff = ord(t[i]) - ord(s[i])
            if diff < 0:
                diff += 26
            need[diff] = need.get(diff, 0) + 1

        for key in need:
            if key == 0:
                continue
            if k < 26 * (need[key] - 1) + key:
                return False
        
        return True
