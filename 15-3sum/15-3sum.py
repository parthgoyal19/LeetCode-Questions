# Last updated: 11/06/2026, 21:32:53
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array
        
        for i in range(len(nums) - 2):
            # Optimization: If the current smallest number is > 0, 
            # no three numbers can sum up to 0.
            if nums[i] > 0:
                break
                
            # Step 3: Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 4: Two-pointer approach
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers inward after finding a valid triplet
                    left += 1
                    right -= 1
                    
                elif total < 0:
                    left += 1  # Sum is too small, increase the left pointer
                else:
                    right -= 1  # Sum is too large, decrease the right pointer
                    
        return res