class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid  # Record the potential answer
                    if is_first:
                        right = mid - 1  # Keep looking left for the first position
                    else:
                        left = mid + 1   # Keep looking right for the last position
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return bound

        # Run binary search for both the first and last positions
        first_pos = find_bound(is_first=True)
        last_pos = find_bound(is_first=False)
        
        return [first_pos, last_pos]