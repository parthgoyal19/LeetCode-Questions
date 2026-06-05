class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.components -= 1
            return True
        return False

class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        
        def can_form_mst(target_stability):
            uf = UnionFind(n)
            upgrades_used = 0
            
            # Step 1: Process all 'must-include' edges
            for u, v, s, must in edges:
                if must == 1:
                    # If a mandatory edge cannot reach target stability, we can't form a valid tree
                    if s < target_stability:
                        return False
                    # Mandatory edges must not form a cycle
                    if not uf.union(u, v):
                        return False
            
            # Step 2: Separate 'optional' edges into those needing upgrades and those that don't
            no_upgrade_needed = []
            upgrade_needed = []
            
            for u, v, s, must in edges:
                if must == 0:
                    if s >= target_stability:
                        no_upgrade_needed.append((u, v))
                    elif s * 2 >= target_stability:
                        upgrade_needed.append((u, v))
            
            # Step 3: Connect components using free optional edges first
            for u, v in no_upgrade_needed:
                uf.union(u, v)
                
            # Step 4: Use upgrades greedily if we still have disconnected components
            for u, v in upgrade_needed:
                if uf.find(u) != uf.find(v):
                    if upgrades_used < k:
                        uf.union(u, v)
                        upgrades_used += 1
                    else:
                        break # Out of upgrades budget
            
            # Valid if everything is completely connected into 1 spanning tree
            return uf.components == 1

        # Binary search range based on constraints
        low, high = 1, 2 * 10**5
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_form_mst(mid):
                ans = mid       # Found a working stability, try to find a larger one
                low = mid + 1
            else:
                high = mid - 1  # Target too high, lower the stability score
                
        return ans