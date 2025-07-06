#TC: add(index, val)	O(1), count(tot)	O(m)
#SC: O(n) → for nums2 and its frequency map
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        """
        Initialize the data structure with nums1 and nums2.
        Also builds a frequency map for nums2 to enable fast counting.
        
        Time Complexity: O(n), where n = len(nums2)
        """
        self.nums1=nums1
        self.nums2=nums2
        self.freq={}
      
        # Build a frequency map for nums2 to avoid traversing nums2 during sum queries
        for num in nums2:
            self.freq[num]= self.freq.get(num,0)+1

    def add(self, index: int, val: int) -> None:
        """
        Add 'val' to nums2[index], and update the frequency map accordingly.

        Time Complexity: O(1)
        """
        old_val = self.nums2[index]
        new_val = old_val + val
        self.nums2[index]=new_val

        # Update the frequency map
        self.freq[old_val] -= 1
        self.freq[new_val]=self.freq.get(new_val,0)+1
       

    def count(self, tot: int) -> int:
        """
        Count number of pairs (i, j) such that nums1[i] + nums2[j] == tot.

        Time Complexity: O(m), where m = len(nums1)
        """
        ans=0
        for val in self.nums1:
            sec_val=tot-val
            if sec_val in self.freq.keys():
                # Add the number of occurrences of the needed complement in nums2
                ans+=self.freq[sec_val]
        return ans

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
