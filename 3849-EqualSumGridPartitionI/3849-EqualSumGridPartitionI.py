# Last updated: 11/06/2026, 21:29:38
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        # Calculate the total sum of all elements in the grid
        total_sum = sum(sum(row) for row in grid)
        
        # If the total sum is odd, it cannot be split into two equal integer halves
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2
        
        # Check for a valid Horizontal Cut
        # We stop at m - 1 because both resulting sections must be non-empty
        running_row_sum = 0
        for i in range(m - 1):
            running_row_sum += sum(grid[i])
            if running_row_sum == target_sum:
                return True
                
        # Check for a valid Vertical Cut
        # We stop at n - 1 because both resulting sections must be non-empty
        running_col_sum = 0
        for j in range(n - 1):
            # Add the sum of the current column j across all rows
            running_col_sum += sum(grid[i][j] for i in range(m))
            if running_col_sum == target_sum:
                return True
                
        return False