# Last updated: 11/06/2026, 21:29:51
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j][0] -> stable arrays with i zeros, j ones, ending in 0
        # dp[i][j][1] -> stable arrays with i zeros, j ones, ending in 1
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        # Base cases: arrays of purely 0s or purely 1s up to the limit
        for i in range(1, min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp[0][j][1] = 1
            
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Case 0: Appending a '0'
                # A '0' can follow any valid sequence ending in 0 or 1 from the previous step
                ways_zero = dp[i-1][j][0] + dp[i-1][j][1]
                if i - limit - 1 > 0:
                    # Subtract invalid sequences that exceed the consecutive '0' limit
                    ways_zero -= dp[i - limit - 1][j][1]
                elif i - limit - 1 == 0:
                    # If i equals limit + 1, there is exactly 1 sequence of all zeros 
                    # followed by j ones that becomes invalid here.
                    ways_zero -= 1 if j == 0 else dp[0][j][1]
                dp[i][j][0] = ways_zero % MOD
                
                # Case 1: Appending a '1'
                # A '1' can follow any valid sequence ending in 0 or 1 from the previous step
                ways_one = dp[i][j-1][0] + dp[i][j-1][1]
                if j - limit - 1 > 0:
                    # Subtract invalid sequences that exceed the consecutive '1' limit
                    ways_one -= dp[i][j - limit - 1][0]
                elif j - limit - 1 == 0:
                    # If j equals limit + 1, there is exactly 1 sequence of all ones
                    # preceded by i zeros that becomes invalid here.
                    ways_one -= 1 if i == 0 else dp[i][0][0]
                dp[i][j][1] = ways_one % MOD
                
        return (dp[zero][one][0] + dp[zero][one][1]) % MOD