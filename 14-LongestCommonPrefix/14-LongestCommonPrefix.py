# Last updated: 11/06/2026, 21:32:55
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Use the first string as a reference
        first_str = strs[0]
        
        for i in range(len(first_str)):
            char = first_str[i]
            
            # Check this character against all other strings
            for other_str in strs[1:]:
                # If we've reached the end of another string or find a mismatch
                if i == len(other_str) or other_str[i] != char:
                    return first_str[:i]
                    
        return first_str