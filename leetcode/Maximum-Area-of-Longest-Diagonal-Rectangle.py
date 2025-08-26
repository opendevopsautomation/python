# TC: O(n)  -> Looping once through all rectangles
# SC: O(1)  -> Only a few scalar variables used, no extra space that grows with input

from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag_sq = 0 # Store the maximum diagonal squared
        max_area = 0 # Store the area corresponding to the maximum diagonal
        # Iterate through each rectangle's dimensions
        for length, width in dimensions:
            diag_sq = length * length + width * width # Calculate the diagonal squared
            area = length * width # Calculate the area of the rectangle
            # Update max_diag_sq and max_area if a larger diagonal is found
            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                max_area = area
            # If the diagonal is equal to the current maximum, update max_area if needed
            elif diag_sq == max_diag_sq:
                max_area = max(max_area,area)
        return max_area