# Last updated: 11/06/2026, 21:29:55
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # The first element is always the cost of the first subarray
        first_cost = nums[0]
        
        # Get all elements after the first one
        remaining_elements = nums[1:]
        
        # Sort them to easily find the two smallest values
        remaining_elements.sort()
        
        # Sum the first element and the two smallest remaining elements
        return first_cost + remaining_elements[0] + remaining_elements[1]