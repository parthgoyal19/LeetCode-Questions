# Last updated: 11/06/2026, 21:30:07
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []
        
        # Single pass to separate elements while preserving relative order
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
                
        # Concatenate the lists together
        return less + equal + greater