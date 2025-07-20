'''
| Approach       | sumRange TC | Space | Use When...                         |
| -------------- | ----------- | ----- | ----------------------------------- |
| Prefix Sum     | O(1)        | O(n)  | Many repeated queries               |
| On-the-fly Sum | O(n)        | O(1)  | One or few queries, no extra memory |
'''
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.prefixnums=[0]
        tsum=0
        for num in self.nums:
            tsum+=num
            self.prefixnums.append(tsum)
            
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixnums[right+1] - self.prefixnums[left]

    # def sumRange(self, left: int, right: int) -> int:
    #     ans=0
    #     for num in self.nums[left:right+1]:
    #         ans+=num
    #     return ans
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
