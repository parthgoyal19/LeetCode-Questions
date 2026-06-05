import heapq

class Solution:
    def minCost(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: Build the adjacency list graph
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            # Original edge traversal
            graph[u].append((v, w))
            # Reverse edge traversal utilizing the node switch
            graph[v].append((u, 2 * w))
            
        # Step 2: Initialize Dijkstra's Algorithm
        min_heap = [(0, 0)]  # (cumulative_cost, current_node)
        distances = [float('inf')] * n
        distances[0] = 0
        
        while min_heap:
            curr_cost, u = heapq.heappop(min_heap)
            
            # If we reached the destination node, return the cost
            if u == n - 1:
                return curr_cost
                
            # If we found a shorter path to u already, skip processing
            if curr_cost > distances[u]:
                continue
                
            # Explore neighbors
            for v, weight in graph[u]:
                next_cost = curr_cost + weight
                if next_cost < distances[v]:
                    distances[v] = next_cost
                    heapq.heappush(min_heap, (next_cost, v))
                    
        return -1