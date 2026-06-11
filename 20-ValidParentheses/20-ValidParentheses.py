# Last updated: 11/06/2026, 21:32:43
class Solution:
    def isValid(self, s: str) -> bool:
        # Map containing closing brackets as keys and opening brackets as values
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack is not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the popped element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched correctly
        return len(stack) == 0