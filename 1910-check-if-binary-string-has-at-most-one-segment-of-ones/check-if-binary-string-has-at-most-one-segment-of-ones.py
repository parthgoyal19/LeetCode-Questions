class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # Since s[0] is always '1', any additional segment of '1's 
        # would require a '0' followed by a '1' somewhere in the string.
        return "01" not in s