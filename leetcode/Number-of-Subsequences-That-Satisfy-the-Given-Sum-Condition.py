class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7  # modulo 10^9 + 7
        nums.sort()  
        left, right = 0, len(nums) - 1  
        sequence = 0  
        
        # Precompute powers of 2 for faster calculations (for subsequences)
        power_of_two = [1]
        for i in range(1, len(nums)):
            power_of_two.append((power_of_two[i-1] * 2) % mod)
        
        # Two-pointer approach to find valid subsequences
        while left <= right:
            if nums[left] + nums[right] > target:  
                right -= 1  
            else:
                sequence = (sequence + power_of_two[right - left]) % mod
                left += 1 
        
        return sequence 
