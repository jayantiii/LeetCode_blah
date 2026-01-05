class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # dfs(i,j) return the max square side length starting at (i,j),
        @lru_cache(None)
        def dfs(m,n):
            if m < 0 or m >= len(matrix) or n < 0 or n >= len(matrix[0]):
                return 0
            
            if matrix[m][n] !="1":
                return 0 
            down = dfs(m+1,n) #down
            right = dfs(m,n+1) #right
            diag = dfs(m+1,n+1) #to grow sqaure diagonally
            
            # grow square only as far as the smallest neighbor allows
            return  1 + min(down,right,diag) #Imp Line

        maxlength = 0
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                if matrix[m][n] == "1":
                    length = dfs(m,n)
                    maxlength = max(maxlength, length)

        return maxlength * maxlength

#No visited set needed      
# In this problem, revisiting a cell is not a bug; recomputing the same dfs(i,j) repeatedly is the bug. Memoization fixes that, visited breaks correctness or forces you into awkward logic.