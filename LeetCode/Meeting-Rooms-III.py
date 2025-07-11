class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available_rooms = [i for i in range(n)]
        current_meetings = []
        room_count = {i: 0 for i in range(n)}

        for i, (start, end) in enumerate(meetings):
            meeting_duration = end - start

            while current_meetings and current_meetings[0][0] <= start:
                e, r = heapq.heappop(current_meetings)
                heapq.heappush(available_rooms, r)

            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(current_meetings, (end, room))
            else:
                e, room = heapq.heappop(current_meetings)
                start = max(start, e)
                end = start + meeting_duration
                heapq.heappush(current_meetings, (end, room))
                
            room_count[room] += 1

        max_count = max(room_count.values())
        for i in room_count:
            if room_count[i] == max_count:
                return i
        return -1
