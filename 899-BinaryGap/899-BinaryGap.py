# Last updated: 11/06/2026, 21:31:11
class Solution:
    def binaryGap(self, n: int) -> int:
        max_gap = 0
        last_position = -1
        current_position = 0
        
        while n > 0:
            # Check if the rightmost bit is 1
            if n & 1:
                if last_position != -1:
                    # Calculate the distance to the previous 1
                    max_gap = max(max_gap, current_position - last_position)
                # Update the last seen position of a 1 bit
                last_position = current_position
                
            # Move to the next bit and increment the position counter
            n >>= 1
            current_position += 1
            
        return max_gap