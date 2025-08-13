#TC: O(log n)
#SC: O(1)
# Comment version TC: O(1) and SC: O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        # lg = round(log(n,3))
        # return 3**lg == n
        while n > 1:
            remainder = n % 3
            if remainder != 0:
                return False
            else:
                n = n //3
        return True
