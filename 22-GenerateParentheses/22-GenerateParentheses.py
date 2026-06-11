# Last updated: 11/06/2026, 21:32:35
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: if the string is complete
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Decision 1: We can add an opening parenthesis if we haven't used all 'n' of them
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # Decision 2: We can add a closing parenthesis if it won't violate well-formed rules
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
                
        # Start the recursion with an empty string and 0 counts
        backtrack("", 0, 0)
        return result