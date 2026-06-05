class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        # Step 1: Sort the scores to place close values next to each other
        nums.sort()
        
        # Initialize the minimum difference to a large value
        min_diff = float('inf')
        
        # Step 2: Slide a window of size k across the sorted array
        # The window starts at index i and ends at index i + k - 1
        for i in range(len(nums) - k + 1):
            current_diff = nums[i + k - 1] - nums[i]
            if current_diff < min_diff:
                min_diff = current_diff
                
        return min_diff