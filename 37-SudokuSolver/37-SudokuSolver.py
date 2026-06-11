# Last updated: 11/06/2026, 21:31:59
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Initialize hash sets for tracking used digits
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # Step 1: Pre-populate sets with existing digits and record empty spaces
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    rows[i].add(val)
                    cols[j].add(val)
                    box_idx = (i // 3) * 3 + (j // 3)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((i, j))
                    
        # Step 2: Backtracking function to fill the cells
        def backtrack(cell_idx: int) -> bool:
            # Base case: if we filled all empty cells, the puzzle is solved
            if cell_idx == len(empty_cells):
                return True
                
            r, c = empty_cells[cell_idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try placing digits '1' through '9'
            for digit in map(str, range(1, 10)):
                # Check if the digit is valid in the current row, column, and box
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box_idx]:
                    # Make a choice
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)
                    
                    # Recursively try to solve the rest of the board
                    if backtrack(cell_idx + 1):
                        return True
                        
                    # Undo choice (Backtrack)
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)
                    
            return False

        # Start the backtracking process from the first empty cell
        backtrack(0)