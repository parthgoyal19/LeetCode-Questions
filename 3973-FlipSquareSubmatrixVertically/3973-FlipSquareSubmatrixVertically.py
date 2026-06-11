# Last updated: 11/06/2026, 21:29:24
class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        # Initialize two pointers for the top and bottom rows of the submatrix
        top = x
        bottom = x + k - 1
        
        # Swap rows inward until the pointers meet
        while top < bottom:
            for c in range(y, y + k):
                # Swap the elements in the current column
                grid[top][c], grid[bottom][c] = grid[bottom][c], grid[top][c]
            
            # Move the row pointers closer to the middle
            top += 1
            bottom -= 1
            
        return grid