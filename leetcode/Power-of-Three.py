class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        lg = round(log(n,3))
        return 3**lg == n
        