class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        
        # Initialize the output matrix size: (m - k + 1) x (n - k + 1)
        ans_rows = m - k + 1
        ans_cols = n - k + 1
        ans = [[0] * ans_cols for _ in range(ans_rows)]
        
        # Iterate over every possible top-left corner (i, j) of the k x k submatrix
        for i in range(ans_rows):
            for j in range(ans_cols):
                
                # Gather all unique values inside the current k x k window
                distinct_elements = set()
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        distinct_elements.add(grid[r][c])
                
                # If all elements are the same, the minimum distinct difference is 0
                if len(distinct_elements) <= 1:
                    ans[i][j] = 0
                    continue
                
                # Sort unique elements to find the closest values adjacent to each other
                sorted_vals = sorted(list(distinct_elements))
                
                # Find the minimum absolute difference between adjacent elements
                min_diff = float('inf')
                for idx in range(len(sorted_vals) - 1):
                    diff = sorted_vals[idx + 1] - sorted_vals[idx]
                    if diff < min_diff:
                        min_diff = diff
                
                ans[i][j] = min_diff
                
        return ans