# Last updated: 11/06/2026, 21:30:33
class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        b_count = 0
        
        for char in s:
            if char == 'b':
                b_count += 1
            else:  # char == 'a'
                # If we've seen 'b's before, we have a violation
                if b_count > 0:
                    # We can either delete this 'a' (deletions + 1) 
                    # or delete all 'b's seen so far (b_count)
                    deletions = min(deletions + 1, b_count)
                    
        return deletions