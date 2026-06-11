# Last updated: 11/06/2026, 21:30:16
class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        unique_sums = set()
        
        for r in range(m):
            for c in range(n):
                # Case 1: Rhombus of area 0 (just a single cell)
                unique_sums.add(grid[r][c])
                
                # Case 2: Rhombus with radius q > 0
                # Find max possible radius q that stays inside the grid boundaries
                max_q = min(r, m - 1 - r, c, n - 1 - c)
                
                for q in range(1, max_q + 1):
                    current_sum = 0
                    
                    # Top corner to Right corner (moving down-right)
                    for i in range(q):
                        current_sum += grid[r - q + i][c + i]
                        
                    # Right corner to Bottom corner (moving down-left)
                    for i in range(q):
                        current_sum += grid[r + i][c + q - i]
                        
                    # Bottom corner to Left corner (moving up-left)
                    for i in range(q):
                        current_sum += grid[r + q - i][c - i]
                        
                    # Left corner to Top corner (moving up-right)
                    for i in range(q):
                        current_sum += grid[r - i][c - q + i]
                        
                    unique_sums.add(current_sum)
                    
        # Sort distinct sums in descending order and return the top 3
        return sorted(list(unique_sums), reverse=True)[:3]