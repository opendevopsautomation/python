from collections import Counter
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Approach 1: Using Counter and max without sorting
        # Time Complexity: O(n + k)
        # Space Complexity: O(k)
        freq = Counter(nums)
        max_freq = max(freq.values())
        #sum counts with max freq
        return sum(count for count in freq.values() if count == max_freq)

        # # Approach 2: Frequency count + Sorting frequencies
        # # Time Complexity: O(n + k log k)
        # # Space Complexity: O(k)
        # num_freq = {}
        # for num in nums:
        #     num_freq[num] = num_freq.get(num, 0) + 1
        # result = 0
        # 
        # sort_freq = sorted(num_freq.items(), key=lambda item: item[1], reverse=True)
        # max_freq = sort_freq[0][1]
        # for _, count in sort_freq:
        #     if count == max_freq:
        #         result += count
        #     else:
        #         break
        # return result
