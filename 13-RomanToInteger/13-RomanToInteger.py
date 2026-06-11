# Last updated: 11/06/2026, 21:32:56
class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping Roman numerals to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # If the current character's value is less than the next character's value
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                # Subtract its value
                total -= roman_map[s[i]]
            else:
                # Otherwise, add its value
                total += roman_map[s[i]]
                
        return total