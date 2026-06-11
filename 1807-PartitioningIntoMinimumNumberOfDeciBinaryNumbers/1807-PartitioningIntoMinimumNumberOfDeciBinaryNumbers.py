# Last updated: 11/06/2026, 21:30:29
class Solution:
    def minPartitions(self, n: str) -> int:
        # The minimum number of deci-binary numbers needed is simply the maximum digit in n
        return int(max(n))