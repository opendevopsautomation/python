class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Brute force method (merge + sort) — commented out
        # merged = sorted(nums1 + nums2)
        # length = len(merged)
        # if length % 2 == 0:
        #     return (merged[length // 2 - 1] + merged[length // 2]) / 2
        # else:
        #     return merged[length // 2]

        # Ensure we do binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # Swap to make nums1 the smaller one

        low, high = 0, len(nums1)

        while low <= high:
            # Partition nums1
            partX = (low + high) // 2
            # Partition nums2 so that left side has half the total elements
            partY = (len(nums1) + len(nums2) + 1) // 2 - partX

            # Edge values if partition is at the start or end
            maxLeftX = float("-inf") if partX == 0 else nums1[partX - 1]
            minRightX = float("inf") if partX == len(nums1) else nums1[partX]

            maxLeftY = float("-inf") if partY == 0 else nums2[partY - 1]
            minRightY = float("inf") if partY == len(nums2) else nums2[partY]

            # Check if partition is correct: all left elements <= all right elements
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # Even total length → average of middle two elements
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    # Odd length → median is the max of the left side
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                # Move search window to the left
                high = partX - 1
            else:
                # Move search window to the right
                low = partX + 1

#Time Complexity: O(log(min(m, n)))
#Space Complexity: O(1)
