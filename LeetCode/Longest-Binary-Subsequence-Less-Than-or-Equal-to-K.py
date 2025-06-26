class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        vals = deque()
        total = int(s, 2)
        count = 0

        for i in range(len(s)):
            if s[i] == "1":
                vals.append(2 ** (len(s) - i - 1))
        
        while total > k:
            total -= vals.popleft()
            count += 1
        
        return len(s) - count
