class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        max_area = 0
        
        for i in range(m):
            for j in range(n):
                # If current cell is 1, accumulate the height from the row above
                if matrix[i][j] == 1 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
            
            # Create a sorted copy of the current row's consecutive heights in descending order
            current_row_heights = sorted(matrix[i], reverse=True)
            
            # Calculate the max submatrix area possible ending at row i
            for k in range(n):
                height = current_row_heights[k]
                width = k + 1
                area = height * width
                max_area = max(max_area, area)
                
        return max_area