class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # Group even indices (0, 2) and odd indices (1, 3) for both strings
        even_s1 = sorted([s1[0], s1[2]])
        even_s2 = sorted([s2[0], s2[2]])
        
        odd_s1 = sorted([s1[1], s1[3]])
        odd_s2 = sorted([s2[1], s2[3]])
        
        # If both individual groups match, s1 can be transformed into s2
        return even_s1 == even_s2 and odd_s1 == odd_s2