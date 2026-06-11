# Last updated: 11/06/2026, 21:30:59
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        # Iterate through the points in the given order
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            # The time to move from points[i] to points[i+1]
            total_time += max(abs(x2 - x1), abs(y2 - y1))
            
        return total_time