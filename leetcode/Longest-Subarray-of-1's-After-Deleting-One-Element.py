#TC: O(n)
#SC: O(1)

#Reference: https://www.youtube.com/watch?v=jhBrybXSFTs
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr = prev = result = 0

        for num in nums:
            if num == 0:
                # Combine current and previous streaks of 1s, simulating deletion of this 0
                result = max(result, curr + prev)
                prev = curr
                curr = 0
            else:
                curr += 1

        # In case array ends with 1s
        result = max(result, curr + prev)

        # If all elements are 1s, we must delete one
        return result - 1 if result == len(nums) else result
