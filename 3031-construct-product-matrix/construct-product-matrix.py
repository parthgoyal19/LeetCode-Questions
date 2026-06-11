class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        
        # Initialize the product matrix with 1s
        p = [[1] * m for _ in range(n)]
        
        # Step 1: Forward pass (Prefix Product)
        running_prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = running_prefix
                running_prefix = (running_prefix * grid[i][j]) % MOD
                
        # Step 2: Backward pass (Suffix Product)
        running_suffix = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * running_suffix) % MOD
                running_suffix = (running_suffix * grid[i][j]) % MOD
                
        return p