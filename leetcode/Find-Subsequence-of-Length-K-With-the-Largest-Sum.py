#Approach 1
#TC: O(n log n + k log k)
#SC: O(n) - stores all n elements
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = [] # Store [value, index] pairs
        for idx, val in enumerate(nums):
            min_heap.append([val,idx]) # Add each element with its index
               
        min_heap.sort(key=lambda item:item[0]) # Sort by value (ascending)
        max_sum=sorted(min_heap[-k:],key=lambda item:item[1]) # Take k largest, sort by original index
        return [val for val, idx in max_sum]
      
#Approach 2
#TC: O(n log k) --> O(n log k(Heap operations (in the loop)) + k log k(Sorting takes )) → Dominated by O(n log k) 
#SC: O(k)
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        for idx, val in enumerate(nums):
            heapq.heappush(min_heap,[val,idx])
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Sort selected k elements by their original indices
        min_heap.sort(key=lambda item:item[1])

        # Extract values to form the subsequence
        return [val for val, idx in min_heap]
