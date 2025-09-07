#TC: O(n), loop runs roughly n/2 times (as left and right move toward the center): O(n)
#SC: O(n) , arr of size n
from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = [0] * n  # Initialize array of size n
        left = 0
        right = n - 1
        val = 1  # Starting value for pairs

        while left < right:
            arr[left] = -val   # Negative value on the left
            arr[right] = val   # Positive value on the right
            left += 1
            right -= 1
            val += 1

        return arr  # Middle stays 0 if n is odd
