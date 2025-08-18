#TC: O(n)
#TC: 1
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero=result=0
        for num in nums:
            if num == 0:
                zero+=1
                result+=zero
            else:
                zero=0
        return result            