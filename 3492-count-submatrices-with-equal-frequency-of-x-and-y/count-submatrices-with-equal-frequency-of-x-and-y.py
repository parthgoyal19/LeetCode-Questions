class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        
        # 2D arrays initialized with an extra row and column to safely handle bounds (i-1, j-1)
        prefix_diff = [[0] * (n + 1) for _ in range(m + 1)]
        prefix_x = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                # Map characters to numeric values for delta differences
                val = 0
                if grid[i][j] == 'X':
                    val = 1
                elif grid[i][j] == 'Y':
                    val = -1
                
                # Check if current cell contains an 'X'
                has_x = 1 if grid[i][j] == 'X' else 0
                
                # Calculate the X-Y balance for the submatrix ending at (i, j)
                prefix_diff[i + 1][j + 1] = (val 
                                             + prefix_diff[i][j + 1] 
                                             + prefix_diff[i + 1][j] 
                                             - prefix_diff[i][j])
                
                # Calculate the total 'X' count for the submatrix ending at (i, j)
                prefix_x[i + 1][j + 1] = (has_x 
                                          + prefix_x[i][j + 1] 
                                          + prefix_x[i + 1][j] 
                                          - prefix_x[i][j])
                
                # Condition: Equal counts (diff == 0) and at least one 'X' (count_x > 0)
                if prefix_diff[i + 1][j + 1] == 0 and prefix_x[i + 1][j + 1] > 0:
                    ans += 1
                    
        return ans