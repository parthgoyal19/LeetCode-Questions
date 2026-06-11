class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        
        # Reduce the number of shifts using modulo
        k = k % n
        
        # If k % n is 0, no net shifting happens, so it is always identical
        if k == 0:
            return True
            
        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # Even row: left shift. Element at j matches element at (j + k) % n
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                    # Odd row: right shift. Element at j matches element at (j - k) % n
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False
                        
        return True