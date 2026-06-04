class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        star_idx = -1
        s_tmp_idx = -1
        
        while s_ptr < len(s):
            # Case 1: Characters match or pattern has '?'
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            
            # Case 2: Pattern has '*'
            elif p_ptr < len(p) and p[p_ptr] == '*':
                # Track the position of the star and current string index
                star_idx = p_ptr
                s_tmp_idx = s_ptr
                # Move pattern pointer forward, assuming '*' matches 0 characters initially
                p_ptr += 1
                
            # Case 3: Current match failed, but we can backtrack to a previous '*'
            elif star_idx != -1:
                # Move pattern pointer back to just after the star
                p_ptr = star_idx + 1
                # Consume one more character from string for the star match
                s_tmp_idx += 1
                s_ptr = s_tmp_idx
                
            # Case 4: Mismatch and no star to fall back on
            else:
                return False
                
        # Consume any remaining trailing stars in the pattern
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        # If the entire pattern was consumed, it's a valid match
        return p_ptr == len(p)