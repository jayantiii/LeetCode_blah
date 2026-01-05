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

##-------------------Bottom up DP!----------------------------
# dp[m,n] , max square side length whose bottom-right corner is at m,n
    #   if not matrix or not matrix[0]:
    #         return 0

    #     R, C = len(matrix), len(matrix[0])
    #     dp = [[0] * (C + 1) for _ in range(R + 1)]

    #     best_side = 0
    #     for i in range(1, R + 1):
    #         for j in range(1, C + 1):
    #             if matrix[i - 1][j - 1] == "1":
    #                 dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    #                 best_side = max(best_side, dp[i][j])

    #     return best_side * best_side

#if we wanna doo top left, corner wise, then fill table backward from bottom
# --------------Example matrix (recursion)-------------------------:
# 1 1 1 1
# 1 1 0 1
# 1 1 1 1
# 1 1 1 1
#
# dfs(i,j) = max SQUARE SIDE starting at (i,j)

# Key cell: dfs(0,0)
# down  = dfs(1,0) = 2   (from row1,col0 you can make a 2x2 of ones)
# right = dfs(0,1) = 1   (from row0,col1 you CANNOT make 2x2 because (1,2)=0 blocks)
# diag  = dfs(1,1) = 1   (same reason, any 2x2 starting at (1,1) hits (1,2)=0)
#
# So:
# dfs(0,0) = 1 + min(down,right,diag)
#          = 1 + min(2,1,1)
#          = 2
#
# Intuition of "min":
# To grow a kxk square at (i,j), you need:
# - (k-1)x(k-1) square at (i+1,j)   (supports everything below top row)
# - (k-1)x(k-1) square at (i,j+1)   (supports everything right of left col)
# - (k-1)x(k-1) square at (i+1,j+1) (supports the interior)
# The weakest of these 3 limits how big you can grow => min(...)
