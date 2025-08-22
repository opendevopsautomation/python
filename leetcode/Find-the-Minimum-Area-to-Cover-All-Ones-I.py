#TC: O(m*n) - m: number of rows, n: number of columns
#SC: O(1)

#Ref: https://www.youtube.com/watch?v=DWQBQvMQKcg&ab_channel=Techdose
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # Initialize bounds for the rectangle that will enclose all 1s
        low_x = float('inf')
        high_x = -1
        low_y = float('inf')
        high_y = -1
        for i in range (m):
            for j in range (n):
                if grid[i][j] == 1:
                    low_x = min(low_x,i)
                    high_x = max(high_x,i)
                    low_y = min(low_y,j)
                    high_y = max(high_y,j)
        return (high_x - low_x + 1) *  (high_y - low_y  + 1)
