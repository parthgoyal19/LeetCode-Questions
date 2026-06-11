# Last updated: 11/06/2026, 21:32:03
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # Target found, return its index
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1  # Target is in the left half
                
        # If not found, 'left' will point to the insertion index
        return left