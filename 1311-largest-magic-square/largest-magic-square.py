class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Row prefix sums: row_sums[i][j+1] = sum of grid[i][0...j]
        row_sums = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row_sums[i][j+1] = row_sums[i][j] + grid[i][j]
                
        # Column prefix sums: col_sums[i+1][j] = sum of grid[0...i][j]
        col_sums = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                col_sums[i+1][j] = col_sums[i][j] + grid[i][j]
                
        def is_magic(r: int, c: int, k: int) -> bool:
            # Determine the baseline target sum using the first row of this subgrid
            target = row_sums[r][c + k] - row_sums[r][c]
            
            # 1. Check all row sums inside the k x k subgrid
            for i in range(r + 1, r + k):
                if row_sums[i][c + k] - row_sums[i][c] != target:
                    return False
                    
            # 2. Check all column sums inside the k x k subgrid
            for j in range(c, c + k):
                if col_sums[r + k][j] - col_sums[r][j] != target:
                    return False
                    
            # 3. Check the main diagonal (top-left to bottom-right)
            diag1 = 0
            for d in range(k):
                diag1 += grid[r + d][c + d]
            if diag1 != target:
                return False
                
            # 4. Check the anti-diagonal (top-right to bottom-left)
            diag2 = 0
            for d in range(k):
                diag2 += grid[r + d][c + k - 1 - d]
            if diag2 != target:
                return False
                
            return True

        # Search from largest possible side length down to 2
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
                        
        return 1