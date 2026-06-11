# Last updated: 11/06/2026, 21:33:10
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            # Expand outwards as long as boundaries are valid and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length palindrome (centered at i)
            len1 = expand_around_center(i, i)
            # Case 2: Even length palindrome (centered between i and i+1)
            len2 = expand_around_center(i, i + 1)
            
            # Get the maximum length found at this center
            max_len = max(len1, len2)
            
            # If it's longer than our previous maximum, update the boundaries
            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]