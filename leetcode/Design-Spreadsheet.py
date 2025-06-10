class Spreadsheet:

    def __init__(self, rows: int):
        # Initialize a matrix with given number of rows and 26 columns (A to Z), all set to 0
        self.matrix = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        # Set the value of a specific cell (e.g., "A1") in the spreadsheet
        col = ord(cell[0]) - ord('A')         # Convert column letter to index (A=0, B=1, ..., Z=25)
        row = int(cell[1:]) - 1               # Convert row number to 0-based index
        self.matrix[row][col] = value

    def resetCell(self, cell: str) -> None:
        # Reset the specified cell to 0
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.matrix[row][col] = 0

    def getValue(self, formula: str) -> int:
        # If formula starts with "=", remove it
        if formula.startswith("="):
            formula = formula[1:]

        # Split the formula by "+" to evaluate each operand separately
        operands = formula.split("+")
        result = 0

        for op in operands:
            op = op.strip()  # Remove extra spaces if any
            if op[0].isalpha():
                # Operand is a cell reference like "A1"
                col = ord(op[0]) - ord('A')
                row = int(op[1:]) - 1
                result += self.matrix[row][col]
            else:
                # Operand is a number like "5"
                result += int(op)

        return result
        # op1 = operands[0][1:]
        # op2 = operands[1]
        # op1val, op2val = 0, 0
        # if 65 <= ord(op1[0]) <= 90:
        #     col = ord(op1[0]) - ord('A')
        #     row = int(op1[1:]) - 1
        #     op1val = self.matrix[row][col]
        # else:
        #     op1val = int(op1)
        
        # if 65 <= ord(op2[0]) <= 90:
        #     col = ord(op2[0]) -  ord('A')
        #     row = int(op2[1:])-1
        #     op2val =  self.matrix[row][col]
        # else:
        #     op2val = int(op2)
       
        # return op1val + op2val

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
