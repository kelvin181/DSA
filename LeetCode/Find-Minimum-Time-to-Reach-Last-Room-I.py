class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        ROWS = len(moveTime)
        COLS = len(moveTime[0])
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        heap = [(0, (0, 0))] # total time, cell
        min_moves = {(r, c): inf for r in range(ROWS) for c in range(COLS)} # set for min time to reach a cell
        min_moves[(0, 0)] = 0 # min time to reach (0, 0) is 0 because we start on it
        
        # run dijkstras
        while heap:
            # current cell
            time, (r, c) = heapq.heappop(heap)
            if r == ROWS - 1 and c == COLS - 1: # reached the end
                return time
            # move in every direction
            for dr, dc in d:
                if 0 <= r + dr < ROWS and 0 <= c + dc < COLS:
                    # in bounds
                    t = max(time, moveTime[r + dr][c + dc]) + 1 # time to reach the neigh cell
                    if t < min_moves[(r + dr, c + dc)]:
                        # add to heap if we have found a faster way to reach the neigh cell
                        min_moves[(r + dr, c + dc)] = t
                        heapq.heappush(heap, (t, (r + dr, c + dc)))
            
        # shouldnt reach
        return -1
