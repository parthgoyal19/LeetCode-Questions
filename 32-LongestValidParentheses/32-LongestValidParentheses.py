# Last updated: 11/06/2026, 21:32:13
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        # Initialize stack with -1 to serve as a base boundary
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the opening parenthesis
                stack.append(i)
            else:
                # Pop the last opening parenthesis or boundary
                stack.pop()
                
                if not stack:
                    # If stack is empty, this ')' is unmatched.
                    # Push its index as the new base boundary.
                    stack.append(i)
                else:
                    # If stack is not empty, calculate the length of the valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len