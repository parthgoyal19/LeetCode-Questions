# Last updated: 11/06/2026, 21:32:52
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)
        
        # Initialize closest_sum with the sum of the first triplet
        closest_sum = nums[0] + nums[1] + nums[2]
        
        # Iterate through the array, leaving room for at least 2 other elements
        for i in range(n - 2):
            # Optimization: Skip duplicate values for the anchor element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find an exact match, return it immediately
                if current_sum == target:
                    return current_sum
                
                # If the current sum is closer to target than the previous best
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on how current_sum compares to target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum