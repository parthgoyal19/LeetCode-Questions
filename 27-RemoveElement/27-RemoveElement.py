# Last updated: 11/06/2026, 21:32:27
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 'k' tracks the position for elements that are NOT equal to 'val'
        k = 0
        
        for i in range(len(nums)):
            # If the current element is not the target value to remove
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        # k represents the total count of elements remaining
        return k