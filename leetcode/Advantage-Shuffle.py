class Solution:
    # TC : O(nlogn)
    # SC : O(n)
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        B = sorted([(val, i) for i, val in enumerate(B)])
        A.sort()
        low=0
        high=len(A)-1
        ans=[0] * len(A)
        while B:
            temp=B.pop()
            maxValueInB = temp[0]
            indexInB= temp[1]
            if(A[high] > maxValueInB):
                ans[indexInB] = A[high]
                high-=1
            else:
                ans[indexInB] = A[low];
                low+=1
                
        return ans