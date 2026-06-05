class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        result = []
        
        # Iterate through each string's corresponding diagonal element
        for i in range(len(nums)):
            # Invert the character at the diagonal position
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')
                
        return "".join(result)