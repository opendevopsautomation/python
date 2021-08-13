"""
1. Check is there any element 0 in first row/column enble the flag to make all element 0
2. Find the element with zero value and mark first element of row and column as 0.
3. Iterate the matrix & make all element 0 of that row and column.
4. Iterate the matrix on the basis of flag & make element wrt that 0
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        first_row = False
        first_col = False
        m = len(matrix)
        n = len(matrix[0])

        for col in range(n):         
            if matrix[0][col] == 0:
                first_col=True
        for row in range(m):
            if matrix[row][0] == 0:
                first_row=True
                
        for row in range(m):
            for col in range(n):
                if matrix[row][col]==0:
                    matrix[row][0]=matrix[0][col]=0

        for row in range(1,m):
            for col in range(1,n):
                if matrix[0][col] == 0 or matrix[row][0] == 0: 
                    matrix[row][col]=0
                    
        if first_row:
            for row in range(m):
                matrix[row][0]=0                            
        if first_col :
            for col in range(n):
                matrix[0][col]=0
