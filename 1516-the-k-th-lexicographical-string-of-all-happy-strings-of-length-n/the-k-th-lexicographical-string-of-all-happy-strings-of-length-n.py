class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.result = []
        
        def backtrack(current_string):
            # If we reached the target length, add to results
            if len(current_string) == n:
                self.result.append(current_string)
                return
            
            # Try appending 'a', 'b', and 'c'
            for char in ['a', 'b', 'c']:
                # Ensure no two adjacent characters are identical
                if not current_string or current_string[-1] != char:
                    backtrack(current_string + char)
                    
                    # Optimization: Stop early if we already found the k-th string
                    if len(self.result) == k:
                        return

        backtrack("")
        
        # If the total number of happy strings is less than k, return ""
        return self.result[k - 1] if len(self.result) >= k else ""