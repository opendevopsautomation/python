# TC: Time Complexity: O(n × log m), n = number of piles (len(piles)),m = the maximum number of bananas in any pile (max(piles))
# SC: O(1)

#Binary search Approach
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = right

        while left <= right:
            mid = (left + right) // 2
            hours = 0  # Reset for each test speed

            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                result = mid        # Valid speed, try to find smaller
                right = mid - 1
            else:
                left = mid + 1      # Too slow, increase speed

        return result

#Brute Force Approach      
        # min=max(piles)
        # for i in range(1,max(piles)+1):
        #     value=0
        #     for pile in piles:
        #         temp=math.ceil(pile/i)
        #         value +=temp
        #         if value > h:
        #             break
        #     if value <= h:
        #         min=i
        #         break
        # return min
           
