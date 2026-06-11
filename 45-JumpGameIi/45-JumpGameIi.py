# Last updated: 11/06/2026, 21:31:42
class Solution:
    def jump(self, nums: List[int]) -> int:
        # If the array has only 1 element, we are already at the destination
        if len(nums) <= 1:
            return 0
            
        jumps = 0
        current_end = 0
        farthest = 0
        
        # Iterate up to the second-to-last element
        for i in range(len(nums) - 1):
            # Update the farthest position we can reach from the current index
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the end of the current jump's reach
            if i == current_end:
                jumps += 1            # We must make a jump
                current_end = farthest # Update the boundary for the next jump layer
                
                # Early exit optimization: if we can already reach the end, stop iterating
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps