class Solution:
    # TC : O(n)
    # SC : O(1)    
    def minOperations(self, n: int) -> int:
        ans=0
        for i in range(1,n,2):
            ans+=(n-i)
        return ans    

# 2nd method
class Solution:
    def minOperations(self, n: int) -> int:
        if(n%2==1):
            n=n//2
            return n*(n+1)
        else:
            n=n//2
            return n*n        