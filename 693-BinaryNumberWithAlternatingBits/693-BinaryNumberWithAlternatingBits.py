# Last updated: 11/06/2026, 21:31:28
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # If bits alternate, x will be all 1s (e.g., 101 ^ 010 = 111)
        x = n ^ (n >> 1)
        
        # Check if x + 1 clears all bits when ANDed with x (e.g., 111 & 1000 == 0)
        return (x & (x + 1)) == 0