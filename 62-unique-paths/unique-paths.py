class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

         # store number of ways to each cell
        memo = [[1] * n for _ in range(m)] #fill first

        for i in range(1,m):
            for j in range(1,n):             
                topvalue = memo[i-1][j] if i > 0 else 0
                leftvalue = memo[i][j-1] if j > 0 else 0
                memo[i][j] = topvalue + leftvalue
        return memo[m-1][n-1] 

#Also, u can do without 2d memo too
#Just store 1d previous row, thats all we need
#in for loop have a temo row and at the end make that row the prev row for next loop

        