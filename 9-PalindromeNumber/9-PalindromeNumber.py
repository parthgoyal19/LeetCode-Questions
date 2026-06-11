# Last updated: 11/06/2026, 21:33:03
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge cases: 
        # Negative numbers are not palindromes.
        # Numbers ending in 0 are not palindromes (except 0 itself).
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_num = 0
        # Loop until we reach the middle of the number
        while x > reversed_num:
            reversed_num = (reversed_num * 10) + (x % 10)
            x //= 10
            
        # For even-length numbers: x == reversed_num
        # For odd-length numbers: x == reversed_num // 10 (discards the middle digit)
        return x == reversed_num or x == reversed_num // 10