# Last updated: 11/06/2026, 21:29:31
class Solution:
    def isTrionic(self, nums: list[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
            
        i = 0
        
        # 1. Walk up the first strictly increasing segment
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            
        # If we didn't even move, or we reached the end, it's invalid
        if i == 0 or i == n - 1:
            return False
            
        # 2. Walk down the strictly decreasing segment
        p = i
        while i + 1 < n and nums[i] > nums[i+1]:
            i += 1
            
        # If we didn't move past p, or we reached the end, it's invalid
        if i == p or i == n - 1:
            return False
            
        # 3. Walk up the final strictly increasing segment
        while i + 1 < n and nums[i] < nums[i+1]:
            i += 1
            
        # If we successfully verified the sequence up to the last element, return True
        return i == n - 1