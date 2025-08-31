class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # store each row, col and square to see possible valid numbers then backtrack
        cols = {i: set() for i in range(9)}
        rows = {i: set() for i in range(9)}
        squares = {(i, j): set() for i in range(3) for j in range(3)}

        need = deque()

        for r in range(9):
            for c in range(9):
                if board[r][c].isdigit():
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[(r // 3, c // 3)].add(board[r][c])
                else:
                    need.append((r, c))
        
        def backtrack():
            if not need:
                return True

            r, c = need[0]
            for num in range(1, 10):
                num = str(num)
                if num not in cols[c] and num not in rows[r] and num not in squares[(r // 3, c // 3)]:
                    board[r][c] = num
                    cols[c].add(num)
                    rows[r].add(num)
                    squares[(r // 3, c // 3)].add(num)
                    need.popleft()
                    if backtrack():
                        return True
                    else:
                        board[r][c] = "."
                        cols[c].remove(num)
                        rows[r].remove(num)
                        squares[(r // 3, c // 3)].remove(num)
                        need.appendleft((r, c))
            return False

        backtrack()