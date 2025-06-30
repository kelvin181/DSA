class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        cols = []
        rows = []

        for row in grid:
            rows.append(sum(row))

        for c in range(len(grid[0])):
            val = 0
            for r in range(len(grid)):
                val += grid[r][c]
            cols.append(val)

        def find(arr):
            total = sum(arr)
            curr = 0
            for i in range(len(arr) - 1):
                curr += arr[i]
                total -= arr[i]
                if curr == total:
                    return True
            return False

        return find(rows) or find(cols)
