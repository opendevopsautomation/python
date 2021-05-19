class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        mid=nums[len(nums)//2]
        for i in nums:
            result+=abs(i-mid)
        return result
#2nd Method
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        result=0
        for i in range(len(nums)//2):
            result+=nums[~i]-nums[i]
        return result        