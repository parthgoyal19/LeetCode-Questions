class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current = "1"
        
        # Build the sequence iteratively up to n
        for _ in range(1, n):
            next_string = []
            prev_char = current[0]
            count = 1
            
            # Scan through the string to perform run-length encoding
            for char in current[1:]:
                if char == prev_char:
                    count += 1
                else:
                    next_string.append(str(count))
                    next_string.append(prev_char)
                    prev_char = char
                    count = 1
            
            # Catch the final sequence group
            next_string.append(str(count))
            next_string.append(prev_char)
            
            # Update current to be the newly generated string
            current = "".join(next_string)
            
        return current