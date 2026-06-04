class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        
        # Initialize a 2D DP matrix with negative infinity
        dp = [[float('-inf')] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                # Product of the current pair of elements
                current_product = nums1[i] * nums2[j]
                
                # Option 1 & 2: Take just the current product, or add it to the previous diagonal DP value
                dp[i][j] = current_product
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i][j], current_product + dp[i-1][j-1])
                
                # Option 3: Skip current element from nums1
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                    
                # Option 4: Skip current element from nums2
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                    
        return dp[m-1][n-1]