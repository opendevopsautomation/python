#Brute-Force Approach 
#Time Complexity: O(n²) → due to nested loops for all (i, j) combinations.
#Space Complexity: O(1)

# class Solution:
#     def maximumDifference(self, nums: List[int]) -> int:
#         result = -1
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[j] > nums[i]:
#                     result = max(result, nums[j] -  nums[i])
#         return result 


#Approach-2 Linear Approach 
#Time Complexity: O(n) 
#Space Complexity: O(1) → only variables minNum and result

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minNum = nums[0]
        result = -1
        for num in nums[1:]:
            if num > minNum:
                result = max(result,num - minNum)
            minNum = min(minNum,num)        
        return result
