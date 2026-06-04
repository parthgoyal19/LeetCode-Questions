class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        for x in range(num1, num2 + 1):
            s = str(x)
            n = len(s)
            
            # Any number with fewer than 3 digits has a waviness of 0
            if n < 3:
                continue
                
            # Check all middle digits (excluding the first and last)
            for i in range(1, n - 1):
                # Peak condition: strictly greater than both neighbors
                if s[i] > s[i - 1] and s[i] > s[i + 1]:
                    total_waviness += 1
                # Valley condition: strictly less than both neighbors
                elif s[i] < s[i - 1] and s[i] < s[i + 1]:
                    total_waviness += 1
                    
        return total_waviness