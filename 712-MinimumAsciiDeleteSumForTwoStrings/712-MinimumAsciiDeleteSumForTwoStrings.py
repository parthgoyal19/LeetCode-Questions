# Last updated: 11/06/2026, 21:31:25
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        # Initialize a 2D DP table with dimensions (m + 1) x (n + 1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: if s2 is empty, we must delete all characters from s1
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
            
        # Base case: if s1 is empty, we must delete all characters from s2
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
            
        # Fill the DP grid row by row
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    # Characters match, no deletion cost added
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Characters mismatch, pick the minimum cost between:
                    # 1. Deleting s1[i-1]
                    # 2. Deleting s2[j-1]
                    dp[i][j] = min(
                        dp[i-1][j] + ord(s1[i-1]),
                        dp[i][j-1] + ord(s2[j-1])
                    )
                    
        return dp[m][n]