class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[u][i][j] stores the min cost to reach (i, j) with 'u' teleports
        dp = [[[float('inf')] * n for _ in range(m)] for _ in range(k + 1)]
        
        # Base case: Starting point at layer 0 (0 teleports used)
        dp[0][0][0] = 0 
        
        # Group cell coordinates by their grid values to optimize teleportations
        cells_by_val = {}
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if val not in cells_by_val:
                    cells_by_val[val] = []
                cells_by_val[val].append((r, c))
                
        # Sorted unique grid values in descending order
        sorted_vals = sorted(cells_by_val.keys(), reverse=True)
        
        # Process layer by layer (from 0 teleports up to k teleports)
        for u in range(k + 1):
            # Step 1: Compute grid path propagation (Normal Moves) for the current layer u
            for r in range(m):
                for c in range(n):
                    if r == 0 and c == 0:
                        continue
                    min_prev = float('inf')
                    if r > 0:
                        min_prev = min(min_prev, dp[u][r-1][c])
                    if c > 0:
                        min_prev = min(min_prev, dp[u][r][c-1])
                    
                    if min_prev != float('inf'):
                        dp[u][r][c] = min(dp[u][r][c], min_prev + grid[r][c])
            
            # Step 2: If we can still teleport, calculate transitions to the next layer (u + 1)
            if u < k:
                running_min_cost = float('inf')
                
                # Walk down from largest grid values to smallest grid values
                for val in sorted_vals:
                    # Collect the minimum path cost from layer u among all cells matching this 'val'
                    current_val_min = float('inf')
                    for r, c in cells_by_val[val]:
                        current_val_min = min(current_val_min, dp[u][r][c])
                        
                    # Update our running minimum; since we walk descending, 
                    # any cell with a smaller or equal 'val' can safely pull from this running_min_cost
                    running_min_cost = min(running_min_cost, current_val_min)
                    
                    # Update the next layer (u + 1) for all cells holding the current 'val'
                    if running_min_cost != float('inf'):
                        for r, c in cells_by_val[val]:
                            dp[u + 1][r][c] = min(dp[u + 1][r][c], running_min_cost)
                            
        # The answer is the minimum cost to reach the bottom-right cell across any layer
        ans = min(dp[u][m-1][n-1] for u in range(k + 1))
        return ans if ans != float('inf') else -1