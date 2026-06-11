# Last updated: 11/06/2026, 21:30:02
class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        # Step 1: Initialize the distance matrix for 26 lowercase letters
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
            
        # Step 2: Populate the graph with existing conversion costs
        for src_char, tgt_char, c in zip(original, changed, cost):
            u = ord(src_char) - ord('a')
            v = ord(tgt_char) - ord('a')
            dist[u][v] = min(dist[u][v], c)
            
        # Step 3: Run Floyd-Warshall to find all-pairs shortest paths
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        # Step 4: Compute the total minimum cost to transform source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char != t_char:
                u = ord(s_char) - ord('a')
                v = ord(t_char) - ord('a')
                
                # If there is no valid transformation path, return -1
                if dist[u][v] == inf:
                    return -1
                total_cost += dist[u][v]
                
        return total_cost