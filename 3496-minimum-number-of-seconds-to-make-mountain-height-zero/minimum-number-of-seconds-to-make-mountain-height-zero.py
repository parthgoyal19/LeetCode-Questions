import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        
        def can_reduce_in_time(max_time: int) -> bool:
            total_height_reduced = 0
            for w in workerTimes:
                # Using the rearranged quadratic formula: x^2 + x - (2 * max_time / w) <= 0
                # Solving for x: x = (-1 + sqrt(1 + 8 * max_time / w)) / 2
                val = (2 * max_time) // w
                if val == 0:
                    continue
                
                # Calculate max integer x units this worker can reduce
                x = int((-1 + math.isqrt(1 + 4 * val)) // 2)
                total_height_reduced += x
                
                # Optimization: If we already meet or exceed the target height, stop early
                if total_height_reduced >= mountainHeight:
                    return True
                    
            return total_height_reduced >= mountainHeight

        # Define binary search boundaries
        low = 1
        # Worst case: 1 worker with max time reducing max mountain height
        high = max(workerTimes) * (mountainHeight * (mountainHeight + 1)) // 2
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_reduce_in_time(mid):
                ans = mid        # mid is a valid time, try to find a smaller minimum
                high = mid - 1
            else:
                low = mid + 1    # Not enough time, increase the limit
                
        return ans