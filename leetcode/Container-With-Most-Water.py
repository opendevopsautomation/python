class Solution:
    def maxArea(self, height: List[int]) -> int:
        #formula to calculate Area = length of shorter vertical line * distance between lines
        left=0
        right=len(height)-1
        maxArea=0
        while(left<right):
            currentArea=min(height[left],height[right])*(right-left)
            maxArea=max(maxArea,currentArea)
            if(height[left] < height[right]):
                left+=1
            else:
                right-=1
        return  maxArea       
    # TC : O(n)
    # SC : O(1)
