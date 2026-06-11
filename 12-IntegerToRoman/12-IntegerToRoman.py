# Last updated: 11/06/2026, 21:32:58
class Solution:
    def intToRoman(self, num: int) -> str:
        # List of tuples containing the integer values and their Roman numeral equivalents
        # sorted in descending order.
        roman_mapping = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
            (1, "I")
        ]
        
        result = []
        
        # Loop through each value-symbol pair
        for value, symbol in roman_mapping:
            # If num is 0, we can break early
            if num == 0:
                break
                
            # Determine how many times the current symbol fits into num
            count = num // value
            if count > 0:
                # Append the symbol 'count' times
                result.append(symbol * count)
                # Reduce num by the total value accounted for
                num %= value
                
        return "".join(result)