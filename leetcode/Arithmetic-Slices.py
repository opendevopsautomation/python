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

#2nd Method
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count=[0]*len(A)
        result=0
        print(count)
        for i in range(2,len(A)):
            if (A[i]-A[i-1])==(A[i-1]-A[i-2]):
                count[i]=count[i-1]+1
            else:
                count[i]=0
            result+=count[i]
        return result
#TC: O(n)
#SC: O(n)
