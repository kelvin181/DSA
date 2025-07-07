class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        res = 0
        i = 0

        for day in range(1, max(event[1] for event in events) + 1):
            # include all events we can attend today
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            # remove the events that we can no longer attend
            while heap and heap[0] < day:
                heapq.heappop(heap)
            # if there is an event we can attend today, attend it
            if heap:
                res += 1
                heapq.heappop(heap)
        
        return res
