#Approach 1 — Brute Force (3 Loops)
#TC:  O(n³) --> 3 nested loops: i, j, k → O(n³)
#SC: O(k) --> k is the number of unique triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_val = set()
        nums.sort()  

        # Try all possible combinations of 3 elements (i < j < k)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    if total == 0:
                        unique_val.add((nums[i], nums[j], nums[k]))

        return [result for result in unique_val]

#Approach 2 — Optimized with Sorting + Two Pointers
#TC: O(n²) --> Sorting: O(n log n),i: O(n),Inner loop with two pointers: up to O(n) per i
#SC: O(k) --> k = number of unique triplets
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique_val = set()

        # Loop through each number as the first in the triplet
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            # Use two-pointer approach to find valid pairs for nums[i]
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    unique_val.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1

        return [result for result in unique_val]
