#TC: O(n*m) n: number of fruits,m: number of baskets
#SC: O(m) m: number of baskets
from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        used = [False] * n
        unplaced = 0

        for fruit in fruits:
            for i, capacity in enumerate(baskets):
                if not used[i] and capacity >= fruit:
                    used[i] = True  # Mark basket as used
                    break  # Fruit placed, move to next fruit
            else:
                unplaced += 1  # No suitable basket found

        return unplaced
