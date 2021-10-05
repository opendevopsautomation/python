class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        temp1=1
        temp2=1
        for i in range(2,n+1):
            result=temp1+temp2
            temp1,temp2=temp2,result
        return result