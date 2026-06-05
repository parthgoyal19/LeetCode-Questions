class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        # Step 1: Sort the array
        arr.sort()
        
        ans = []
        min_diff = float('inf')
        
        # Step 2: Single pass to find min_diff and collect pairs
        for i in range(len(arr) - 1):
            current_diff = arr[i+1] - arr[i]
            
            if current_diff < min_diff:
                # Found a new strictly smaller difference: reset and update
                min_diff = current_diff
                ans = [[arr[i], arr[i+1]]]
            elif current_diff == min_diff:
                # Found another pair with the same minimum difference
                ans.append([arr[i], arr[i+1]])
                
        return ans