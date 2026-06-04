class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                # Find the first '0' bit from the right, and flip the '1' to its right to '0'
                # Example: 11 (1011) -> flip the second bit from right -> 9 (1001)
                t = num
                i = 0
                while (t & 1) == 1:
                    t >>= 1
                    i += 1
                # Flip the i-1-th bit from 1 to 0
                ans.append(num ^ (1 << (i - 1)))
        return ans