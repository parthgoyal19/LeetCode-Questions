# Last updated: 11/06/2026, 21:29:44
class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        
        for i in range(n):
            # Calculate target circular index using modulo arithmetic
            target_idx = (i + nums[i]) % n
            result[i] = nums[target_idx]
            
        return result