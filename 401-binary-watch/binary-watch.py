class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []
        
        # Iterate through all possible hours (0 to 11)
        for h in range(12):
            # Iterate through all possible minutes (0 to 59)
            for m in range(60):
                # Count the total number of set bits (LEDs turned on) for both hour and minute
                if h.bit_count() + m.bit_count() == turnedOn:
                    # Format the time representation matching constraints
                    result.append(f"{h}:{m:02d}")
                    
        return result