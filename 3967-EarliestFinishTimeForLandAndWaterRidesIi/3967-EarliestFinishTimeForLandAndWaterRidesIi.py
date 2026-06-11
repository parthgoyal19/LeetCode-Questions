# Last updated: 11/06/2026, 21:29:26
from typing import List
import bisect

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        def solve_one_way(start1, dur1, start2, dur2):
            # Combine and sort the second category of rides by their start time
            rides2 = sorted(zip(start2, dur2))
            s2_sorted = [r[0] for r in rides2]
            d2_sorted = [r[1] for r in rides2]
            n2 = len(rides2)
            
            # Pref_min_dur[i] stores the minimum duration among rides2[0...i]
            pref_min_dur = [0] * n2
            current_min_dur = float('inf')
            for i in range(n2):
                current_min_dur = min(current_min_dur, d2_sorted[i])
                pref_min_dur[i] = current_min_dur
                
            # Suff_min_finish[i] stores the minimum (start + duration) among rides2[i...n2-1]
            suff_min_finish = [0] * n2
            current_min_finish = float('inf')
            for i in range(n2 - 1, -1, -1):
                current_min_finish = min(current_min_finish, s2_sorted[i] + d2_sorted[i])
                suff_min_finish[i] = current_min_finish
                
            min_total_finish = float('inf')
            
            # For each ride in the first category
            for s1, d1 in zip(start1, dur1):
                finish1 = s1 + d1
                
                # Find the division point where start2 <= finish1
                idx = bisect.bisect_right(s2_sorted, finish1) - 1
                
                # Case A: Boarding a ride from group 2 that is already open
                if idx >= 0:
                    min_total_finish = min(min_total_finish, finish1 + pref_min_dur[idx])
                    
                # Case B: Boarding a ride from group 2 that opens after finish1
                if idx + 1 < n2:
                    min_total_finish = min(min_total_finish, suff_min_finish[idx + 1])
                    
            return min_total_finish

        # Answer is the minimum of (Land -> Water) or (Water -> Land)
        ans1 = solve_one_way(landStartTime, landDuration, waterStartTime, waterDuration)
        ans2 = solve_one_way(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(ans1, ans2)