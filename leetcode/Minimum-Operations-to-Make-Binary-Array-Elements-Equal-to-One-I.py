class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(nums, i):
            # Flip the current bit and the next two bits
            nums[i] ^= 1
            nums[i+1] ^= 1
            nums[i+2] ^= 1
        
        count = 0
        # Iterate up to len(nums)-2 so we don't go out of bounds
        for i in range(len(nums) - 2):
            # If nums[i] is not 1, flip the bits starting at index i
            if nums[i] != 1:
                flip(nums, i)
                count += 1
        
        # After the loop, check if the last two elements can be made 1
        if nums[-2] == 0 or nums[-1] == 0:
            return -1
        
        return count

#TC=O(3*n) as fliping element 3times when not current element is not 1 =O(n)
#SC=O(1)
