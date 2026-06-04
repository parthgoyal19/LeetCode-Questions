class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Include the outer non-removable boundaries of the field
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        
        # Sort to easily compute positive differences, though not strictly required
        hFences.sort()
        vFences.sort()
        
        # Step 1: Collect all possible horizontal side lengths
        h_gaps = set()
        len_h = len(hFences)
        for i in range(len_h):
            for j in range(i + 1, len_h):
                h_gaps.add(hFences[j] - hFences[i])
                
        # Step 2: Find the maximum vertical side length that matches a horizontal one
        max_side = -1
        len_v = len(vFences)
        for i in range(len_v):
            for j in range(i + 1, len_v):
                v_gap = vFences[j] - vFences[i]
                if v_gap in h_gaps:
                    max_side = max(max_side, v_gap)
                    
        # Step 3: Return the area modulo 10^9 + 7 if a square can be formed
        if max_side == -1:
            return -1
            
        return (max_side * max_side) % (10**9 + 7)