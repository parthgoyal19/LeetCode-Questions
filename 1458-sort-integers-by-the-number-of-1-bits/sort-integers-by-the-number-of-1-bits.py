class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        # Sort using a tuple key: (number of 1 bits, the value itself)
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr