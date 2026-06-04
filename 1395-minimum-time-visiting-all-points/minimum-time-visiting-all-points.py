class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        # Traverse through the points two at a time
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            # The time taken is determined by the maximum delta between the coordinates
            total_time += max(abs(x2 - x1), abs(y2 - y1))
            
        return total_time