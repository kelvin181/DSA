class Solution:
        
    def minMoves(self, matrix: List[str]) -> int:

        def updateQ(r, c):
            if mat[r][c] == ".":
                q.append((r, c))
                mat[r][c] = "#" # set as visited
            elif mat[r][c] in portals: 
                q.extend(portals[mat[r][c]]) # append all of portals arr onto q
                portals.pop(mat[r][c])
            # ignore "#"

        ROWS = len(matrix)
        COLS = len(matrix[0])
        res = 0
        mat = list(map(list, matrix))
        portals = defaultdict(list)
        d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        q = deque()

        # create portals dict
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c].isalpha():
                    portals[mat[r][c]].append((r, c))
        
        # init q
        updateQ(0, 0)

        while q:
            if (ROWS - 1, COLS - 1) in q:
                return res
            
            # q always has cells at the same distance from (0, 0)
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in d: # add all possible reachable cells in 1 move
                    if 0 <= r + dr < ROWS and 0 <= c + dc < COLS:
                        updateQ(r + dr, c + dc)

            res += 1
        
        return -1
