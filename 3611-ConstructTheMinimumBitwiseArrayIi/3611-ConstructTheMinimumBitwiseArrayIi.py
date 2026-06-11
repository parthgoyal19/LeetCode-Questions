# Last updated: 11/06/2026, 21:29:45
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
            else:
                # Find the rightmost bit that is 1 followed by a 0 (or end of number)
                # This corresponds to the most significant bit of the trailing continuous 1s.
                for i in range(31):
                    if (num >> i) & 1 == 1 and (num >> (i + 1)) & 1 == 0:
                        # Turn off this i-th bit to get the minimized ans[i]
                        ans.append(num ^ (1 << i))
                        break
        return ans