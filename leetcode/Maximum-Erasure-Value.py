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
# Using two pointers and hashmap to track unique elements   
#TC: O(n)
#SC: O(n)
# class Solution:
#     def maximumUniqueSubarray(self, nums: List[int]) -> int:
#         left,right=0,0
#         win_sum=0
#         max_sum=0
#         hashmap={}
#         while right < len(nums):
            
#             if nums[right] not in hashmap.keys():
#                 hashmap[nums[right]] = True
#                 win_sum += nums[right]
#                 max_sum = max(win_sum, max_sum )
#                 right+=1
#             else:    
#                 del hashmap[nums[left]]
#                 win_sum -= nums[left]
#                 left+=1
            
#         return max_sum
    