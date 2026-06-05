from collections import deque
from sortedcontainers import SortedSet

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        
        # Two sorted sets to handle tracking unvisited states by parity (even/odd)
        unvisited = [SortedSet(), SortedSet()]
        for i in range(n + 1):
            unvisited[i % 2].add(i)
            
        # Count initial zeros
        initial_zeros = s.count('0')
        
        # Remove the starting state from unvisited
        unvisited[initial_zeros % 2].remove(initial_zeros)
        
        queue = deque([initial_zeros])
        operations = 0
        
        while queue:
            # Process current BFS level
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                # Goal reached
                if cur == 0:
                    return operations
                
                # Calculate boundary window for next states
                left_boundary = cur + k - 2 * min(cur, k)
                right_boundary = cur + k - 2 * max(k - n + cur, 0)
                
                # Select the correct parity set
                target_set = unvisited[left_boundary % 2]
                
                # Find the first element >= left_boundary
                idx = target_set.bisect_left(left_boundary)
                
                # Collect and remove all elements within [left_boundary, right_boundary]
                states_to_remove = []
                while idx < len(target_set) and target_set[idx] <= right_boundary:
                    next_state = target_set[idx]
                    queue.append(next_state)
                    states_to_remove.append(next_state)
                    idx += 1
                
                for state in states_to_remove:
                    target_set.remove(state)
                    
            operations += 1
            
        return -1