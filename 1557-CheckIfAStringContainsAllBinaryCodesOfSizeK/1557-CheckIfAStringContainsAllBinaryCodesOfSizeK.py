# Last updated: 11/06/2026, 21:30:43
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Total distinct binary codes of length k
        total_required_codes = 1 << k  # This is equivalent to 2^k
        
        # Early exit optimization: if the string doesn't have enough characters
        # to produce 2^k unique substrings, it's impossible.
        if len(s) - k + 1 < total_required_codes:
            return False
            
        seen_codes = set()
        
        # Slide a window of size k across the string
        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            seen_codes.add(substring)
            
            # Optimization: stop early if we've already found all combinations
            if len(seen_codes) == total_required_codes:
                return True
                
        return len(seen_codes) == total_required_codes