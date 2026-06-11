# Last updated: 11/06/2026, 21:31:22
class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        i = 0
        subresults = []
        
        # Iterate through the string to break it into independent special substrings
        for j, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
                
            # When count hits 0, we found an independent special substring boundary s[i : j+1]
            if count == 0:
                # Inside a special string, it always starts with '1' and ends with '0'.
                # We recursively solve for the inner content: s[i+1 : j]
                inner_maximized = self.makeLargestSpecial(s[i + 1 : j])
                
                # Reconstruct this block as '1' + maximized_inner + '0'
                subresults.append("1" + inner_maximized + "0")
                
                # Move the pointer to the start of the next potential block
                i = j + 1
                
        # Sort the independent blocks in descending order to maximize lexicographical size
        subresults.sort(reverse=True)
        
        # Join and return the final string
        return "".join(subresults)