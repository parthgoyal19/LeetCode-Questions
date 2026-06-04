class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        # Helper function to find the maximum number of consecutive bars + 1
        def getMaxGap(bars: List[int]) -> int:
            bars.sort()
            max_consecutive = 1
            current_consecutive = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current_consecutive += 1
                else:
                    max_consecutive = max(max_consecutive, current_consecutive)
                    current_consecutive = 1
            
            # Account for the last tracking sequence
            max_consecutive = max(max_consecutive, current_consecutive)
            
            # Removing 'k' consecutive bars creates a continuous gap spanning 'k + 1' units
            return max_consecutive + 1

        # Find the max structural gap possible on both axes
        max_h_gap = getMaxGap(hBars)
        max_v_gap = getMaxGap(vBars)
        
        # The constraint of a square forces us to pick the bottleneck side length
        max_side = min(max_h_gap, max_v_gap)
        
        return max_side * max_side