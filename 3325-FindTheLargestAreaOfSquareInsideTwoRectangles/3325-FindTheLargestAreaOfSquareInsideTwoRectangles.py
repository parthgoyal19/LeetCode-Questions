# Last updated: 11/06/2026, 21:29:54
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        max_side = 0
        
        # Iterate through every unique pair of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the boundaries of the intersection rectangle
                inter_bl_x = max(bottomLeft[i][0], bottomLeft[j][0])
                inter_bl_y = max(bottomLeft[i][1], bottomLeft[j][1])
                inter_tr_x = min(topRight[i][0], topRight[j][0])
                inter_tr_y = min(topRight[i][1], topRight[j][1])
                
                # Check if there is a valid overlapping region
                if inter_tr_x > inter_bl_x and inter_tr_y > inter_bl_y:
                    width = inter_tr_x - inter_bl_x
                    height = inter_tr_y - inter_bl_y
                    
                    # The maximum square inside a rectangle is bounded by its shortest dimension
                    current_side = min(width, height)
                    if current_side > max_side:
                        max_side = current_side
                        
        return max_side * max_side