# TC: O(n)
# SC: O(n / k × k) = O(n) The result list stores n / k strings, each of length k, totaling O(n) space.

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list:
        # If the length of s is not a multiple of k, add fill characters at the end
        if len(s) % k != 0:
            remainder = len(s) % k
            s += fill * (k - remainder)

        # Split the string into parts of length k and return as a list
        return [s[i:i+k] for i in range(0, len(s), k)]
