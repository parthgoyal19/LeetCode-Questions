class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Traverse the string from the rightmost bit up to the second bit (index 1)
        for i in range(len(s) - 1, 0, -1):
            # Calculate the current bit value including any incoming carry
            current_val = int(s[i]) + carry
            
            if current_val == 1:
                # Odd number: requires 2 steps (add 1, then divide by 2)
                steps += 2
                carry = 1
            else:
                # Even number (either 0 + 0 or 1 + 1): requires 1 step (divide by 2)
                steps += 1
                # If current_val was 2, carry remains 1. If it was 0, carry remains 0.
                
        # Process the final most significant bit at index 0
        # s[0] is guaranteed to be '1'. If there's a carry, it's 1 + 1 = 2, needing 1 more divide step.
        return steps + carry