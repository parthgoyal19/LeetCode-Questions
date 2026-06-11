# Last updated: 11/06/2026, 21:31:19
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Start with the top row containing just the initial poured amount
        current_row = [poured]
        
        # Simulate row by row down to the requested query_row
        for row in range(query_row):
            # The next row will have one more glass than the current row
            next_row = [0.0] * (len(current_row) + 1)
            
            for glass in range(len(current_row)):
                # Calculate how much excess champagne overflows from the current glass
                overflow = (current_row[glass] - 1.0) / 2.0
                
                # If there is overflow, distribute it to the two glasses directly underneath
                if overflow > 0:
                    next_row[glass] += overflow
                    next_row[glass + 1] += overflow
            
            # Move to the next row
            current_row = next_row
            
        # The queried glass might have received more than 1 cup passing through it during simulation,
        # but it can only hold a maximum of 1 cup.
        return min(1.0, current_row[query_glass])