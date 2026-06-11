from collections import Counter

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Count frequencies for even positions
        even_s1 = Counter(s1[0::2])
        even_s2 = Counter(s2[0::2])
        
        # Count frequencies for odd positions
        odd_s1 = Counter(s1[1::2])
        odd_s2 = Counter(s2[1::2])
        
        # The strings can be made equal if both position groups have identical characters
        return even_s1 == even_s2 and odd_s1 == odd_s2