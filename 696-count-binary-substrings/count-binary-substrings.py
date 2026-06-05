class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total_substrings = 0
        prev_run_length = 0
        current_run_length = 1
        
        # Traverse the string starting from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # If the character matches the previous one, extend the current run
                current_run_length += 1
            else:
                # Character flipped! Add the valid combinations formed by the last two groups
                total_substrings += min(prev_run_length, current_run_length)
                # The current run now becomes the previous run
                prev_run_length = current_run_length
                # Reset current run for the new character group
                current_run_length = 1
                
        # Don't forget to add the combinations for the final pair of groups at the end of the loop
        total_substrings += min(prev_run_length, current_run_length)
        
        return total_substrings