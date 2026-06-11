# Last updated: 11/06/2026, 21:31:38
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        cols = len(matrix[0])
        heights = [0] * (cols + 1) # Extra 0 at the end to flush out remaining elements in the stack
        max_area = 0
        
        for row in matrix:
            # Step 1: Update the heights histogram for the current row base
            for col in range(cols):
                if row[col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
                    
            # Step 2: Find the largest rectangle in the current histogram using a monotonic stack
            stack = []
            for i in range(len(heights)):
                # While the current bar is shorter than the bar at the top of the stack
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    # Calculate width: if stack is empty, it means 'h' was the shortest bar seen so far
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area