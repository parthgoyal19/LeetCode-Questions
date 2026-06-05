class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        # Pointers starting at the rightmost (least significant) digits
        i = len(a) - 1
        j = len(b) - 1
        
        # Loop as long as there are digits to add or a carry to process
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The digit to append is total modulo 2 (remainder)
            result.append(str(total % 2))
            
            # The next carry is total divided by 2 (integer division)
            carry = total // 2
            
        # Reverse the list because we added digits from right to left
        return "".join(reversed(result))