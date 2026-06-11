# Last updated: 11/06/2026, 21:33:07
class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        # Keep track of the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x != 0:
            # Pop the last digit
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying by 10
            if reversed_num > INT_MAX // 10:
                return 0
            if reversed_num == INT_MAX // 10 and digit > INT_MAX % 10:
                return 0
                
            # Push digit to the reversed number
            reversed_num = (reversed_num * 10) + digit
            
        # Reapply the sign
        actual_result = sign * reversed_num
        
        # Final boundary sanity check
        if actual_result < INT_MIN or actual_result > INT_MAX:
            return 0
            
        return actual_result