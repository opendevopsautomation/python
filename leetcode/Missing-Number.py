class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)

#2nd Method
'''
(sum of numbers from 0 to n is given by the formula) - (actual sum is found by adding all the elements in the array)
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=n*(n + 1)//2
        sum_of_list=sum(nums)
        return total - sum_of_list        