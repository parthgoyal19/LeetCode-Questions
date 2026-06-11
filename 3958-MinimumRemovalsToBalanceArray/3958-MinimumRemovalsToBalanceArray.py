# Last updated: 11/06/2026, 21:29:29
class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        # Step 1: Sort the array to easily manage min and max bounds
        nums.sort()
        
        n = len(nums)
        max_len = 0
        i = 0
        
        # Step 2: Expand the right pointer 'j' to find the maximum valid window
        for j in range(n):
            # If the condition is violated, shrink the window from the left
            while nums[j] > k * nums[i]:
                i += 1
                
            # Maintain the maximum valid window length found so far
            max_len = max(max_len, j - i + 1)
            
        # The minimum removals is the remaining elements outside the largest window
        return n - max_len