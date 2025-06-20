# TC - O(n)
# SC - O(1)
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        max_dis = 0   # This will store the maximum Manhattan distance found
        north = south = east = west = 0   # Track how many times we move in each direction
        for ind in range(len(s)):
          # Update direction counters based on the current character
            if s[ind] == 'N':
                north += 1
            elif s[ind] == 'S':
                south += 1
            elif s[ind] == 'W':
                west += 1
            elif s[ind] == 'E':
                east += 1

           # Compute net movement along vertical (y-axis) and horizontal (x-axis)
            x = abs(north - south)   # net vertical movement (North - South)
            y = abs(east - west)     # net horizontal movement (East - West)
            d = x + y                # current Manhattan distance from origin

            # Calculate how much we can improve the distance using at most k changes
            # ind + 1 is number of steps so far
            # d is current distance — the rest (ind + 1 - d) are moves that cancel out (e.g., N vs. S)
            # Changing a move can increase distance by up to 2, so max boost is 2*k
            # But we can only fix as many moves as actually cancel out
          
            dis = d + min( 2 * k, ind + 1 - d )
            max_dis = max(max_dis,dis)
        return max_dis
