class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        
        # ---------------------------------------------------------------------
        # CASE 1: Substrings with exactly 1 distinct character
        # ---------------------------------------------------------------------
        current_run = 0
        for i in range(n):
            if i == 0 or s[i] == s[i-1]:
                current_run += 1
            else:
                current_run = 1
            max_len = max(max_len, current_run)
            
        # ---------------------------------------------------------------------
        # CASE 2: Substrings with exactly 2 distinct characters
        # ---------------------------------------------------------------------
        for char1, char2, forbidden in [('a', 'b', 'c'), ('b', 'c', 'a'), ('a', 'c', 'b')]:
            # Maps running balance to the earliest index it appeared
            balance_map = {0: -1}
            running_balance = 0
            last_forbidden_idx = -1
            
            for idx, char in enumerate(s):
                if char == forbidden:
                    # Reset mapping bounds because the forbidden character breaks continuity
                    balance_map = {0: idx}
                    running_balance = 0
                    last_forbidden_idx = idx
                else:
                    if char == char1:
                        running_balance += 1
                    elif char == char2:
                        running_balance -= 1
                    
                    if running_balance in balance_map:
                        prev_idx = balance_map[running_balance]
                        # Ensure both characters have appeared at least once in this window
                        # by verifying that the window length is greater than a single character run
                        if idx - prev_idx > 0:
                            # Verify that both characters actually exist in s[prev_idx+1 : idx+1]
                            window = s[prev_idx + 1 : idx + 1]
                            if char1 in window and char2 in window:
                                max_len = max(max_len, idx - prev_idx)
                    else:
                        balance_map[running_balance] = idx

        # ---------------------------------------------------------------------
        # CASE 3: Substrings with exactly 3 distinct characters
        # ---------------------------------------------------------------------
        # Maps (count_b - count_a, count_c - count_a) -> list of indices
        prefix_map = {(0, 0): [-1]}
        
        cnt_a = cnt_b = cnt_c = 0
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        
        for idx, char in enumerate(s):
            if char == 'a': cnt_a += 1
            elif char == 'b': cnt_b += 1
            elif char == 'c': cnt_c += 1
            
            last_seen[char] = idx
            
            key = (cnt_b - cnt_a, cnt_c - cnt_a)
            
            if key in prefix_map:
                # The cut-off point: all three characters must have appeared after our starting match index
                min_last_seen = min(last_seen['a'], last_seen['b'], last_seen['c'])
                
                # Binary search or scan for the earliest valid matching prefix index
                for prev_idx in prefix_map[key]:
                    if prev_idx < min_last_seen:
                        max_len = max(max_len, idx - prev_idx)
                        break # Since the list is sorted, the first one yields the maximum length
                        
            if key not in prefix_map:
                prefix_map[key] = []
            prefix_map[key].append(idx)
            
        return max_len