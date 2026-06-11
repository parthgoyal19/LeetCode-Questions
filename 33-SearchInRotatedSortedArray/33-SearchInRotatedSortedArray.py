# Last updated: 11/06/2026, 21:32:11
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # If target is found, return its index
            if nums[mid] == target:
                return mid
            
            # Check if the left half is strictly sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right half must be strictly sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
        # Target was not found in the array
        return -1