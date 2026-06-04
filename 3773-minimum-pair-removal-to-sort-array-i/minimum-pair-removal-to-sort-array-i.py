class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        operations = 0
        
        while True:
            # Check if the current array is non-decreasing
            is_sorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    is_sorted = False
                    break
            
            # If already non-decreasing, we are done
            if is_sorted:
                return operations
            
            # Find the leftmost adjacent pair with the minimum sum
            min_sum = float('inf')
            target_idx = -1
            
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i+1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    target_idx = i
            
            # Replace the pair at target_idx with their sum
            nums[target_idx] = min_sum
            nums.pop(target_idx + 1)
            
            operations += 1