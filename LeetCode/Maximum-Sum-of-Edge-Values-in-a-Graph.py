class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        if n == len(edges):
            # full cycle
            if n == 3:
                return 11
            else:
                curr = 11
                for i in range(4, n + 1):
                    curr -= (i - 1) * (i - 2)
                    curr += (i * (i - 1)) + (i * (i - 2))
                return curr
        else:
            # linked list
            if n == 2:
                return 2
            elif n == 3:
                return 9
            else:
                curr = 9
                for i in range(4, n + 1):
                    curr -= (i - 1) * (i - 2)
                    curr += (i * (i - 1)) + (i * (i - 2))
                return curr

        return -1
