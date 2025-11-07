class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        curr = 0
        power = []

        # find initial power of each station
        for i in range(min(len(stations), r)):
            curr += stations[i]

        for i in range(len(stations)):
            if i + r < len(stations):
                curr += stations[i + r]
            power.append(curr)
            if i >= r:
                curr -= stations[i - r]

        def search(target):
            count = 0
            curr = 0
            bomb = deque()
            for i, num in enumerate(power):
                if bomb and bomb[0][0] == i:
                    index, value = bomb.popleft()
                    curr -= value
                if num + curr < target:
                    value = target - (num + curr)
                    count += value
                    curr += value
                    bomb.append((i + 2 * r + 1, value))
            return count <= k
        
        # binary search the max min power
        left = 0
        right = max(power) + k
        res = 0
        while left <= right:
            m = left + (right - left) // 2
            if search(m):
                res = max(res, m)
                left = m + 1
            else:
                right = m - 1
        
        return res
