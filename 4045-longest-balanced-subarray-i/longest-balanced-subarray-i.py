class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = 0
        
        # Check every possible starting position of the subarray
        for i in range(n):
            evens = set()
            odds = set()
            
            # Expand the subarray to the right
            for j in range(i, n):
                val = nums[j]
                
                if val % 2 == 0:
                    evens.add(val)
                else:
                    odds.add(val)
                
                # If the number of unique evens equals unique odds, it's balanced
                if len(evens) == len(odds):
                    max_len = max(max_len, j - i + 1)
                    
        return max_len