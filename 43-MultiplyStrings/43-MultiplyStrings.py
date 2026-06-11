# Last updated: 11/06/2026, 21:31:47
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
            
        len1, len2 = len(num1), len(num2)
        # Array to store the intermediate addition results
        result = [0] * (len1 + len2)
        
        # Multiply from right to left
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                # Convert characters to integer values using ASCII arithmetic
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # The product of current digits
                mul = digit1 * digit2
                
                # Sum of the current product and any previous carry/value at this position
                p1 = i + j
                p2 = i + j + 1
                total_sum = mul + result[p2]
                
                # Update positions
                result[p2] = total_sum % 10     # Single digit remainder goes to the right position
                result[p1] += total_sum // 10    # Carry over goes to the left position
                
        # Convert the integer array back to a string array
        # Skipping any leading zero that might remain at index 0
        start_idx = 1 if result[0] == 0 else 0
        return "".join(map(str, result[start_idx:]))