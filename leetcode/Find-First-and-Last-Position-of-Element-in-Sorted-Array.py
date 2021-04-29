class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        left=self.leftsearch(nums,target)
        right=self.rightsearch(nums,target)
        return [left,right]
    
    def leftsearch(self,nums,target):
        l=0
        r=len(nums)-1
        res=-1
        while l <= r:

            mid=(l+r)//2
            print(l,r,mid)
            if nums[mid] < target:
                l=mid + 1
            elif nums[mid] > target :
                r=mid - 1
            else:
                res=mid
                r=mid - 1
        return res  
    
    def rightsearch(self,nums,target):
        l=0
        r=len(nums)-1
        res=-1
        while l <= r:
            mid=(l+r)//2
            if nums[mid] < target:
                l=mid + 1
            elif nums[mid] > target :
                r=mid - 1
            else:
                res=mid
                l=mid+1
        return res