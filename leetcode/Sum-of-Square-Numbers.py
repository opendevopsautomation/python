class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        right=int(c**(1/2))
        left=0
        while left <= right:
            temp= left*left+right*right
            if temp==c:
                return True
            if temp < c:
                left+=1
            else:
                right-=1
        return False