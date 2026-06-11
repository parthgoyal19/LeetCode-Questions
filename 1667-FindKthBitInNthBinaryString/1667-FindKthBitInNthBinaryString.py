# Last updated: 11/06/2026, 21:30:38
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: S_1 is always "0"
        if n == 1:
            return "0"
        
        # Calculate the length of S_n, which is 2^n - 1
        length = (1 << n) - 1
        mid = (length // 2) + 1
        
        if k == mid:
            # The middle bit is always "1"
            return "1"
        elif k < mid:
            # Element is in the left part (exactly matches S_{n-1})
            return self.findKthBit(n - 1, k)
        else:
            # Element is in the right part (reversed and inverted version of S_{n-1})
            # Find the mirrored index position in S_{n-1}
            mirrored_k = length - k + 1
            corresponding_bit = self.findKthBit(n - 1, mirrored_k)
            # Invert the bit
            return "1" if corresponding_bit == "0" else "0"