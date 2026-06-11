# Last updated: 11/06/2026, 21:31:09
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        ans = 0
        factor = 1
        
        while n > 0:
            # Extract the last bit, flip it (1 - bit)
            bit = n & 1
            flipped_bit = 1 - bit
            
            # Place the flipped bit in its correct position
            ans += flipped_bit * factor
            
            # Move to the next bit
            factor <<= 1
            n >>= 1
            
        return ans