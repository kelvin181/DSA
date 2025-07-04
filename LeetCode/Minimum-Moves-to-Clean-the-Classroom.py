class Solution:
    def minMoves(self, grid: List[str], energy: int) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        litter = 0
        visited = defaultdict(int) # state is cell and which litter has been picked up. stores max energy for each state.
        grid = [list(row) for row in grid]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "S":
                    q = deque([(r, c, energy, 0, 0)])
                    visited[(r, c, 0)] = energy
                if grid[r][c] == "L":
                    grid[r][c] = str(litter)
                    litter += 1

        if litter == 0:
            return 0

        res = 0
        
        while q:
            r, c, e, mask, moves = q.popleft()
            moves += 1

            for dr, dc in d:
                row = r + dr
                col = c + dc

                if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "X":
                    continue
                
                if grid[row][col] == "R":
                    currE = energy
                else:
                    currE = e - 1
                
                if grid[row][col].isdigit():
                    nxt = mask | (1 << int(grid[row][col])) # 10 bits, 1 if seen, 0 if not
                    if nxt.bit_count() == litter: # first litter bits == 1
                        return moves
                else:
                    nxt = mask
                
                state = (row, col, nxt)

                if visited[state] < currE: # energy level at current state is greater than previous iterations
                    visited[state] = currE
                    q.append((row, col, currE, nxt, moves))

        return -1
