class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if letters[mid] <= target:
                # Move right to find a strictly greater element
                low = mid + 1
            else:
                # Candidate found, but let's check if there is a smaller one to the left
                high = mid - 1
                
        # If low is out of bounds, it means no element is greater than target.
        # Using modulo wraps it back to index 0 safely.
        return letters[low % len(letters)]