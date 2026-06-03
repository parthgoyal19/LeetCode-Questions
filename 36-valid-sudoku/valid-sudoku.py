class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize lists of sets for rows, columns, and 3x3 sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                
                # Skip empty cells
                if val == '.':
                    continue
                
                # Determine the index of the 3x3 sub-box
                box_idx = (i // 3) * 3 + (j // 3)
                
                # Check for duplicates in row, column, or sub-box
                if val in rows[i] or val in cols[j] or val in boxes[box_idx]:
                    return False
                
                # Add the current value to the respective sets
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_idx].add(val)
                
        return True