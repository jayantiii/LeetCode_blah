class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[0])
 
        #dp[i][j] is min path some ending at i,j
        # Outer loop first, then inner loop
        dp = [[float("inf") for j in range(i+1)] for i in range(m)]
        dp[0][0] = triangle[0][0]

        for i in range(1,m):
            for j in range(0,i+1):
                # from directly above (i-1, j) exists only when j <= i-1  <=> j < i
                above = float("inf")   
                left  = float("inf")   
                if  j < i: #THIS!
                    above = min(dp[i][j], dp[i-1][j])

                # from above-left (i-1, j-1)
                if  j-1 >=0:
                    left =  min(dp[i][j],dp[i-1][j-1])

                dp[i][j] =  triangle[i][j] + min(above,left)

        return min(dp[m-1]) #max in the last row


#BACKTRACKING!!
        # m = len(triangle)
        # n = len(triangle[0])

        # @lru_cache(None)
        # def backtrack(i,j): #return min pathsum of cell (i,j)
        #     if i < 0 or i >= m or j <0 or j >= i + 1: # cond j >= i + 1
        #         return 0

        #     first = backtrack(i+1, j)
        #     second = backtrack(i+1,j+1)

        #     return triangle[i][j] + min(first,second)

        # return backtrack(0,0)
        