class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        tmp=set()
        start=end=0
        r_sum=max_sum=0
        while end < len(nums):
            if nums[end] not in tmp:
                r_sum+=nums[end] 
                tmp.add(nums[end])
                end+=1
                if r_sum > max_sum:
                    max_sum=r_sum
            else:
                tmp.remove(nums[start])
                r_sum-=nums[start]
                start+=1
        return max_sum