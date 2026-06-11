# Last updated: 11/06/2026, 21:33:19
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store the value and its corresponding index
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in the map, we found the pair
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, store the current number and its index in the map
            seen[num] = index