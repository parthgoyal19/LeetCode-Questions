# Last updated: 11/06/2026, 21:29:40
from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list for the tree
        # Since n is not explicitly given, we deduce it from the edge list.
        # The number of nodes n = len(edges) + 1
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 2: Use BFS to find the maximum depth from the root (node 1)
        # Queue stores tuple of (current_node, current_depth)
        queue = deque([(1, 0)])
        visited = [False] * (n + 1)
        visited[1] = True
        max_depth = 0
        
        while queue:
            node, depth = queue.popleft()
            max_depth = max(max_depth, depth)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, depth + 1))
        
        # Step 3: Calculate 2^(max_depth - 1) % (10^9 + 7)
        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)