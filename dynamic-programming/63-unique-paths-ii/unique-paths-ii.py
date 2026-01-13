class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}
        def dfs(i,j):
            if i < 0 or j < 0 or i >=m or j >=n or obstacleGrid[i][j] == 1: #obstacle:
                return 0
            if i == m-1 and j == n-1:
                return 1 #found one way
            if (i, j) in memo:
                return memo[(i, j)]

            a = dfs(i+1,j) #down
            b = dfs(i,j+1) #right
            memo[(i,j)] = a + b
            return  memo[(i,j)] #dont return this here stupid, memo[(m-1,n-1)]
        
        return dfs(0,0) # or memo[(m-1,n-1)]

#
# DFS explores EVERY possible path:
# Worst case = 2^(m+n) → impossible for bigger grids.

# if i < 0 or j < 0 o This is technically not necessary, as we never go nehative

# if i == m-1 and j == n-1:return 1 #found one way
#This if case shouldnt be the first if case caus eits possible that destination is obstacle and u still return 1
        