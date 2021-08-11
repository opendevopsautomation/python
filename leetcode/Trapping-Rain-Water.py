#TC=O(n)
'''Water can be trapped only if any block before and after the ith position has greater height.
    Logic: Need to pre-process & store somewhere.
   1] We will travse from 1 to length of the array & store the max element of ith position of height and left[-1] (temporary list) on ith position .
   2]Similarly step 1 but from length of the array to 0 th position.

'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        left=[height[0]]
        for i in range(1,len(height)):
            if height[i]> left[-1]:
                left.append(height[i])
            else:
                left.append(left[i-1])
        right=[height[-1]]
        for i in range(len(height)-2, -1, -1):

            if height[i]> right[-1]:
                right.append(height[i])
            else:
                right.append(right[-1])
        right.reverse()
        result=0
        print(left,right)
        for i in range(len(height)):

            result+=min(left[i],right[i])-height[i]
        return result
