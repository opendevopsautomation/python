#TC: O(n)
#SC: O(1)
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        curr_length = max_length = 0
        for num in nums:
            if num  == max_num:
                curr_length += 1
                max_length = max(max_length, curr_length)
            else:
                curr_length = 0
        
        return max_length

# Example usage:
obj = Solution()
nums = [1,2,3,3,2,2]
print(obj.longestSubarray(nums))  # Output: 2 (the longest subarray with maximum bitwise AND is [3, 3])