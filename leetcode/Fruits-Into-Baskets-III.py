#https://www.youtube.com/watch?v=Ydrwd7ro8po&ab_channel=Intuit%26Code
#TC: O(n*sqrt(n))
#SC: O(sqrt(n))
# This solution uses a sector-based approach to optimize the placement of fruits into baskets.
# It divides the baskets into sectors and processes each sector independently.
from typing import List

import math
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        sec_size = int(math.sqrt(n)) or 1  # avoid division by zero
        sector = []
        
        # Build the sector max values
        for idx in range(0, n, sec_size):
            sector.append(max(baskets[idx:min(idx + sec_size, n)]))

        unplaced = 0

        for fruit in fruits:
            placed = False
            for sec_idx in range(len(sector)):
                # Skip this sector if no basket in it can hold the fruit
                if fruit > sector[sec_idx]:
                    continue

                # Determine the start and end of the sector
                start = sec_idx * sec_size
                end = min(start + sec_size, n)

                for i in range(start, end):
                    if baskets[i] >= fruit:
                        baskets[i] = 0  # mark basket as used
                        # Update sector max
                        sector[sec_idx] = max(baskets[start:end])
                        placed = True
                        break

                if placed:
                    break

            if not placed:
                unplaced += 1

        return unplaced
