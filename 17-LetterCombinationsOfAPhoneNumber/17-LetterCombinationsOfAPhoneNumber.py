# Last updated: 11/06/2026, 21:32:48
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If the input is empty, return an empty array
        if not digits:
            return []
            
        # Keypad mapping mapping digits to letters
        phone_map = {
            "2": "abc", "3": "def",  "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def backtrack(index: int, current_path: str):
            # If the path length matches digits length, we found a complete combination
            if len(current_path) == len(digits):
                res.append(current_path)
                return
            
            # Get the letters corresponding to the current digit
            possible_letters = phone_map[digits[index]]
            
            # Explore each letter choice recursively
            for letter in possible_letters:
                backtrack(index + 1, current_path + letter)
                
        # Start the backtracking process from index 0 with an empty combination path
        backtrack(0, "")
        return res