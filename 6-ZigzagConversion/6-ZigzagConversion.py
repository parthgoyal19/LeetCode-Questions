# Last updated: 11/06/2026, 21:33:09
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if there's only 1 row, or the string is shorter than the rows,
        # the zigzag pattern doesn't change the string structure.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize an array of strings for each row
        rows = ["" for _ in range(numRows)]
        
        current_row = 0
        going_down = False
        
        # Traverse through each character in the string
        for char in s:
            rows[current_row] += char
            
            # Change direction if we hit the top or bottom boundary
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
                
            # Move up or down to the next row
            current_row += 1 if going_down else -1
            
        # Join all rows together to form the final string
        return "".join(rows)