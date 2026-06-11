# Last updated: 11/06/2026, 21:30:57
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        # Step 1: Build the 2D Prefix Sum matrix
        # Dimensions are (m + 1) x (n + 1) to seamlessly handle boundary conditions
        pref = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pref[i][j] = (mat[i-1][j-1] 
                              + pref[i-1][j] 
                              + pref[i][j-1] 
                              - pref[i-1][j-1])
        
        max_side = 0
        
        # Step 2: Iterate through every cell treating it as the bottom-right corner
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # We only check if we can expand our current maximum side length by 1
                k = max_side + 1
                
                # Ensure the top-left boundary of this square size stays within matrix limits
                if i - k >= 0 and j - k >= 0:
                    # Calculate the sum of the k x k square subgrid in O(1) time
                    current_sum = (pref[i][j] 
                                   - pref[i-k][j] 
                                   - pref[i][j-k] 
                                   + pref[i-k][j-k])
                    
                    # If the sum is valid, grow our max_side permanently
                    if current_sum <= threshold:
                        max_side = k
                        
        return max_side