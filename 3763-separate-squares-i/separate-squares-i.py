class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Step 1: Calculate total area and determine the bounding box limits
        total_area = 0.0
        low = float('inf')
        high = float('-inf')
        
        for x, y, l in squares:
            total_area += l * l
            if y < low:
                low = y
            if y + l > high:
                high = y + l
                
        half_area = total_area / 2.0
        
        # Step 2: Binary search for the optimal y-coordinate line
        # Running for 80 iterations gives us sub-atomic level floating-point precision
        for _ in range(80):
            mid = (low + high) / 2.0
            
            # Calculate the total area below the current line 'mid'
            area_below = 0.0
            for x, y, l in squares:
                if y + l <= mid:
                    area_below += l * l
                elif y >= mid:
                    continue
                else:
                    # The line intersects the current square
                    area_below += (mid - y) * l
            
            # Step 3: Shift boundaries based on the area split
            if area_below < half_area:
                low = mid
            else:
                high = mid
                
        return low