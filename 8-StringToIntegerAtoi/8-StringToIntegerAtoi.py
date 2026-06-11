# Last updated: 11/06/2026, 21:33:04
class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed integer bounds
        INT_MIN, INT_MAX = -2147483648, 2147483647
        
        n = len(s)
        i = 0
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        # Step 2: Handle sign selection
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
            
        # Step 3: Convert valid numeric digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Handle potential 32-bit integer overflow before updating
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
                
            result = (result * 10) + digit
            i += 1
            
        return sign * result