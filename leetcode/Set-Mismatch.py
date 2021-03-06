class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result=[]
        temp=[]
        for i in nums:
            if i in temp:
                result.append(i)
            else:
                temp.append(i)
        i=1
        while i <= len(nums):
            if i not in temp:
                result.append(i)
                break
            i+=1
        return result  