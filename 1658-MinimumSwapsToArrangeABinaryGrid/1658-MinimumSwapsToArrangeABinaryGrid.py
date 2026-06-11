# Last updated: 11/06/2026, 21:30:39
class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n = len(grid)
        trailing_zeros = []
        
        # Step 1: Count trailing zeros for each row
        for row in grid:
            zeros = 0
            for val in reversed(row):
                if val == 0:
                    zeros += 1
                else:
                    break
            trailing_zeros.append(zeros)
            
        total_swaps = 0
        
        # Step 2: Satisfy the requirement for each row position i
        for i in range(n):
            required_zeros = n - 1 - i
            
            # Search for the first available row that satisfies the condition
            found_idx = -1
            for j in range(i, n):
                if trailing_zeros[j] >= required_zeros:
                    found_idx = j
                    break
            
            # If no valid row is found, it's impossible to satisfy the condition
            if found_idx == -1:
                return -1
                
            # Accumulate the adjacent swaps needed to bring row found_idx to position i
            total_swaps += (found_idx - i)
            
            # Simulate the row movement by shifting elements in our tracking array
            # This extracts the row at found_idx and inserts it at position i
            row_to_move = trailing_zeros.pop(found_idx)
            trailing_zeros.insert(i, row_to_move)
            
        return total_swaps