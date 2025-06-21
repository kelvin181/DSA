class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count = Counter(word)
        res = len(word)

        # 26 ^ 2 because 26 chars in alphabet
        for a in count.values():
            curr = 0
            for b in count.values():
                if b < a:
                    curr += b
                elif b > a + k:
                    curr += b - (a + k)
            res = min(res, curr)
            
        return res
