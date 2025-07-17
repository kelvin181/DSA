# q for current router
# set for packets in current router
# hashmap of queues that store sorted times for each destination
# binary search for count

class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.packets = set()
        self.destinations = {}
        self.limit = memoryLimit
        self.length = 0

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if tuple([source, destination, timestamp]) in self.packets:
            return False
        if self.length == self.limit:
            s, d, t = self.q.popleft()
            self.packets.remove((s, d, t))
            self.destinations[d].popleft()
            self.length -= 1
        self.q.append((source, destination, timestamp))
        self.packets.add((source, destination, timestamp))
        if destination not in self.destinations:
            self.destinations[destination] = deque()
        self.destinations[destination].append(timestamp)
        self.length += 1
        return True

    def forwardPacket(self) -> List[int]:
        if self.length == 0:
            return []
        s, d, t = self.q.popleft()
        self.packets.remove((s, d, t))
        self.destinations[d].popleft()
        self.length -= 1
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:

        times = self.destinations.get(destination, [])

        if not times:
            return 0

        # search first number >= startTime
        left = inf
        l = 0
        r = len(times) - 1
        while l <= r:
            m = l + (r - l) // 2
            if times[m] < startTime:
                l = m + 1
            else:
                left = min(left, m)
                r = m - 1

        # search first number <= endTime
        right = -inf
        l = 0
        r = len(times) - 1
        while l <= r:
            m = l + (r - l) // 2
            if times[m] > endTime:
                r = m - 1
            else:
                right = max(right, m)
                l = m + 1
        
        if right == -inf or left == inf:
            return 0
        return right - left + 1

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)