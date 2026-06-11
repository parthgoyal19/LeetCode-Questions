# Last updated: 11/06/2026, 21:31:52
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            # Place each number in its correct index position if possible
            # e.g., the number 3 belongs at index 2 (nums[i] - 1)
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # Swap the elements to place nums[i] at its correct target index
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
                
        # Scan the array to find the first index that doesn't match its value
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all numbers from 1 to n are present, the answer is n + 1
        return n + 1