# Last updated: 11/06/2026, 21:32:24
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define 32-bit signed integer boundaries
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle the overflow edge case explicitly
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
            
        # Determine the sign of the final quotient
        # If both numbers have the same sign, result is positive; otherwise negative
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values to simplify the logic
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        # Shift the divisor to the left as much as possible while it's <= dividend
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            
            # Keep doubling the divisor using bitwise left shift (<< 1)
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            # Subtract the largest found chunk from the dividend
            abs_dividend -= temp_divisor
            # Add the matching multiple to our quotient
            quotient += multiple
            
        # Apply the correct sign to the result
        if is_negative:
            quotient = -quotient
            
        # Ensure the final answer stays within the 32-bit integer range
        return max(INT_MIN, min(INT_MAX, quotient))