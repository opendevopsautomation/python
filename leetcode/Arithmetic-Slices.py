#Arithmetic Formula >> A,B,C (B-C= B-A)
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count=0
        result=0
        for i in range(2,len(A)):
            if (A[i]-A[i-1])==(A[i-1]-A[i-2]):
                count+=1
            else:
                count=0
            result+=count
        return result
#TC: O(n)
#SC: O(1)
