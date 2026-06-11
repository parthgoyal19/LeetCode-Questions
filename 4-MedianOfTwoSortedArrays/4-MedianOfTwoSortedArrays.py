# Last updated: 11/06/2026, 21:33:12
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize the binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        total_left = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2  # Partition index for nums1
            j = total_left - i     # Partition index for nums2
            
            # Get the elements around the partition boundaries, handling edge cases with infinity
            A_left = nums1[i - 1] if i > 0 else float('-inf')
            A_right = nums1[i] if i < m else float('inf')
            
            B_left = nums2[j - 1] if j > 0 else float('-inf')
            B_right = nums2[j] if j < n else float('inf')
            
            # If a valid partition is found
            if A_left <= B_right and B_left <= A_right:
                # Odd total elements: median is the maximum of the left side
                if (m + n) % 2 == 1:
                    return float(max(A_left, B_left))
                # Even total elements: median is the average of the middle elements
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            # If we need to shift the partition in nums1 to the left
            elif A_left > B_right:
                high = i - 1
            # If we need to shift the partition in nums1 to the right
            else:
                low = i + 1
                
        return 0.0