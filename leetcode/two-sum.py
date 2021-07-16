class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct={}
        for idx,num in enumerate(nums):
            diff=target-num
            if diff in dct:
                return [dct[diff],idx]
            else:
                dct[num]=idx