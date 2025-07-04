class Solution:
    def maxSubstrings(self, word: str) -> int:
        seen = {}
        l = 0
        res = 0

        for r, char in enumerate(word):
            if char in seen:
                if r - seen[char] + 1 >= 4:
                    if seen[char] >= l:
                        l = r + 1
                        res += 1
                        del seen[char]
                    else:
                        seen[char] = r
                else:
                    if seen[char] < l:
                        seen[char] = r
            else:
                seen[char] = r

        return res
        