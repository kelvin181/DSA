class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        nxt = []
        starts = [event[0] for event in events]

        for i, (start, end, val) in enumerate(events):
            nxt_index = bisect_right(starts, end)
            nxt.append(nxt_index)

        memo = [[-1] * len(events) for _ in range(k)]

        def find(i, amount):
            if amount == k or i == len(events):
                return 0
            
            if memo[amount][i] != -1:
                return memo[amount][i]

            # take
            take = events[i][2]
            take += find(nxt[i], amount + 1)

            # leave
            leave = find(i + 1, amount)
            memo[amount][i] = max(take, leave)
            return memo[amount][i]
        
        return find(0, 0)
