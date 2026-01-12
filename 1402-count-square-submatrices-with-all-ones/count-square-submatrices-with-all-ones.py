class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # dp[i][j] = number of all-1 squares whose bottom-right corner is (i,j)
        dp = [[0]*n for i in range(m)]

        for j in range(m):
            dp[j][0] = matrix[j][0] #  # 1 count  if value 1
        
        for j in range(n):
            dp[0][j] = matrix[0][j] # 1 count  if value 1

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 1:

                    # grow square if top/left/diag can support it
                    top = dp[i-1][j]
                    left = dp[i][j-1]
                    diag = dp[i-1][j-1]

                    dp[i][j] = 1+ min(top,left,diag)

        return  sum(sum(row) for row in dp)

#main goal is to figure out how to grow squares from surrounding squares 

#------------------ Recursion---------------------------------
        # @lru_cache(None)
        # def f(i: int, j: int) -> int:
        #     if i >= m or j >= n:
        #         return 0
        #     if matrix[i][j] == 0:
        #         return 0
        #     return 1 + min(
        #         f(i + 1, j),     # down
        #         f(i, j + 1),     # right
        #         f(i + 1, j + 1)  # diag
        #     )

        # total = 0
        # for i in range(m):
        #     for j in range(n):
        #         total += f(i, j)
        # return total