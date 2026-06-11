# Last updated: 11/06/2026, 21:29:21
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # Outer loop sets the starting position of the substring
        for i in range(n):
            freq = {}
            
            # Inner loop expands the substring to the right
            for j in range(i, n):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1
                
                # Take the count of the first character as our target frequency
                target_count = next(iter(freq.values()))
                
                # Check if all other distinct characters match this target count
                is_balanced = all(count == target_count for count in freq.values())
                
                if is_balanced:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len