class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        diff = [0] # bits to represent parity of count of chars

        for i, char in enumerate(s):
            diff.append(diff[-1] ^ (1 << (ord(char) - ord('a'))))
        
        return [(diff[r + 1] ^ diff[l]).bit_count() // 2 <= k for l, r, k in queries]
