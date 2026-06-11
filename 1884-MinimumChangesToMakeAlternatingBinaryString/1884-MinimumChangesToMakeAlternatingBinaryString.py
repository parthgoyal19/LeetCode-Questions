# Last updated: 11/06/2026, 21:30:19
class Solution:
    def minOperations(self, s: str) -> int:
        changes_for_0 = 0
        
        # Count operations needed to make the string match the pattern "010101..."
        for i, char in enumerate(s):
            # For "0101...", even indices should be '0', odd indices should be '1'
            expected_char = str(i % 2)
            if char != expected_char:
                changes_for_0 += 1
                
        # The operations needed for the alternative pattern "101010..." 
        # is just the total length minus the changes needed for the first pattern.
        changes_for_1 = len(s) - changes_for_0
        
        return min(changes_for_0, changes_for_1)