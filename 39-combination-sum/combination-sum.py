class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def backtrack(remain: int, current_combo: List[int], start: int):
            # Base Case 1: Target achieved
            if remain == 0:
                results.append(list(current_combo))
                return
            # Base Case 2: Exceeded the target
            if remain < 0:
                return
                
            # Explore further combinations
            for i in range(start, len(candidates)):
                # Make a choice
                current_combo.append(candidates[i])
                
                # Recurse with updated remaining sum. 
                # Note: We pass 'i' as the start index because we can reuse the same number.
                backtrack(remain - candidates[i], current_combo, i)
                
                # Undo choice (Backtrack)
                current_combo.pop()
                
        backtrack(target, [], 0)
        return results