# Last updated: 11/06/2026, 21:31:50
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                # Water level is limited by the left maximum
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                # Water level is limited by the right maximum
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1
                
        return water_trapped