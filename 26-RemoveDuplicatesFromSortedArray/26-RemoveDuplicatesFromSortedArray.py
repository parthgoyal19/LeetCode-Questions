# Last updated: 11/06/2026, 21:32:29
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'insert_index' tracks where the next unique element should be placed
        insert_index = 1
        
        # Scan through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[insert_index] = nums[i]
                insert_index += 1
                
        # The value of insert_index is exactly the number of unique elements
        return insert_index