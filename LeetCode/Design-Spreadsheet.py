class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col_char = cell[0]
        row = int(cell[1:]) - 1
        col = ord(col_char) - ord("A")
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        first, second = formula.split("+")
        first = first[1:]

        if first.isdigit():
            first = int(first)
        else:
            first_row = int(first[1:]) - 1
            first_col = ord(first[0]) - ord("A")
            first = self.sheet[first_row][first_col]
        
        if second.isdigit():
            second = int(second)
        else:
            second_row = int(second[1:]) - 1
            second_col = ord(second[0]) - ord("A")
            second = self.sheet[second_row][second_col]

        return first + second


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)