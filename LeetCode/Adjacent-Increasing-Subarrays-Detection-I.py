class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        q = deque()
        valid = [False] * len(nums)

        for i, num in enumerate(nums):
            while q and q[-1][1] >= num:
                q.pop()
            q.append((i, num))
            while q and q[0][0] < i - k + 1:
                q.popleft()
            if len(q) == k:
                valid[i] = True

        for i in range(len(nums) - 1, (2 * k) - 2, -1):
            if valid[i] and valid[i - k]:
                return True
        return False