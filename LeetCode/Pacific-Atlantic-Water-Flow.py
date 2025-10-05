class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        pacifics = set()
        atlantics = set()

        def dfs_p(r, c):
            pacifics.add((r, c))
            for dr, dc in d:
                if (
                    (r + dr, c + dc) not in pacifics and 
                    0 <= r + dr < ROWS and 
                    0 <= c + dc < COLS and 
                    heights[r][c] <= heights[r + dr][c + dc]
                ):
                    dfs_p(r + dr, c + dc)

        def dfs_a(r, c):
            atlantics.add((r, c))
            for dr, dc in d:
                if (
                    (r + dr, c + dc) not in atlantics and 
                    0 <= r + dr < ROWS and 
                    0 <= c + dc < COLS and 
                    heights[r][c] <= heights[r + dr][c + dc]
                ):
                    dfs_a(r + dr, c + dc)

        for c in range(COLS):
            dfs_p(0, c)
        for r in range(ROWS):
            dfs_p(r, 0)
        
        for c in range(COLS):
            dfs_a(ROWS - 1, c)
        for r in range(ROWS):
            dfs_a(r, COLS - 1)
        
        return [list(coord) for coord in pacifics & atlantics]
