# Last updated: 11/06/2026, 21:30:13
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        # Double the string to simulate all possible cyclic shifts
        extended_s = s + s
        
        # Target alternating patterns
        pattern1 = []
        pattern2 = []
        for i in range(len(extended_s)):
            pattern1.append("0" if i % 2 == 0 else "1")
            pattern2.append("1" if i % 2 == 0 else "0")
            
        diff1 = 0
        diff2 = 0
        min_flips = float('inf')
        
        left = 0
        # Slide a window of size n over extended_s
        for right in range(len(extended_s)):
            if extended_s[right] != pattern1[right]:
                diff1 += 1
            if extended_s[right] != pattern2[right]:
                diff2 += 1
                
            # If window size exceeds n, remove the element sliding out from the left
            if (right - left + 1) > n:
                if extended_s[left] != pattern1[left]:
                    diff1 -= 1
                if extended_s[left] != pattern2[left]:
                    diff2 -= 1
                left += 1
                
            # Once the window reaches exactly size n, track the minimum flips
            if (right - left + 1) == n:
                min_flips = min(min_flips, diff1, diff2)
                
        return min_flips