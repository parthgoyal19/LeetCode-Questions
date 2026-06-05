class Solution:
    def countSubmatrices(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        # Initialize a 2D DP/Prefix Sum table with an extra row and column of zeros
        # to handle out-of-bound edge cases cleanly.
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                # Calculate the prefix sum for the submatrix from (0,0) to (i,j)
                # We shift indices by +1 when reading from the prefix table
                current_sum = (grid[i][j] 
                               + prefix[i][j + 1] 
                               + prefix[i + 1][j] 
                               - prefix[i][j])
                
                # Save the computed sum into our prefix table
                prefix[i + 1][j + 1] = current_sum
                
                # If the sum satisfies the condition, it's a valid submatrix
                if current_sum <= k:
                    count += 1
                else:
                    # Optimization: Since elements are non-negative (grid[i][j] >= 0),
                    # if the row prefix sum exceeds k, expanding further right in this row 
                    # will only increase the sum. We can safely break the inner loop early.
                    break
                    
        return count