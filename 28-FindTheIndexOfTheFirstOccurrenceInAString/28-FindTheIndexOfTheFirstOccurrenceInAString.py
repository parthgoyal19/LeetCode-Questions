# Last updated: 11/06/2026, 21:32:26
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is empty, it's always found at index 0
        if not needle:
            return 0
        
        h_len, n_len = len(haystack), len(needle)
        
        # Only iterate up to the point where the remaining characters 
        # are at least as long as the needle
        for i in range(h_len - n_len + 1):
            # Check if the slice matches the needle
            if haystack[i:i + n_len] == needle:
                return i
                
        return -1