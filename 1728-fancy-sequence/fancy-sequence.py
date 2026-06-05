class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.seq = []
        self.m = 1  # Global multiplier
        self.c = 0  # Global increment

    def append(self, val: int) -> None:
        # Reverse the current transformation to get the "raw" baseline value
        # stored_val = (val - c) / m
        inverse_m = pow(self.m, self.MOD - 2, self.MOD)
        raw_val = ((val - self.c) * inverse_m) % self.MOD
        self.seq.append(raw_val)

    def addAll(self, inc: int) -> None:
        # y = m * x + (c + inc)
        self.c = (self.c + inc) % self.MOD

    def multAll(self, m: int) -> None:
        # y = (m * old_m) * x + (m * old_c)
        self.m = (self.m * m) % self.MOD
        self.c = (self.c * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        # Apply the current global transformation to the baseline value
        return (self.seq[idx] * self.m + self.c) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)