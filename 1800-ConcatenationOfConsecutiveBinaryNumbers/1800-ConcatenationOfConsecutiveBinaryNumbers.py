# Last updated: 11/06/2026, 21:30:31
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        bit_length = 0
        
        for i in range(1, n + 1):
            # If i is a power of 2, its binary representation requires 1 more bit
            # (e.g., 1 -> '1', 2 -> '10', 4 -> '100', 8 -> '1000')
            if i & (i - 1) == 0:
                bit_length += 1
                
            # Shift the existing result to the left by bit_length and add i
            result = ((result << bit_length) + i) % MOD
            
        return result