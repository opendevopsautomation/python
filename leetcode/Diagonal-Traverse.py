# TC: O(m * n)
# SC: O(m * n)
#Reference:https://www.youtube.com/watch?v=7HAKiGZSrWc
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal_map = {}
        rows, cols = len(mat), len(mat[0])
        
        # Group elements by the sum of their row and column indices
        for row in range(rows):
            for col in range(cols):
                key = row + col
                diagonal_map[key] = diagonal_map.get(key, []) + [mat[row][col]]
        
        result = []
        # Traverse diagonals in order and reverse even-indexed ones
        for key in diagonal_map:
            if key % 2 == 0:
                result.extend(diagonal_map[key][::-1])
            else:
                result.extend(diagonal_map[key])
        
        return result
