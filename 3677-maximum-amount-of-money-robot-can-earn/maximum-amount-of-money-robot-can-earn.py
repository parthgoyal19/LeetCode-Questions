class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m = len(coins)
        n = len(coins[0])
        
        # dp[i][j][k] represents the max coins at (i, j) with k neutralizations used
        # k can be 0, 1, or 2. Initialize with negative infinity.
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Base case: Starting at (0, 0)
        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
            # Neutralizing a positive cell gives no extra benefit, but technically valid
            dp[0][0][1] = coins[0][0]
            dp[0][0][2] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0]  # Take the penalty
            dp[0][0][1] = 0            # Neutralize the penalty once
            dp[0][0][2] = 0            # Neutralize (same as using 1, but placeholder for 2)

        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                for k in range(3):
                    max_prev = -float('inf')
                    
                    # Came from Top
                    if i > 0:
                        max_prev = max(max_prev, dp[i - 1][j][k])
                    # Came from Left
                    if j > 0:
                        max_prev = max(max_prev, dp[i][j - 1][k])
                    
                    # Option A: Accept the coin value normally (whether positive or negative)
                    if max_prev != -float('inf'):
                        dp[i][j][k] = max(dp[i][j][k], max_prev + coins[i][j])
                    
                    # Option B: If it's a robber, we can neutralize it by using a credit
                    if coins[i][j] < 0 and k > 0:
                        max_prev_neutralized = -float('inf')
                        if i > 0:
                            max_prev_neutralized = max(max_prev_neutralized, dp[i - 1][j][k - 1])
                        if j > 0:
                            max_prev_neutralized = max(max_prev_neutralized, dp[i][j - 1][k - 1])
                            
                        if max_prev_neutralized != -float('inf'):
                            dp[i][j][k] = max(dp[i][j][k], max_prev_neutralized) # +0 coins
                            
        # The answer is the maximum value reached at the bottom-right corner
        return max(dp[m - 1][n - 1])