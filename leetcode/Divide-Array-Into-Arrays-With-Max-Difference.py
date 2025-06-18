#Time	Complexity: O(n log n) [ Sorting - O(nlogn) and Looping: O(n) (since we process 3 elements at a time)]
#Space Complexity:	O(n)

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Step 1: Sort the input list so elements that are close in value stay together.
        nums.sort()
        
        # Initialize the result list to store valid groups of size 3
        result = []

        # Step 2: Iterate through the sorted list in chunks of 3 elements
        for i in range(2, len(nums), 3):
            # nums[i-2], nums[i-1], and nums[i] form one group of 3 elements
            # Step 3: Check if the maximum difference in the group is <= k
            # Since the array is sorted, the difference between the first and last in the group will be the largest
            if nums[i] - nums[i-2] > k:
                # If the difference exceeds k, we cannot form a valid group — return empty list
                return []

            # Step 4: Group is valid, append it to the result
            result.append([nums[i-2], nums[i - 1], nums[i]])

        # Step 5: After processing all groups, return the result
        return result
