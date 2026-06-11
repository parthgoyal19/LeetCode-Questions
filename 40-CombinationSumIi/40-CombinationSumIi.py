# Last updated: 11/06/2026, 21:31:53
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        # Sort candidates to handle duplicates efficiently
        candidates.sort()
        
        def backtrack(remain: int, current_combo: List[int], start: int):
            # Base Case 1: Target achieved
            if remain == 0:
                results.append(list(current_combo))
                return
            # Base Case 2: Exceeded the target
            if remain < 0:
                return
                
            for i in range(start, len(candidates)):
                # Early optimization: since the array is sorted, if the current 
                # candidate exceeds the remaining sum, all subsequent ones will too.
                if candidates[i] > remain:
                    break
                    
                # Skip duplicate elements at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                # Make a choice
                current_combo.append(candidates[i])
                
                # Recurse moving the start index to i + 1 (cannot reuse the same element)
                backtrack(remain - candidates[i], current_combo, i + 1)
                
                # Undo choice (Backtrack)
                current_combo.pop()
                
        backtrack(target, [], 0)
        return results