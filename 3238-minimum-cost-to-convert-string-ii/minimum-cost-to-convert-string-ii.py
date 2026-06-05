class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        # Step 1: Assign a unique ID to each unique string
        string_to_id = {}
        for s in original + changed:
            if s not in string_to_id:
                string_to_id[s] = len(string_to_id)
                
        num_nodes = len(string_to_id)
        inf = float('inf')
        dist = [[inf] * num_nodes for _ in range(num_nodes)]
        
        for i in range(num_nodes):
            dist[i][i] = 0
            
        # Step 2: Populate conversion graph weights
        for src_str, tgt_str, c in zip(original, changed, cost):
            u = string_to_id[src_str]
            v = string_to_id[tgt_str]
            dist[u][v] = min(dist[u][v], c)
            
        # Run Floyd-Warshall to compute all-pairs shortest paths
        for k in range(num_nodes):
            for i in range(num_nodes):
                for j in range(num_nodes):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        # Keep track of valid substring lengths to optimize lookback
        valid_lengths = set(len(s) for s in string_to_id.keys())
        
        # Step 3: Linear Dynamic Programming over string length
        n = len(source)
        dp = [inf] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            # Option A: Characters match directly, no conversion cost
            if source[i - 1] == target[i - 1]:
                dp[i] = min(dp[i], dp[i - 1])
                
            # Option B: Look back at valid substring windows
            for length in valid_lengths:
                j = i - length
                if j < 0:
                    continue
                    
                sub_src = source[j:i]
                sub_tgt = target[j:i]
                
                if sub_src in string_to_id and sub_tgt in string_to_id:
                    u = string_to_id[sub_src]
                    v = string_to_id[sub_tgt]
                    if dist[u][v] != inf and dp[j] != inf:
                        dp[i] = min(dp[i], dp[j] + dist[u][v])
                        
        return dp[n] if dp[n] != inf else -1