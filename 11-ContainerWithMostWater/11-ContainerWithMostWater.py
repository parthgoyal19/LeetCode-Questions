# Last updated: 11/06/2026, 21:33:00
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the width between the two lines
            width = right - left
            
            # Find the limiting height of the container
            current_height = min(height[left], height[right])
            
            # Calculate current water capacity and update max_water if it's larger
            current_water = current_height * width
            max_water = max(max_water, current_water)
            
            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water