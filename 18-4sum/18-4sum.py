# Last updated: 11/06/2026, 21:32:46
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Early termination optimizations
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break  # Smallest possible sum is greater than target
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue  # Largest possible sum with this 'i' is less than target
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Early termination optimizations for the second loop
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue
                
                # Two pointer approach for the remaining two numbers
                left, right = j + 1, n - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res