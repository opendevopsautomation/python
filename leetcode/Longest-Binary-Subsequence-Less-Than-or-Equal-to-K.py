# Time Complexity: O(n), n = length of s
# Space Complexity: O(1)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        value = 0
        power = 0
        
        # Traverse string from right to left (least significant bit first)
        for ind in range(n - 1, -1, -1):
            if s[ind] == '0':
                count += 1  # Always include zeros
            else:
                if power < 32 and value + 2**power <= k:
                    value += 2**power
                    count += 1
            power += 1
            
        return count


