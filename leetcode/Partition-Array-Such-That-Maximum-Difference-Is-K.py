# Time Complexity: O(n log n) - Sorting [O(n log n)] + Traversing array [O(n)]
# Space Complexity: O(1) 

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        # Step 1: Sort the array to process elements in order
        nums.sort()
        
        # Step 2: Start the first subsequence with the first number as the minimum
        min_val = nums[0]
        subsequences = 1  # At least one subsequence is required
        
        # Step 3: Traverse the rest of the sorted array
        for ind in range(1, len(nums)):
            # If the current number is too far from the current min (diff > k)
            # Start a new subsequence
            if nums[ind] - min_val > k:
                min_val = nums[ind]  # Set new min for the next subsequence
                subsequences += 1    # Increment the count
        
        # Step 4: Return the total number of subsequences formed
        return subsequences
