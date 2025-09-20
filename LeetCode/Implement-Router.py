class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit
        self.q = deque()
        self.items = set()
        self.destinations = {}

    def addPacket(self, s: int, d: int, t: int) -> bool:
        if (s, d, t) in self.items:
            return False
        if len(self.items) == self.limit:
            removed = self.q.popleft()
            self.items.remove(removed)
            self.destinations[removed[1]].popleft()
        self.q.append((s, d, t))
        self.items.add((s, d, t))
        if d not in self.destinations:
            self.destinations[d] = deque()
        self.destinations[d].append(t)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.items.remove((s, d, t))
        self.destinations[d].popleft()
        return [s, d, t]

    def getCount(self, d: int, s: int, e: int) -> int:
        if d not in self.destinations:
            return 0
            
        arr = self.destinations[d]
        left = inf
        right = -inf

        # first greater than or equal to s 
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] >= s:
                left = min(left, m)
                r = m - 1
            else:
                l = m + 1
        
        # first less than or equal to e
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] <= e:
                right = max(right, m)
                l = m + 1
            else:
                r = m - 1

        return max(0, right - left + 1)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)