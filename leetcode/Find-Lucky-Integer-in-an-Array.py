#Approach 1
#TC= O(n)
#SC= O(n)

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1

        ans=-1
        for idx in freq.keys():
            if idx==freq[idx]:
                ans=max(ans,idx)
        return ans

#Approach 2
#TC= O(n)
#SC= O(1)
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=[0]*501 #Fixed array size (501 elements)
        for num in arr:
            freq[num]+=1

      # check from largest to smallest
        for idx in range(500,0,-1):
            if freq[idx] == idx:
                return idx
        return -1
  
